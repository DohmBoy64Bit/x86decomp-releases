from __future__ import annotations

import hmac
import json
import os
import stat
import tempfile
import zipfile
from hashlib import sha256
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, sha256_file, utc_now
from .store import GovernanceStore

PROOF_STATUSES = {"byte_identical", "structurally_equivalent", "symbolically_proved", "behaviorally_tested", "partially_validated", "assumption_dependent", "unresolved", "failed"}


class ProofLedger:
    def __init__(self, store: GovernanceStore):
        self.store = store
        self.store.initialize()

    def create_obligation(self, scope_kind: str, scope_id: str, property_name: str, required_status: str, *, assumptions: list[str] | None = None, actor: str = "analyst") -> dict[str, Any]:
        if required_status not in PROOF_STATUSES:
            raise ContractError(f"invalid required proof status: {required_status}")
        obligation_id = random_id("obl")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_proof_obligations(obligation_id,scope_kind,scope_id,property_name,required_status,assumptions_json,created_at) VALUES(?,?,?,?,?,?,?)",
                (obligation_id, scope_kind, scope_id, property_name, required_status, canonical_json(assumptions or []), utc_now()),
            )
            self.store.audit(actor, "proof.obligation.create", obligation_id, {"scope_kind": scope_kind, "scope_id": scope_id, "property": property_name, "required_status": required_status, "assumptions": assumptions or []}, connection=connection)
        return self.obligation(obligation_id)

    def add_result(self, obligation_id: str, status: str, validator: str, report: dict[str, Any], *, artifact_sha256: str | None = None, actor: str = "validator") -> dict[str, Any]:
        if status not in PROOF_STATUSES:
            raise ContractError(f"invalid proof status: {status}")
        self.obligation(obligation_id)
        if artifact_sha256 is not None and len(artifact_sha256) != 64:
            raise ContractError("artifact_sha256 must be a 64-character digest")
        result_id = random_id("proof")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_proof_results(result_id,obligation_id,status,validator,report_json,artifact_sha256,created_at) VALUES(?,?,?,?,?,?,?)",
                (result_id, obligation_id, status, validator, canonical_json(report), artifact_sha256, utc_now()),
            )
            self.store.audit(actor, "proof.result.add", result_id, {"obligation_id": obligation_id, "status": status, "validator": validator, "artifact_sha256": artifact_sha256}, connection=connection)
        return self.result(result_id)

    def obligation(self, obligation_id: str) -> dict[str, Any]:
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_proof_obligations WHERE obligation_id=?", (obligation_id,)).fetchone()
            results = connection.execute("SELECT result_id FROM governance_proof_results WHERE obligation_id=? ORDER BY created_at", (obligation_id,)).fetchall() if row else []
        if not row:
            raise KeyError(obligation_id)
        result = dict(row)
        result["assumptions"] = json.loads(result.pop("assumptions_json"))
        result["results"] = [self.result(r[0]) for r in results]
        return result

    def result(self, result_id: str) -> dict[str, Any]:
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_proof_results WHERE result_id=?", (result_id,)).fetchone()
        if not row:
            raise KeyError(result_id)
        result = dict(row)
        result["report"] = json.loads(result.pop("report_json"))
        return result

    def evaluate(self, obligation_id: str) -> dict[str, Any]:
        obligation = self.obligation(obligation_id)
        statuses = [item["status"] for item in obligation["results"]]
        passed = obligation["required_status"] in statuses
        return {"obligation_id": obligation_id, "passed": passed, "required_status": obligation["required_status"], "observed_statuses": statuses, "assumptions": obligation["assumptions"]}


