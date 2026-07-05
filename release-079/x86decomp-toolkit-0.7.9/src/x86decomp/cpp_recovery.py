"""Bounded C++ relationship recovery from MSVC metadata and code patterns.

The output distinguishes directly parsed metadata from derived candidates.  It
never claims original source declarations, access modifiers, or method names.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .disassembly import decode_instructions
from .errors import ContractError
from .msvc_metadata import PEView, analyze_msvc_metadata
from .util import load_json, utc_now, write_json


def _function_prefix(view: PEView, rva: int, size: int = 24) -> bytes:
    """Implement function prefix.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not view.valid_rva(rva, 1):
        return b""
    for length in range(size, 0, -1):
        if view.valid_rva(rva, length):
            return view.read(rva, length)
    return b""


def _adjustor_thunk_candidate(view: PEView, rva: int) -> dict[str, Any] | None:
    """Implement adjustor thunk candidate.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    prefix = _function_prefix(view, rva)
    if not prefix:
        return None
    try:
        instructions = decode_instructions(prefix, base_address=rva, architecture=view.architecture)
    except Exception:
        return None
    if len(instructions) < 2:
        return None
    first, second = instructions[0], instructions[1]
    this_register = "ecx" if view.architecture == "x86" else "rcx"
    text = f"{first.mnemonic} {first.op_str}".lower()
    if first.mnemonic not in ("add", "sub", "lea") or this_register not in text:
        return None
    if second.mnemonic not in ("jmp", "call"):
        return None
    return {
        "function_rva": rva,
        "this_adjustment_instruction": text,
        "transfer_instruction": f"{second.mnemonic} {second.op_str}",
        "classification": "adjustor_thunk_candidate",
        "evidence_strength": "instruction_pattern",
        "original_method_identity_claimed": False,
    }


def recover_cpp_model(
    pe_path: Path,
    *,
    metadata_report: Path | None = None,
    object_paths: list[Path] | None = None,
    map_path: Path | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Recover cpp model.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if metadata_report is None:
        metadata = analyze_msvc_metadata(pe_path, object_paths=object_paths or (), map_path=map_path)
        metadata_source = "generated"
    else:
        metadata = load_json(metadata_report)
        if not isinstance(metadata, dict) or metadata.get("kind") != "msvc_metadata_analysis":
            raise ContractError("metadata report must be an msvc_metadata_analysis document")
        metadata_source = str(metadata_report.resolve())
    view = PEView(pe_path)
    rtti = metadata.get("rtti", {})
    locators = rtti.get("complete_object_locators", [])
    vtables = rtti.get("vtables", [])
    classes: dict[str, dict[str, Any]] = {}
    for locator in locators:
        type_name = locator.get("type_name")
        if not isinstance(type_name, str) or not type_name:
            continue
        record = classes.setdefault(
            type_name,
            {
                "type_name": type_name,
                "locators": [],
                "bases": [],
                "vtables": [],
                "provenance": [],
            },
        )
        record["locators"].append(locator["rva"])
        record["provenance"].append(
            {
                "kind": "parsed_rtti",
                "locator_rva": locator["rva"],
                "source": metadata_source,
            }
        )
        for base in locator.get("bases", []):
            base_name = base.get("type_name")
            if not base_name:
                continue
            relationship = {
                "base_type": base_name,
                "pmd": base.get("pmd"),
                "attributes": base.get("attributes"),
                "descriptor_rva": base.get("descriptor_rva"),
                "classification": "rtti_base_relationship",
                "source_level_access_claimed": False,
            }
            if relationship not in record["bases"]:
                record["bases"].append(relationship)
    thunks: list[dict[str, Any]] = []
    seen_thunks: set[int] = set()
    for vtable in vtables:
        type_name = vtable.get("type_name")
        if not isinstance(type_name, str) or not type_name:
            continue
        record = classes.setdefault(
            type_name,
            {"type_name": type_name, "locators": [], "bases": [], "vtables": [], "provenance": []},
        )
        functions = list(vtable.get("function_rvas", []))
        vtable_model = {
            "address_point_rva": vtable.get("address_point_rva"),
            "locator_rva": vtable.get("locator_rva"),
            "function_rvas": functions,
            "slot_count": len(functions),
            "classification": "parsed_vtable_candidate",
        }
        record["vtables"].append(vtable_model)
        for function_rva in functions:
            if not isinstance(function_rva, int) or function_rva in seen_thunks:
                continue
            candidate = _adjustor_thunk_candidate(view, function_rva)
            if candidate is not None:
                thunks.append(candidate)
                seen_thunks.add(function_rva)
    # Group vtables by locator and type. Multiple address points for one type are
    # retained rather than collapsed into a guessed source class layout.
    vtable_groups = []
    for type_name, record in sorted(classes.items()):
        vtable_groups.append(
            {
                "type_name": type_name,
                "vtable_address_points": sorted(
                    item["address_point_rva"] for item in record["vtables"] if isinstance(item.get("address_point_rva"), int)
                ),
                "locator_rvas": sorted(set(record["locators"])),
                "grouping_basis": "shared RTTI type name and complete-object locator references",
            }
        )
    initializers = metadata.get("static_initializers", {})
    object_initializers = initializers.get("objects", []) if isinstance(initializers, dict) else []
    initializer_order = [
        {
            "order_key": item.get("order_key"),
            "object": item.get("object"),
            "section": item.get("section"),
            "initializer_symbols": item.get("initializer_symbols", []),
            "classification": "coff_subsection_order_evidence",
        }
        for item in object_initializers
    ]
    initializer_order.sort(key=lambda item: (item.get("order_key") or "", item.get("object") or ""))
    report = {
        "schema_version": 1,
        "kind": "bounded_cpp_recovery",
        "created_at": utc_now(),
        "image": metadata.get("image"),
        "metadata_source": metadata_source,
        "classes": [classes[name] for name in sorted(classes)],
        "vtable_groups": vtable_groups,
        "adjustor_thunk_candidates": sorted(thunks, key=lambda item: item["function_rva"]),
        "static_initializer_order_evidence": initializer_order,
        "counts": {
            "classes": len(classes),
            "vtables": sum(len(record["vtables"]) for record in classes.values()),
            "base_relationships": sum(len(record["bases"]) for record in classes.values()),
            "adjustor_thunk_candidates": len(thunks),
            "initializer_contributions": len(initializer_order),
        },
        "claims": {
            "original_source_declarations_recovered": False,
            "method_names_recovered": False,
            "access_modifiers_recovered": False,
            "template_source_recovered": False,
        },
        "limitations": [
            "RTTI names and relationships are emitted metadata, not a complete source-level class declaration.",
            "Adjustor thunks are instruction-pattern candidates and require call-site or symbol corroboration.",
            "Static-initializer subsection order does not alone prove runtime dependency order.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
