"""Architecture-dispatching PE parser with PE32+ x86-64 support."""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import FormatError
from .pe32 import (
    BaseRelocation,
    DataDirectory,
    DebugRecord,
    DelayImportLibrary,
    ExportSymbol,
    ImportLibrary,
    LoadConfigInfo,
    ResourceLeaf,
    Section,
    _Reader,
    _directory,
    _parse_debug_records,
    _parse_exports,
    _parse_relocations,
    _parse_resources,
    _parse_thunk_symbols,
    _parse_tls_callbacks,
    _rva_to_offset,
    parse_pe32,
)
from .util import sha256_bytes

IMAGE_FILE_MACHINE_AMD64 = 0x8664
PE32_PLUS_MAGIC = 0x020B
IMAGE_ORDINAL_FLAG64 = 0x8000000000000000
DIRECTORY_NAMES = (
    "export", "import", "resource", "exception", "certificate", "base_relocation", "debug", "architecture",
    "global_pointer", "tls", "load_config", "bound_import", "iat", "delay_import", "clr_runtime", "reserved",
)

#: Upper bound on entries scanned while walking a null-terminated import or
#: delay-import thunk array. The arrays are terminated by a zero entry; this
#: cap prevents an unbounded loop on a malformed or hostile PE image.
MAX_IMPORT_THUNKS = 1_000_000
#: Upper bound on entries scanned while walking the null-terminated TLS
#: callback array, guarding against malformed or hostile PE images.
MAX_TLS_CALLBACKS = 65_536


@dataclass(frozen=True)
class TLS64Info:
    """Store validated t l s64 info fields used by toolkit reports and adapters."""
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
class RuntimeFunction:
    """Store validated runtime function fields used by toolkit reports and adapters."""
    begin_rva: int
    end_rva: int
    unwind_info_rva: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "begin_rva": self.begin_rva,
            "end_rva": self.end_rva,
            "unwind_info_rva": self.unwind_info_rva,
        }


@dataclass(frozen=True)
class PE64Image:
    """Store validated p e64 image fields used by toolkit reports and adapters."""
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
    tls: TLS64Info | None
    resources: tuple[ResourceLeaf, ...]
    delay_imports: tuple[DelayImportLibrary, ...]
    load_config: LoadConfigInfo | None
    runtime_functions: tuple[RuntimeFunction, ...]

    @property
    def entry_va(self) -> int:
        """Return the entry point as a virtual address (image base plus entry RVA)."""
        return self.image_base + self.entry_rva

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 2,
            "format": "PE32+",
            "architecture": "x86_64",
            "source_path": str(self.path),
            "file_sha256": self.file_sha256,
            "machine": self.machine,
            "machine_hex": f"0x{self.machine:04x}",
            "number_of_sections": self.number_of_sections,
            "timestamp": self.timestamp,
            "characteristics": self.characteristics,
            "characteristics_hex": f"0x{self.characteristics:04x}",
            "image_base": self.image_base,
            "image_base_hex": f"0x{self.image_base:016x}",
            "entry_rva": self.entry_rva,
            "entry_rva_hex": f"0x{self.entry_rva:08x}",
            "entry_va": self.entry_va,
            "entry_va_hex": f"0x{self.entry_va:016x}",
            "section_alignment": self.section_alignment,
            "file_alignment": self.file_alignment,
            "size_of_image": self.size_of_image,
            "size_of_headers": self.size_of_headers,
            "subsystem": self.subsystem,
            "dll_characteristics": self.dll_characteristics,
            "checksum": self.checksum,
            "directories": [item.to_dict() for item in self.directories],
            "sections": [item.to_dict() for item in self.sections],
            "imports": [item.to_dict() for item in self.imports],
            "exports": [item.to_dict() for item in self.exports],
            "base_relocations": [item.to_dict() for item in self.base_relocations],
            "debug_records": [item.to_dict() for item in self.debug_records],
            "tls": None if self.tls is None else self.tls.to_dict(),
            "resources": [item.to_dict() for item in self.resources],
            "delay_imports": [item.to_dict() for item in self.delay_imports],
            "load_config": None if self.load_config is None else self.load_config.to_dict(),
            "runtime_functions": [item.to_dict() for item in self.runtime_functions],
        }


