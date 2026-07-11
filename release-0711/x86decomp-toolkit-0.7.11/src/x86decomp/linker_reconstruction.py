"""Evidence-driven linker reconstruction plans.

Plans are generated only from supplied PE/MAP/COFF/archive evidence.  Unknown
placement, runtime library, linker flag, and import decisions remain explicit
unresolved items rather than inferred facts.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

from .coff import parse_coff, resolve_comdats
from .coff_archive import parse_coff_archive
from .errors import ContractError
from .linker_layout import reconstruct_linker_layout
from .pe import parse_pe
from .util import sha256_file, utc_now, write_json


def build_linker_reconstruction_plan(
    pe_path: Path,
    map_path: Path,
    *,
    object_paths: Iterable[Path],
    library_paths: Iterable[Path] = (),
    linker: str = "lld-link",
    output_path: str = "build/reconstructed.exe",
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Build linker reconstruction plan."""
    objects = [path.resolve() for path in object_paths]
    libraries = [path.resolve() for path in library_paths]
    if not objects:
        raise ContractError("linker reconstruction requires at least one COFF object")
    layout = reconstruct_linker_layout(pe_path, map_path, object_paths=objects)
    parsed_objects = [parse_coff(path) for path in objects]
    comdat = resolve_comdats(parsed_objects).to_dict()
    archives = [parse_coff_archive(path).to_dict() for path in libraries]
    image = parse_pe(pe_path)
    object_by_basename = {path.name.lower(): path for path in objects}
    ordered_objects: list[Path] = []
    unresolved = list(layout.get("unresolved", []))
    for object_name in layout.get("object_order", []):
        candidate = object_by_basename.get(Path(object_name).name.lower())
        if candidate is None:
            unresolved.append(f"object order entry not supplied: {object_name}")
        elif candidate not in ordered_objects:
            ordered_objects.append(candidate)
    for path in objects:
        if path not in ordered_objects:
            ordered_objects.append(path)
    placements: list[dict[str, Any]] = []
    occupied: dict[str, list[tuple[int, int, str]]] = {}
    for contribution in layout.get("contributions", []):
        rva = contribution.get("rva")
        end_rva = contribution.get("end_rva")
        section_name = contribution.get("section_name")
        if not isinstance(rva, int) or not isinstance(end_rva, int) or not section_name:
            unresolved.append(f"contribution has no exact placement: {contribution.get('object')}")
            continue
        placement = {
            "object": contribution["object"],
            "section": section_name,
            "rva": rva,
            "end_rva": end_rva,
            "length": contribution["length"],
            "evidence": "linker_map_contribution",
            "exact_extent": True,
        }
        for start, end, owner in occupied.setdefault(section_name, []):
            if rva < end and start < end_rva:
                unresolved.append(f"overlapping contributions in {section_name}: {owner} and {contribution['object']}")
        occupied[section_name].append((rva, end_rva, contribution["object"]))
        placements.append(placement)
    sections = [
        {
            "name": section.name,
            "virtual_address": section.virtual_address,
            "virtual_size": section.virtual_size,
            "raw_offset": section.raw_offset,
            "raw_size": section.raw_size,
            "characteristics": section.characteristics,
        }
        for section in image.sections
    ]
    arguments = [
        "/NOLOGO",
        f"/MACHINE:{'X86' if image.to_dict()['architecture'] == 'x86' else 'X64'}",
        f"/BASE:0x{image.image_base:x}",
        f"/FILEALIGN:{image.file_alignment}",
        f"/ALIGN:{image.section_alignment}",
        "/OUT:{output}",
        "@{response_file}",
    ]
    # Subsystem values are observed directly; translate only the common numeric
    # values whose linker names are stable.
    subsystem_names = {1: "NATIVE", 2: "WINDOWS", 3: "CONSOLE", 9: "WINDOWSCE", 10: "EFI_APPLICATION"}
    if image.subsystem in subsystem_names:
        arguments.insert(2, f"/SUBSYSTEM:{subsystem_names[image.subsystem]}")
    else:
        unresolved.append(f"linker subsystem argument not generated for numeric subsystem {image.subsystem}")
    plan = {
        "schema_version": 1,
        "kind": "linker_reconstruction_plan",
        "created_at": utc_now(),
        "reference_image": {
            "path": str(pe_path.resolve()),
            "sha256": image.file_sha256,
            "architecture": image.to_dict()["architecture"],
        },
        "map": {"path": str(map_path.resolve()), "sha256": sha256_file(map_path)},
        "objects": [{"path": str(path), "sha256": sha256_file(path)} for path in ordered_objects],
        "libraries": [{"path": str(path), "sha256": sha256_file(path)} for path in libraries],
        "archives": archives,
        "sections": sections,
        "placements": placements,
        "comdat_resolution": comdat,
        "linker": linker,
        "relink_manifest": {
            "schema_version": 1,
            "linker": linker,
            "objects": [str(path) for path in ordered_objects] + [str(path) for path in libraries],
            "output": output_path,
            "arguments": arguments,
            "reference_image": str(pe_path.resolve()),
            "map_file": str(map_path.resolve()),
            "layout_objects": [str(path) for path in ordered_objects],
            "timeout_seconds": 600,
            "inherit_environment": True,
        },
        "unresolved": sorted(set(unresolved)),
        "ready_for_relink": not unresolved and bool(placements),
        "complete_original_link_command_claimed": False,
        "limitations": [
            "A linker map may omit private-symbol and padding decisions.",
            "The generated response preserves evidenced object order but cannot recover erased command-line flags.",
            "Archive member selection is inventoried; exact historical library-search behavior requires the original toolchain.",
        ],
    }
    if report_path is not None:
        write_json(report_path, plan)
    return plan


def write_relink_manifest_from_plan(plan: dict[str, Any], output: Path) -> dict[str, Any]:
    """Write relink manifest from plan."""
    if plan.get("kind") != "linker_reconstruction_plan":
        raise ContractError("plan kind must be linker_reconstruction_plan")
    manifest = plan.get("relink_manifest")
    if not isinstance(manifest, dict):
        raise ContractError("plan has no relink_manifest")
    write_json(output, manifest)
    return manifest
