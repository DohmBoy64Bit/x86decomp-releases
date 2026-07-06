"""MSVC linker-map parsing and object contribution layout reconstruction.

The parser accepts the text format emitted by LINK.EXE ``/MAP`` and LLD's
MSVC-compatible map writer.  It records segment groups, public symbols, object
contributions, preferred load address, and entry point.  Reconstruction is
explicitly evidence driven: a map file and actual COFF objects are required for
claims about original object ordering.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .coff import CoffObject, parse_coff, resolve_comdats
from .errors import ContractError, FormatError
from .pe import parse_pe
from .util import sha256_file, utc_now, write_json

_SEGMENT_RE = re.compile(
    r"^\s*([0-9A-Fa-f]{4}):([0-9A-Fa-f]{8,16})\s+([0-9A-Fa-f]+)H\s+(\S+)\s+(\S+)\s*$"
)
_PUBLIC_RE = re.compile(
    r"^\s*([0-9A-Fa-f]{4}):([0-9A-Fa-f]{8,16})\s+(\S+)\s+([0-9A-Fa-f]{8,16})\s+([fFiI ]*)\s*(.*?)\s*$"
)
_CONTRIB_RE = re.compile(
    r"^\s*([0-9A-Fa-f]{4}):([0-9A-Fa-f]{8,16})\s+([0-9A-Fa-f]+)H\s+(.*?\.(?:obj|o|lib)(?:\([^)]*\))?)\s*$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class MapSegment:
    """Store validated map segment fields used by toolkit reports and adapters."""
    segment: int
    offset: int
    length: int
    name: str
    class_name: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "segment": self.segment,
            "offset": self.offset,
            "length": self.length,
            "name": self.name,
            "class": self.class_name,
        }


@dataclass(frozen=True)
class MapContribution:
    """Store validated map contribution fields used by toolkit reports and adapters."""
    segment: int
    offset: int
    length: int
    object_name: str

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "segment": self.segment,
            "offset": self.offset,
            "length": self.length,
            "object": self.object_name,
        }


@dataclass(frozen=True)
class MapPublic:
    """Store validated map public fields used by toolkit reports and adapters."""
    segment: int
    offset: int
    name: str
    rva_plus_base: int
    flags: str
    object_name: str | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "segment": self.segment,
            "offset": self.offset,
            "name": self.name,
            "rva_plus_base": self.rva_plus_base,
            "flags": self.flags,
            "object": self.object_name,
        }


@dataclass(frozen=True)
class LinkerMap:
    """Store validated linker map fields used by toolkit reports and adapters."""
    path: Path | None
    module_name: str | None
    timestamp: str | None
    preferred_load_address: int | None
    entry_segment: int | None
    entry_offset: int | None
    segments: tuple[MapSegment, ...]
    contributions: tuple[MapContribution, ...]
    publics: tuple[MapPublic, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "format": "msvc_map",
            "source_path": None if self.path is None else str(self.path),
            "source_sha256": None if self.path is None else sha256_file(self.path),
            "module_name": self.module_name,
            "timestamp": self.timestamp,
            "preferred_load_address": self.preferred_load_address,
            "entry": None
            if self.entry_segment is None
            else {"segment": self.entry_segment, "offset": self.entry_offset},
            "segments": [item.to_dict() for item in self.segments],
            "contributions": [item.to_dict() for item in self.contributions],
            "publics": [item.to_dict() for item in self.publics],
        }


def parse_msvc_map_text(text: str, *, path: Path | None = None) -> LinkerMap:
    """Parse msvc map text for the current toolkit workflow."""
    module_name: str | None = None
    timestamp: str | None = None
    preferred: int | None = None
    entry_segment: int | None = None
    entry_offset: int | None = None
    segments: list[MapSegment] = []
    contributions: list[MapContribution] = []
    publics: list[MapPublic] = []
    section = "header"

    lines = text.splitlines()
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        lower = stripped.lower()
        if module_name is None and not lower.startswith(("timestamp", "preferred", "start ")):
            # LINK writes the image name as the first non-empty line.
            module_name = stripped
            continue
        if lower.startswith("timestamp is"):
            timestamp = stripped[len("Timestamp is") :].strip()
            continue
        if lower.startswith("preferred load address is"):
            value = stripped.rsplit(" ", 1)[-1]
            try:
                preferred = int(value, 16)
            except ValueError as exc:
                raise FormatError(f"invalid preferred load address in map: {value}") from exc
            continue
        if lower.startswith("start") and "length" in lower and "name" in lower and "class" in lower:
            section = "segments"
            continue
        if "address" in lower and "publics by value" in lower:
            section = "publics"
            continue
        if lower.startswith("entry point at"):
            token = stripped.split()[-1]
            try:
                seg, off = token.split(":", 1)
                entry_segment, entry_offset = int(seg, 16), int(off, 16)
            except (ValueError, TypeError) as exc:
                raise FormatError(f"invalid map entry point: {token}") from exc
            continue
        segment_match = _SEGMENT_RE.match(line)
        if segment_match and section == "segments":
            segments.append(
                MapSegment(
                    segment=int(segment_match.group(1), 16),
                    offset=int(segment_match.group(2), 16),
                    length=int(segment_match.group(3), 16),
                    name=segment_match.group(4),
                    class_name=segment_match.group(5),
                )
            )
            continue
        contribution_match = _CONTRIB_RE.match(line)
        if contribution_match:
            contributions.append(
                MapContribution(
                    segment=int(contribution_match.group(1), 16),
                    offset=int(contribution_match.group(2), 16),
                    length=int(contribution_match.group(3), 16),
                    object_name=contribution_match.group(4).strip(),
                )
            )
            continue
        public_match = _PUBLIC_RE.match(line)
        if public_match and section == "publics":
            object_name = public_match.group(6).strip() or None
            publics.append(
                MapPublic(
                    segment=int(public_match.group(1), 16),
                    offset=int(public_match.group(2), 16),
                    name=public_match.group(3),
                    rva_plus_base=int(public_match.group(4), 16),
                    flags=public_match.group(5).strip(),
                    object_name=object_name,
                )
            )
    if not segments and not publics and preferred is None:
        raise FormatError("input does not look like an MSVC-compatible linker map")
    return LinkerMap(
        path=path,
        module_name=module_name,
        timestamp=timestamp,
        preferred_load_address=preferred,
        entry_segment=entry_segment,
        entry_offset=entry_offset,
        segments=tuple(segments),
        contributions=tuple(contributions),
        publics=tuple(publics),
    )


def parse_msvc_map(path: Path) -> LinkerMap:
    """Parse msvc map for the current toolkit workflow."""
    resolved = path.resolve()
    if not resolved.is_file():
        raise ContractError(f"linker map does not exist: {resolved}")
    return parse_msvc_map_text(resolved.read_text(encoding="utf-8", errors="replace"), path=resolved)


def _normalize_object_key(value: str) -> str:
    """Support normalize object key processing for internal toolkit callers."""
    value = value.replace("\\", "/")
    if "(" in value and value.endswith(")"):
        value = value[value.rfind("(") + 1 : -1]
    return Path(value).name.lower()


def reconstruct_linker_layout(
    pe_path: Path,
    map_path: Path,
    *,
    object_paths: Iterable[Path] = (),
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Reconstruct linker layout for the current toolkit workflow."""
    image = parse_pe(pe_path)
    linker_map = parse_msvc_map(map_path)
    objects = [parse_coff(path) for path in object_paths]
    object_lookup: dict[str, list[CoffObject]] = {}
    for obj in objects:
        assert obj.path is not None
        object_lookup.setdefault(_normalize_object_key(str(obj.path)), []).append(obj)
    section_by_index = {index + 1: section for index, section in enumerate(image.sections)}
    # A map segment number normally corresponds to a PE section group, but the
    # exact relationship can diverge after subsection merging. Prefer an
    # explicit map-segment name match and retain the index fallback as evidence
    # of lower confidence rather than silently asserting equivalence.
    section_by_segment: dict[int, tuple[Any, str]] = {}
    for segment in linker_map.segments:
        base_name = segment.name.split("$", 1)[0]
        named = next((item for item in image.sections if item.name == base_name), None)
        if named is not None:
            section_by_segment[segment.segment] = (named, "map_segment_name")
        elif segment.segment in section_by_index:
            section_by_segment[segment.segment] = (section_by_index[segment.segment], "ordinal_fallback")
    contributions: list[dict[str, Any]] = []
    unresolved: list[str] = []
    for contribution in linker_map.contributions:
        section_match = section_by_segment.get(contribution.segment)
        section = None if section_match is None else section_match[0]
        section_mapping_source = None if section_match is None else section_match[1]
        normalized = _normalize_object_key(contribution.object_name)
        matches = object_lookup.get(normalized, [])
        object_record: dict[str, Any] | None = None
        if len(matches) == 1:
            obj = matches[0]
            object_record = {
                "path": str(obj.path),
                "sha256": obj.raw_sha256,
                "section_count": len(obj.sections),
                "comdat_sections": [item.index for item in obj.sections if item.is_comdat],
            }
        elif len(matches) > 1:
            unresolved.append(f"ambiguous object basename: {normalized}")
        elif objects:
            unresolved.append(f"map contribution object not supplied: {contribution.object_name}")
        rva = None
        if section is not None:
            rva = section.virtual_address + contribution.offset
        contributions.append(
            {
                **contribution.to_dict(),
                "section_name": None if section is None else section.name,
                "section_mapping_source": section_mapping_source,
                "rva": rva,
                "end_rva": None if rva is None else rva + contribution.length,
                "object_record": object_record,
            }
        )
    # Standard LINK /MAP files reliably identify the owning object for public
    # symbols even when they do not emit byte-accurate contribution records.
    # Use those public records to reconstruct an evidenced object ordering while
    # explicitly not claiming the gaps or private-symbol extents are known.
    public_groups: dict[tuple[str, int], list[MapPublic]] = {}
    for public in linker_map.publics:
        if public.object_name:
            public_groups.setdefault((_normalize_object_key(public.object_name), public.segment), []).append(public)
    public_object_ranges: list[dict[str, Any]] = []
    for (object_key, segment_number), records in public_groups.items():
        records.sort(key=lambda item: (item.offset, item.name))
        matches = object_lookup.get(object_key, [])
        object_record = None
        if len(matches) == 1:
            obj = matches[0]
            object_record = {
                "path": str(obj.path),
                "sha256": obj.raw_sha256,
                "section_count": len(obj.sections),
                "comdat_sections": [item.index for item in obj.sections if item.is_comdat],
            }
        elif len(matches) > 1:
            unresolved.append(f"ambiguous public-symbol object basename: {object_key}")
        elif objects:
            unresolved.append(f"public-symbol object not supplied: {object_key}")
        public_object_ranges.append(
            {
                "object": object_key,
                "segment": segment_number,
                "first_offset": records[0].offset,
                "last_public_offset": records[-1].offset,
                "first_rva_plus_base": min(item.rva_plus_base for item in records),
                "public_count": len(records),
                "publics": [item.to_dict() for item in records],
                "object_record": object_record,
                "extent_is_exact": False,
            }
        )
    public_object_ranges.sort(key=lambda item: (item["first_rva_plus_base"], item["object"]))

    comdat = resolve_comdats(objects).to_dict() if objects else None
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "linker_layout_reconstruction",
        "image": {
            "path": str(pe_path.resolve()),
            "sha256": image.file_sha256,
            "image_base": image.image_base,
            "sections": [section.to_dict() for section in image.sections],
        },
        "map": linker_map.to_dict(),
        "contributions": contributions,
        "public_object_ranges": public_object_ranges,
        "object_order": [item["object"] for item in public_object_ranges],
        "comdat_resolution": comdat,
        "unresolved": sorted(set(unresolved)),
        "object_order_evidenced": bool(linker_map.contributions or public_object_ranges),
        "byte_accurate_contributions_evidenced": bool(linker_map.contributions),
        "complete_original_layout_claimed": False,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
