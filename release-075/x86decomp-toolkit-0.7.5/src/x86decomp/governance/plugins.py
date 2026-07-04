from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, sha256_file, utc_now
from .store import GovernanceStore

PLUGIN_API_VERSION = "1"


class PluginRegistry:
    def __init__(self, store: GovernanceStore):
        self.store = store
        self.store.initialize()

    @staticmethod
    def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
        required = {"name", "version", "api_version", "executable", "capabilities"}
        missing = sorted(required - set(manifest))
        failures = [f"missing field: {item}" for item in missing]
        if manifest.get("api_version") != PLUGIN_API_VERSION:
            failures.append(f"unsupported plugin API version: {manifest.get('api_version')!r}")
        if not isinstance(manifest.get("capabilities"), list) or not all(isinstance(item, str) and item for item in manifest.get("capabilities", [])):
            failures.append("capabilities must be a non-empty-safe string list")
        executable = Path(str(manifest.get("executable", ""))).expanduser().resolve()
        if not executable.is_file() or executable.is_symlink():
            failures.append("executable must be a regular non-symlink file")
        return {"passed": not failures, "failures": failures, "resolved_executable": str(executable)}

    def install(self, manifest_path: str | Path, *, actor: str = "analyst") -> dict[str, Any]:
        path = Path(manifest_path).resolve()
        manifest = json.loads(path.read_text(encoding="utf-8"))
        validation = self.validate_manifest(manifest)
        if not validation["passed"]:
            raise ContractError("invalid plugin manifest: " + "; ".join(validation["failures"]))
        executable = Path(validation["resolved_executable"])
        plugin_id = random_id("plugin")
        digest = sha256_file(executable)
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_plugin_records(plugin_id,name,version,api_version,executable,executable_sha256,capabilities_json,installed_at) VALUES(?,?,?,?,?,?,?,?)",
                (plugin_id, manifest["name"], manifest["version"], manifest["api_version"], str(executable), digest, canonical_json(manifest["capabilities"]), utc_now()),
            )
            self.store.audit(actor, "plugin.install", plugin_id, {"name": manifest["name"], "version": manifest["version"], "executable": str(executable), "sha256": digest, "capabilities": manifest["capabilities"]}, connection=connection)
        return self.get(plugin_id)

    def get(self, plugin_id: str) -> dict[str, Any]:
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_plugin_records WHERE plugin_id=?", (plugin_id,)).fetchone()
        if not row:
            raise KeyError(plugin_id)
        result = dict(row)
        result["capabilities"] = json.loads(result.pop("capabilities_json"))
        result["enabled"] = bool(result["enabled"])
        return result

    def list(self) -> list[dict[str, Any]]:
        with self.store.connect() as connection:
            ids = [r[0] for r in connection.execute("SELECT plugin_id FROM governance_plugin_records ORDER BY name").fetchall()]
        return [self.get(item) for item in ids]

    def doctor(self, plugin_id: str) -> dict[str, Any]:
        plugin = self.get(plugin_id)
        executable = Path(plugin["executable"])
        failures = []
        if not executable.is_file() or executable.is_symlink():
            failures.append("plugin executable is missing or unsafe")
        elif sha256_file(executable) != plugin["executable_sha256"]:
            failures.append("plugin executable hash changed")
        return {"plugin_id": plugin_id, "passed": not failures, "failures": failures, "enabled": plugin["enabled"]}

    def invoke(self, plugin_id: str, capability: str, request: dict[str, Any], *, timeout_seconds: int = 60, max_output_bytes: int = 16 * 1024 * 1024, actor: str = "system") -> dict[str, Any]:
        if not 1 <= timeout_seconds <= 3600:
            raise ContractError("timeout_seconds must be in [1,3600]")
        plugin = self.get(plugin_id)
        health = self.doctor(plugin_id)
        if not health["passed"] or not plugin["enabled"]:
            raise ContractError("plugin is not healthy and enabled")
        if capability not in plugin["capabilities"]:
            raise ContractError(f"plugin does not declare capability: {capability}")
        envelope = {"api_version": PLUGIN_API_VERSION, "capability": capability, "request": request}
        environment = {"PATH": os.environ.get("PATH", ""), "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8"}
        exe_path = plugin["executable"]
        try:
            if os.name == "nt" and not exe_path.lower().endswith((".exe", ".com", ".bat", ".cmd")):
                envelope_data = (canonical_json(envelope) + "\n").encode("utf-8")
                completed = subprocess.run(
                    [sys.executable, exe_path], input=envelope_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    timeout=timeout_seconds, check=False, env=environment,
                )
            else:
                completed = subprocess.run(
                    [exe_path], input=(canonical_json(envelope) + "\n").encode("utf-8"), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    timeout=timeout_seconds, check=False, env=environment,
                )
        except subprocess.TimeoutExpired as exc:
            raise ContractError(f"plugin timed out after {timeout_seconds}s") from exc
        if len(completed.stdout) > max_output_bytes or len(completed.stderr) > max_output_bytes:
            raise ContractError("plugin output exceeded configured bound")
        if completed.returncode != 0:
            raise ContractError(f"plugin exited {completed.returncode}: {completed.stderr.decode('utf-8', 'replace')[:4096]}")
        try:
            response = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            raise ContractError("plugin returned invalid JSON") from exc
        if not isinstance(response, dict) or response.get("api_version") != PLUGIN_API_VERSION or "result" not in response:
            raise ContractError("plugin response violates the API envelope")
        self.store.audit(actor, "plugin.invoke", plugin_id, {"capability": capability, "request_sha256": __import__("hashlib").sha256(canonical_json(request).encode()).hexdigest(), "returncode": completed.returncode})
        return {"plugin_id": plugin_id, "capability": capability, "result": response["result"], "stderr": completed.stderr.decode("utf-8", "replace")}
