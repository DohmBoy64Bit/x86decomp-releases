"""Provide the current runtime implementation for the `x86decomp.native.slots` module."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from x86decomp.pe import parse_pe
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import NativeStore


def _int(value: Any, name: str) -> int:
    """Support int processing for internal toolkit callers."""
    if isinstance(value, str):
        try:
            return int(value, 0)
        except ValueError as exc:
            raise ContractError(f"invalid integer for {name}: {value}") from exc
    if isinstance(value, bool) or not isinstance(value, int):
        raise ContractError(f"{name} must be an integer")
    return value


def inventory_from_project(project_root: Path) -> list[dict[str, Any]]:
    """Execute the inventory from project operation for the current toolkit workflow."""
    result: list[dict[str, Any]] = []
    root = project_root.resolve() / "functions"
    if not root.is_dir():
        raise ContractError(f"function artifact directory does not exist: {root}")
    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        manifest_path = directory / "function.json"
        if not manifest_path.is_file():
            continue
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        ranges = data.get("body_ranges", [])
        size = sum(int(record.get("size", 0)) for record in ranges)
        if size <= 0:
            size = sum((directory / str(record["file"])).stat().st_size for record in ranges)
        result.append({
            "function_id": str(data["id"]),
            "rva": _int(data["entry_rva"], "entry_rva"),
            "body_size": size,
            "evidence": [{"kind": "function-artifact", "path": str(manifest_path)}],
        })
    return result


class FunctionSlots:
    """Coordinate function slots behavior for the current toolkit workflow."""
    def __init__(self, store: NativeStore):
        """Initialize the instance with validated constructor state."""
        self.store = store
        store.initialize()

    def audit(
        self,
        functions: Iterable[dict[str, Any]],
        *,
        text_end_rva: int | None = None,
        actor: str = "analyst",
    ) -> dict[str, Any]:
        """Audit audit for the current toolkit workflow."""
        normalized: list[dict[str, Any]] = []
        ids: set[str] = set()
        rvas: set[int] = set()
        for raw in functions:
            function_id = str(raw.get("function_id", raw.get("id", ""))).strip()
            if not function_id:
                raise ContractError("function inventory item lacks function_id")
            rva = _int(raw.get("rva", raw.get("entry_rva")), "rva")
            body_size = _int(raw.get("body_size", raw.get("size")), "body_size")
            confidence = float(raw.get("boundary_confidence", 1.0))
            if function_id in ids or rva in rvas:
                raise ContractError(f"duplicate function id or RVA: {function_id} 0x{rva:x}")
            if rva < 0 or body_size <= 0 or not 0.0 <= confidence <= 1.0:
                raise ContractError(f"invalid function inventory item: {function_id}")
            ids.add(function_id); rvas.add(rva)
            normalized.append({
                "function_id": function_id,
                "rva": rva,
                "body_size": body_size,
                "boundary_confidence": confidence,
                "evidence": list(raw.get("evidence", [])),
            })
        normalized.sort(key=lambda item: item["rva"])
        if not normalized:
            raise ContractError("function inventory is empty")
        if text_end_rva is not None and text_end_rva <= normalized[-1]["rva"]:
            raise ContractError("text_end_rva must lie after the final function")
        now = utc_now()
        counts: dict[str, int] = {}
        records: list[dict[str, Any]] = []
        with self.store.transaction() as connection:
            connection.execute("DELETE FROM native_boundary_findings")
            connection.execute("DELETE FROM native_function_slots")
            for index, item in enumerate(normalized):
                next_rva = normalized[index + 1]["rva"] if index + 1 < len(normalized) else text_end_rva
                slot_end = item["rva"] + item["body_size"] if next_rva is None else next_rva
                slot_size = slot_end - item["rva"]
                if slot_size <= 0:
                    classification = "invalid-range"
                elif item["body_size"] == slot_size:
                    classification = "exact"
                elif item["body_size"] < slot_size:
                    classification = "padded"
                else:
                    classification = "overlap"
                counts[classification] = counts.get(classification, 0) + 1
                slot_id = random_id("slot")
                connection.execute(
                    "INSERT INTO native_function_slots VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                    (slot_id, item["function_id"], item["rva"], item["body_size"], slot_size,
                     slot_end, classification, item["boundary_confidence"], canonical_json(item["evidence"]), now, now),
                )
                if classification in {"overlap", "invalid-range"}:
                    severity = "error"
                    finding_id = random_id("boundary")
                    details = {"rva": item["rva"], "body_size": item["body_size"], "slot_size": slot_size, "slot_end_rva": slot_end}
                    connection.execute(
                        "INSERT INTO native_boundary_findings VALUES(?,?,?,?,?,?,?,?)",
                        (finding_id, item["function_id"], classification, severity,
                         canonical_json(details), "open", now, now),
                    )
                records.append({**item, "slot_id": slot_id, "slot_end_rva": slot_end, "slot_size": slot_size, "classification": classification})
            self.store.audit(actor, "native.boundary.audit", "function-slots", {"counts": counts, "function_count": len(records)}, connection=connection)
        return {"function_count": len(records), "counts": counts, "slots": records}

    def audit_project(self, project_root: Path, binary: Path, *, actor: str = "analyst") -> dict[str, Any]:
        """Audit project for the current toolkit workflow."""
        image = parse_pe(binary)
        text = next((section for section in image.sections if section.name == ".text"), None)
        if text is None:
            raise ContractError("PE has no .text section")
        return self.audit(
            inventory_from_project(project_root),
            text_end_rva=text.virtual_address + text.virtual_size,
            actor=actor,
        )

    def list(self, *, classification: str | None = None) -> list[dict[str, Any]]:
        """Execute the list operation for the current toolkit workflow."""
        query = "SELECT * FROM native_function_slots"
        params: tuple[Any, ...] = ()
        if classification:
            query += " WHERE classification=?"; params = (classification,)
        query += " ORDER BY rva"
        with self.store.connect() as connection:
            return [self.store.decode(row, "evidence_json") for row in connection.execute(query, params)]

    def show(self, function_id: str) -> dict[str, Any]:
        """Execute the show operation for the current toolkit workflow."""
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM native_function_slots WHERE function_id=?", (function_id,)).fetchone()
            if row is None: raise KeyError(function_id)
            result = self.store.decode(row, "evidence_json")
            result["findings"] = [self.store.decode(item, "details_json") for item in connection.execute(
                "SELECT * FROM native_boundary_findings WHERE function_id=? ORDER BY created_at", (function_id,)
            )]
            return result

    def export_fixes(self, output: Path) -> dict[str, Any]:
        """Execute the export fixes operation for the current toolkit workflow."""
        fixes = []
        for slot in self.list():
            if slot["classification"] == "overlap":
                fixes.append({"function_id": slot["function_id"], "entry_rva": slot["rva"], "recommended_body_end_rva": slot["slot_end_rva"], "reason": "body extends into next function slot"})
        payload = {"schema_version": 1, "kind": "ghidra-boundary-fix-proposals", "fixes": fixes}
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return {"output": str(output.resolve()), "fix_count": len(fixes)}
