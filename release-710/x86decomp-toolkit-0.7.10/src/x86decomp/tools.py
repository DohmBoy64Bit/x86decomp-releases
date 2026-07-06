"""External-tool discovery and version capture."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .util import utc_now, write_json

_DEFAULT_TOOLS = (
    ("python", "python3", ["--version"]),
    ("gcc", "gcc", ["--version"]),
    ("clang", "clang", ["--version"]),
    ("objdiff-cli", "objdiff-cli", ["--version"]),
    ("java", "java", ["-version"]),
)


def _capture(path: str, args: list[str]) -> dict[str, Any]:
    """Support capture processing for internal toolkit callers."""
    try:
        completed = subprocess.run(
            [path, *args], capture_output=True, text=True, timeout=10, check=False
        )
        combined = (completed.stdout + "\n" + completed.stderr).strip()
        first_line = combined.splitlines()[0] if combined else None
        return {
            "available": True,
            "path": path,
            "version": first_line,
            "return_code": completed.returncode,
        }
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "path": path, "error": str(exc)}


def discover_analyze_headless(explicit_ghidra_home: Path | None = None) -> Path | None:
    """Discover analyze headless for the current toolkit workflow."""
    candidates: list[Path] = []
    if explicit_ghidra_home is not None:
        candidates.append(explicit_ghidra_home)
    env_home = os.environ.get("GHIDRA_HOME")
    if env_home:
        candidates.append(Path(env_home))
    preferred = ("analyzeHeadless.bat", "analyzeHeadless") if os.name == "nt" else ("analyzeHeadless", "analyzeHeadless.bat")
    for home in candidates:
        for name in preferred:
            candidate = home / "support" / name
            if candidate.is_file():
                return candidate.resolve()
    for name in preferred:
        from_path = shutil.which(name)
        if from_path:
            return Path(from_path).resolve()
    return None


def snapshot_tools(output: Path | None = None, ghidra_home: Path | None = None) -> dict[str, Any]:
    """Execute the snapshot tools operation for the current toolkit workflow."""
    tools: dict[str, Any] = {}
    for label, executable, args in _DEFAULT_TOOLS:
        path = shutil.which(executable)
        tools[label] = {"available": False} if path is None else _capture(path, args)
    analyze_headless = discover_analyze_headless(ghidra_home)
    tools["ghidra-analyzeHeadless"] = (
        {"available": False}
        if analyze_headless is None
        else {"available": True, "path": str(analyze_headless)}
    )
    report = {"schema_version": 1, "captured_at": utc_now(), "tools": tools}
    if output is not None:
        write_json(output, report)
    return report
