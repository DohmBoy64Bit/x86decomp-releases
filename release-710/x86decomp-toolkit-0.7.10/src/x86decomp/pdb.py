"""Bounded MSF 7.0 / PDB inventory and PE identity correlation.

This parser intentionally inventories stable container, PDB, TPI/IPI, and DBI metadata.
It does not claim complete CodeView type/symbol reconstruction. Every read is bounds checked,
stream blocks may be discontiguous, and unsupported variants fail explicitly.
"""

from __future__ import annotations

import math
import struct
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ContractError, FormatError
from .pe import parse_pe
from .util import sha256_bytes, sha256_file

_MAGIC = b"Microsoft C/C++ MSF 7.00\r\n\x1aDS\x00\x00\x00"
_ALLOWED_BLOCK_SIZES = {512, 1024, 2048, 4096}
_MAX_STREAMS = 1_000_000
_MAX_BLOCKS = 16_777_216
_MAX_MODULES = 1_000_000
_MAX_SOURCE_CONTRIBUTIONS = 10_000_000


def _require(data: bytes, offset: int, size: int, context: str) -> None:
    """Support require processing for internal toolkit callers."""
    if offset < 0 or size < 0 or offset > len(data) or size > len(data) - offset:
        raise FormatError(f"{context} exceeds bounds")


def _u16(data: bytes, offset: int, context: str) -> int:
    """Support u16 processing for internal toolkit callers."""
    _require(data, offset, 2, context)
    return struct.unpack_from("<H", data, offset)[0]


def _u32(data: bytes, offset: int, context: str) -> int:
    """Support u32 processing for internal toolkit callers."""
    _require(data, offset, 4, context)
    return struct.unpack_from("<I", data, offset)[0]


def _cstring(data: bytes, offset: int, limit: int, context: str) -> tuple[str, int]:
    """Support cstring processing for internal toolkit callers."""
    if offset < 0 or offset >= limit or limit > len(data):
        raise FormatError(f"{context} starts outside bounds")
    end = data.find(b"\x00", offset, limit)
    if end < 0:
        raise FormatError(f"{context} is unterminated")
    return data[offset:end].decode("utf-8", errors="replace"), end + 1


def _align4(value: int) -> int:
    """Support align4 processing for internal toolkit callers."""
    return (value + 3) & ~3


@dataclass(frozen=True)
class PDBStream:
    """Store validated p d b stream fields used by toolkit reports and adapters."""
    index: int
    size: int | None
    blocks: tuple[int, ...]
    sha256: str | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "index": self.index,
            "size": self.size,
            "blocks": list(self.blocks),
            "sha256": self.sha256,
        }


@dataclass(frozen=True)
class PDBFile:
    """Store validated p d b file fields used by toolkit reports and adapters."""
    path: Path | None
    file_sha256: str
    block_size: int
    free_block_map_block: int
    number_of_blocks: int
    directory_bytes: int
    block_map_address: int
    streams: tuple[PDBStream, ...]
    info: dict[str, Any] | None
    tpi: dict[str, Any] | None
    ipi: dict[str, Any] | None
    dbi: dict[str, Any] | None
    pe_match: dict[str, Any] | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "format": "PDB_MSF_7_00",
            "source_path": None if self.path is None else str(self.path),
            "source_sha256": self.file_sha256,
            "superblock": {
                "block_size": self.block_size,
                "free_block_map_block": self.free_block_map_block,
                "number_of_blocks": self.number_of_blocks,
                "directory_bytes": self.directory_bytes,
                "block_map_address": self.block_map_address,
            },
            "stream_count": len(self.streams),
            "streams": [stream.to_dict() for stream in self.streams],
            "pdb_info": self.info,
            "tpi": self.tpi,
            "ipi": self.ipi,
            "dbi": self.dbi,
            "pe_match": self.pe_match,
            "scope": {
                "msf_directory_parsed": True,
                "pdb_identity_parsed": self.info is not None,
                "tpi_ipi_headers_parsed": True,
                "dbi_modules_sources_contributions_parsed": self.dbi is not None,
                "codeview_type_records_fully_parsed": False,
                "codeview_symbol_records_fully_parsed": False,
            },
        }


