"""Strict COFF object parsing, COMDAT resolution, and deterministic synthesis.

The implementation covers classic Microsoft COFF and ``ANON_OBJECT_HEADER_BIGOBJ``
objects for IMAGE_FILE_MACHINE_I386 and IMAGE_FILE_MACHINE_AMD64.  It preserves
auxiliary symbol records, section-definition COMDAT metadata, weak externals,
function definitions, relocation-overflow records, and enough linker semantics
to reconstruct deterministic object groups for matching-decompilation projects.

It intentionally does not pretend that a linked PE still contains every original
COFF relocation.  This module operates on actual object files or explicitly
reconstructed synthetic objects.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from .binary_reader import BinaryReader
from .errors import ContractError, FormatError
from .util import sha256_bytes

IMAGE_FILE_MACHINE_I386 = 0x014C
IMAGE_FILE_MACHINE_AMD64 = 0x8664

IMAGE_SCN_LNK_COMDAT = 0x00001000
IMAGE_SCN_LNK_NRELOC_OVFL = 0x01000000
IMAGE_SCN_CNT_CODE = 0x00000020
IMAGE_SCN_CNT_INITIALIZED_DATA = 0x00000040
IMAGE_SCN_CNT_UNINITIALIZED_DATA = 0x00000080
IMAGE_SCN_MEM_EXECUTE = 0x20000000
IMAGE_SCN_MEM_READ = 0x40000000
IMAGE_SCN_MEM_WRITE = 0x80000000

IMAGE_SYM_CLASS_EXTERNAL = 2
IMAGE_SYM_CLASS_STATIC = 3
IMAGE_SYM_CLASS_FILE = 103
IMAGE_SYM_CLASS_WEAK_EXTERNAL = 105
IMAGE_SYM_UNDEFINED = 0
IMAGE_SYM_ABSOLUTE = -1
IMAGE_SYM_DEBUG = -2

IMAGE_COMDAT_SELECT_NODUPLICATES = 1
IMAGE_COMDAT_SELECT_ANY = 2
IMAGE_COMDAT_SELECT_SAME_SIZE = 3
IMAGE_COMDAT_SELECT_EXACT_MATCH = 4
IMAGE_COMDAT_SELECT_ASSOCIATIVE = 5
IMAGE_COMDAT_SELECT_LARGEST = 6
IMAGE_COMDAT_SELECT_NEWEST = 7

COMDAT_SELECTION_NAMES = {
    0: "none",
    IMAGE_COMDAT_SELECT_NODUPLICATES: "noduplicates",
    IMAGE_COMDAT_SELECT_ANY: "any",
    IMAGE_COMDAT_SELECT_SAME_SIZE: "same_size",
    IMAGE_COMDAT_SELECT_EXACT_MATCH: "exact_match",
    IMAGE_COMDAT_SELECT_ASSOCIATIVE: "associative",
    IMAGE_COMDAT_SELECT_LARGEST: "largest",
    IMAGE_COMDAT_SELECT_NEWEST: "newest",
}

I386_RELOCATION_NAMES = {
    0x0000: "ABSOLUTE",
    0x0001: "DIR16",
    0x0002: "REL16",
    0x0006: "DIR32",
    0x0007: "DIR32NB",
    0x0009: "SEG12",
    0x000A: "SECTION",
    0x000B: "SECREL",
    0x000C: "TOKEN",
    0x000D: "SECREL7",
    0x0014: "REL32",
}
I386_RELOCATION_WIDTHS = {
    0x0001: 2,
    0x0002: 2,
    0x0006: 4,
    0x0007: 4,
    0x0009: 2,
    0x000A: 2,
    0x000B: 4,
    0x000C: 4,
    0x000D: 1,
    0x0014: 4,
}
AMD64_RELOCATION_NAMES = {
    0x0000: "ABSOLUTE",
    0x0001: "ADDR64",
    0x0002: "ADDR32",
    0x0003: "ADDR32NB",
    0x0004: "REL32",
    0x0005: "REL32_1",
    0x0006: "REL32_2",
    0x0007: "REL32_3",
    0x0008: "REL32_4",
    0x0009: "REL32_5",
    0x000A: "SECTION",
    0x000B: "SECREL",
    0x000C: "SECREL7",
    0x000D: "TOKEN",
    0x000E: "SREL32",
    0x000F: "PAIR",
    0x0010: "SSPAN32",
}
AMD64_RELOCATION_WIDTHS = {
    0x0001: 8,
    0x0002: 4,
    0x0003: 4,
    0x0004: 4,
    0x0005: 4,
    0x0006: 4,
    0x0007: 4,
    0x0008: 4,
    0x0009: 4,
    0x000A: 2,
    0x000B: 4,
    0x000C: 1,
    0x000D: 4,
    0x000E: 4,
    0x000F: 4,
    0x0010: 4,
}


def relocation_name(machine: int, relocation_type: int) -> str:
    """Execute the relocation name operation for the current toolkit workflow."""
    table = I386_RELOCATION_NAMES if machine == IMAGE_FILE_MACHINE_I386 else AMD64_RELOCATION_NAMES
    return table.get(relocation_type, f"UNKNOWN_0x{relocation_type:04x}")


def relocation_width(machine: int, relocation_type: int) -> int | None:
    """Execute the relocation width operation for the current toolkit workflow."""
    table = I386_RELOCATION_WIDTHS if machine == IMAGE_FILE_MACHINE_I386 else AMD64_RELOCATION_WIDTHS
    return table.get(relocation_type)


def relocation_is_pc_relative(machine: int, relocation_type: int) -> bool:
    """Execute the relocation is pc relative operation for the current toolkit workflow."""
    if machine == IMAGE_FILE_MACHINE_I386:
        return relocation_type in {0x0002, 0x0014}
    return relocation_type in {0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x0009}


@dataclass(frozen=True)
class CoffRelocation:
    """Store validated coff relocation fields used by toolkit reports and adapters."""
    offset: int
    symbol_index: int
    type: int
    symbol_name: str | None = None
    addend: int | None = None

    def width(self, machine: int) -> int | None:
        """Execute the width operation for the current toolkit workflow."""
        return relocation_width(machine, self.type)

    def to_dict(self, machine: int) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "offset": self.offset,
            "symbol_index": self.symbol_index,
            "symbol_name": self.symbol_name,
            "type": self.type,
            "type_hex": f"0x{self.type:04x}",
            "type_name": relocation_name(machine, self.type),
            "width": self.width(machine),
            "pc_relative": relocation_is_pc_relative(machine, self.type),
            "addend": self.addend,
        }


@dataclass(frozen=True)
class SectionDefinitionAux:
    """Store validated section definition aux fields used by toolkit reports and adapters."""
    length: int
    relocation_count: int
    line_number_count: int
    checksum: int
    associative_section: int
    selection: int

    @property
    def selection_name(self) -> str:
        """Select ion name for the current toolkit workflow."""
        return COMDAT_SELECTION_NAMES.get(self.selection, f"unknown_{self.selection}")

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "kind": "section_definition",
            "length": self.length,
            "relocation_count": self.relocation_count,
            "line_number_count": self.line_number_count,
            "checksum": self.checksum,
            "checksum_hex": f"0x{self.checksum:08x}",
            "associative_section": self.associative_section,
            "selection": self.selection,
            "selection_name": self.selection_name,
        }


@dataclass(frozen=True)
class FunctionDefinitionAux:
    """Store validated function definition aux fields used by toolkit reports and adapters."""
    tag_index: int
    total_size: int
    line_number_pointer: int
    next_function_pointer: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "kind": "function_definition",
            "tag_index": self.tag_index,
            "total_size": self.total_size,
            "line_number_pointer": self.line_number_pointer,
            "next_function_pointer": self.next_function_pointer,
        }


@dataclass(frozen=True)
class WeakExternalAux:
    """Store validated weak external aux fields used by toolkit reports and adapters."""
    tag_index: int
    characteristics: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        names = {1: "no_library", 2: "library", 3: "alias", 4: "anti_dependency"}
        return {
            "kind": "weak_external",
            "tag_index": self.tag_index,
            "characteristics": self.characteristics,
            "characteristics_name": names.get(self.characteristics, f"unknown_{self.characteristics}"),
        }


@dataclass(frozen=True)
class FileAux:
    """Store validated file aux fields used by toolkit reports and adapters."""
    filename: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"kind": "file", "filename": self.filename}


@dataclass(frozen=True)
class RawAux:
    """Store validated raw aux fields used by toolkit reports and adapters."""
    raw_hex: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"kind": "raw", "raw_hex": self.raw_hex}


CoffAuxRecord = SectionDefinitionAux | FunctionDefinitionAux | WeakExternalAux | FileAux | RawAux


@dataclass(frozen=True)
class CoffSection:
    """Store validated coff section fields used by toolkit reports and adapters."""
    index: int
    name: str
    raw_data: bytes
    characteristics: int
    relocations: tuple[CoffRelocation, ...]
    virtual_size: int = 0
    virtual_address: int = 0
    line_number_count: int = 0
    relocation_overflow: bool = False
    comdat_symbol: str | None = None
    comdat_selection: int = 0
    associative_section: int = 0
    comdat_checksum: int | None = None

    @property
    def is_comdat(self) -> bool:
        """Execute the is comdat operation for the current toolkit workflow."""
        return bool(self.characteristics & IMAGE_SCN_LNK_COMDAT)

    @property
    def comdat_selection_name(self) -> str:
        """Execute the comdat selection name operation for the current toolkit workflow."""
        return COMDAT_SELECTION_NAMES.get(self.comdat_selection, f"unknown_{self.comdat_selection}")

    @property
    def alignment_power(self) -> int | None:
        """Execute the alignment power operation for the current toolkit workflow."""
        encoded = (self.characteristics >> 20) & 0xF
        if encoded == 0:
            return None
        if 1 <= encoded <= 14:
            return encoded - 1
        return None

    @property
    def alignment(self) -> int | None:
        """Execute the alignment operation for the current toolkit workflow."""
        power = self.alignment_power
        return None if power is None else 1 << power

    def to_dict(self, machine: int) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "index": self.index,
            "name": self.name,
            "size": len(self.raw_data),
            "sha256": sha256_bytes(self.raw_data),
            "virtual_size": self.virtual_size,
            "virtual_address": self.virtual_address,
            "characteristics": self.characteristics,
            "characteristics_hex": f"0x{self.characteristics:08x}",
            "alignment": self.alignment,
            "relocation_overflow": self.relocation_overflow,
            "relocations": [reloc.to_dict(machine) for reloc in self.relocations],
            "comdat": {
                "enabled": self.is_comdat,
                "symbol": self.comdat_symbol,
                "selection": self.comdat_selection,
                "selection_name": self.comdat_selection_name,
                "associative_section": self.associative_section,
                "checksum": self.comdat_checksum,
            },
        }


@dataclass(frozen=True)
class CoffSymbol:
    """Store validated coff symbol fields used by toolkit reports and adapters."""
    index: int
    name: str
    value: int
    section_number: int
    type: int
    storage_class: int
    auxiliary_count: int
    auxiliary_records: tuple[CoffAuxRecord, ...] = ()

    @property
    def is_function(self) -> bool:
        """Execute the is function operation for the current toolkit workflow."""
        return (self.type & 0x20) != 0 or any(
            isinstance(record, FunctionDefinitionAux) for record in self.auxiliary_records
        )

    @property
    def section_definition(self) -> SectionDefinitionAux | None:
        """Execute the section definition operation for the current toolkit workflow."""
        return next(
            (record for record in self.auxiliary_records if isinstance(record, SectionDefinitionAux)),
            None,
        )

    @property
    def function_definition(self) -> FunctionDefinitionAux | None:
        """Execute the function definition operation for the current toolkit workflow."""
        return next(
            (record for record in self.auxiliary_records if isinstance(record, FunctionDefinitionAux)),
            None,
        )

    @property
    def weak_external(self) -> WeakExternalAux | None:
        """Execute the weak external operation for the current toolkit workflow."""
        return next(
            (record for record in self.auxiliary_records if isinstance(record, WeakExternalAux)),
            None,
        )

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "index": self.index,
            "name": self.name,
            "value": self.value,
            "section_number": self.section_number,
            "type": self.type,
            "storage_class": self.storage_class,
            "auxiliary_count": self.auxiliary_count,
            "auxiliary_records": [record.to_dict() for record in self.auxiliary_records],
            "is_function_candidate": self.is_function,
        }


@dataclass(frozen=True)
class CoffObject:
    """Store validated coff object fields used by toolkit reports and adapters."""
    path: Path | None
    machine: int
    timestamp: int
    characteristics: int
    sections: tuple[CoffSection, ...]
    symbols: tuple[CoffSymbol, ...]
    raw_sha256: str
    format_variant: str = "coff"
    symbol_record_size: int = 18

    @property
    def architecture(self) -> str:
        """Execute the architecture operation for the current toolkit workflow."""
        if self.machine == IMAGE_FILE_MACHINE_I386:
            return "x86"
        if self.machine == IMAGE_FILE_MACHINE_AMD64:
            return "x86_64"
        return f"unknown-0x{self.machine:04x}"

    def section(self, number: int) -> CoffSection:
        """Execute the section operation for the current toolkit workflow."""
        if number <= 0 or number > len(self.sections):
            raise ContractError(f"symbol references invalid section number {number}")
        return self.sections[number - 1]

    def find_symbols(self, name: str) -> list[CoffSymbol]:
        """Execute the find symbols operation for the current toolkit workflow."""
        candidates = {name}
        if self.machine == IMAGE_FILE_MACHINE_I386:
            candidates.update({f"_{name}", name.lstrip("_")})
        return [symbol for symbol in self.symbols if symbol.name in candidates]

    def symbol_by_index(self, index: int) -> CoffSymbol | None:
        """Execute the symbol by index operation for the current toolkit workflow."""
        return next((symbol for symbol in self.symbols if symbol.index == index), None)

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 2,
            "format": "COFF",
            "format_variant": self.format_variant,
            "architecture": self.architecture,
            "machine": self.machine,
            "machine_hex": f"0x{self.machine:04x}",
            "timestamp": self.timestamp,
            "characteristics": self.characteristics,
            "raw_sha256": self.raw_sha256,
            "symbol_record_size": self.symbol_record_size,
            "sections": [section.to_dict(self.machine) for section in self.sections],
            "symbols": [symbol.to_dict() for symbol in self.symbols],
        }


@dataclass(frozen=True)
class ExtractedSymbol:
    """Store validated extracted symbol fields used by toolkit reports and adapters."""
    symbol: CoffSymbol
    section: CoffSection
    offset: int
    size: int
    data: bytes
    relocations: tuple[CoffRelocation, ...]

    def to_dict(self, machine: int) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "symbol": self.symbol.to_dict(),
            "section": self.section.name,
            "offset": self.offset,
            "size": self.size,
            "sha256": sha256_bytes(self.data),
            "relocations": [reloc.to_dict(machine) for reloc in self.relocations],
        }


@dataclass(frozen=True)
class ComdatCandidate:
    """Store validated comdat candidate fields used by toolkit reports and adapters."""
    object_id: str
    object_index: int
    section_index: int
    symbol: str
    selection: int
    associative_section: int
    timestamp: int
    size: int
    sha256: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "object_id": self.object_id,
            "object_index": self.object_index,
            "section_index": self.section_index,
            "symbol": self.symbol,
            "selection": self.selection,
            "selection_name": COMDAT_SELECTION_NAMES.get(self.selection, f"unknown_{self.selection}"),
            "associative_section": self.associative_section,
            "timestamp": self.timestamp,
            "size": self.size,
            "sha256": self.sha256,
        }


@dataclass(frozen=True)
class ComdatResolution:
    """Store validated comdat resolution fields used by toolkit reports and adapters."""
    winners: tuple[ComdatCandidate, ...]
    discarded: tuple[ComdatCandidate, ...]
    conflicts: tuple[dict[str, Any], ...]

    @property
    def valid(self) -> bool:
        """Execute the valid operation for the current toolkit workflow."""
        return not self.conflicts

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "valid": self.valid,
            "winners": [candidate.to_dict() for candidate in self.winners],
            "discarded": [candidate.to_dict() for candidate in self.discarded],
            "conflicts": list(self.conflicts),
        }


@dataclass(frozen=True)
class SyntheticSymbolSpec:
    """Store validated synthetic symbol spec fields used by toolkit reports and adapters."""
    name: str
    section_number: int
    value: int = 0
    type: int = 0
    storage_class: int = IMAGE_SYM_CLASS_EXTERNAL
    auxiliary_records: tuple[bytes, ...] = ()


@dataclass(frozen=True)
class SyntheticSectionSpec:
    """Store validated synthetic section spec fields used by toolkit reports and adapters."""
    name: str
    data: bytes
    characteristics: int
    relocations: tuple[CoffRelocation, ...] = ()
    comdat_symbol: str | None = None
    comdat_selection: int = 0
    associative_section: int = 0
    comdat_checksum: int = 0


_Reader = BinaryReader

def _read_string_table(
    reader: _Reader, pointer_to_symbols: int, count: int, symbol_record_size: int
) -> bytes:
    """Support read string table processing for internal toolkit callers."""
    offset = pointer_to_symbols + count * symbol_record_size
    if offset == len(reader.data):
        return b"\x04\x00\x00\x00"
    reader.require(offset, 4, "COFF string table size")
    size = struct.unpack_from("<I", reader.data, offset)[0]
    if size < 4:
        raise FormatError("COFF string table size is smaller than 4")
    reader.require(offset, size, "COFF string table")
    return reader.data[offset : offset + size]


def _string_at(table: bytes, offset: int, context: str) -> str:
    """Support string at processing for internal toolkit callers."""
    if offset < 4 or offset >= len(table):
        raise FormatError(f"{context} string-table offset is invalid: {offset}")
    end = table.find(b"\x00", offset)
    if end < 0:
        raise FormatError(f"unterminated {context} string")
    return table[offset:end].decode("utf-8", errors="replace")


def _decode_symbol_name(raw: bytes, table: bytes) -> str:
    """Support decode symbol name processing for internal toolkit callers."""
    if raw[:4] == b"\x00\x00\x00\x00":
        offset = struct.unpack_from("<I", raw, 4)[0]
        return _string_at(table, offset, "symbol")
    return raw.rstrip(b"\x00").decode("utf-8", errors="replace")


def _decode_section_name(raw: bytes, table: bytes) -> str:
    """Support decode section name processing for internal toolkit callers."""
    inline = raw.rstrip(b"\x00").decode("ascii", errors="replace")
    if inline.startswith("/") and inline[1:].isdigit():
        return _string_at(table, int(inline[1:]), "section")
    return inline


def _parse_header(reader: _Reader) -> tuple[str, int, int, int, int, int, int, int, int]:
    """Return variant, machine, sections, timestamp, symptr, symcount,
    characteristics, section-header-offset, symbol-record-size.
    """
    reader.require(0, 20, "COFF or bigobj header")
    sig1, sig2 = reader.unpack("<HH", 0, "COFF signature")
    if sig1 == 0 and sig2 == 0xFFFF:
        reader.require(0, 56, "bigobj header")
        (
            _sig1,
            _sig2,
            version,
            machine,
            timestamp,
            _class_id,
            _size_of_data,
            _flags,
            _metadata_size,
            _metadata_offset,
            section_count,
            symbol_pointer,
            symbol_count,
        ) = reader.unpack("<HHHHI16sIIIIIII", 0, "bigobj header")
        if version < 2:
            raise FormatError(f"unsupported bigobj version {version}")
        return (
            "bigobj",
            machine,
            section_count,
            timestamp,
            symbol_pointer,
            symbol_count,
            0,
            56,
            20,
        )
    machine, section_count, timestamp, symbol_pointer, symbol_count, optional_size, characteristics = reader.unpack(
        "<HHIIIHH", 0, "COFF file header"
    )
    if optional_size != 0:
        raise FormatError("input appears to be an image, not a COFF object (optional header is present)")
    return (
        "coff",
        machine,
        section_count,
        timestamp,
        symbol_pointer,
        symbol_count,
        characteristics,
        20,
        18,
    )


def _parse_auxiliary_records(
    *,
    symbol_name: str,
    section_number: int,
    symbol_type: int,
    storage_class: int,
    raw_records: Sequence[bytes],
    symbol_record_size: int,
) -> tuple[CoffAuxRecord, ...]:
    """Support parse auxiliary records processing for internal toolkit callers."""
    if not raw_records:
        return ()
    if storage_class == IMAGE_SYM_CLASS_FILE:
        filename = b"".join(raw_records).split(b"\x00", 1)[0].decode("utf-8", errors="replace")
        return (FileAux(filename=filename),)
    first = raw_records[0]
    if (
        storage_class == IMAGE_SYM_CLASS_STATIC
        and section_number > 0
        and len(first) >= 18
    ):
        length, reloc_count, line_count, checksum, number, selection, _reserved, high = struct.unpack_from(
            "<IHHIhBBH", first, 0
        )
        associative = number
        if symbol_record_size == 20 and len(first) >= 20:
            # Bigobj stores the associated section as a 32-bit split number.
            associative = (high << 16) | (number & 0xFFFF)
        return (
            SectionDefinitionAux(
                length=length,
                relocation_count=reloc_count,
                line_number_count=line_count,
                checksum=checksum,
                associative_section=associative,
                selection=selection,
            ),
            *(RawAux(record.hex()) for record in raw_records[1:]),
        )
    if storage_class in (IMAGE_SYM_CLASS_EXTERNAL, IMAGE_SYM_CLASS_WEAK_EXTERNAL) and section_number == IMAGE_SYM_UNDEFINED and len(first) >= 8:
        tag_index, characteristics = struct.unpack_from("<II", first, 0)
        return (
            WeakExternalAux(tag_index=tag_index, characteristics=characteristics),
            *(RawAux(record.hex()) for record in raw_records[1:]),
        )
    if storage_class == IMAGE_SYM_CLASS_EXTERNAL and (symbol_type & 0x20) and len(first) >= 16:
        tag_index, total_size, line_pointer, next_pointer = struct.unpack_from("<IIII", first, 0)
        return (
            FunctionDefinitionAux(
                tag_index=tag_index,
                total_size=total_size,
                line_number_pointer=line_pointer,
                next_function_pointer=next_pointer,
            ),
            *(RawAux(record.hex()) for record in raw_records[1:]),
        )
    return tuple(RawAux(record.hex()) for record in raw_records)


def _read_addend(raw_data: bytes, offset: int, width: int | None) -> int | None:
    """Support read addend processing for internal toolkit callers."""
    if width is None or width not in {1, 2, 4, 8} or offset < 0 or offset + width > len(raw_data):
        return None
    return int.from_bytes(raw_data[offset : offset + width], "little", signed=False)


def parse_coff_bytes(data: bytes, *, path: Path | None = None) -> CoffObject:
    """Parse coff bytes for the current toolkit workflow."""
    reader = _Reader(data)
    (
        variant,
        machine,
        section_count,
        timestamp,
        symbol_pointer,
        symbol_count,
        characteristics,
        section_headers_offset,
        symbol_record_size,
    ) = _parse_header(reader)
    if machine not in (IMAGE_FILE_MACHINE_I386, IMAGE_FILE_MACHINE_AMD64):
        raise FormatError(f"unsupported COFF machine 0x{machine:04x}")
    if section_count <= 0 or section_count > 1_000_000:
        raise FormatError(f"invalid COFF section count {section_count}")
    reader.require(section_headers_offset, section_count * 40, "COFF section table")
    if symbol_count:
        reader.require(symbol_pointer, symbol_count * symbol_record_size, "COFF symbol table")
    string_table = (
        _read_string_table(reader, symbol_pointer, symbol_count, symbol_record_size)
        if symbol_count
        else b"\x04\x00\x00\x00"
    )

    raw_section_records: list[dict[str, Any]] = []
    for section_index in range(section_count):
        offset = section_headers_offset + section_index * 40
        name_raw = data[offset : offset + 8]
        (
            virtual_size,
            virtual_address,
            raw_size,
            raw_pointer,
            relocation_pointer,
            _line_pointer,
            relocation_count16,
            line_count,
            section_characteristics,
        ) = reader.unpack("<IIIIIIHHI", offset + 8, "COFF section header")
        name = _decode_section_name(name_raw, string_table)
        if raw_size:
            reader.require(raw_pointer, raw_size, f"section {name} raw data")
        raw_data = data[raw_pointer : raw_pointer + raw_size] if raw_size else b""
        overflow = bool(
            relocation_count16 == 0xFFFF and section_characteristics & IMAGE_SCN_LNK_NRELOC_OVFL
        )
        relocation_count = relocation_count16
        relocation_start_index = 0
        if overflow:
            reader.require(relocation_pointer, 10, f"section {name} relocation overflow record")
            true_count, zero_symbol, zero_type = reader.unpack(
                "<IIH", relocation_pointer, f"section {name} relocation overflow record"
            )
            if zero_symbol != 0 or zero_type != 0 or true_count == 0:
                raise FormatError(f"section {name} has malformed relocation overflow record")
            # The count includes the overflow record itself according to PE/COFF.
            relocation_count = true_count
            relocation_start_index = 1
        if relocation_count:
            reader.require(relocation_pointer, relocation_count * 10, f"section {name} relocations")
        raw_section_records.append(
            {
                "name": name,
                "raw_data": raw_data,
                "characteristics": section_characteristics,
                "relocation_pointer": relocation_pointer,
                "relocation_count": relocation_count,
                "relocation_start_index": relocation_start_index,
                "overflow": overflow,
                "virtual_size": virtual_size,
                "virtual_address": virtual_address,
                "line_count": line_count,
            }
        )

    symbols: list[CoffSymbol] = []
    index = 0
    while index < symbol_count:
        offset = symbol_pointer + index * symbol_record_size
        raw_name = data[offset : offset + 8]
        if symbol_record_size == 18:
            value, section_number, symbol_type, storage_class, aux_count = reader.unpack(
                "<IhHBB", offset + 8, "COFF symbol"
            )
        else:
            value, section_number, symbol_type, storage_class, aux_count = reader.unpack(
                "<IiHBB", offset + 8, "bigobj symbol"
            )
        if index + aux_count >= symbol_count:
            raise FormatError("COFF symbol auxiliary count exceeds table")
        raw_aux = tuple(
            data[
                symbol_pointer + (index + aux_index) * symbol_record_size :
                symbol_pointer + (index + aux_index + 1) * symbol_record_size
            ]
            for aux_index in range(1, aux_count + 1)
        )
        name = _decode_symbol_name(raw_name, string_table)
        aux_records = _parse_auxiliary_records(
            symbol_name=name,
            section_number=section_number,
            symbol_type=symbol_type,
            storage_class=storage_class,
            raw_records=raw_aux,
            symbol_record_size=symbol_record_size,
        )
        symbols.append(
            CoffSymbol(
                index=index,
                name=name,
                value=value,
                section_number=section_number,
                type=symbol_type,
                storage_class=storage_class,
                auxiliary_count=aux_count,
                auxiliary_records=aux_records,
            )
        )
        index += 1 + aux_count
    symbol_by_index = {symbol.index: symbol for symbol in symbols}

    section_definitions: dict[int, tuple[CoffSymbol, SectionDefinitionAux]] = {}
    for symbol in symbols:
        definition = symbol.section_definition
        if definition is not None and symbol.section_number > 0:
            section_definitions[symbol.section_number] = (symbol, definition)

    sections: list[CoffSection] = []
    for section_index, record in enumerate(raw_section_records, start=1):
        name = str(record["name"])
        raw_data = bytes(record["raw_data"])
        relocations: list[CoffRelocation] = []
        start_index = int(record["relocation_start_index"])
        relocation_count = int(record["relocation_count"])
        relocation_pointer = int(record["relocation_pointer"])
        for relocation_index in range(start_index, relocation_count):
            offset = relocation_pointer + relocation_index * 10
            virtual_address, symbol_index, relocation_type = reader.unpack(
                "<IIH", offset, f"section {name} relocation"
            )
            if symbol_index >= symbol_count:
                raise FormatError(f"relocation references invalid symbol index {symbol_index}")
            target = symbol_by_index.get(symbol_index)
            width = relocation_width(machine, relocation_type)
            relocations.append(
                CoffRelocation(
                    offset=virtual_address,
                    symbol_index=symbol_index,
                    type=relocation_type,
                    symbol_name=None if target is None else target.name,
                    addend=_read_addend(raw_data, virtual_address, width),
                )
            )
        definition_pair = section_definitions.get(section_index)
        section_symbol = definition_pair[0] if definition_pair else None
        definition = definition_pair[1] if definition_pair else None
        comdat_public = next(
            (
                symbol
                for symbol in symbols
                if symbol.section_number == section_index
                and symbol.storage_class == IMAGE_SYM_CLASS_EXTERNAL
                and symbol.value == 0
            ),
            None,
        )
        sections.append(
            CoffSection(
                index=section_index,
                name=name,
                raw_data=raw_data,
                characteristics=int(record["characteristics"]),
                relocations=tuple(relocations),
                virtual_size=int(record["virtual_size"]),
                virtual_address=int(record["virtual_address"]),
                line_number_count=int(record["line_count"]),
                relocation_overflow=bool(record["overflow"]),
                comdat_symbol=(None if definition is None else (comdat_public.name if comdat_public is not None else (None if section_symbol is None else section_symbol.name))),
                comdat_selection=0 if definition is None else definition.selection,
                associative_section=0 if definition is None else definition.associative_section,
                comdat_checksum=None if definition is None else definition.checksum,
            )
        )
    return CoffObject(
        path=path,
        machine=machine,
        timestamp=timestamp,
        characteristics=characteristics,
        sections=tuple(sections),
        symbols=tuple(symbols),
        raw_sha256=sha256_bytes(data),
        format_variant=variant,
        symbol_record_size=symbol_record_size,
    )


def parse_coff(path: Path) -> CoffObject:
    """Parse coff for the current toolkit workflow."""
    resolved = path.resolve()
    if not resolved.is_file():
        raise ContractError(f"COFF object does not exist: {resolved}")
    return parse_coff_bytes(resolved.read_bytes(), path=resolved)


def extract_symbol(obj: CoffObject, name: str, *, size: int | None = None) -> ExtractedSymbol:
    """Extract symbol for the current toolkit workflow."""
    matches = [symbol for symbol in obj.find_symbols(name) if symbol.section_number > 0]
    if not matches:
        available = sorted(symbol.name for symbol in obj.symbols if symbol.section_number > 0)
        raise ContractError(f"COFF symbol not found: {name}; available={available[:30]}")
    if len(matches) > 1:
        exact = [symbol for symbol in matches if symbol.name == name]
        if len(exact) == 1:
            symbol = exact[0]
        else:
            raise ContractError(f"COFF symbol name is ambiguous: {name}")
    else:
        symbol = matches[0]
    section = obj.section(symbol.section_number)
    start = symbol.value
    if start < 0 or start > len(section.raw_data):
        raise FormatError(f"symbol {symbol.name} offset lies outside section {section.name}")
    if size is None:
        explicit_size = symbol.function_definition.total_size if symbol.function_definition else 0
        if explicit_size:
            end = start + explicit_size
        else:
            following = sorted(
                candidate.value
                for candidate in obj.symbols
                if candidate.section_number == symbol.section_number and candidate.value > start
            )
            end = following[0] if following else len(section.raw_data)
    else:
        if size <= 0:
            raise ContractError("symbol extraction size must be positive")
        end = start + size
    if end > len(section.raw_data) or end <= start:
        raise FormatError(f"symbol {symbol.name} has invalid inferred range [{start}, {end})")
    relocations = tuple(
        CoffRelocation(
            offset=relocation.offset - start,
            symbol_index=relocation.symbol_index,
            type=relocation.type,
            symbol_name=relocation.symbol_name,
            addend=relocation.addend,
        )
        for relocation in section.relocations
        if start <= relocation.offset < end
    )
    return ExtractedSymbol(
        symbol=symbol,
        section=section,
        offset=start,
        size=end - start,
        data=section.raw_data[start:end],
        relocations=relocations,
    )


def collect_comdat_candidates(objects: Sequence[CoffObject]) -> tuple[ComdatCandidate, ...]:
    """Execute the collect comdat candidates operation for the current toolkit workflow."""
    candidates: list[ComdatCandidate] = []
    for object_index, obj in enumerate(objects):
        object_id = str(obj.path) if obj.path is not None else f"memory:{obj.raw_sha256}"
        for section in obj.sections:
            if not section.is_comdat:
                continue
            if not section.comdat_symbol:
                raise ContractError(
                    f"COMDAT section {section.name} in {object_id} lacks a section-definition symbol"
                )
            candidates.append(
                ComdatCandidate(
                    object_id=object_id,
                    object_index=object_index,
                    section_index=section.index,
                    symbol=section.comdat_symbol,
                    selection=section.comdat_selection,
                    associative_section=section.associative_section,
                    timestamp=obj.timestamp,
                    size=len(section.raw_data),
                    sha256=sha256_bytes(section.raw_data),
                )
            )
    return tuple(candidates)


def resolve_comdats(objects: Sequence[CoffObject]) -> ComdatResolution:
    """Resolve COMDAT groups using PE/COFF selection semantics.

    Associative sections follow the winner of their associated parent section in
    the same object.  The function reports conflicts instead of silently choosing
    for NODUPLICATES, SAME_SIZE, or EXACT_MATCH violations.
    """
    candidates = collect_comdat_candidates(objects)
    by_symbol: dict[str, list[ComdatCandidate]] = {}
    associative: list[ComdatCandidate] = []
    for candidate in candidates:
        if candidate.selection == IMAGE_COMDAT_SELECT_ASSOCIATIVE:
            associative.append(candidate)
        else:
            by_symbol.setdefault(candidate.symbol, []).append(candidate)
    winners: list[ComdatCandidate] = []
    discarded: list[ComdatCandidate] = []
    conflicts: list[dict[str, Any]] = []
    winner_keys: set[tuple[int, int]] = set()

    for symbol, group in sorted(by_symbol.items()):
        group = sorted(group, key=lambda item: (item.object_index, item.section_index))
        selections = {item.selection for item in group}
        if len(selections) != 1:
            conflicts.append(
                {
                    "symbol": symbol,
                    "reason": "selection_mismatch",
                    "selections": sorted(selections),
                    "candidates": [item.to_dict() for item in group],
                }
            )
            continue
        selection = group[0].selection
        winner = group[0]
        if selection == IMAGE_COMDAT_SELECT_NODUPLICATES and len(group) > 1:
            conflicts.append(
                {
                    "symbol": symbol,
                    "reason": "noduplicates_violation",
                    "candidates": [item.to_dict() for item in group],
                }
            )
            continue
        if selection == IMAGE_COMDAT_SELECT_SAME_SIZE and len({item.size for item in group}) > 1:
            conflicts.append(
                {
                    "symbol": symbol,
                    "reason": "same_size_violation",
                    "candidates": [item.to_dict() for item in group],
                }
            )
            continue
        if selection == IMAGE_COMDAT_SELECT_EXACT_MATCH and len({item.sha256 for item in group}) > 1:
            conflicts.append(
                {
                    "symbol": symbol,
                    "reason": "exact_match_violation",
                    "candidates": [item.to_dict() for item in group],
                }
            )
            continue
        if selection == IMAGE_COMDAT_SELECT_LARGEST:
            winner = max(group, key=lambda item: (item.size, -item.object_index, -item.section_index))
        elif selection == IMAGE_COMDAT_SELECT_NEWEST:
            winner = max(group, key=lambda item: (item.timestamp, -item.object_index, -item.section_index))
        elif selection not in {
            IMAGE_COMDAT_SELECT_NODUPLICATES,
            IMAGE_COMDAT_SELECT_ANY,
            IMAGE_COMDAT_SELECT_SAME_SIZE,
            IMAGE_COMDAT_SELECT_EXACT_MATCH,
            IMAGE_COMDAT_SELECT_LARGEST,
            IMAGE_COMDAT_SELECT_NEWEST,
        }:
            conflicts.append(
                {
                    "symbol": symbol,
                    "reason": "unsupported_selection",
                    "selection": selection,
                    "candidates": [item.to_dict() for item in group],
                }
            )
            continue
        winners.append(winner)
        winner_keys.add((winner.object_index, winner.section_index))
        discarded.extend(item for item in group if item != winner)

    for candidate in sorted(associative, key=lambda item: (item.object_index, item.section_index)):
        parent_key = (candidate.object_index, candidate.associative_section)
        if parent_key in winner_keys:
            winners.append(candidate)
            winner_keys.add((candidate.object_index, candidate.section_index))
        else:
            discarded.append(candidate)
    return ComdatResolution(
        winners=tuple(winners),
        discarded=tuple(discarded),
        conflicts=tuple(conflicts),
    )


def _encode_name(name: str, strings: bytearray) -> bytes:
    """Support encode name processing for internal toolkit callers."""
    encoded = name.encode("utf-8")
    if len(encoded) <= 8:
        return encoded.ljust(8, b"\x00")
    offset = 4 + len(strings)
    strings.extend(encoded + b"\x00")
    return b"\x00\x00\x00\x00" + struct.pack("<I", offset)


def _section_aux_bytes(
    *, length: int, relocation_count: int, checksum: int, associative_section: int, selection: int
) -> bytes:
    """Support section aux bytes processing for internal toolkit callers."""
    return struct.pack(
        "<IHHIhBBH",
        length,
        min(relocation_count, 0xFFFF),
        0,
        checksum,
        associative_section,
        selection,
        0,
        0,
    )


def build_synthetic_coff_object(
    *,
    sections: Sequence[SyntheticSectionSpec],
    symbols: Sequence[SyntheticSymbolSpec],
    machine: int = IMAGE_FILE_MACHINE_I386,
    timestamp: int = 0,
) -> bytes:
    """Build a deterministic classic COFF object with multiple sections.

    Symbol indices referenced by relocations are the final on-disk indices,
    including auxiliary records.  Callers should usually generate symbols first
    and use :func:`synthetic_symbol_indices` to compute stable indices.
    """
    if machine not in (IMAGE_FILE_MACHINE_I386, IMAGE_FILE_MACHINE_AMD64):
        raise ContractError("synthetic COFF supports x86 and x86-64 only")
    if not sections:
        raise ContractError("synthetic COFF requires at least one section")
    if len(sections) > 0xFFFF:
        raise ContractError("classic synthetic COFF supports at most 65535 sections")
    for section in sections:
        if not section.name:
            raise ContractError("synthetic section name may not be empty")
        if len(section.relocations) > 0xFFFF:
            raise ContractError("synthetic section relocation overflow is not emitted by this writer")
        for relocation in section.relocations:
            width = relocation.width(machine)
            if width is None:
                raise ContractError(f"unsupported relocation type 0x{relocation.type:04x}")
            if relocation.offset < 0 or relocation.offset + width > len(section.data):
                raise ContractError(f"relocation outside section {section.name}")
    for symbol in symbols:
        if not symbol.name:
            raise ContractError("synthetic symbol name may not be empty")
        if symbol.section_number < IMAGE_SYM_DEBUG or symbol.section_number > len(sections):
            raise ContractError(f"synthetic symbol {symbol.name} has invalid section number")
        if symbol.section_number > 0 and symbol.value > len(sections[symbol.section_number - 1].data):
            raise ContractError(f"synthetic symbol {symbol.name} lies outside its section")
        if any(len(record) != 18 for record in symbol.auxiliary_records):
            raise ContractError("classic COFF auxiliary records must be exactly 18 bytes")

    strings = bytearray()
    encoded_section_names = [_encode_name(section.name, strings) for section in sections]
    encoded_symbol_names = [_encode_name(symbol.name, strings) for symbol in symbols]

    header_size = 20
    section_table_size = len(sections) * 40
    cursor = header_size + section_table_size
    raw_offsets: list[int] = []
    for section in sections:
        raw_offsets.append(cursor if section.data else 0)
        cursor += len(section.data)
    relocation_offsets: list[int] = []
    for section in sections:
        relocation_offsets.append(cursor if section.relocations else 0)
        cursor += len(section.relocations) * 10
    symbol_pointer = cursor
    symbol_count = sum(1 + len(symbol.auxiliary_records) for symbol in symbols)
    string_table = struct.pack("<I", 4 + len(strings)) + bytes(strings)

    header = struct.pack(
        "<HHIIIHH",
        machine,
        len(sections),
        timestamp,
        symbol_pointer,
        symbol_count,
        0,
        0,
    )
    section_headers = bytearray()
    for index, section in enumerate(sections):
        section_headers += encoded_section_names[index]
        section_headers += struct.pack(
            "<IIIIIIHHI",
            0,
            0,
            len(section.data),
            raw_offsets[index],
            relocation_offsets[index],
            0,
            len(section.relocations),
            0,
            section.characteristics,
        )
    relocation_blob = bytearray()
    for section in sections:
        for relocation in section.relocations:
            if relocation.symbol_index < 0 or relocation.symbol_index >= symbol_count:
                raise ContractError(
                    f"relocation in {section.name} references invalid final symbol index {relocation.symbol_index}"
                )
            relocation_blob += struct.pack(
                "<IIH", relocation.offset, relocation.symbol_index, relocation.type
            )
    symbol_blob = bytearray()
    for encoded_name, symbol in zip(encoded_symbol_names, symbols):
        symbol_blob += encoded_name
        symbol_blob += struct.pack(
            "<IhHBB",
            symbol.value,
            symbol.section_number,
            symbol.type,
            symbol.storage_class,
            len(symbol.auxiliary_records),
        )
        for record in symbol.auxiliary_records:
            symbol_blob += record
    return (
        header
        + bytes(section_headers)
        + b"".join(section.data for section in sections)
        + bytes(relocation_blob)
        + bytes(symbol_blob)
        + string_table
    )


def synthetic_symbol_indices(symbols: Sequence[SyntheticSymbolSpec]) -> dict[str, int]:
    """Execute the synthetic symbol indices operation for the current toolkit workflow."""
    result: dict[str, int] = {}
    index = 0
    for symbol in symbols:
        if symbol.name in result:
            raise ContractError(f"duplicate synthetic symbol name {symbol.name}")
        result[symbol.name] = index
        index += 1 + len(symbol.auxiliary_records)
    return result


def build_synthetic_coff(
    *,
    code: bytes,
    symbol_name: str,
    machine: int = IMAGE_FILE_MACHINE_I386,
    relocations: Iterable[CoffRelocation] = (),
    timestamp: int = 0,
) -> bytes:
    """Backward-compatible one-section synthetic COFF builder."""
    if not code:
        raise ContractError("synthetic COFF code may not be empty")
    if not symbol_name:
        raise ContractError("synthetic COFF symbol_name may not be empty")
    relocs = tuple(relocations)
    for relocation in relocs:
        if relocation.symbol_index != 0:
            raise ContractError("single-symbol synthetic COFF requires relocation symbol_index 0")
    return build_synthetic_coff_object(
        sections=(
            SyntheticSectionSpec(
                name=".text",
                data=code,
                characteristics=IMAGE_SCN_CNT_CODE | IMAGE_SCN_MEM_EXECUTE | IMAGE_SCN_MEM_READ,
                relocations=relocs,
            ),
        ),
        symbols=(
            SyntheticSymbolSpec(
                name=symbol_name,
                section_number=1,
                value=0,
                type=0x20,
                storage_class=IMAGE_SYM_CLASS_EXTERNAL,
            ),
        ),
        machine=machine,
        timestamp=timestamp,
    )


def build_comdat_coff(
    *,
    data: bytes,
    symbol_name: str,
    section_name: str = ".text$mn",
    machine: int = IMAGE_FILE_MACHINE_I386,
    selection: int = IMAGE_COMDAT_SELECT_ANY,
    associative_section: int = 0,
    timestamp: int = 0,
    characteristics: int = IMAGE_SCN_CNT_CODE | IMAGE_SCN_MEM_EXECUTE | IMAGE_SCN_MEM_READ,
    relocations: Iterable[CoffRelocation] = (),
) -> bytes:
    """Build comdat coff for the current toolkit workflow."""
    if selection not in COMDAT_SELECTION_NAMES or selection == 0:
        raise ContractError("invalid COMDAT selection")
    checksum = int.from_bytes(bytes.fromhex(sha256_bytes(data))[:4], "little")
    section_aux = _section_aux_bytes(
        length=len(data),
        relocation_count=len(tuple(relocations)),
        checksum=checksum,
        associative_section=associative_section,
        selection=selection,
    )
    # Section definition is index 0 with one aux, public symbol is index 2.
    relocation_list = tuple(
        CoffRelocation(
            offset=item.offset,
            symbol_index=item.symbol_index,
            type=item.type,
            symbol_name=item.symbol_name,
            addend=item.addend,
        )
        for item in relocations
    )
    return build_synthetic_coff_object(
        sections=(
            SyntheticSectionSpec(
                name=section_name,
                data=data,
                characteristics=characteristics | IMAGE_SCN_LNK_COMDAT,
                relocations=relocation_list,
                comdat_symbol=section_name,
                comdat_selection=selection,
                associative_section=associative_section,
                comdat_checksum=checksum,
            ),
        ),
        symbols=(
            SyntheticSymbolSpec(
                name=section_name,
                section_number=1,
                storage_class=IMAGE_SYM_CLASS_STATIC,
                auxiliary_records=(section_aux,),
            ),
            SyntheticSymbolSpec(
                name=symbol_name,
                section_number=1,
                type=0x20,
                storage_class=IMAGE_SYM_CLASS_EXTERNAL,
            ),
        ),
        machine=machine,
        timestamp=timestamp,
    )


def write_synthetic_coff(
    path: Path,
    *,
    code: bytes,
    symbol_name: str,
    machine: int = IMAGE_FILE_MACHINE_I386,
    relocations: Iterable[CoffRelocation] = (),
) -> dict[str, Any]:
    """Write synthetic coff for the current toolkit workflow."""
    payload = build_synthetic_coff(
        code=code, symbol_name=symbol_name, machine=machine, relocations=relocations
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    parsed = parse_coff(path)
    return parsed.to_dict()


def write_synthetic_coff_object(
    path: Path,
    *,
    sections: Sequence[SyntheticSectionSpec],
    symbols: Sequence[SyntheticSymbolSpec],
    machine: int = IMAGE_FILE_MACHINE_I386,
    timestamp: int = 0,
) -> dict[str, Any]:
    """Write synthetic coff object for the current toolkit workflow."""
    payload = build_synthetic_coff_object(
        sections=sections, symbols=symbols, machine=machine, timestamp=timestamp
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return parse_coff(path).to_dict()
