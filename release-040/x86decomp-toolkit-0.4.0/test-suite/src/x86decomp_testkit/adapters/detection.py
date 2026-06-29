from __future__ import annotations

import importlib
import importlib.metadata
import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Iterable

from ..config import TestConfig
from ..models import AdapterKind, AdapterSpec, ProbeResult


def _module_version(module_name: str) -> str | None:
    candidates = [module_name]
    if module_name == "yaml":
        candidates.insert(0, "PyYAML")
    elif module_name == "z3":
        candidates.insert(0, "z3-solver")
    for name in candidates:
        try:
            return importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            continue
    try:
        module = importlib.import_module(module_name)
    except Exception:
        return None
    value = getattr(module, "__version__", None)
    return str(value) if value is not None else None


def _run_version(executable: Path, args: tuple[str, ...], timeout: int = 15) -> tuple[str | None, str | None]:
    try:
        completed = subprocess.run(
            [str(executable), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return None, str(exc)
    text = (completed.stdout + "\n" + completed.stderr).strip()
    first = next((line.strip() for line in text.splitlines() if line.strip()), None)
    return first, None if completed.returncode in (0, 1) else f"version probe returned {completed.returncode}"


def _windows_executable_suffixes() -> set[str]:
    return {".exe", ".bat", ".cmd", ".com"}


def _prefer_windows_executable(candidates: list[Path]) -> Path | None:
    if platform.system() != "Windows":
        return candidates[0] if candidates else None
    no_ext: list[Path] = []
    has_ext: list[Path] = []
    suffixes = _windows_executable_suffixes()
    for c in candidates:
        (has_ext if c.suffix.lower() in suffixes else no_ext).append(c)
    return (has_ext[0] if has_ext else (no_ext[0] if no_ext else None))


def _candidate_from_root(root: Path, spec: AdapterSpec) -> Path | None:
    if root.is_file():
        return root
    root_matches: list[Path] = []
    for marker in spec.root_markers:
        candidate = root / marker
        if candidate.exists():
            root_matches.append(candidate)
    result = _prefer_windows_executable(root_matches)
    if result:
        return result
    for command in spec.commands:
        candidate = root / command
        if candidate.exists():
            return candidate
        candidate = root / "bin" / command
        if candidate.exists():
            return candidate
    return root if spec.kind in {AdapterKind.DIRECTORY, AdapterKind.TOOLCHAIN} and root.exists() else None


def _known_windows_msvc_roots() -> list[Path]:
    roots: list[Path] = []
    for variable in ("VCINSTALLDIR", "VSINSTALLDIR"):
        value = os.environ.get(variable)
        if value:
            roots.append(Path(value))
    program_files_x86 = os.environ.get("ProgramFiles(x86)")
    if program_files_x86:
        vswhere = Path(program_files_x86) / "Microsoft Visual Studio" / "Installer" / "vswhere.exe"
        if vswhere.exists():
            try:
                completed = subprocess.run(
                    [str(vswhere), "-latest", "-products", "*", "-requires", "Microsoft.VisualStudio.Component.VC.Tools.x86.x64", "-property", "installationPath"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=15,
                    check=False,
                )
                value = completed.stdout.strip()
                if value:
                    roots.append(Path(value))
            except (OSError, subprocess.SubprocessError):
                pass
    return roots


def _find_recursive(root: Path, names: Iterable[str], max_depth: int = 6) -> Path | None:
    names_lower = {name.lower() for name in names}
    root_depth = len(root.parts)
    try:
        for path in root.rglob("*"):
            if len(path.parts) - root_depth > max_depth:
                continue
            if path.is_file() and path.name.lower() in names_lower:
                return path
    except OSError:
        return None
    return None


def detect_adapter(spec: AdapterSpec, config: TestConfig) -> ProbeResult:
    diagnostics: list[str] = []

    if spec.kind == AdapterKind.PYTHON:
        probe_script = r"""
import importlib, importlib.metadata, json, sys
modules = json.loads(sys.argv[1])
result = {"versions": {}, "errors": {}}
for module_name in modules:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", None)
        if version is None:
            for distribution in ({"yaml": "PyYAML", "z3": "z3-solver"}.get(module_name, module_name), module_name):
                try:
                    version = importlib.metadata.version(distribution)
                    break
                except importlib.metadata.PackageNotFoundError:
                    pass
        result["versions"][module_name] = str(version or "unknown")
    except Exception as exc:
        result["errors"][module_name] = repr(exc)
print(json.dumps(result, sort_keys=True))
"""
        try:
            completed = subprocess.run(
                [config.python_executable, "-c", probe_script, __import__("json").dumps(list(spec.python_modules))],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,
                check=False,
            )
            payload = __import__("json").loads(completed.stdout) if completed.stdout.strip() else {}
            errors = payload.get("errors", {}) if isinstance(payload, dict) else {}
            versions = payload.get("versions", {}) if isinstance(payload, dict) else {}
            if completed.returncode != 0:
                diagnostics.append(f"Python probe returned {completed.returncode}: {completed.stderr.strip()}")
            diagnostics.extend(f"import {name!r} failed: {message}" for name, message in sorted(errors.items()))
            installed = completed.returncode == 0 and not errors and all(name in versions for name in spec.python_modules)
            return ProbeResult(
                spec.adapter_id,
                installed=installed,
                path=config.python_executable if installed else None,
                version=", ".join(f"{name}={versions[name]}" for name in spec.python_modules if name in versions) or None,
                source="python-subprocess" if installed else None,
                diagnostics=diagnostics,
            )
        except (OSError, subprocess.SubprocessError, ValueError) as exc:
            diagnostics.append(f"Python probe failed using {config.python_executable!r}: {exc}")
            return ProbeResult(spec.adapter_id, False, diagnostics=diagnostics)

    configured = config.adapter_paths.get(spec.adapter_id)
    if configured:
        configured_path = Path(configured).expanduser().absolute()
        candidate = _candidate_from_root(configured_path, spec)
        if candidate and candidate.exists():
            version_target = candidate
            if candidate.is_dir():
                executable = _find_recursive(candidate, spec.commands, max_depth=8)
                if executable:
                    version_target = executable
            version, error = _run_version(version_target, spec.version_args) if version_target.is_file() else (None, None)
            if error:
                diagnostics.append(error)
            return ProbeResult(spec.adapter_id, True, str(candidate), version, "configured-path", diagnostics)
        diagnostics.append(f"configured path does not satisfy adapter contract: {configured_path}")

    for variable in spec.environment_variables:
        value = os.environ.get(variable)
        if not value:
            continue
        root = Path(value).expanduser()
        candidate = _candidate_from_root(root, spec)
        if candidate and candidate.exists():
            version_target = candidate
            if candidate.is_dir():
                executable = _find_recursive(candidate, spec.commands, max_depth=8)
                if executable:
                    version_target = executable
            version, error = _run_version(version_target, spec.version_args) if version_target.is_file() else (None, None)
            if error:
                diagnostics.append(error)
            return ProbeResult(spec.adapter_id, True, str(candidate), version, f"environment:{variable}", diagnostics)

    for command in spec.commands:
        value = shutil.which(command)
        if value:
            path = Path(value).absolute()
            version, error = _run_version(path, spec.version_args)
            if error:
                diagnostics.append(error)
            return ProbeResult(spec.adapter_id, True, str(path), version, "PATH", diagnostics)

    if spec.adapter_id == "msvc" and platform.system() == "Windows":
        for root in _known_windows_msvc_roots():
            candidate = _find_recursive(root, ("cl.exe",), max_depth=12)
            if candidate:
                version, error = _run_version(candidate, ())
                if error:
                    diagnostics.append(error)
                return ProbeResult(spec.adapter_id, True, str(candidate), version, "visual-studio-discovery", diagnostics)

    if spec.adapter_id == "ghidra":
        known = [Path.home() / "ghidra", Path("/opt/ghidra"), Path("/usr/local/ghidra")]
        if platform.system() == "Windows":
            known.extend([Path("C:/ghidra"), Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Ghidra"])
        for root in known:
            if root.exists():
                candidate = _candidate_from_root(root, spec) or _find_recursive(root, spec.commands, max_depth=4)
                if candidate and candidate.exists():
                    return ProbeResult(spec.adapter_id, True, str(candidate), None, "known-location", diagnostics)

    diagnostics.append("not found in configuration, environment variables, PATH, or known locations")
    return ProbeResult(spec.adapter_id, False, diagnostics=diagnostics)


def detect_all(catalog: dict[str, AdapterSpec], config: TestConfig) -> list[ProbeResult]:
    return [detect_adapter(catalog[key], config) for key in sorted(catalog)]