class _MSF:
    """Coordinate m s f behavior for the current toolkit workflow."""
    def __init__(self, data: bytes):
        """Initialize the instance with validated constructor state."""
        self.data = data
        if len(data) < 56 or data[:32] != _MAGIC:
            raise FormatError("not an MSF 7.0 PDB")
        (
            self.block_size,
            self.free_block_map_block,
            self.number_of_blocks,
            self.directory_bytes,
            self.unknown,
            self.block_map_address,
        ) = struct.unpack_from("<IIIIII", data, 32)
        if self.block_size not in _ALLOWED_BLOCK_SIZES:
            raise FormatError(f"unsupported MSF block size: {self.block_size}")
        if self.free_block_map_block not in (1, 2):
            raise FormatError("invalid MSF free block map selector")
        if self.number_of_blocks == 0 or self.number_of_blocks > _MAX_BLOCKS:
            raise FormatError("invalid MSF block count")
        expected = self.number_of_blocks * self.block_size
        if expected != len(data):
            raise FormatError(f"MSF size mismatch: header describes {expected} bytes, file has {len(data)}")
        if self.block_map_address >= self.number_of_blocks:
            raise FormatError("MSF block map address is outside file")
        if self.directory_bytes > len(data):
            raise FormatError("MSF directory size exceeds file")
        self.stream_sizes, self.stream_blocks = self._parse_directory()

    def _block(self, index: int, context: str) -> bytes:
        """Support block processing for internal toolkit callers."""
        if index < 0 or index >= self.number_of_blocks:
            raise FormatError(f"{context} references block outside file: {index}")
        start = index * self.block_size
        return self.data[start : start + self.block_size]

    def _parse_directory(self) -> tuple[list[int | None], list[tuple[int, ...]]]:
        """Support parse directory processing for internal toolkit callers."""
        directory_block_count = math.ceil(self.directory_bytes / self.block_size) if self.directory_bytes else 0
        map_bytes_needed = directory_block_count * 4
        if map_bytes_needed > self.block_size:
            raise FormatError("MSF directory block map exceeds one block; unsupported bounded variant")
        map_block = self._block(self.block_map_address, "MSF directory block map")
        directory_blocks = list(struct.unpack_from(f"<{directory_block_count}I", map_block, 0)) if directory_block_count else []
        directory = b"".join(self._block(index, "MSF stream directory") for index in directory_blocks)[: self.directory_bytes]
        if len(directory) < 4:
            raise FormatError("MSF stream directory is truncated")
        stream_count = _u32(directory, 0, "MSF stream count")
        if stream_count > _MAX_STREAMS:
            raise FormatError("MSF stream count exceeds safety limit")
        cursor = 4
        _require(directory, cursor, stream_count * 4, "MSF stream sizes")
        raw_sizes = list(struct.unpack_from(f"<{stream_count}I", directory, cursor)) if stream_count else []
        cursor += stream_count * 4
        sizes: list[int | None] = [None if value == 0xFFFFFFFF else value for value in raw_sizes]
        blocks: list[tuple[int, ...]] = []
        for index, size in enumerate(sizes):
            count = 0 if size is None else math.ceil(size / self.block_size)
            _require(directory, cursor, count * 4, f"MSF stream {index} block list")
            values = tuple(struct.unpack_from(f"<{count}I", directory, cursor)) if count else ()
            cursor += count * 4
            for block in values:
                if block >= self.number_of_blocks:
                    raise FormatError(f"MSF stream {index} references block outside file")
            blocks.append(values)
        if cursor > len(directory):
            raise FormatError("MSF stream directory overrun")
        return sizes, blocks

    def stream(self, index: int) -> bytes | None:
        """Execute the stream operation for the current toolkit workflow."""
        if index < 0 or index >= len(self.stream_sizes):
            return None
        size = self.stream_sizes[index]
        if size is None:
            return None
        return b"".join(self._block(block, f"MSF stream {index}") for block in self.stream_blocks[index])[:size]


