"""Provide the current runtime implementation for the `x86decomp.governance.changesets` module."""
from __future__ import annotations

import json
import stat
import zipfile
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, sha256_bytes, sha256_file, utc_now
from .store import GovernanceStore


class ChangeSet:
    """Portable, append-only governance audit changesets with base-tip conflict checks."""

    @staticmethod
    def export(store: GovernanceStore, output: str | Path, *, after_hash: str | None = None) -> dict[str, Any]:
        """Execute the export operation for the current toolkit workflow."""
        store.initialize()
        with store.connect() as connection:
            if after_hash:
                base = connection.execute("SELECT sequence FROM governance_audit_events WHERE event_hash=?", (after_hash,)).fetchone()
                if not base:
                    raise ContractError("after_hash is not in the local audit chain")
                rows = connection.execute("SELECT * FROM governance_audit_events WHERE sequence>? ORDER BY sequence", (base[0],)).fetchall()
            else:
                rows = connection.execute("SELECT * FROM governance_audit_events ORDER BY sequence").fetchall()
        events = [dict(row) for row in rows]
        tip_hash = events[-1]["event_hash"] if events else after_hash
        manifest = {"format": "x86decomp-governance-changeset-v1", "changeset_id": random_id("change"), "base_event_hash": after_hash, "tip_event_hash": tip_hash, "event_count": len(events), "created_at": utc_now()}
        payload = (json.dumps({"manifest": manifest, "events": events}, indent=2, sort_keys=True) + "\n").encode("utf-8")
        output = Path(output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        info = zipfile.ZipInfo("changeset.json", date_time=(1980, 1, 1, 0, 0, 0)); info.compress_type = zipfile.ZIP_DEFLATED; info.external_attr = (stat.S_IFREG | 0o644) << 16
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            archive.writestr(info, payload)
        with store.transaction() as connection:
            connection.execute("INSERT INTO governance_changesets(changeset_id,base_event_hash,tip_event_hash,manifest_json,created_at) VALUES(?,?,?,?,?)", (manifest["changeset_id"], after_hash, tip_hash, canonical_json(manifest), manifest["created_at"]))
            store.audit("system", "changeset.export", manifest["changeset_id"], {"output_sha256": sha256_file(output), **manifest}, connection=connection)
        return {**manifest, "path": str(output), "sha256": sha256_file(output)}

    @staticmethod
    def inspect(path: str | Path) -> dict[str, Any]:
        """Execute the inspect operation for the current toolkit workflow."""
        path = Path(path).resolve()
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            if [item.filename for item in infos] != ["changeset.json"]:
                raise ContractError("changeset archive must contain only changeset.json")
            if infos[0].file_size > 128 * 1024 * 1024:
                raise ContractError("changeset exceeds size bound")
            document = json.loads(archive.read("changeset.json"))
        manifest = document.get("manifest", {})
        events = document.get("events", [])
        if manifest.get("format") != "x86decomp-governance-changeset-v1" or manifest.get("event_count") != len(events):
            raise ContractError("invalid changeset manifest")
        previous = manifest.get("base_event_hash")
        failures = []
        for event in events:
            body = {"occurred_at": event["occurred_at"], "actor": event["actor"], "category": event["category"], "subject_id": event["subject_id"], "payload": json.loads(event["payload_json"]), "previous_hash": event["previous_hash"]}
            expected = sha256_bytes(canonical_json(body).encode("utf-8"))
            if event["previous_hash"] != previous or event["event_hash"] != expected:
                failures.append(event["event_id"])
            previous = event["event_hash"]
        if previous != manifest.get("tip_event_hash"):
            failures.append("tip_hash")
        return {"path": str(path), "sha256": sha256_file(path), "manifest": manifest, "events": events, "passed": not failures, "failures": failures}

    @classmethod
    def apply(cls, store: GovernanceStore, path: str | Path, *, actor: str = "analyst") -> dict[str, Any]:
        """Execute the apply operation for the current toolkit workflow."""
        inspected = cls.inspect(path)
        if not inspected["passed"]:
            raise ContractError("changeset integrity failed")
        local_tip = store.verify_audit_chain()["tip_hash"]
        base = inspected["manifest"].get("base_event_hash")
        if base != local_tip:
            raise ContractError(f"changeset base mismatch: local={local_tip!r} expected={base!r}")
        # Changesets deliberately carry audit records only. Domain mutations require
        # explicit subsystem importers so no schema/table can be overwritten silently.
        with store.transaction() as connection:
            for event in inspected["events"]:
                connection.execute(
                    "INSERT INTO governance_audit_events(event_id,occurred_at,actor,category,subject_id,payload_json,previous_hash,event_hash) VALUES(?,?,?,?,?,?,?,?)",
                    (event["event_id"], event["occurred_at"], event["actor"], event["category"], event["subject_id"], event["payload_json"], event["previous_hash"], event["event_hash"]),
                )
            connection.execute("INSERT OR IGNORE INTO governance_changesets(changeset_id,base_event_hash,tip_event_hash,manifest_json,created_at,applied_at) VALUES(?,?,?,?,?,?)", (inspected["manifest"]["changeset_id"], base, inspected["manifest"].get("tip_event_hash"), canonical_json(inspected["manifest"]), inspected["manifest"].get("created_at"), utc_now()))
        return {"applied": True, "changeset_id": inspected["manifest"]["changeset_id"], "events": len(inspected["events"]), "new_tip": store.verify_audit_chain()["tip_hash"], "actor": actor}