def _parse_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ImportLibrary, ...]:
    """Parse the PE32+ import directory into resolved import libraries and symbols.

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
    descriptor_offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    libraries: list[ImportLibrary] = []
    for descriptor_index in range(min(65_536, max(1, directory.size // 20 + 1))):
        original_thunk, timestamp, forwarder_chain, name_rva, first_thunk = reader.unpack("<IIIII", descriptor_offset + descriptor_index * 20, "import descriptor")
        if not any((original_thunk, timestamp, forwarder_chain, name_rva, first_thunk)):
            break
        if name_rva == 0 or first_thunk == 0:
            raise FormatError("import descriptor has a missing name or first thunk")
        name = reader.c_string(_rva_to_offset(name_rva, sections, size_of_headers, len(reader.data)), "import library name")
        lookup_rva = original_thunk or first_thunk
        symbols = _parse_thunk_symbols(
            reader,
            sections,
            size_of_headers,
            lookup_rva,
            first_thunk,
            pointer_size=8,
            ordinal_flag=IMAGE_ORDINAL_FLAG64,
            context="PE32+ import",
        )
        libraries.append(ImportLibrary(name, tuple(symbols)))
    else:
        raise FormatError("import descriptor table has no terminator")
    return tuple(libraries)


def _parse_tls64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> TLS64Info | None:
    """Parse the PE32+ TLS directory, resolving the 64-bit callback array when present.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.
        image_base: Preferred image base, used to convert callback VAs to RVAs.

    Returns:
        A :class:`TLS64Info` record, or ``None`` when the image has no TLS directory.

    Raises:
        FormatError: If a callback address is below the image base or the callback
            table exceeds :data:`MAX_TLS_CALLBACKS`.
    """
    directory = _directory(directories, "tls")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    start, end, index_va, callbacks_va, zero_fill, characteristics = reader.unpack("<QQQQII", offset, "PE32+ TLS directory")
    callbacks = _parse_tls_callbacks(
        reader,
        sections,
        size_of_headers,
        callbacks_va,
        image_base,
        pointer_size=8,
        context="PE32+ TLS",
    )
    return TLS64Info(start, end, index_va, callbacks_va, zero_fill, characteristics, tuple(callbacks))


def _parse_delay_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> tuple[DelayImportLibrary, ...]:
    """Parse the PE32+ delay-import directory into resolved libraries and symbols.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.
        image_base: Preferred image base, used to convert VA-based fields to RVAs.

    Returns:
        A tuple of :class:`DelayImportLibrary` records, empty when the image has none.

    Raises:
        FormatError: If a descriptor VA is below the image base, or a thunk or
            descriptor table exceeds its safety limit or lacks a terminator.
    """
    directory = _directory(directories, "delay_import")
    if directory.rva == 0 or directory.size == 0:
        return ()
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    libraries: list[DelayImportLibrary] = []
    for descriptor_index in range(min(65_536, max(1, directory.size // 32 + 1))):
        fields = reader.unpack("<IIIIIIII", offset + descriptor_index * 32, "delay import descriptor")
        if not any(fields):
            break
        attributes, name_value, _hmod, iat_value, int_value, _bound, _unload, _timestamp = fields
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
        name_rva, iat_rva, lookup_rva = to_rva(name_value), to_rva(iat_value), to_rva(int_value) or to_rva(iat_value)
        name = reader.c_string(_rva_to_offset(name_rva, sections, size_of_headers, len(reader.data)), "delay import name")
        symbols = _parse_thunk_symbols(
            reader,
            sections,
            size_of_headers,
            lookup_rva,
            iat_rva,
            pointer_size=8,
            ordinal_flag=IMAGE_ORDINAL_FLAG64,
            context="PE32+ delay import",
            value_to_rva=to_rva,
        )
        libraries.append(DelayImportLibrary(name, attributes, iat_rva, tuple(symbols)))
    else:
        raise FormatError("delay import descriptor table has no terminator")
    return tuple(libraries)


def _parse_load_config64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> LoadConfigInfo | None:
    """Parse the PE32+ load configuration directory, reading fields within its size.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A :class:`LoadConfigInfo` record, or ``None`` when no load config directory exists.
    """
    directory = _directory(directories, "load_config")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    size = reader.u32(offset, "load config size")
    available = min(size, directory.size)
    return LoadConfigInfo(
        size=size, timestamp=reader.optional_u32(offset, 4, available, "load config field"), major_version=reader.optional_u16(offset, 8, available, "load config field"), minor_version=reader.optional_u16(offset, 10, available, "load config field"), global_flags_clear=reader.optional_u32(offset, 12, available, "load config field"), global_flags_set=reader.optional_u32(offset, 16, available, "load config field"),
        security_cookie_va=reader.optional_u64(offset, 88, available, "load config field"), seh_table_va=None, seh_count=None,
        guard_cf_check_function_pointer_va=reader.optional_u64(offset, 112, available, "load config field"), guard_cf_dispatch_function_pointer_va=reader.optional_u64(offset, 120, available, "load config field"),
        guard_cf_function_table_va=reader.optional_u64(offset, 128, available, "load config field"), guard_cf_function_count=reader.optional_u64(offset, 136, available, "load config field"), guard_flags=reader.optional_u32(offset, 144, available, "load config field"),
    )


def _parse_runtime_functions(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[RuntimeFunction, ...]:
    """Parse the x64 exception directory into its RUNTIME_FUNCTION table.

    Args:
        reader: Binary reader over the PE image bytes.
        directories: Parsed data directory entries.
        sections: Parsed section table used for RVA translation.
        size_of_headers: Size of the PE headers, used for RVA translation.

    Returns:
        A tuple of :class:`RuntimeFunction` records, empty when no exception directory exists.

    Raises:
        FormatError: If the exception directory size is not a multiple of the 12-byte entry.
    """
    directory = _directory(directories, "exception")
    if directory.rva == 0 or directory.size == 0:
        return ()
    if directory.size % 12 != 0:
        raise FormatError("x64 exception directory size is not a multiple of 12")
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    return tuple(RuntimeFunction(*reader.unpack("<III", offset + index * 12, "RUNTIME_FUNCTION")) for index in range(directory.size // 12))


def parse_pe64(path: Path) -> PE64Image:
    """Parse an x86-64 PE32+ image into a fully resolved :class:`PE64Image`.

    The file is read but never executed. Headers, the section table, and every parsed
    data directory (imports, exports, relocations, debug, TLS, resources, delay imports,
    load config, and x64 exception/unwind functions) are validated as they are decoded.

    Args:
        path: Filesystem path to the PE32+ binary to parse.

    Returns:
        A :class:`PE64Image` describing the binary.

    Raises:
        FormatError: If the file does not exist, lacks the MZ or PE signatures, targets a
            machine other than IMAGE_FILE_MACHINE_AMD64, is not a PE32+ optional-header
            image, or is otherwise structurally invalid.
    """
    path = path.resolve()
    if not path.is_file():
        raise FormatError(f"binary does not exist: {path}")
    data = path.read_bytes()
    reader = _Reader(data)
    reader.require(0, 64, "DOS header")
    if data[:2] != b"MZ":
        raise FormatError("missing DOS MZ signature")
    pe_offset = reader.u32(0x3C, "DOS e_lfanew")
    reader.require(pe_offset, 24, "PE signature and COFF header")
    if data[pe_offset : pe_offset + 4] != b"PE\x00\x00":
        raise FormatError("missing PE signature")
    coff_offset = pe_offset + 4
    machine, section_count, timestamp, _symptr, _symcount, optional_size, characteristics = reader.unpack("<HHIIIHH", coff_offset, "COFF header")
    if machine != IMAGE_FILE_MACHINE_AMD64:
        raise FormatError(f"unsupported PE32+ machine 0x{machine:04x}")
    if section_count == 0 or section_count > 96:
        raise FormatError(f"invalid section count: {section_count}")
    optional_offset = coff_offset + 20
    reader.require(optional_offset, optional_size, "PE32+ optional header")
    if reader.u16(optional_offset, "optional header magic") != PE32_PLUS_MAGIC or optional_size < 112:
        raise FormatError("invalid PE32+ optional header")
    entry_rva = reader.u32(optional_offset + 16, "AddressOfEntryPoint")
    image_base = reader.u64(optional_offset + 24, "ImageBase")
    section_alignment = reader.u32(optional_offset + 32, "SectionAlignment")
    file_alignment = reader.u32(optional_offset + 36, "FileAlignment")
    size_of_image = reader.u32(optional_offset + 56, "SizeOfImage")
    size_of_headers = reader.u32(optional_offset + 60, "SizeOfHeaders")
    checksum = reader.u32(optional_offset + 64, "CheckSum")
    subsystem = reader.u16(optional_offset + 68, "Subsystem")
    dll_characteristics = reader.u16(optional_offset + 70, "DllCharacteristics")
    directory_count = reader.u32(optional_offset + 108, "NumberOfRvaAndSizes")
    available = max(0, (optional_size - 112) // 8)
    directories = tuple(
        DataDirectory(name, *reader.unpack("<II", optional_offset + 112 + index * 8, f"data directory {name}"))
        if index < min(directory_count, available) else DataDirectory(name, 0, 0)
        for index, name in enumerate(DIRECTORY_NAMES)
    )
    section_offset = optional_offset + optional_size
    sections_list: list[Section] = []
    names: set[str] = set()
    for index in range(section_count):
        offset = section_offset + index * 40
        reader.require(offset, 40, f"section header {index}")
        name = data[offset : offset + 8].split(b"\x00", 1)[0].decode("ascii", errors="replace") or f"section_{index}"
        virtual_size, virtual_address, raw_size, raw_offset = reader.unpack("<IIII", offset + 8, f"section {name}")
        section_characteristics = reader.u32(offset + 36, f"section characteristics {name}")
        if raw_size:
            reader.require(raw_offset, raw_size, f"section raw data {name}")
        unique = name
        suffix = 1
        while unique in names:
            suffix += 1
            unique = f"{name}#{suffix}"
        names.add(unique)
        sections_list.append(Section(unique, virtual_size, virtual_address, raw_size, raw_offset, section_characteristics, sha256_bytes(data[raw_offset : raw_offset + raw_size]) if raw_size else sha256_bytes(b"")))
    sections = tuple(sections_list)
    return PE64Image(
        path=path, file_sha256=sha256_bytes(data), machine=machine, number_of_sections=section_count, timestamp=timestamp,
        characteristics=characteristics, image_base=image_base, entry_rva=entry_rva, section_alignment=section_alignment,
        file_alignment=file_alignment, size_of_image=size_of_image, size_of_headers=size_of_headers, subsystem=subsystem,
        dll_characteristics=dll_characteristics, checksum=checksum, directories=directories, sections=sections,
        imports=_parse_imports64(reader, directories, sections, size_of_headers),
        exports=_parse_exports(reader, directories, sections, size_of_headers),
        base_relocations=_parse_relocations(reader, directories, sections, size_of_headers),
        debug_records=_parse_debug_records(reader, directories, sections, size_of_headers),
        tls=_parse_tls64(reader, directories, sections, size_of_headers, image_base),
        resources=_parse_resources(reader, directories, sections, size_of_headers),
        delay_imports=_parse_delay_imports64(reader, directories, sections, size_of_headers, image_base),
        load_config=_parse_load_config64(reader, directories, sections, size_of_headers),
        runtime_functions=_parse_runtime_functions(reader, directories, sections, size_of_headers),
    )


def inspect_pe_kind(path: Path) -> tuple[int, int]:
    """Read the COFF machine type and optional-header magic without full parsing.

    Args:
        path: Filesystem path to the PE binary to inspect.

    Returns:
        A ``(machine, optional_magic)`` tuple used to dispatch to the correct parser.

    Raises:
        FormatError: If the file lacks a DOS MZ signature or a PE signature.
    """
    data = path.read_bytes()
    if len(data) < 0x40 or data[:2] != b"MZ":
        raise FormatError("missing DOS MZ signature")
    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    if pe_offset + 26 > len(data) or data[pe_offset : pe_offset + 4] != b"PE\x00\x00":
        raise FormatError("missing PE signature")
    machine = struct.unpack_from("<H", data, pe_offset + 4)[0]
    optional_magic = struct.unpack_from("<H", data, pe_offset + 24)[0]
    return machine, optional_magic


def parse_pe(path: Path) -> Any:
    """Parse a PE binary, dispatching to the PE32 or PE32+ parser by architecture.

    Args:
        path: Filesystem path to the PE binary to parse.

    Returns:
        A :class:`~x86decomp.pe32.PE32Image` for x86 PE32 images or a :class:`PE64Image`
        for x86-64 PE32+ images.

    Raises:
        FormatError: If the machine and optional-header magic combination is unsupported.
    """
    machine, magic = inspect_pe_kind(path)
    if machine == 0x014C and magic == 0x010B:
        return parse_pe32(path)
    if machine == IMAGE_FILE_MACHINE_AMD64 and magic == PE32_PLUS_MAGIC:
        return parse_pe64(path)
    raise FormatError(f"unsupported PE machine/magic combination: machine=0x{machine:04x} magic=0x{magic:04x}")