def _parse_info(data: bytes | None) -> dict[str, Any] | None:
    """Support parse info processing for internal toolkit callers."""
    if data is None:
        return None
    if len(data) < 28:
        raise FormatError("PDB info stream is truncated")
    version, signature, age = struct.unpack_from("<III", data, 0)
    guid_raw = data[12:28]
    return {
        "version": version,
        "signature": signature,
        "age": age,
        "guid_raw_hex": guid_raw.hex(),
        "guid": str(uuid.UUID(bytes_le=guid_raw)),
        "stream_size": len(data),
        "named_stream_map_parsed": False,
    }


def _parse_tpi(data: bytes | None, name: str) -> dict[str, Any] | None:
    """Support parse tpi processing for internal toolkit callers."""
    if data is None:
        return None
    if len(data) < 56:
        raise FormatError(f"{name} stream is truncated")
    values = struct.unpack_from("<IIIIIHHIIiIiIiI", data, 0)
    (
        version,
        header_size,
        type_begin,
        type_end,
        record_bytes,
        hash_stream,
        hash_aux_stream,
        hash_key_size,
        hash_bucket_count,
        hash_values_offset,
        hash_values_length,
        index_offsets_offset,
        index_offsets_length,
        hash_adjust_offset,
        hash_adjust_length,
    ) = values
    if header_size < 56 or header_size > len(data):
        raise FormatError(f"{name} header size is invalid")
    if type_end < type_begin:
        raise FormatError(f"{name} type index range is reversed")
    if record_bytes > len(data) - header_size:
        raise FormatError(f"{name} type record bytes exceed stream")
    return {
        "stream": name,
        "version": version,
        "header_size": header_size,
        "type_index_begin": type_begin,
        "type_index_end": type_end,
        "type_record_count": type_end - type_begin,
        "type_record_bytes": record_bytes,
        "hash_stream_index": None if hash_stream == 0xFFFF else hash_stream,
        "hash_aux_stream_index": None if hash_aux_stream == 0xFFFF else hash_aux_stream,
        "hash_key_size": hash_key_size,
        "hash_bucket_count": hash_bucket_count,
        "hash_value_buffer": {"offset": hash_values_offset, "length": hash_values_length},
        "index_offset_buffer": {"offset": index_offsets_offset, "length": index_offsets_length},
        "hash_adjust_buffer": {"offset": hash_adjust_offset, "length": hash_adjust_length},
    }


def _parse_modules(data: bytes) -> list[dict[str, Any]]:
    """Support parse modules processing for internal toolkit callers."""
    modules: list[dict[str, Any]] = []
    cursor = 0
    while cursor < len(data):
        if len(data) - cursor < 64:
            if all(byte == 0 for byte in data[cursor:]):
                break
            raise FormatError("DBI module info record is truncated")
        fields = struct.unpack_from("<I H2x ii I H2x II H H III H2x III", data, cursor)
        (
            _unused1,
            section,
            section_offset,
            section_size,
            characteristics,
            module_index,
            data_crc,
            reloc_crc,
            flags,
            module_stream,
            symbol_bytes,
            c11_bytes,
            c13_bytes,
            source_file_count,
            _unused2,
            source_name_index,
            pdb_path_index,
        ) = fields
        string_cursor = cursor + 64
        module_name, string_cursor = _cstring(data, string_cursor, len(data), "DBI module name")
        object_name, string_cursor = _cstring(data, string_cursor, len(data), "DBI object name")
        next_cursor = _align4(string_cursor)
        if next_cursor <= cursor or next_cursor > len(data):
            raise FormatError("DBI module info alignment is invalid")
        modules.append(
            {
                "index": len(modules),
                "module_name": module_name,
                "object_file_name": object_name,
                "module_stream_index": None if module_stream == 0xFFFF else module_stream,
                "symbol_bytes": symbol_bytes,
                "c11_line_bytes": c11_bytes,
                "c13_line_bytes": c13_bytes,
                "source_file_count": source_file_count,
                "source_file_name_index": source_name_index,
                "pdb_file_path_name_index": pdb_path_index,
                "flags": flags,
                "section_contribution": {
                    "section": section,
                    "offset": section_offset,
                    "size": section_size,
                    "characteristics": characteristics,
                    "module_index": module_index,
                    "data_crc": data_crc,
                    "relocation_crc": reloc_crc,
                },
            }
        )
        if len(modules) > _MAX_MODULES:
            raise FormatError("DBI module count exceeds safety limit")
        cursor = next_cursor
    return modules


