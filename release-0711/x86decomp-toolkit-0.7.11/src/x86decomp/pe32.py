"""Strict, dependency-free parser for native x86 PE32 images.

The parser intentionally supports the first toolkit scope only: little-endian
Windows PE32 images for IMAGE_FILE_MACHINE_I386. It never executes the input.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .binary_reader import BinaryReader
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

#: Upper bound on entries scanned while walking a null-terminated import or
#: delay-import thunk array. The arrays are terminated by a zero entry; this
#: cap prevents an unbounded loop on a malformed or hostile PE image.
MAX_IMPORT_THUNKS = 1_000_000
#: Upper bound on entries scanned while walking the null-terminated TLS
#: callback array, guarding against malformed or hostile PE images.
MAX_TLS_CALLBACKS = 65_536


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
        """Return the on-disk footprint of the section as the larger of its virtual and raw sizes."""
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
        """Return the entry point as a virtual address (image base plus entry RVA)."""
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


_Reader = BinaryReader

def _rva_to_offset(rva: int, sections: tuple[Section, ...], size_of_headers: int, file_size: int) -> int:
    """Map a relative virtual address to its file offset.

    Args:
        rva: Relative virtual address to translate.
        sections: Parsed section table used to locate the containing section.
        size_of_headers: Size of the PE headers; RVAs below this map directly to the file.
        file_size: Total length of the backing file, used for bounds checks.

    Returns:
        The file offset corresponding to ``rva``.

    Raises:
        FormatError: If the RVA lies in a section's zero-filled tail, maps beyond the
            file, or is not covered by the headers or any section.
    """
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
    """Return the named data directory, or an empty directory if it is absent.

    Args:
        directories: Parsed data directory entries.
        name: Directory name to look up (for example ``"import"``).

    Returns:
        The matching :class:`DataDirectory`, or one with zero RVA and size when not found.
    """
    for directory in directories:
        if directory.name == name:
            return directory
    return DataDirectory(name=name, rva=0, size=0)


def _parse_thunk_symbols(
    reader: _Reader,
    sections: tuple[Section, ...],
    size_of_headers: int,
    lookup_rva: int,
    iat_rva: int,
    *,
    pointer_size: int,
    ordinal_flag: int,
    context: str,
    value_to_rva: Callable[[int], int] | None = None,
) -> tuple[ImportSymbol, ...]:
    """Parse a bounded import-thunk array for either PE32 or PE32+."""
    if pointer_size not in (4, 8):
        raise ValueError("pointer_size must be 4 or 8")
    lookup_offset = _rva_to_offset(lookup_rva, sections, size_of_headers, len(reader.data))
    read_value = reader.u32 if pointer_size == 4 else reader.u64
    convert = value_to_rva or (lambda value: value)
    symbols: list[ImportSymbol] = []
    for index in range(MAX_IMPORT_THUNKS):
        value = read_value(lookup_offset + index * pointer_size, f"{context} thunk")
        if value == 0:
            break
        thunk_rva = lookup_rva + index * pointer_size
        symbol_iat_rva = iat_rva + index * pointer_size
        if value & ordinal_flag:
            symbols.append(ImportSymbol(None, value & 0xFFFF, None, thunk_rva, symbol_iat_rva))
            continue
        hint_name_rva = convert(value)
        hint_name_offset = _rva_to_offset(
            hint_name_rva, sections, size_of_headers, len(reader.data)
        )
        symbols.append(
            ImportSymbol(
                reader.c_string(hint_name_offset + 2, f"{context} symbol name"),
                None,
                reader.u16(hint_name_offset, f"{context} hint"),
                thunk_rva,
                symbol_iat_rva,
            )
        )
    else:
        raise FormatError(f"{context} thunk table exceeds safety limit")
    return tuple(symbols)


def _parse_tls_callbacks(
    reader: _Reader,
    sections: tuple[Section, ...],
    size_of_headers: int,
    callbacks_va: int,
    image_base: int,
    *,
    pointer_size: int,
    context: str,
) -> tuple[int, ...]:
    """Parse a bounded null-terminated TLS callback array for either PE width."""
    if callbacks_va == 0:
        return ()
    if callbacks_va < image_base:
        raise FormatError("TLS callback address is below image base")
    callback_offset = _rva_to_offset(
        callbacks_va - image_base, sections, size_of_headers, len(reader.data)
    )
    read_value = reader.u32 if pointer_size == 4 else reader.u64
    callbacks: list[int] = []
    for index in range(MAX_TLS_CALLBACKS):
        callback = read_value(callback_offset + index * pointer_size, f"{context} callback")
        if callback == 0:
            break
        callbacks.append(callback)
    else:
        raise FormatError("TLS callback table exceeds safety limit")
    return tuple(callbacks)


def _parse_imports(
    reader: _Reader,
    directories: tuple[DataDirectory, ...],
    sections: tuple[Section, ...],
    size_of_headers: int,
) -> tuple[ImportLibrary, ...]:
    """Parse the import directory into resolved import libraries and symbols.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A tuple of :class:`ImportLibrary` records, empty when the image has no imports.

    Raises:
        FormatError: If a descriptor is missing its name or first thunk, or a thunk
            table or descriptor table exceeds its safety limit or lacks a terminator.
    """
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
        symbols = _parse_thunk_symbols(
            reader,
            sections,
            size_of_headers,
            lookup_rva,
            first_thunk,
            pointer_size=4,
            ordinal_flag=IMAGE_ORDINAL_FLAG32,
            context="import",
        )
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
    """Parse the export directory into resolved export symbols.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A tuple of :class:`ExportSymbol` records, empty when the image exports nothing.

    Raises:
        FormatError: If the function or name count exceeds the safety limit, or an
            ordinal index points past the function table.
    """
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
    """Parse the base relocation directory into individual relocation entries.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A tuple of :class:`BaseRelocation` records; padding entries (type 0) are omitted.

    Raises:
        FormatError: If a relocation block is truncated or declares an invalid size.
    """
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
    """Parse the debug directory, decoding CodeView RSDS/NB10 records when present.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A tuple of :class:`DebugRecord` entries, empty when no debug directory exists.

    Raises:
        FormatError: If the debug directory size is not a multiple of the 28-byte entry.
    """
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
    """Parse the TLS directory, resolving the callback array when present.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.
        image_base: Preferred image base, used to convert callback VAs to RVAs.

    Returns:
        A :class:`TLSInfo` record, or ``None`` when the image has no TLS directory.

    Raises:
        FormatError: If a callback address is below the image base or the callback
            table exceeds :data:`MAX_TLS_CALLBACKS`.
    """
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
    callbacks = _parse_tls_callbacks(
        reader,
        sections,
        size_of_headers,
        address_of_callbacks_va,
        image_base,
        pointer_size=4,
        context="PE32 TLS",
    )
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
    """Parse the resource directory tree into a flat tuple of resource leaves.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A tuple of :class:`ResourceLeaf` records, empty when no resource directory exists.

    Raises:
        FormatError: If the resource tree is malformed, cyclic, or exceeds depth or
            entry safety limits.
    """
    directory = _directory(directories, "resource")
    if directory.rva == 0 or directory.size == 0:
        return ()
    base_offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    reader.require(base_offset, directory.size, "resource directory")
    leaves: list[ResourceLeaf] = []
    visited: set[int] = set()
    entry_budget = 100_000

    def read_name(raw: int) -> str:
        """Decode a resource directory entry name.

        Args:
            raw: The raw name field; the high bit selects a UTF-16 string offset,
                otherwise the low bits are a numeric identifier.

        Returns:
            The decoded UTF-16 name, or ``"id:<n>"`` for a numeric identifier.
        """
        if raw & 0x80000000:
            relative = raw & 0x7FFFFFFF
            offset = base_offset + relative
            length = reader.u16(offset, "resource name length")
            reader.require(offset + 2, length * 2, "resource UTF-16 name")
            return reader.data[offset + 2 : offset + 2 + length * 2].decode("utf-16le", errors="replace")
        return f"id:{raw}"

    def walk(relative: int, path: tuple[str, ...], depth: int) -> None:
        """Recursively traverse a resource directory node, collecting leaf payloads.

        Args:
            relative: Offset of the node relative to the resource directory base.
            path: Accumulated name components leading to this node.
            depth: Current recursion depth, used to enforce the maximum tree depth.

        Raises:
            FormatError: If the tree exceeds the maximum depth, contains a directory
                cycle, or exceeds the safety entry budget.
        """
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
    """Parse the delay-import directory into resolved libraries and symbols.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.
        image_base: Preferred image base, used to convert VA-based fields to RVAs.

    Returns:
        A tuple of :class:`DelayImportLibrary` records, empty when the image has none.

    Raises:
        FormatError: If a descriptor VA is below the image base, a descriptor is missing
            required fields, or a thunk or descriptor table exceeds its safety limit.
    """
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
            """Convert a descriptor field to an RVA, honoring the RVA-based attribute flag.

            Args:
                value: The raw field value; interpreted as an RVA when the descriptor
                    is RVA-based, otherwise as a virtual address relative to the image base.

            Returns:
                The corresponding RVA, or ``0`` when ``value`` is ``0``.

            Raises:
                FormatError: If a VA-based value is below the image base.
            """
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
        symbols = _parse_thunk_symbols(
            reader,
            sections,
            size_of_headers,
            lookup_rva,
            iat_rva,
            pointer_size=4,
            ordinal_flag=IMAGE_ORDINAL_FLAG32,
            context="delay import",
            value_to_rva=to_rva,
        )
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
    """Parse the load configuration directory, reading fields present within its size.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A :class:`LoadConfigInfo` record, or ``None`` when no load config directory exists.

    Raises:
        FormatError: If the load config directory is too small to hold its size field.
    """
    directory = _directory(directories, "load_config")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    size = reader.u32(offset, "load config size")
    available = min(size, directory.size)
    if available < 4:
        raise FormatError("load config directory is too small")

    return LoadConfigInfo(
        size=size,
        timestamp=reader.optional_u32(offset, 4, available, "load config field"),
        major_version=reader.optional_u16(offset, 8, available, "load config field"),
        minor_version=reader.optional_u16(offset, 10, available, "load config field"),
        global_flags_clear=reader.optional_u32(offset, 12, available, "load config field"),
        global_flags_set=reader.optional_u32(offset, 16, available, "load config field"),
        security_cookie_va=reader.optional_u32(offset, 60, available, "load config field"),
        seh_table_va=reader.optional_u32(offset, 64, available, "load config field"),
        seh_count=reader.optional_u32(offset, 68, available, "load config field"),
        guard_cf_check_function_pointer_va=reader.optional_u32(offset, 72, available, "load config field"),
        guard_cf_dispatch_function_pointer_va=reader.optional_u32(offset, 76, available, "load config field"),
        guard_cf_function_table_va=reader.optional_u32(offset, 80, available, "load config field"),
        guard_cf_function_count=reader.optional_u32(offset, 84, available, "load config field"),
        guard_flags=reader.optional_u32(offset, 88, available, "load config field"),
    )

def parse_pe32(path: Path) -> PE32Image:
    """Parse a little-endian x86 PE32 image into a fully resolved :class:`PE32Image`.

    The file is read but never executed. Headers, the section table, and every parsed
    data directory (imports, exports, relocations, debug, TLS, resources, delay imports,
    and load config) are validated as they are decoded.

    Args:
        path: Filesystem path to the PE32 binary to parse.

    Returns:
        A :class:`PE32Image` describing the binary.

    Raises:
        FormatError: If the file does not exist, lacks the MZ or PE signatures, targets a
            machine other than IMAGE_FILE_MACHINE_I386, is not a PE32 optional-header image,
            or is otherwise structurally invalid.
    """
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
