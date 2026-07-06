"""Provide the current runtime implementation for the `x86decomp.assembly.relocations` module."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from x86decomp.coff import (
    IMAGE_FILE_MACHINE_AMD64,
    IMAGE_FILE_MACHINE_I386,
    CoffObject,
    CoffRelocation,
    CoffSymbol,
    ExtractedSymbol,
    extract_symbol,
    parse_coff,
    relocation_name,
    relocation_width,
)
from x86decomp.contracts import ContractError, atomic_write_bytes, sha256_bytes, sha256_file
from x86decomp.errors import FormatError


@dataclass(frozen=True)
class SymbolAddress:
    """Store validated symbol address fields used by toolkit reports and adapters."""
    name: str
    rva: int
    section_rva: int | None = None
    section_index: int | None = None
    kind: str = "unknown"

    @property
    def safe_name(self) -> str:
        """Execute the safe name operation for the current toolkit workflow."""
        return self.name

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "name": self.name,
            "rva": self.rva,
            "section_rva": self.section_rva,
            "section_index": self.section_index,
            "kind": self.kind,
        }


def normalize_symbol_map(raw: Mapping[str, Any] | list[Mapping[str, Any]]) -> dict[str, SymbolAddress]:
    """Normalize symbol map for the current toolkit workflow."""
    items: list[tuple[str, Any]]
    if isinstance(raw, Mapping):
        items = [(str(name), value) for name, value in raw.items()]
    elif isinstance(raw, list):
        items = []
        for entry in raw:
            if not isinstance(entry, Mapping) or "name" not in entry:
                raise ContractError("symbol-map list entries require a name")
            items.append((str(entry["name"]), entry))
    else:
        raise ContractError("symbol map must be an object or list")
    result: dict[str, SymbolAddress] = {}
    for name, value in items:
        if isinstance(value, int):
            entry = SymbolAddress(name=name, rva=value)
        elif isinstance(value, str):
            entry = SymbolAddress(name=name, rva=int(value, 0))
        elif isinstance(value, Mapping):
            if "rva" not in value:
                raise ContractError(f"symbol-map entry {name!r} lacks rva")
            raw_rva = value["rva"]
            raw_section_rva = value.get("section_rva")
            entry = SymbolAddress(
                name=name,
                rva=int(raw_rva, 0) if isinstance(raw_rva, str) else int(raw_rva),
                section_rva=(
                    None
                    if raw_section_rva is None
                    else int(raw_section_rva, 0)
                    if isinstance(raw_section_rva, str)
                    else int(raw_section_rva)
                ),
                section_index=(
                    None if value.get("section_index") is None else int(value["section_index"])
                ),
                kind=str(value.get("kind", "unknown")),
            )
        else:
            raise ContractError(f"unsupported symbol-map entry for {name!r}")
        if entry.rva < 0:
            raise ContractError(f"negative RVA for symbol {name!r}")
        result[name] = entry
        if name.startswith("_"):
            result.setdefault(name[1:], entry)
        else:
            result.setdefault("_" + name, entry)
    return result


def supported_relocations() -> dict[str, list[str]]:
    """Execute the supported relocations operation for the current toolkit workflow."""
    return {
        "x86": ["DIR16", "REL16", "DIR32", "DIR32NB", "SECTION", "SECREL", "REL32"],
        "x86_64": [
            "ADDR64",
            "ADDR32",
            "ADDR32NB",
            "REL32",
            "REL32_1",
            "REL32_2",
            "REL32_3",
            "REL32_4",
            "REL32_5",
            "SECTION",
            "SECREL",
            "SECREL7",
        ],
    }


def _read_addend(data: bytes, offset: int, width: int, *, signed: bool) -> int:
    """Support read addend processing for internal toolkit callers."""
    if offset < 0 or offset + width > len(data):
        raise ContractError(f"relocation field [{offset},{offset + width}) exceeds extracted symbol")
    return int.from_bytes(data[offset : offset + width], "little", signed=signed)


def _write_value(buffer: bytearray, offset: int, width: int, value: int, *, signed: bool) -> None:
    """Support write value processing for internal toolkit callers."""
    low = -(1 << (width * 8 - 1)) if signed else 0
    high = (1 << (width * 8 - (1 if signed else 0))) - 1
    if not low <= value <= high:
        raise ContractError(
            f"relocation result {value} does not fit {'signed' if signed else 'unsigned'} {width * 8}-bit field"
        )
    buffer[offset : offset + width] = int(value).to_bytes(width, "little", signed=signed)


def _object_symbol_target(
    obj: CoffObject,
    symbol: CoffSymbol | None,
    *,
    extracted: ExtractedSymbol,
    base_rva: int,
    placements: Mapping[int | str, int],
) -> tuple[int, int | None, int | None] | None:
    """Support object symbol target processing for internal toolkit callers."""
    if symbol is None or symbol.section_number <= 0:
        return None
    section = obj.section(symbol.section_number)
    if symbol.section_number == extracted.symbol.section_number:
        section_rva = base_rva - extracted.offset
    else:
        raw = placements.get(symbol.section_number, placements.get(section.name))
        if raw is None:
            return None
        section_rva = int(raw)
    return section_rva + symbol.value, section_rva, symbol.section_number


def _resolve_target(
    obj: CoffObject,
    relocation: CoffRelocation,
    *,
    extracted: ExtractedSymbol,
    base_rva: int,
    symbol_map: Mapping[str, SymbolAddress],
    placements: Mapping[int | str, int],
) -> tuple[str | None, int | None, int | None, int | None]:
    """Support resolve target processing for internal toolkit callers."""
    symbol = obj.symbol_by_index(relocation.symbol_index)
    local = _object_symbol_target(
        obj, symbol, extracted=extracted, base_rva=base_rva, placements=placements
    )
    name = relocation.symbol_name if relocation.symbol_name is not None else (None if symbol is None else symbol.name)
    if local is not None:
        target_rva, section_rva, section_index = local
        return name, target_rva, section_rva, section_index
    if name is None:
        return None, None, None, None
    mapped = symbol_map.get(name) or symbol_map.get(name.lstrip("_"))
    if mapped is None:
        return name, None, None, None
    return name, mapped.rva, mapped.section_rva, mapped.section_index


def _compute_value(
    *,
    machine: int,
    relocation_type: int,
    target_rva: int,
    field_rva: int,
    addend: int,
    image_base: int,
    target_section_rva: int | None,
    target_section_index: int | None,
) -> tuple[int, bool]:
    """Support compute value processing for internal toolkit callers."""
    if machine == IMAGE_FILE_MACHINE_I386:
        if relocation_type == 0x0001:  # DIR16
            return image_base + target_rva + addend, False
        if relocation_type == 0x0002:  # REL16
            return target_rva + addend - (field_rva + 2), True
        if relocation_type == 0x0006:  # DIR32
            return image_base + target_rva + addend, False
        if relocation_type == 0x0007:  # DIR32NB
            return target_rva + addend, False
        if relocation_type == 0x000A:  # SECTION
            if target_section_index is None:
                raise ContractError("SECTION relocation requires section_index in symbol map")
            return target_section_index + addend, False
        if relocation_type == 0x000B:  # SECREL
            if target_section_rva is None:
                raise ContractError("SECREL relocation requires section_rva in symbol map")
            return target_rva - target_section_rva + addend, False
        if relocation_type == 0x0014:  # REL32
            return target_rva + addend - (field_rva + 4), True
    elif machine == IMAGE_FILE_MACHINE_AMD64:
        if relocation_type == 0x0001:  # ADDR64
            return image_base + target_rva + addend, False
        if relocation_type == 0x0002:  # ADDR32
            return image_base + target_rva + addend, False
        if relocation_type == 0x0003:  # ADDR32NB
            return target_rva + addend, False
        if 0x0004 <= relocation_type <= 0x0009:  # REL32 .. REL32_5
            bias = relocation_type - 0x0004
            return target_rva + addend - (field_rva + 4 + bias), True
        if relocation_type == 0x000A:  # SECTION
            if target_section_index is None:
                raise ContractError("SECTION relocation requires section_index in symbol map")
            return target_section_index + addend, False
        if relocation_type == 0x000B:  # SECREL
            if target_section_rva is None:
                raise ContractError("SECREL relocation requires section_rva in symbol map")
            return target_rva - target_section_rva + addend, False
        if relocation_type == 0x000C:  # SECREL7
            if target_section_rva is None:
                raise ContractError("SECREL7 relocation requires section_rva in symbol map")
            return target_rva - target_section_rva + addend, False
    raise ContractError(
        f"unsupported relocation {relocation_name(machine, relocation_type)} for machine 0x{machine:04x}"
    )


class RelocationResolver:
    """Resolve COFF relocation fields under an explicit original-RVA symbol map."""

    def inspect(self, object_path: Path, *, symbol: str | None = None) -> dict[str, Any]:
        """Execute the inspect operation for the current toolkit workflow."""
        obj = parse_coff(object_path)
        if symbol is None:
            sections = [section.to_dict(obj.machine) for section in obj.sections]
            return {
                "object": str(object_path.resolve()),
                "object_sha256": sha256_file(object_path),
                "architecture": obj.architecture,
                "sections": sections,
                "supported": supported_relocations()[obj.architecture],
            }
        extracted = extract_symbol(obj, symbol)
        return {
            "object": str(object_path.resolve()),
            "object_sha256": sha256_file(object_path),
            "architecture": obj.architecture,
            "extracted": extracted.to_dict(obj.machine),
            "relocations": [relocation.to_dict(obj.machine) for relocation in extracted.relocations],
        }

    def resolve(
        self,
        object_path: Path,
        *,
        symbol: str,
        base_rva: int,
        symbol_map: Mapping[str, Any] | list[Mapping[str, Any]],
        image_base: int = 0,
        section_placements: Mapping[int | str, int] | None = None,
        output_path: Path | None = None,
        expected_bytes: bytes | None = None,
    ) -> dict[str, Any]:
        """Resolve resolve for the current toolkit workflow."""
        obj = parse_coff(object_path)
        # Local labels emitted for intra-function branches may appear in the COFF
        # symbol table after the public function symbol.  In exact round-trip mode
        # the original byte length is authoritative, so do not let the first local
        # label truncate extraction of the function body.
        try:
            extracted = extract_symbol(
                obj, symbol, size=None if expected_bytes is None else len(expected_bytes)
            )
        except FormatError:
            if expected_bytes is None:
                raise
            # A canonicalized mnemonic may shrink the assembled section.  Extract
            # the available function bytes so the caller can identify the first
            # mismatch and fall back only the affected instruction.
            extracted = extract_symbol(obj, symbol)
        normalized = normalize_symbol_map(symbol_map)
        placements = {} if section_placements is None else dict(section_placements)
        buffer = bytearray(extracted.data)
        records: list[dict[str, Any]] = []
        unresolved = 0
        for relocation in extracted.relocations:
            width = relocation_width(obj.machine, relocation.type)
            name = relocation_name(obj.machine, relocation.type)
            record: dict[str, Any] = {
                "offset": relocation.offset,
                "type": name,
                "type_code": relocation.type,
                "symbol_index": relocation.symbol_index,
                "target_symbol": relocation.symbol_name,
                "width": width,
            }
            try:
                if width is None:
                    raise ContractError(f"unknown width for relocation {name}")
                target_name, target_rva, section_rva, section_index = _resolve_target(
                    obj,
                    relocation,
                    extracted=extracted,
                    base_rva=base_rva,
                    symbol_map=normalized,
                    placements=placements,
                )
                record["target_symbol"] = target_name
                if target_rva is None:
                    raise ContractError(f"unresolved relocation target: {target_name!r}")
                pc_relative = (
                    (obj.machine == IMAGE_FILE_MACHINE_I386 and relocation.type in {0x0002, 0x0014})
                    or (obj.machine == IMAGE_FILE_MACHINE_AMD64 and 0x0004 <= relocation.type <= 0x0009)
                )
                addend = _read_addend(
                    extracted.data, relocation.offset, width, signed=pc_relative
                )
                value, signed = _compute_value(
                    machine=obj.machine,
                    relocation_type=relocation.type,
                    target_rva=target_rva,
                    field_rva=base_rva + relocation.offset,
                    addend=addend,
                    image_base=image_base,
                    target_section_rva=section_rva,
                    target_section_index=section_index,
                )
                _write_value(buffer, relocation.offset, width, value, signed=signed)
                record.update(
                    {
                        "status": "resolved",
                        "target_rva": target_rva,
                        "target_section_rva": section_rva,
                        "target_section_index": section_index,
                        "addend": addend,
                        "computed_value": value,
                    }
                )
            except ContractError as exc:
                unresolved += 1
                record.update({"status": "unresolved", "reason": str(exc)})
            records.append(record)
        resolved = bytes(buffer)
        exact = expected_bytes is None or resolved == expected_bytes
        if output_path is not None:
            atomic_write_bytes(output_path, resolved)
        return {
            "object": str(object_path.resolve()),
            "object_sha256": sha256_file(object_path),
            "symbol": symbol,
            "architecture": obj.architecture,
            "machine": obj.machine,
            "base_rva": base_rva,
            "image_base": image_base,
            "input_sha256": sha256_bytes(extracted.data),
            "resolved_sha256": sha256_bytes(resolved),
            "resolved_bytes": resolved,
            "resolved_count": len(records) - unresolved,
            "unresolved_count": unresolved,
            "relocations": records,
            "exact_match": exact,
            "expected_sha256": None if expected_bytes is None else sha256_bytes(expected_bytes),
            "output": None if output_path is None else str(output_path.resolve()),
        }