def _parse_source_info(data: bytes) -> dict[str, Any]:
    """Support parse source info processing for internal toolkit callers."""
    if not data:
        return {"module_count": 0, "contribution_count": 0, "files_by_module": [], "unique_files": []}
    if len(data) < 4:
        raise FormatError("DBI source info substream is truncated")
    module_count, legacy_source_count = struct.unpack_from("<HH", data, 0)
    if module_count > _MAX_MODULES:
        raise FormatError("DBI source module count exceeds safety limit")
    cursor = 4
    _require(data, cursor, module_count * 2, "DBI source module indices")
    module_indices = list(struct.unpack_from(f"<{module_count}H", data, cursor)) if module_count else []
    cursor += module_count * 2
    _require(data, cursor, module_count * 2, "DBI source file counts")
    counts = list(struct.unpack_from(f"<{module_count}H", data, cursor)) if module_count else []
    cursor += module_count * 2
    contribution_count = sum(counts)
    if contribution_count > _MAX_SOURCE_CONTRIBUTIONS:
        raise FormatError("DBI source file contribution count exceeds safety limit")
    _require(data, cursor, contribution_count * 4, "DBI source name offsets")
    offsets = list(struct.unpack_from(f"<{contribution_count}I", data, cursor)) if contribution_count else []
    cursor += contribution_count * 4
    names_buffer = data[cursor:]
    names: list[str] = []
    for offset in offsets:
        if offset >= len(names_buffer):
            raise FormatError("DBI source name offset exceeds names buffer")
        name, _ = _cstring(names_buffer, offset, len(names_buffer), "DBI source filename")
        names.append(name)
    files_by_module: list[dict[str, Any]] = []
    position = 0
    for module_position, count in enumerate(counts):
        files_by_module.append(
            {
                "module_position": module_position,
                "module_index": module_indices[module_position],
                "files": names[position : position + count],
            }
        )
        position += count
    return {
        "module_count": module_count,
        "legacy_source_count": legacy_source_count,
        "contribution_count": contribution_count,
        "files_by_module": files_by_module,
        "unique_files": sorted(set(names)),
    }


def _parse_section_contributions(data: bytes) -> dict[str, Any]:
    """Support parse section contributions processing for internal toolkit callers."""
    if not data:
        return {"version": None, "entries": []}
    if len(data) < 4:
        raise FormatError("DBI section contribution substream is truncated")
    version = _u32(data, 0, "DBI section contribution version")
    record_size = 32 if version == 0xEFFE0000 + 20140516 else 28
    payload = data[4:]
    if len(payload) % record_size != 0:
        raise FormatError("DBI section contribution payload is misaligned")
    entries: list[dict[str, Any]] = []
    for cursor in range(0, len(payload), record_size):
        section, offset, size, characteristics, module_index, data_crc, reloc_crc = struct.unpack_from(
            "<H2xiiIH2xII", payload, cursor
        )
        entry = {
            "section": section,
            "offset": offset,
            "size": size,
            "characteristics": characteristics,
            "module_index": module_index,
            "data_crc": data_crc,
            "relocation_crc": reloc_crc,
        }
        if record_size == 32:
            entry["coff_section_index"] = _u32(payload, cursor + 28, "DBI contribution COFF section")
        entries.append(entry)
    return {"version": version, "record_size": record_size, "entries": entries}