class ProofBundle:
    """Deterministic, path-safe, independently verifiable proof package."""

    @staticmethod
    def _zip_info(name: str) -> zipfile.ZipInfo:
        info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = (stat.S_IFREG | 0o644) << 16
        return info

    @classmethod
    def export(cls, store: GovernanceStore, output: str | Path, *, include_paths: list[str | Path] | None = None, hmac_key: bytes | None = None) -> dict[str, Any]:
        store.initialize()
        output = Path(output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        audit = store.verify_audit_chain()
        with store.connect() as connection:
            obligations = [dict(r) for r in connection.execute("SELECT * FROM governance_proof_obligations ORDER BY obligation_id").fetchall()]
            results = [dict(r) for r in connection.execute("SELECT * FROM governance_proof_results ORDER BY result_id").fetchall()]
        records = {"obligations": obligations, "results": results, "audit_chain": audit, "exported_at": utc_now(), "truth_boundary": "Finite recorded results only; no arbitrary-program or original-source claim."}
        files: dict[str, bytes] = {"records.json": (json.dumps(records, indent=2, sort_keys=True) + "\n").encode("utf-8")}
        for raw_path in include_paths or []:
            source = Path(raw_path).resolve()
            try:
                relative = source.relative_to(store.project_root).as_posix()
            except ValueError as exc:
                raise ContractError(f"proof artifact outside project root: {source}") from exc
            if not source.is_file() or source.is_symlink():
                raise ContractError(f"proof artifact must be a regular non-symlink file: {source}")
            files[f"artifacts/{relative}"] = source.read_bytes()
        manifest = {
            "format": "x86decomp-proof-bundle-v1",
            "release": "0.7.8",
            "files": {name: {"sha256": sha256(data).hexdigest(), "size": len(data)} for name, data in sorted(files.items())},
            "audit_tip": audit["tip_hash"],
        }
        manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
        files["manifest.json"] = manifest_bytes
        if hmac_key is not None:
            files["manifest.hmac-sha256"] = (hmac.new(hmac_key, manifest_bytes, sha256).hexdigest() + "\n").encode("ascii")
        fd, temporary = tempfile.mkstemp(prefix=output.name + ".", suffix=".tmp", dir=output.parent)
        os.close(fd)
        try:
            with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for name in sorted(files):
                    archive.writestr(cls._zip_info(name), files[name])
            os.replace(temporary, output)
        finally:
            Path(temporary).unlink(missing_ok=True)
        return {"path": str(output), "sha256": sha256_file(output), "files": len(files), "audit_tip": audit["tip_hash"]}

    @staticmethod
    def _validate_member(name: str) -> None:
        path = Path(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name or ":" in name:
            raise ContractError(f"unsafe proof bundle member: {name}")

    @classmethod
    def verify(cls, path: str | Path, *, hmac_key: bytes | None = None, max_members: int = 10000, max_total_bytes: int = 1024 * 1024 * 1024) -> dict[str, Any]:
        path = Path(path).resolve()
        failures: list[str] = []
        with zipfile.ZipFile(path, "r") as archive:
            infos = archive.infolist()
            if len(infos) > max_members:
                raise ContractError("proof bundle has too many members")
            total = 0
            names: set[str] = set()
            for info in infos:
                cls._validate_member(info.filename)
                if info.filename in names:
                    raise ContractError(f"duplicate proof member: {info.filename}")
                names.add(info.filename)
                total += info.file_size
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode):
                    raise ContractError(f"proof bundle contains a symlink: {info.filename}")
            if total > max_total_bytes:
                raise ContractError("proof bundle exceeds uncompressed size limit")
            if "manifest.json" not in names or "records.json" not in names:
                raise ContractError("proof bundle is missing required records")
            manifest_bytes = archive.read("manifest.json")
            manifest = json.loads(manifest_bytes)
            if manifest.get("format") != "x86decomp-proof-bundle-v1":
                failures.append("unsupported proof bundle format")
            for name, expected in manifest.get("files", {}).items():
                if name not in names:
                    failures.append(f"missing declared member: {name}")
                    continue
                data = archive.read(name)
                if sha256(data).hexdigest() != expected.get("sha256") or len(data) != expected.get("size"):
                    failures.append(f"member integrity mismatch: {name}")
            if hmac_key is not None:
                if "manifest.hmac-sha256" not in names:
                    failures.append("missing requested HMAC")
                else:
                    observed = archive.read("manifest.hmac-sha256").decode("ascii").strip()
                    expected = hmac.new(hmac_key, manifest_bytes, sha256).hexdigest()
                    if not hmac.compare_digest(observed, expected):
                        failures.append("manifest HMAC mismatch")
            records = json.loads(archive.read("records.json"))
        return {"path": str(path), "sha256": sha256_file(path), "passed": not failures, "failures": failures, "manifest": manifest, "records_summary": {"obligations": len(records.get("obligations", [])), "results": len(records.get("results", [])), "audit_tip": records.get("audit_chain", {}).get("tip_hash")}}

    @classmethod
    def inspect(cls, path: str | Path) -> dict[str, Any]:
        return cls.verify(path)
