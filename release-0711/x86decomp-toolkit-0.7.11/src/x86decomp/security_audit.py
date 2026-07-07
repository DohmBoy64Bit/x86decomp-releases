"""Release/project security auditing and SBOM generation.

The audit is deterministic and offline.  It inventories dependencies and risky
filesystem state; vulnerability databases require an external scanner and are
reported as unavailable rather than fabricated.
"""

from __future__ import annotations

import importlib.metadata
import json
import os
import re
import stat
from pathlib import Path
from typing import Any

from .errors import ContractError
from .util import sha256_file, utc_now, write_json


_PEM_BLOCKS = (
    ("PRIVATE KEY", re.compile(r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----[\s\S]+?-----END (?:RSA |OPENSSH )?PRIVATE KEY-----", re.IGNORECASE)),
)
_SECRET_ASSIGNMENT = re.compile(
    r"(?im)^\s*(aws_secret_access_key|client_secret)\s*[:=]\s*[\"']?([A-Za-z0-9_+/=-]{12,})",
)


def _secret_findings(text: str) -> list[dict[str, str]]:
    """Support secret findings processing for internal toolkit callers."""
    findings: list[dict[str, str]] = []
    for name, pattern in _PEM_BLOCKS:
        if pattern.search(text):
            findings.append({"pattern": name, "reason": "complete PEM private-key block"})
    for match in _SECRET_ASSIGNMENT.finditer(text):
        value = match.group(2)
        if value.lower() not in {"placeholder", "example_secret", "changeme", "not-a-secret"}:
            findings.append({"pattern": match.group(1), "reason": "credential-like assignment"})
    return findings



def generate_sbom(output: Path | None = None) -> dict[str, Any]:
    """Generate sbom for the current toolkit workflow."""
    components: list[dict[str, Any]] = []
    for distribution in sorted(importlib.metadata.distributions(), key=lambda item: (item.metadata.get("Name") or "").lower()):
        name = distribution.metadata.get("Name")
        if not name:
            continue
        components.append(
            {
                "type": "library",
                "name": name,
                "version": distribution.version,
                "purl": f"pkg:pypi/{name.lower().replace('_', '-')}@{distribution.version}",
                "licenses": [distribution.metadata.get("License")] if distribution.metadata.get("License") else [],
            }
        )
    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "serialNumber": "urn:uuid:x86decomp-offline-environment",
        "version": 1,
        "metadata": {
            "timestamp": utc_now(),
            "component": {"type": "application", "name": "x86decomp-toolkit", "version": "0.7.11"},
            "properties": [
                {"name": "x86decomp:inventory_scope", "value": "current_python_environment"},
                {"name": "x86decomp:vulnerability_scan_performed", "value": "false"},
            ],
        },
        "components": components,
    }
    if output is not None:
        write_json(output, sbom)
    return sbom


def audit_source_tree(root: Path, *, report_path: Path | None = None) -> dict[str, Any]:
    """Audit source tree for the current toolkit workflow."""
    root = root.resolve()
    if not root.is_dir():
        raise ContractError(f"audit root is not a directory: {root}")
    findings: list[dict[str, Any]] = []
    files = 0
    total_bytes = 0
    for path in sorted(root.rglob("*")):
        relative = str(path.relative_to(root))
        if path.is_symlink():
            findings.append({"severity": "high", "kind": "symlink", "path": relative, "target": os.readlink(path)})
            continue
        if path.is_dir():
            if path.name in {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "venv", "dist", "build"}:
                findings.append({"severity": "medium", "kind": "transient_directory", "path": relative})
            continue
        if not path.is_file():
            findings.append({"severity": "high", "kind": "special_file", "path": relative})
            continue
        files += 1
        total_bytes += path.stat().st_size
        mode = stat.S_IMODE(path.stat().st_mode)
        if mode & stat.S_IWOTH:
            findings.append({"severity": "medium", "kind": "world_writable", "path": relative, "mode": oct(mode)})
        if path.suffix in {".pyc", ".pyo"} or path.name.endswith(".egg-info"):
            findings.append({"severity": "medium", "kind": "build_artifact", "path": relative})
        if path.stat().st_size <= 4 * 1024 * 1024:
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                text = ""
            for secret in _secret_findings(text):
                findings.append({"severity": "critical", "kind": "possible_secret", "path": relative, **secret})
    severity_counts = {severity: sum(1 for item in findings if item["severity"] == severity) for severity in ("critical", "high", "medium", "low")}
    report = {
        "schema_version": 1,
        "kind": "source_security_audit",
        "created_at": utc_now(),
        "root": str(root),
        "file_count": files,
        "total_bytes": total_bytes,
        "findings": findings,
        "severity_counts": severity_counts,
        "passed": severity_counts["critical"] == 0 and severity_counts["high"] == 0,
        "vulnerability_database_checked": False,
        "limitations": [
            "This offline audit does not query vulnerability databases.",
            "Secret-pattern matches require human review and may be false positives.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
    return report


def verify_release_manifest(root: Path, manifest_path: Path | None = None) -> dict[str, Any]:
    """Verify release manifest for the current toolkit workflow."""
    root = root.resolve()
    manifest_path = manifest_path.resolve() if manifest_path is not None else root / "MANIFEST.sha256"
    if not manifest_path.is_file():
        raise ContractError(f"manifest is missing: {manifest_path}")
    failures: list[str] = []
    checked = 0
    listed: set[str] = set()
    for line_number, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        digest, separator, relative = line.partition("  ")
        if not separator or len(digest) != 64:
            failures.append(f"invalid manifest line {line_number}")
            continue
        path = (root / relative).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            failures.append(f"manifest path escapes root: {relative}")
            continue
        listed.add(relative)
        if not path.is_file() or path.is_symlink():
            failures.append(f"manifest file missing or unsafe: {relative}")
        elif sha256_file(path) != digest:
            failures.append(f"manifest hash mismatch: {relative}")
        else:
            checked += 1
    return {"valid": not failures, "checked": checked, "listed": len(listed), "failures": failures}


def run_dependency_vulnerability_audit(
    *,
    executable: str = "pip-audit",
    report_path: Path | None = None,
    timeout_seconds: int = 300,
) -> dict[str, Any]:
    """Run an installed pip-audit executable and preserve its exact findings.

    Exit code 1 is accepted when the tool produced a valid vulnerability report.
    Missing tools and malformed output are errors, never silent passes.
    """
    import shutil
    import subprocess
    import sys

    candidate = Path(executable).expanduser()
    if candidate.is_absolute() or candidate.parent != Path("."):
        if not candidate.is_file():
            raise ContractError(f"dependency audit executable is missing: {candidate}")
        resolved = str(candidate.resolve())
    else:
        discovered = shutil.which(executable)
        if discovered is None:
            raise ContractError(f"dependency audit executable is not installed: {executable}")
        resolved = discovered
    if os.name == "nt" and not resolved.lower().endswith((".exe", ".com", ".bat", ".cmd")):
        command = [sys.executable, resolved, "--format", "json", "--progress-spinner", "off"]
    else:
        command = [resolved, "--format", "json", "--progress-spinner", "off"]
    completed = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout_seconds,
        check=False,
        shell=False,
    )
    if completed.returncode not in (0, 1):
        raise ContractError(f"dependency audit failed with exit code {completed.returncode}: {completed.stderr.strip()}")
    try:
        document = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise ContractError("dependency audit did not return valid JSON") from exc
    dependencies = document.get("dependencies", []) if isinstance(document, dict) else document if isinstance(document, list) else []
    vulnerabilities: list[dict[str, Any]] = []
    for dependency in dependencies:
        if not isinstance(dependency, dict):
            continue
        for vulnerability in dependency.get("vulns", dependency.get("vulnerabilities", [])):
            vulnerabilities.append(
                {
                    "dependency": dependency.get("name"),
                    "version": dependency.get("version"),
                    "vulnerability": vulnerability,
                }
            )
    report = {
        "schema_version": 1,
        "kind": "python_dependency_vulnerability_audit",
        "created_at": utc_now(),
        "tool": resolved,
        "tool_sha256": sha256_file(Path(resolved)),
        "return_code": completed.returncode,
        "dependency_count": len(dependencies),
        "vulnerability_count": len(vulnerabilities),
        "vulnerabilities": vulnerabilities,
        "passed": len(vulnerabilities) == 0,
        "stderr": completed.stderr,
        "raw_report": document,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
