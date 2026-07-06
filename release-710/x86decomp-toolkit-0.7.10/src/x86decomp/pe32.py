"""Strict, dependency-free parser for native x86 PE32 images.

The parser intentionally supports the first toolkit scope only: little-endian
Windows PE32 images for IMAGE_FILE_MACHINE_I386. It never executes the input.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import FormatError
from .util import sha256_bytes

IMAGE_FILE_MACHINE_I386 = 0x014C
PE32_MAGIC = 0x010B
IMAGE_ORDINAL_FLAG32 = 0x80000000

DIRECTORY_NAMES = (
    "export",
    "import",
    "resource",
    "exception",
    "certificate",
    "base_relocation",
    "debug",
    "architecture",
    "global_pointer",
    "tls",
    "load_config",
    "bound_import",
    "iat",
    "delay_import",
    "clr_runtime",
    "reserved",
)


@dataclass(frozen=True)
class DataDirectory:
    """Store validated data directory fields used by toolkit reports and adapters."""
    name: str
    rva: int
    size: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"name": self.name, "rva": self.rva, "rva_hex": f"0x{self.rva:08x}", "size": self.size}


@dataclass(frozen=True)
class Section:
    """Store validated section fields used by toolkit reports and adapters."""
    name: str
    virtual_size: int
    virtual_address: int
    raw_size: int
    raw_offset: int
    characteristics: int
    sha256: str

    @property
    def mapped_size(self) -> int:
        """Execute the mapped size operation for the current toolkit workflow."""
        return max(self.virtual_size, self.raw_size)

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "name": self.name,
            "virtual_size": self.virtual_size,
            "virtual_address": self.virtual_address,
            "virtual_address_hex": f"0x{self.virtual_address:08x}",
            "raw_size": self.raw_size,
            "raw_offset": self.raw_offset,
            "characteristics": self.characteristics,
            "characteristics_hex": f"0x{self.characteristics:08x}",
            "sha256": self.sha256,
        }


@dataclass(frozen=True)
class ImportSymbol:
    """Store validated import symbol fields used by toolkit reports and adapters."""
    name: str | None
    ordinal: int | None
    hint: int | None
    thunk_rva: int
    iat_rva: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "name": self.name,
            "ordinal": self.ordinal,
            "hint": self.hint,
            "thunk_rva": self.thunk_rva,
            "iat_rva": self.iat_rva,
        }


@dataclass(frozen=True)
class ImportLibrary:
    """Store validated import library fields used by toolkit reports and adapters."""
    name: str
    symbols: tuple[ImportSymbol, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"name": self.name, "symbols": [symbol.to_dict() for symbol in self.symbols]}


@dataclass(frozen=True)
class ExportSymbol:
    """Store validated export symbol fields used by toolkit reports and adapters."""
    name: str | None
    ordinal: int
    rva: int
    forwarder: str | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "name": self.name,
            "ordinal": self.ordinal,
            "rva": self.rva,
            "rva_hex": f"0x{self.rva:08x}",
            "forwarder": self.forwarder,
        }


@dataclass(frozen=True)
class BaseRelocation:
    """Store validated base relocation fields used by toolkit reports and adapters."""
    rva: int
    type: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"rva": self.rva, "rva_hex": f"0x{self.rva:08x}", "type": self.type}


@dataclass(frozen=True)
class DebugRecord:
    """Store validated debug record fields used by toolkit reports and adapters."""
    type: int
    timestamp: int
    size_of_data: int
    raw_data_offset: int
    codeview_signature: str | None
    pdb_path: str | None
    age: int | None
    guid_hex: str | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "type": self.type,
            "timestamp": self.timestamp,
            "size_of_data": self.size_of_data,
            "raw_data_offset": self.raw_data_offset,
            "codeview_signature": self.codeview_signature,
            "pdb_path": self.pdb_path,
            "age": self.age,
            "guid_hex": self.guid_hex,
        }


@dataclass(frozen=True)
class TLSInfo:
    """Store validated t l s info fields used by toolkit reports and adapters."""
    start_raw_data_va: int
    end_raw_data_va: int
    address_of_index_va: int
    address_of_callbacks_va: int
    zero_fill_size: int
    characteristics: int
    callbacks_va: tuple[int, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "start_raw_data_va": self.start_raw_data_va,
            "end_raw_data_va": self.end_raw_data_va,
            "address_of_index_va": self.address_of_index_va,
            "address_of_callbacks_va": self.address_of_callbacks_va,
            "zero_fill_size": self.zero_fill_size,
            "characteristics": self.characteristics,
            "callbacks_va": list(self.callbacks_va),
        }




@dataclass(frozen=True)
class ResourceLeaf:
    """Store validated resource leaf fields used by toolkit reports and adapters."""
    path: tuple[str, ...]
    data_rva: int
    size: int
    code_page: int
    sha256: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "path": list(self.path),
            "data_rva": self.data_rva,
            "data_rva_hex": f"0x{self.data_rva:08x}",
            "size": self.size,
            "code_page": self.code_page,
            "sha256": self.sha256,
        }


@dataclass(frozen=True)
class DelayImportLibrary:
    """Store validated delay import library fields used by toolkit reports and adapters."""
    name: str
    attributes: int
    iat_rva: int
    symbols: tuple[ImportSymbol, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "name": self.name,
            "attributes": self.attributes,
            "iat_rva": self.iat_rva,
            "symbols": [symbol.to_dict() for symbol in self.symbols],
        }


@dataclass(frozen=True)
class LoadConfigInfo:
    """Store validated load config info fields used by toolkit reports and adapters."""
    size: int
    timestamp: int | None
    major_version: int | None
    minor_version: int | None
    global_flags_clear: int | None
    global_flags_set: int | None
    security_cookie_va: int | None
    seh_table_va: int | None
    seh_count: int | None
    guard_cf_check_function_pointer_va: int | None
    guard_cf_dispatch_function_pointer_va: int | None
    guard_cf_function_table_va: int | None
    guard_cf_function_count: int | None
    guard_flags: int | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {key: value for key, value in {
            "size": self.size,
            "timestamp": self.timestamp,
            "major_version": self.major_version,
            "minor_version": self.minor_version,
            "global_flags_clear": self.global_flags_clear,
            "global_flags_set": self.global_flags_set,
            "security_cookie_va": self.security_cookie_va,
            "seh_table_va": self.seh_table_va,
            "seh_count": self.seh_count,
            "guard_cf_check_function_pointer_va": self.guard_cf_check_function_pointer_va,
            "guard_cf_dispatch_function_pointer_va": self.guard_cf_dispatch_function_pointer_va,
            "guard_cf_function_table_va": self.guard_cf_function_table_va,
            "guard_cf_function_count": self.guard_cf_function_count,
            "guard_flags": self.guard_flags,
        }.items()}


@dataclass(frozen=True)
class PE32Image:
    """Store validated p e32 image fields used by toolkit reports and adapters."""
    path: Path
    file_sha256: str
    machine: int
    number_of_sections: int
    timestamp: int
    characteristics: int
    image_base: int
    entry_rva: int
    section_alignment: int
    file_alignment: int
    size_of_image: int
    size_of_headers: int
    subsystem: int
    dll_characteristics: int
    checksum: int
    directories: tuple[DataDirectory, ...]
    sections: tuple[Section, ...]
    imports: tuple[ImportLibrary, ...]
    exports: tuple[ExportSymbol, ...]
    base_relocations: tuple[BaseRelocation, ...]
    debug_records: tuple[DebugRecord, ...]
    tls: TLSInfo | None
    resources: tuple[ResourceLeaf, ...]
    delay_imports: tuple[DelayImportLibrary, ...]
    load_config: LoadConfigInfo | None

    @property
    def entry_va(self) -> int:
        """Execute the entry va operation for the current toolkit workflow."""
        return self.image_base + self.entry_rva

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "format": "PE32",
            "architecture": "x86",
            "source_path": str(self.path),
            "file_sha256": self.file_sha256,
            "machine": self.machine,
            "machine_hex": f"0x{self.machine:04x}",
            "number_of_sections": self.number_of_sections,
            "timestamp": self.timestamp,
            "characteristics": self.characteristics,
            "characteristics_hex": f"0x{self.characteristics:04x}",
            "image_base": self.image_base,
            "image_base_hex": f"0x{self.image_base:08x}",
            "entry_rva": self.entry_rva,
            "entry_rva_hex": f"0x{self.entry_rva:08x}",
            "entry_va": self.entry_va,
            "entry_va_hex": f"0x{self.entry_va:08x}",
            "section_alignment": self.section_alignment,
            "file_alignment": self.file_alignment,
            "size_of_image": self.size_of_image,
            "size_of_headers": self.size_of_headers,
            "subsystem": self.subsystem,
            "dll_characteristics": self.dll_characteristics,
            "checksum": self.checksum,
            "directories": [directory.to_dict() for directory in self.directories],
            "sections": [section.to_dict() for section in self.sections],
            "imports": [library.to_dict() for library in self.imports],
            "exports": [symbol.to_dict() for symbol in self.exports],
            "base_relocations": [relocation.to_dict() for relocation in self.base_relocations],
            "debug_records": [record.to_dict() for record in self.debug_records],
            "tls": None if self.tls is None else self.tls.to_dict(),
            "resources": [resource.to_dict() for resource in self.resources],
            "delay_imports": [library.to_dict() for library in self.delay_imports],
            "load_config": None if self.load_config is None else self.load_config.to_dict(),
        }


class _Reader:
    """Coordinate reader behavior for the current toolkit workflow."""
    def __init__(self, data: bytes):
        """Initialize the instance with validated constructor state."""
        self.data = data

    def require(self, offset: int, size: int, context: str) -> None:
        """Execute the require operation for the current toolkit workflow."""
        if offset < 0 or size < 0 or offset + size > len(self.data):
            raise FormatError(
                f"{context} exceeds file bounds: offset={offset} size={size} file={len(self.data)}"
            )

    def unpack(self, fmt: str, offset: int, context: str) -> tuple[Any, ...]:
        """Execute the unpack operation for the current toolkit workflow."""
        size = struct.calcsize(fmt)
        self.require(offset, size, context)
        return struct.unpack_from(fmt, self.data, offset)

    def u16(self, offset: int, context: str) -> int:
        """Execute the u16 operation for the current toolkit workflow."""
        return int(self.unpack("<H", offset, context)[0])

    def u32(self, offset: int, context: str) -> int:
        """Execute the u32 operation for the current toolkit workflow."""
        return int(self.unpack("<I", offset, context)[0])

    def u64(self, offset: int, context: str) -> int:
        """Execute the u64 operation for the current toolkit workflow."""
        return int(self.unpack("<Q", offset, context)[0])

    def c_string(self, offset: int, context: str, max_length: int = 4096) -> str:
        """Execute the c string operation for the current toolkit workflow."""
        self.require(offset, 1, context)
        end_limit = min(len(self.data), offset + max_length)
        end = self.data.find(b"\x00", offset, end_limit)
        if end < 0:
            raise FormatError(f"unterminated string while reading {context}")
        return self.data[offset:end].decode("utf-8", errors="replace")


def _rva_to_offset(rva: int, sections: tuple[Section, ...], size_of_headers: int, file_size: int) -> int:
    """Support rva to offset processing for internal toolkit callers."""
    if rva < size_of_headers:
        if rva >= file_size:
            raise FormatError(f"header RVA 0x{rva:x} exceeds file size")
        return rva
    for section in sections:
        start = section.virtual_address
        end = start + section.mapped_size
        if start <= rva < end:
            delta = rva - start
            if delta >= section.raw_size:
                raise FormatError(
                    f"RVA 0x{rva:x} lies in zero-filled tail of section {section.name}"
                )
            offset = section.raw_offset + delta
            if offset >= file_size:
                raise FormatError(f"RVA 0x{rva:x} maps beyond file")
            return offset
    raise FormatError(f"RVA 0x{rva:x} is not mapped by any section")


def _directory(directories: tuple[DataDirectory, ...], name: str) -> DataDirectory:
    """Support directory processing for internal toolkit callers."""
    for directory in directories:
        if directory.name == name:
            return directory
    return DataDirectory(name=name, rva=0, size=0)


def _parse_imports(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> tuple[ImportLibrary, ...]:
    """Support parse imports processing for internal toolkit callers."""
    directory = _directory(directories, "import")
    if directory.rva == 0 or directory.size == 0:
        return ()
    descriptor_offset = _rva_to_offset(
        directory.rva, sections, size_of_headers, len(reader.data)
    )
    libraries: list[ImportLibrary] = []
    max_descriptors = max(1, directory.size // 20 + 1)
    for descriptor_index in range(max_descriptors):
        offset = descriptor_offset + descriptor_index * 20
        original_thunk, timestamp, forwarder_chain, name_rva, first_thunk = reader.unpack(
            "<IIIII", offset, "import descriptor"
        )
        if not any((original_thunk, timestamp, forwarder_chain, name_rva, first_thunk)):
            break
        if name_rva == 0 or first_thunk == 0:
            raise FormatError("import descriptor has a missing name or first thunk")
        library_name = reader.c_string(
            _rva_to_offset(name_rva, sections, size_of_headers, len(reader.data)),
            "import library name",
        )
        lookup_rva = original_thunk or first_thunk
        lookup_offset = _rva_to_offset(
            lookup_rva, sections, size_of_headers, len(reader.data)
        )
        symbols: list[ImportSymbol] = []
        max_thunks = 1_000_000
        for thunk_index in range(max_thunks):
            value = reader.u32(lookup_offset + thunk_index * 4, "import thunk")
            if value == 0:
                break
            thunk_rva = lookup_rva + thunk_index * 4
            iat_rva = first_thunk + thunk_index * 4
            if value & IMAGE_ORDINAL_FLAG32:
                symbols.append(
                    ImportSymbol(
                        name=None,
                        ordinal=value & 0xFFFF,
                        hint=None,
                        thunk_rva=thunk_rva,
                        iat_rva=iat_rva,
                    )
                )
            else:
                name_offset = _rva_to_offset(
                    value, sections, size_of_headers, len(reader.data)
                )
                hint = reader.u16(name_offset, "import hint")
                name = reader.c_string(name_offset + 2, "import symbol name")
                symbols.append(
                    ImportSymbol(
                        name=name,
                        ordinal=None,
                        hint=hint,
                        thunk_rva=thunk_rva,
                        iat_rva=iat_rva,
                    )
                )
        else:
            raise FormatError("import thunk table exceeds safety limit")
        libraries.append(ImportLibrary(name=library_name, symbols=tuple(symbols)))
    else:
        raise FormatError("import descriptor table has no terminator within its declared size")
    return tuple(libraries)


def _parse_exports(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> tuple[ExportSymbol, ...]:
    """Support parse exports processing for internal toolkit callers."""
    directory = _directory(directories, "export")
    if directory.rva == 0 or directory.size == 0:
        return ()
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    (
        _characteristics,
        _timestamp,
        _major,
        _minor,
        _name_rva,
        ordinal_base,
        function_count,
        name_count,
        functions_rva,
        names_rva,
        ordinals_rva,
    ) = reader.unpack("<IIHHIIIIIII", offset, "export directory")
    if function_count > 1_000_000 or name_count > 1_000_000:
        raise FormatError("export table exceeds safety limit")
    functions_offset = _rva_to_offset(
        functions_rva, sections, size_of_headers, len(reader.data)
    ) if function_count else 0
    names_offset = _rva_to_offset(names_rva, sections, size_of_headers, len(reader.data)) if name_count else 0
    ordinals_offset = _rva_to_offset(
        ordinals_rva, sections, size_of_headers, len(reader.data)
    ) if name_count else 0
    names_by_index: dict[int, str] = {}
    for index in range(name_count):
        name_rva = reader.u32(names_offset + index * 4, "export name pointer")
        ordinal_index = reader.u16(ordinals_offset + index * 2, "export ordinal index")
        if ordinal_index >= function_count:
            raise FormatError("export ordinal index exceeds function table")
        name = reader.c_string(
            _rva_to_offset(name_rva, sections, size_of_headers, len(reader.data)),
            "export name",
        )
        names_by_index[ordinal_index] = name
    exports: list[ExportSymbol] = []
    directory_end = directory.rva + directory.size
    for index in range(function_count):
        function_rva = reader.u32(functions_offset + index * 4, "export function RVA")
        if function_rva == 0:
            continue
        forwarder: str | None = None
        if directory.rva <= function_rva < directory_end:
            forwarder = reader.c_string(
                _rva_to_offset(function_rva, sections, size_of_headers, len(reader.data)),
                "export forwarder",
            )
        exports.append(
            ExportSymbol(
                name=names_by_index.get(index),
                ordinal=ordinal_base + index,
                rva=function_rva,
                forwarder=forwarder,
            )
        )
    return tuple(exports)


def _parse_relocations(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> tuple[BaseRelocation, ...]:
    """Support parse relocations processing for internal toolkit callers."""
    directory = _directory(directories, "base_relocation")
    if directory.rva == 0 or directory.size == 0:
        return ()
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    consumed = 0
    relocations: list[BaseRelocation] = []
    while consumed < directory.size:
        if directory.size - consumed < 8:
            raise FormatError("truncated base relocation block")
        page_rva, block_size = reader.unpack("<II", offset + consumed, "base relocation block")
        if page_rva == 0 and block_size == 0:
            break
        if block_size < 8 or block_size % 2 != 0 or consumed + block_size > directory.size:
            raise FormatError("invalid base relocation block size")
        entry_count = (block_size - 8) // 2
        for index in range(entry_count):
            value = reader.u16(offset + consumed + 8 + index * 2, "base relocation entry")
            relocation_type = value >> 12
            relocation_offset = value & 0x0FFF
            if relocation_type != 0:
                relocations.append(
                    BaseRelocation(rva=page_rva + relocation_offset, type=relocation_type)
                )
        consumed += block_size
    return tuple(relocations)


def _parse_debug_records(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> tuple[DebugRecord, ...]:
    """Support parse debug records processing for internal toolkit callers."""
    directory = _directory(directories, "debug")
    if directory.rva == 0 or directory.size == 0:
        return ()
    if directory.size % 28 != 0:
        raise FormatError("debug directory size is not a multiple of 28")
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    records: list[DebugRecord] = []
    for index in range(directory.size // 28):
        (
            _characteristics,
            timestamp,
            _major,
            _minor,
            debug_type,
            size_of_data,
            _address_of_raw_data,
            pointer_to_raw_data,
        ) = reader.unpack("<IIHHIIII", offset + index * 28, "debug directory entry")
        signature: str | None = None
        pdb_path: str | None = None
        age: int | None = None
        guid_hex: str | None = None
        if debug_type == 2 and size_of_data >= 4 and pointer_to_raw_data != 0:
            reader.require(pointer_to_raw_data, size_of_data, "CodeView record")
            blob = reader.data[pointer_to_raw_data : pointer_to_raw_data + size_of_data]
            if blob.startswith(b"RSDS") and len(blob) >= 24:
                signature = "RSDS"
                guid_hex = blob[4:20].hex()
                age = struct.unpack_from("<I", blob, 20)[0]
                end = blob.find(b"\x00", 24)
                if end < 0:
                    end = len(blob)
                pdb_path = blob[24:end].decode("utf-8", errors="replace")
            elif blob.startswith(b"NB10") and len(blob) >= 16:
                signature = "NB10"
                age = struct.unpack_from("<I", blob, 12)[0]
                end = blob.find(b"\x00", 16)
                if end < 0:
                    end = len(blob)
                pdb_path = blob[16:end].decode("utf-8", errors="replace")
        records.append(
            DebugRecord(
                type=debug_type,
                timestamp=timestamp,
                size_of_data=size_of_data,
                raw_data_offset=pointer_to_raw_data,
                codeview_signature=signature,
                pdb_path=pdb_path,
                age=age,
                guid_hex=guid_hex,
            )
        )
    return tuple(records)


def _parse_tls(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
    image_base: int,
) -> TLSInfo | None:
    """Support parse tls processing for internal toolkit callers."""
    directory = _directory(directories, "tls")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    (
        start_raw_data_va,
        end_raw_data_va,
        address_of_index_va,
        address_of_callbacks_va,
        zero_fill_size,
        characteristics,
    ) = reader.unpack("<IIIIII", offset, "PE32 TLS directory")
    callbacks: list[int] = []
    if address_of_callbacks_va:
        if address_of_callbacks_va < image_base:
            raise FormatError("TLS callback address is below image base")
        callbacks_rva = address_of_callbacks_va - image_base
        callbacks_offset = _rva_to_offset(
            callbacks_rva, sections, size_of_headers, len(reader.data)
        )
        for index in range(65_536):
            callback_va = reader.u32(callbacks_offset + index * 4, "TLS callback")
            if callback_va == 0:
                break
            callbacks.append(callback_va)
        else:
            raise FormatError("TLS callback table exceeds safety limit")
    return TLSInfo(
        start_raw_data_va=start_raw_data_va,
        end_raw_data_va=end_raw_data_va,
        address_of_index_va=address_of_index_va,
        address_of_callbacks_va=address_of_callbacks_va,
        zero_fill_size=zero_fill_size,
        characteristics=characteristics,
        callbacks_va=tuple(callbacks),
    )



def _parse_resources(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> tuple[ResourceLeaf, ...]:
    """Support parse resources processing for internal toolkit callers."""
    directory = _directory(directories, "resource")
    if directory.rva == 0 or directory.size == 0:
        return ()
    base_offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    reader.require(base_offset, directory.size, "resource directory")
    leaves: list[ResourceLeaf] = []
    visited: set[int] = set()
    entry_budget = 100_000

    def read_name(raw: int) -> str:
        """Read name for the current toolkit workflow."""
        if raw & 0x80000000:
            relative = raw & 0x7FFFFFFF
            offset = base_offset + relative
            length = reader.u16(offset, "resource name length")
            reader.require(offset + 2, length * 2, "resource UTF-16 name")
            return reader.data[offset + 2 : offset + 2 + length * 2].decode("utf-16le", errors="replace")
        return f"id:{raw}"

    def walk(relative: int, path: tuple[str, ...], depth: int) -> None:
        """Execute the walk operation for the current toolkit workflow."""
        nonlocal entry_budget
        if depth > 8:
            raise FormatError("resource tree exceeds maximum depth")
        if relative in visited:
            raise FormatError("resource tree contains a directory cycle")
        visited.add(relative)
        offset = base_offset + relative
        reader.require(offset, 16, "resource directory node")
        named_count = reader.u16(offset + 12, "resource named entry count")
        id_count = reader.u16(offset + 14, "resource id entry count")
        count = named_count + id_count
        entry_budget -= count
        if entry_budget < 0:
            raise FormatError("resource tree exceeds safety entry limit")
        reader.require(offset + 16, count * 8, "resource directory entries")
        for index in range(count):
            name_raw, data_raw = reader.unpack("<II", offset + 16 + index * 8, "resource directory entry")
            component = read_name(name_raw)
            if data_raw & 0x80000000:
                walk(data_raw & 0x7FFFFFFF, path + (component,), depth + 1)
            else:
                data_entry_offset = base_offset + data_raw
                data_rva, size, code_page, _reserved = reader.unpack("<IIII", data_entry_offset, "resource data entry")
                data_offset = _rva_to_offset(data_rva, sections, size_of_headers, len(reader.data))
                reader.require(data_offset, size, "resource payload")
                leaves.append(
                    ResourceLeaf(
                        path=path + (component,),
                        data_rva=data_rva,
                        size=size,
                        code_page=code_page,
                        sha256=sha256_bytes(reader.data[data_offset : data_offset + size]),
                    )
                )
        visited.remove(relative)

    walk(0, (), 0)
    return tuple(leaves)


def _parse_delay_imports(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
    image_base: int,
) -> tuple[DelayImportLibrary, ...]:
    """Support parse delay imports processing for internal toolkit callers."""
    directory = _directory(directories, "delay_import")
    if directory.rva == 0 or directory.size == 0:
        return ()
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    libraries: list[DelayImportLibrary] = []
    max_descriptors = min(65_536, max(1, directory.size // 32 + 1))
    for descriptor_index in range(max_descriptors):
        fields = reader.unpack("<IIIIIIII", offset + descriptor_index * 32, "delay import descriptor")
        if not any(fields):
            break
        attributes, name_value, _module_handle, iat_value, int_value, _bound_iat, _unload_iat, _timestamp = fields
        rva_based = bool(attributes & 1)

        def to_rva(value: int) -> int:
            """Execute the to rva operation for the current toolkit workflow."""
            if value == 0:
                return 0
            if rva_based:
                return value
            if value < image_base:
                raise FormatError("delay import VA is below image base")
            return value - image_base

        name_rva = to_rva(name_value)
        iat_rva = to_rva(iat_value)
        lookup_rva = to_rva(int_value) or iat_rva
        if name_rva == 0 or iat_rva == 0 or lookup_rva == 0:
            raise FormatError("delay import descriptor has missing required fields")
        name = reader.c_string(_rva_to_offset(name_rva, sections, size_of_headers, len(reader.data)), "delay import library name")
        lookup_offset = _rva_to_offset(lookup_rva, sections, size_of_headers, len(reader.data))
        symbols: list[ImportSymbol] = []
        for thunk_index in range(1_000_000):
            value = reader.u32(lookup_offset + thunk_index * 4, "delay import thunk")
            if value == 0:
                break
            thunk_rva = lookup_rva + thunk_index * 4
            symbol_iat_rva = iat_rva + thunk_index * 4
            if value & IMAGE_ORDINAL_FLAG32:
                symbols.append(ImportSymbol(name=None, ordinal=value & 0xFFFF, hint=None, thunk_rva=thunk_rva, iat_rva=symbol_iat_rva))
            else:
                hint_name_rva = to_rva(value)
                hint_name_offset = _rva_to_offset(hint_name_rva, sections, size_of_headers, len(reader.data))
                hint = reader.u16(hint_name_offset, "delay import hint")
                symbol_name = reader.c_string(hint_name_offset + 2, "delay import symbol name")
                symbols.append(ImportSymbol(name=symbol_name, ordinal=None, hint=hint, thunk_rva=thunk_rva, iat_rva=symbol_iat_rva))
        else:
            raise FormatError("delay import thunk table exceeds safety limit")
        libraries.append(DelayImportLibrary(name=name, attributes=attributes, iat_rva=iat_rva, symbols=tuple(symbols)))
    else:
        raise FormatError("delay import descriptor table has no terminator")
    return tuple(libraries)


def _parse_load_config(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> LoadConfigInfo | None:
    """Support parse load config processing for internal toolkit callers."""
    directory = _directory(directories, "load_config")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    size = reader.u32(offset, "load config size")
    available = min(size, directory.size)
    if available < 4:
        raise FormatError("load config directory is too small")

    def u16_at(relative: int) -> int | None:
        """Execute the u16 at operation for the current toolkit workflow."""
        return reader.u16(offset + relative, "load config field") if available >= relative + 2 else None

    def u32_at(relative: int) -> int | None:
        """Execute the u32 at operation for the current toolkit workflow."""
        return reader.u32(offset + relative, "load config field") if available >= relative + 4 else None

    return LoadConfigInfo(
        size=size,
        timestamp=u32_at(4),
        major_version=u16_at(8),
        minor_version=u16_at(10),
        global_flags_clear=u32_at(12),
        global_flags_set=u32_at(16),
        security_cookie_va=u32_at(60),
        seh_table_va=u32_at(64),
        seh_count=u32_at(68),
        guard_cf_check_function_pointer_va=u32_at(72),
        guard_cf_dispatch_function_pointer_va=u32_at(76),
        guard_cf_function_table_va=u32_at(80),
        guard_cf_function_count=u32_at(84),
        guard_flags=u32_at(88),
    )

def parse_pe32(path: Path) -> PE32Image:
    """Parse pe32 for the current toolkit workflow."""
    path = path.resolve()
    if not path.is_file():
        raise FormatError(f"binary does not exist: {path}")
    data = path.read_bytes()
    reader = _Reader(data)
    reader.require(0, 64, "DOS header")
    if data[0:2] != b"MZ":
        raise FormatError("missing DOS MZ signature")
    pe_offset = reader.u32(0x3C, "DOS e_lfanew")
    reader.require(pe_offset, 24, "PE signature and COFF header")
    if data[pe_offset : pe_offset + 4] != b"PE\x00\x00":
        raise FormatError("missing PE signature")
    coff_offset = pe_offset + 4
    (
        machine,
        number_of_sections,
        timestamp,
        _pointer_to_symbols,
        _number_of_symbols,
        optional_header_size,
        characteristics,
    ) = reader.unpack("<HHIIIHH", coff_offset, "COFF header")
    if machine != IMAGE_FILE_MACHINE_I386:
        raise FormatError(
            f"unsupported machine 0x{machine:04x}; first release supports IMAGE_FILE_MACHINE_I386"
        )
    if number_of_sections == 0 or number_of_sections > 96:
        raise FormatError(f"invalid section count: {number_of_sections}")
    optional_offset = coff_offset + 20
    reader.require(optional_offset, optional_header_size, "optional header")
    magic = reader.u16(optional_offset, "optional header magic")
    if magic != PE32_MAGIC:
        raise FormatError(f"unsupported optional header magic 0x{magic:04x}; expected PE32")
    if optional_header_size < 96:
        raise FormatError("PE32 optional header is too small")

    entry_rva = reader.u32(optional_offset + 16, "AddressOfEntryPoint")
    image_base = reader.u32(optional_offset + 28, "ImageBase")
    section_alignment = reader.u32(optional_offset + 32, "SectionAlignment")
    file_alignment = reader.u32(optional_offset + 36, "FileAlignment")
    size_of_image = reader.u32(optional_offset + 56, "SizeOfImage")
    size_of_headers = reader.u32(optional_offset + 60, "SizeOfHeaders")
    checksum = reader.u32(optional_offset + 64, "CheckSum")
    subsystem = reader.u16(optional_offset + 68, "Subsystem")
    dll_characteristics = reader.u16(optional_offset + 70, "DllCharacteristics")
    directory_count = reader.u32(optional_offset + 92, "NumberOfRvaAndSizes")
    available_directory_count = max(0, (optional_header_size - 96) // 8)
    parsed_directory_count = min(directory_count, available_directory_count, len(DIRECTORY_NAMES))
    directories_list: list[DataDirectory] = []
    for index, name in enumerate(DIRECTORY_NAMES):
        if index < parsed_directory_count:
            rva, size = reader.unpack(
                "<II", optional_offset + 96 + index * 8, f"data directory {name}"
            )
            directories_list.append(DataDirectory(name=name, rva=rva, size=size))
        else:
            directories_list.append(DataDirectory(name=name, rva=0, size=0))
    directories = tuple(directories_list)

    section_offset = optional_offset + optional_header_size
    sections_list: list[Section] = []
    seen_names: set[str] = set()
    for index in range(number_of_sections):
        offset = section_offset + index * 40
        reader.require(offset, 40, f"section header {index}")
        raw_name = data[offset : offset + 8]
        name = raw_name.split(b"\x00", 1)[0].decode("ascii", errors="replace") or f"section_{index}"
        virtual_size, virtual_address, raw_size, raw_offset = reader.unpack(
            "<IIII", offset + 8, f"section header {name}"
        )
        characteristics_value = reader.u32(offset + 36, f"section characteristics {name}")
        if raw_size:
            reader.require(raw_offset, raw_size, f"section raw data {name}")
            digest = sha256_bytes(data[raw_offset : raw_offset + raw_size])
        else:
            digest = sha256_bytes(b"")
        unique_name = name
        suffix = 1
        while unique_name in seen_names:
            suffix += 1
            unique_name = f"{name}#{suffix}"
        seen_names.add(unique_name)
        sections_list.append(
            Section(
                name=unique_name,
                virtual_size=virtual_size,
                virtual_address=virtual_address,
                raw_size=raw_size,
                raw_offset=raw_offset,
                characteristics=characteristics_value,
                sha256=digest,
            )
        )
    sections = tuple(sections_list)

    imports = _parse_imports(reader, directories, sections, size_of_headers)
    exports = _parse_exports(reader, directories, sections, size_of_headers)
    base_relocations = _parse_relocations(reader, directories, sections, size_of_headers)
    debug_records = _parse_debug_records(reader, directories, sections, size_of_headers)
    tls = _parse_tls(reader, directories, sections, size_of_headers, image_base)
    resources = _parse_resources(reader, directories, sections, size_of_headers)
    delay_imports = _parse_delay_imports(reader, directories, sections, size_of_headers, image_base)
    load_config = _parse_load_config(reader, directories, sections, size_of_headers)

    return PE32Image(
        path=path,
        file_sha256=sha256_bytes(data),
        machine=machine,
        number_of_sections=number_of_sections,
        timestamp=timestamp,
        characteristics=characteristics,
        image_base=image_base,
        entry_rva=entry_rva,
        section_alignment=section_alignment,
        file_alignment=file_alignment,
        size_of_image=size_of_image,
        size_of_headers=size_of_headers,
        subsystem=subsystem,
        dll_characteristics=dll_characteristics,
        checksum=checksum,
        directories=directories,
        sections=sections,
        imports=imports,
        exports=exports,
        base_relocations=base_relocations,
        debug_records=debug_records,
        tls=tls,
        resources=resources,
        delay_imports=delay_imports,
        load_config=load_config,
    )