def _parse_section_map(data: bytes) -> dict[str, Any]:
    """Support parse section map processing for internal toolkit callers."""
    if not data:
        return {"count": 0, "logical_count": 0, "entries": []}
    if len(data) < 4:
        raise FormatError("DBI section map substream is truncated")
    count, logical_count = struct.unpack_from("<HH", data, 0)
    required = 4 + count * 20
    if required > len(data):
        raise FormatError("DBI section map entries exceed substream")
    entries = []
    cursor = 4
    for _ in range(count):
        flags, overlay, group, frame, section_name, class_name, offset, length = struct.unpack_from(
            "<HHHHHHII", data, cursor
        )
        cursor += 20
        entries.append(
            {
                "flags": flags,
                "overlay": overlay,
                "group": group,
                "frame": frame,
                "section_name_offset": None if section_name == 0xFFFF else section_name,
                "class_name_offset": None if class_name == 0xFFFF else class_name,
                "offset": offset,
                "length": length,
            }
        )
    return {"count": count, "logical_count": logical_count, "entries": entries}


def _parse_dbi(data: bytes | None) -> dict[str, Any] | None:
    """Support parse dbi processing for internal toolkit callers."""
    if data is None:
        return None
    if len(data) < 64:
        raise FormatError("DBI stream is truncated")
    fields = struct.unpack_from("<iIIHHHHHHiiiiiIiiHHI", data, 0)
    (
        version_signature,
        version_header,
        age,
        global_stream,
        build_number,
        public_stream,
        pdb_dll_version,
        symbol_record_stream,
        pdb_dll_rebuild,
        module_info_size,
        section_contribution_size,
        section_map_size,
        source_info_size,
        type_server_map_size,
        mfc_type_server_index,
        optional_debug_header_size,
        ec_substream_size,
        flags,
        machine,
        padding,
    ) = fields
    sizes = [
        module_info_size,
        section_contribution_size,
        section_map_size,
        source_info_size,
        type_server_map_size,
        ec_substream_size,
        optional_debug_header_size,
    ]
    if any(size < 0 for size in sizes):
        raise FormatError("DBI substream size is negative")
    if 64 + sum(sizes) > len(data):
        raise FormatError("DBI substreams exceed stream size")
    cursor = 64
    module_data = data[cursor : cursor + module_info_size]
    cursor += module_info_size
    contribution_data = data[cursor : cursor + section_contribution_size]
    cursor += section_contribution_size
    section_map_data = data[cursor : cursor + section_map_size]
    cursor += section_map_size
    source_data = data[cursor : cursor + source_info_size]
    cursor += source_info_size
    type_server_data = data[cursor : cursor + type_server_map_size]
    cursor += type_server_map_size
    ec_data = data[cursor : cursor + ec_substream_size]
    cursor += ec_substream_size
    optional_data = data[cursor : cursor + optional_debug_header_size]
    debug_stream_names = [
        "fpo", "exception", "fixup", "omap_to_source", "omap_from_source", "section_headers",
        "token_rid_map", "xdata", "pdata", "new_fpo", "original_section_headers",
    ]
    debug_streams = []
    for index in range(0, len(optional_data) - (len(optional_data) % 2), 2):
        value = _u16(optional_data, index, "DBI optional debug stream")
        debug_streams.append(
            {
                "kind": debug_stream_names[index // 2] if index // 2 < len(debug_stream_names) else f"unknown_{index // 2}",
                "stream_index": None if value == 0xFFFF else value,
            }
        )
    build_major = (build_number >> 8) & 0x7F if build_number & 0x8000 else None
    build_minor = build_number & 0xFF if build_number & 0x8000 else None
    return {
        "version_signature": version_signature,
        "version_header": version_header,
        "age": age,
        "global_stream_index": None if global_stream == 0xFFFF else global_stream,
        "public_stream_index": None if public_stream == 0xFFFF else public_stream,
        "symbol_record_stream_index": None if symbol_record_stream == 0xFFFF else symbol_record_stream,
        "build_number": build_number,
        "build_major": build_major,
        "build_minor": build_minor,
        "new_build_number_format": bool(build_number & 0x8000),
        "pdb_dll_version": pdb_dll_version,
        "pdb_dll_rebuild": pdb_dll_rebuild,
        "mfc_type_server_index": mfc_type_server_index,
        "flags": {
            "raw": flags,
            "incrementally_linked": bool(flags & 1),
            "private_symbols_stripped": bool(flags & 2),
            "conflicting_types": bool(flags & 4),
        },
        "machine": machine,
        "machine_hex": f"0x{machine:04x}",
        "padding": padding,
        "substream_sizes": {
            "module_info": module_info_size,
            "section_contributions": section_contribution_size,
            "section_map": section_map_size,
            "source_info": source_info_size,
            "type_server_map": type_server_map_size,
            "ec": ec_substream_size,
            "optional_debug_header": optional_debug_header_size,
        },
        "modules": _parse_modules(module_data),
        "section_contributions": _parse_section_contributions(contribution_data),
        "section_map": _parse_section_map(section_map_data),
        "source_info": _parse_source_info(source_data),
        "type_server_map_sha256": sha256_bytes(type_server_data),
        "ec_substream_sha256": sha256_bytes(ec_data),
        "optional_debug_streams": debug_streams,
    }


def _correlate_pe(info: dict[str, Any] | None, pe_path: Path | None) -> dict[str, Any] | None:
    """Support correlate pe processing for internal toolkit callers."""
    if pe_path is None:
        return None
    image = parse_pe(pe_path).to_dict()
    codeview = [record for record in image.get("debug_records", []) if record.get("codeview_signature") == "RSDS"]
    if not codeview:
        return {
            "pe_path": str(pe_path.resolve()),
            "pe_sha256": image["file_sha256"],
            "rsds_found": False,
            "identity_match": False,
            "reason": "PE has no RSDS CodeView record",
        }
    record = codeview[0]
    guid_match = info is not None and record.get("guid_hex") == info.get("guid_raw_hex")
    age_match = info is not None and record.get("age") == info.get("age")
    return {
        "pe_path": str(pe_path.resolve()),
        "pe_sha256": image["file_sha256"],
        "rsds_found": True,
        "pdb_path_recorded": record.get("pdb_path"),
        "pe_guid_raw_hex": record.get("guid_hex"),
        "pdb_guid_raw_hex": None if info is None else info.get("guid_raw_hex"),
        "pe_age": record.get("age"),
        "pdb_age": None if info is None else info.get("age"),
        "guid_match": bool(guid_match),
        "age_match": bool(age_match),
        "identity_match": bool(guid_match and age_match),
    }


def parse_pdb_bytes(data: bytes, *, path: Path | None = None, pe_path: Path | None = None) -> PDBFile:
    """Parse pdb bytes for the current toolkit workflow."""
    msf = _MSF(data)
    streams: list[PDBStream] = []
    for index, (size, blocks) in enumerate(zip(msf.stream_sizes, msf.stream_blocks)):
        payload = msf.stream(index)
        streams.append(
            PDBStream(
                index=index,
                size=size,
                blocks=blocks,
                sha256=None if payload is None else sha256_bytes(payload),
            )
        )
    info = _parse_info(msf.stream(1))
    tpi = _parse_tpi(msf.stream(2), "TPI")
    dbi = _parse_dbi(msf.stream(3))
    ipi = _parse_tpi(msf.stream(4), "IPI")
    if info is not None and dbi is not None and info["age"] != dbi["age"]:
        raise FormatError("PDB info and DBI ages do not match")
    return PDBFile(
        path=path,
        file_sha256=sha256_bytes(data),
        block_size=msf.block_size,
        free_block_map_block=msf.free_block_map_block,
        number_of_blocks=msf.number_of_blocks,
        directory_bytes=msf.directory_bytes,
        block_map_address=msf.block_map_address,
        streams=tuple(streams),
        info=info,
        tpi=tpi,
        ipi=ipi,
        dbi=dbi,
        pe_match=_correlate_pe(info, pe_path),
    )


def parse_pdb(path: Path, *, pe_path: Path | None = None) -> PDBFile:
    """Parse pdb for the current toolkit workflow."""
    resolved = path.resolve()
    if not resolved.is_file():
        raise ContractError(f"PDB does not exist: {resolved}")
    result = parse_pdb_bytes(resolved.read_bytes(), path=resolved, pe_path=pe_path)
    if result.file_sha256 != sha256_file(resolved):
        raise AssertionError("PDB hash calculation mismatch")
    return result
