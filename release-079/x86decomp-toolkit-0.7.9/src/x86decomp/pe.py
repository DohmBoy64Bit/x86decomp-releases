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
    ImportSymbol,
    LoadConfigInfo,
    ResourceLeaf,
    Section,
    _Reader,
    _directory,
    _parse_debug_records,
    _parse_exports,
    _parse_relocations,
    _parse_resources,
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


@dataclass(frozen=True)
class TLS64Info:
    """Store the validated fields for t l s64 info records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    start_raw_data_va: int
    end_raw_data_va: int
    address_of_index_va: int
    address_of_callbacks_va: int
    zero_fill_size: int
    characteristics: int
    callbacks_va: tuple[int, ...]

    def to_dict(self) -> dict[str, Any]:
        """Convert dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
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
    """Store the validated fields for runtime function records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    begin_rva: int
    end_rva: int
    unwind_info_rva: int

    def to_dict(self) -> dict[str, Any]:
        """Convert dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return {
            "begin_rva": self.begin_rva,
            "end_rva": self.end_rva,
            "unwind_info_rva": self.unwind_info_rva,
        }


@dataclass(frozen=True)
class PE64Image:
    """Store the validated fields for p e64 image records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
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
        """Implement entry va.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return self.image_base + self.entry_rva

    def to_dict(self) -> dict[str, Any]:
        """Convert dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
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
    """Parse imports64.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
        lookup_offset = _rva_to_offset(lookup_rva, sections, size_of_headers, len(reader.data))
        symbols: list[ImportSymbol] = []
        for index in range(1_000_000):
            value = reader.u64(lookup_offset + index * 8, "PE32+ import thunk")
            if value == 0:
                break
            if value & IMAGE_ORDINAL_FLAG64:
                symbols.append(ImportSymbol(None, value & 0xFFFF, None, lookup_rva + index * 8, first_thunk + index * 8))
            else:
                name_offset = _rva_to_offset(value, sections, size_of_headers, len(reader.data))
                symbols.append(ImportSymbol(reader.c_string(name_offset + 2, "import symbol name"), None, reader.u16(name_offset, "import hint"), lookup_rva + index * 8, first_thunk + index * 8))
        else:
            raise FormatError("import thunk table exceeds safety limit")
        libraries.append(ImportLibrary(name, tuple(symbols)))
    else:
        raise FormatError("import descriptor table has no terminator")
    return tuple(libraries)


def _parse_tls64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> TLS64Info | None:
    """Parse tls64.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    directory = _directory(directories, "tls")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    start, end, index_va, callbacks_va, zero_fill, characteristics = reader.unpack("<QQQQII", offset, "PE32+ TLS directory")
    callbacks: list[int] = []
    if callbacks_va:
        if callbacks_va < image_base:
            raise FormatError("TLS callback address is below image base")
        callback_offset = _rva_to_offset(callbacks_va - image_base, sections, size_of_headers, len(reader.data))
        for index in range(65_536):
            callback = reader.u64(callback_offset + index * 8, "PE32+ TLS callback")
            if callback == 0:
                break
            callbacks.append(callback)
        else:
            raise FormatError("TLS callback table exceeds safety limit")
    return TLS64Info(start, end, index_va, callbacks_va, zero_fill, characteristics, tuple(callbacks))


def _parse_delay_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> tuple[DelayImportLibrary, ...]:
    """Parse delay imports64.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
            """Convert rva.
            
            Parameters and return values follow the signature and runtime validation in the body.
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
        lookup_offset = _rva_to_offset(lookup_rva, sections, size_of_headers, len(reader.data))
        symbols: list[ImportSymbol] = []
        for index in range(1_000_000):
            value = reader.u64(lookup_offset + index * 8, "delay import thunk")
            if value == 0:
                break
            if value & IMAGE_ORDINAL_FLAG64:
                symbols.append(ImportSymbol(None, value & 0xFFFF, None, lookup_rva + index * 8, iat_rva + index * 8))
            else:
                hint_name_rva = to_rva(value)
                hint_name_offset = _rva_to_offset(hint_name_rva, sections, size_of_headers, len(reader.data))
                symbols.append(ImportSymbol(reader.c_string(hint_name_offset + 2, "delay import symbol"), None, reader.u16(hint_name_offset, "delay import hint"), lookup_rva + index * 8, iat_rva + index * 8))
        else:
            raise FormatError("delay import thunk table exceeds safety limit")
        libraries.append(DelayImportLibrary(name, attributes, iat_rva, tuple(symbols)))
    else:
        raise FormatError("delay import descriptor table has no terminator")
    return tuple(libraries)


def _parse_load_config64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> LoadConfigInfo | None:
    """Parse load config64.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    directory = _directory(directories, "load_config")
    if directory.rva == 0 or directory.size == 0:
        return None
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    size = reader.u32(offset, "load config size")
    available = min(size, directory.size)
    def u16(relative: int) -> int | None:
        """Implement u16.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return reader.u16(offset + relative, "load config field") if available >= relative + 2 else None
    def u32(relative: int) -> int | None:
        """Implement u32.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return reader.u32(offset + relative, "load config field") if available >= relative + 4 else None
    def u64(relative: int) -> int | None:
        """Implement u64.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return reader.u64(offset + relative, "load config field") if available >= relative + 8 else None
    return LoadConfigInfo(
        size=size, timestamp=u32(4), major_version=u16(8), minor_version=u16(10), global_flags_clear=u32(12), global_flags_set=u32(16),
        security_cookie_va=u64(88), seh_table_va=None, seh_count=None,
        guard_cf_check_function_pointer_va=u64(112), guard_cf_dispatch_function_pointer_va=u64(120),
        guard_cf_function_table_va=u64(128), guard_cf_function_count=u64(136), guard_flags=u32(144),
    )


def _parse_runtime_functions(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[RuntimeFunction, ...]:
    """Parse runtime functions.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    directory = _directory(directories, "exception")
    if directory.rva == 0 or directory.size == 0:
        return ()
    if directory.size % 12 != 0:
        raise FormatError("x64 exception directory size is not a multiple of 12")
    offset = _rva_to_offset(directory.rva, sections, size_of_headers, len(reader.data))
    return tuple(RuntimeFunction(*reader.unpack("<III", offset + index * 12, "RUNTIME_FUNCTION")) for index in range(directory.size // 12))


def parse_pe64(path: Path) -> PE64Image:
    """Parse pe64.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
    """Inspect pe kind.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
    """Parse pe.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    machine, magic = inspect_pe_kind(path)
    if machine == 0x014C and magic == 0x010B:
        return parse_pe32(path)
    if machine == IMAGE_FILE_MACHINE_AMD64 and magic == PE32_PLUS_MAGIC:
        return parse_pe64(path)
    raise FormatError(f"unsupported PE machine/magic combination: machine=0x{machine:04x} magic=0x{magic:04x}")
