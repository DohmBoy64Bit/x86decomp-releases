"""Record, minimize, and promote governance counterexamples."""
from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any, Callable

from x86decomp.contracts import ContractError, canonical_json, random_id, sha256_bytes, sha256_file, utc_now
from .store import GovernanceStore

Predicate = Callable[[bytes], bool]


class CounterexampleStore:
    """Manage counterexample store state and operations."""
    def __init__(self, store: GovernanceStore):
        """Initialize CounterexampleStore with `store`."""
        self.store = store
        self.store.initialize()
        self.root = self.store.project_root / "counterexamples"

    def add(self, scope_kind: str, scope_id: str, payload: bytes | str | Path, *, predicate: dict[str, Any], provenance: dict[str, Any] | None = None, actor: str = "validator") -> str:
        """Add a record to counterexample store."""
        data = payload if isinstance(payload, bytes) else Path(payload).read_bytes()
        if not data:
            raise ContractError("counterexample payload must not be empty")
        counterexample_id = random_id("cex")
        digest = sha256_bytes(data)
        path = self.root / counterexample_id / "payload.bin"
        path.parent.mkdir(parents=True, exist_ok=False)
        path.write_bytes(data)
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_counterexamples(counterexample_id,scope_kind,scope_id,original_sha256,current_sha256,payload_path,size_bytes,state,predicate_json,provenance_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (counterexample_id, scope_kind, scope_id, digest, digest, str(path.relative_to(self.store.project_root)), len(data), "recorded", canonical_json(predicate), canonical_json(provenance or {}), now, now),
            )
            self.store.audit(actor, "counterexample.add", counterexample_id, {"scope_kind": scope_kind, "scope_id": scope_id, "sha256": digest, "size_bytes": len(data), "predicate": predicate, "provenance": provenance or {}}, connection=connection)
        return counterexample_id

    def minimize(self, counterexample_id: str, predicate: Predicate, *, actor: str = "validator", max_tests: int = 10000) -> dict[str, Any]:
        """Minimize CounterexampleStore for CounterexampleStore."""
        item = self.get(counterexample_id)
        data = Path(item["absolute_payload_path"]).read_bytes()
        if not predicate(data):
            raise ContractError("recorded payload no longer satisfies the failure predicate")
        minimized, tests = ddmin_bytes(data, predicate, max_tests=max_tests)
        digest = sha256_bytes(minimized)
        path = Path(item["absolute_payload_path"])
        original_backup = path.with_name("original.bin")
        if not original_backup.exists():
            shutil.copyfile(path, original_backup)
        temp = path.with_suffix(".tmp")
        temp.write_bytes(minimized)
        if sha256_file(temp) != digest:
            temp.unlink(missing_ok=True)
            raise ContractError("minimized counterexample hash mismatch")
        temp.replace(path)
        with self.store.transaction() as connection:
            connection.execute(
                "UPDATE governance_counterexamples SET current_sha256=?,size_bytes=?,state='minimized',updated_at=? WHERE counterexample_id=?",
                (digest, len(minimized), utc_now(), counterexample_id),
            )
            self.store.audit(actor, "counterexample.minimize", counterexample_id, {"old_size": len(data), "new_size": len(minimized), "tests": tests, "sha256": digest}, connection=connection)
        return {"counterexample_id": counterexample_id, "old_size": len(data), "new_size": len(minimized), "tests": tests, "sha256": digest}

    def promote_to_regression(self, counterexample_id: str, destination_root: str | Path, *, actor: str = "analyst") -> dict[str, Any]:
        """Promote to regression for CounterexampleStore."""
        item = self.get(counterexample_id)
        destination = Path(destination_root) / f"{counterexample_id}.bin"
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(item["absolute_payload_path"], destination)
        digest = sha256_file(destination)
        if digest != item["current_sha256"]:
            destination.unlink(missing_ok=True)
            raise ContractError("regression fixture copy hash mismatch")
        metadata = destination.with_suffix(".json")
        metadata.write_text(json.dumps({k: v for k, v in item.items() if k != "absolute_payload_path"}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        with self.store.transaction() as connection:
            connection.execute("UPDATE governance_counterexamples SET state='regression',updated_at=? WHERE counterexample_id=?", (utc_now(), counterexample_id))
            self.store.audit(actor, "counterexample.promote_regression", counterexample_id, {"destination": str(destination), "sha256": digest}, connection=connection)
        return {"fixture": str(destination), "metadata": str(metadata), "sha256": digest}

    def get(self, counterexample_id: str) -> dict[str, Any]:
        """Return data from counterexample store."""
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_counterexamples WHERE counterexample_id=?", (counterexample_id,)).fetchone()
        if not row:
            raise KeyError(counterexample_id)
        result = dict(row)
        result["predicate"] = json.loads(result.pop("predicate_json"))
        result["provenance"] = json.loads(result.pop("provenance_json"))
        result["absolute_payload_path"] = str(self.store.project_root / result["payload_path"])
        return result

    def list(self) -> list[dict[str, Any]]:
        """List records in counterexample store."""
        with self.store.connect() as connection:
            ids = [row[0] for row in connection.execute("SELECT counterexample_id FROM governance_counterexamples ORDER BY created_at").fetchall()]
        return [self.get(item_id) for item_id in ids]


def ddmin_bytes(data: bytes, predicate: Predicate, *, max_tests: int = 10000) -> tuple[bytes, int]:
    """Delta-debug a byte string while preserving predicate(data) == True."""
    if not data:
        raise ContractError("ddmin input must not be empty")
    tests = 0
    current = data
    granularity = 2
    while len(current) >= 2 and tests < max_tests:
        chunk_size = max(1, (len(current) + granularity - 1) // granularity)
        reduced = False
        for start in range(0, len(current), chunk_size):
            candidate = current[:start] + current[start + chunk_size :]
            if not candidate:
                continue
            tests += 1
            if predicate(candidate):
                current = candidate
                granularity = max(2, granularity - 1)
                reduced = True
                break
            if tests >= max_tests:
                break
        if not reduced:
            if granularity >= len(current):
                break
            granularity = min(len(current), granularity * 2)
    return current, tests
