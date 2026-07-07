"""Detect installed external adapters (toolchains, Python packages, HTTP endpoints)."""
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
from .capabilities import probe_openai_compatible_endpoint


def _module_version(module_name: str) -> str | None:
    """Resolve the version string of an importable module or its distribution.

    Distribution metadata is tried first, mapping ``yaml`` to ``PyYAML`` and ``z3`` to
    ``z3-solver``, before falling back to the module's ``__version__`` attribute.

    Args:
        module_name: Import name of the module to inspect.

    Returns:
        The version string, or ``None`` if neither metadata nor the module is available.
    """
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
    """Run an executable's version command and capture its first output line.

    Args:
        executable: Path to the program to invoke.
        args: Version-probe arguments to pass.
        timeout: Maximum seconds to wait for the process.

    Returns:
        A ``(version_line, error)`` pair. ``version_line`` is the first non-empty output line
        or ``None``; ``error`` describes an invocation failure or a return code outside
        ``0``/``1``, otherwise ``None``.
    """
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
    """Return the set of Windows executable file suffixes used to rank candidates."""
    return {".exe", ".bat", ".cmd", ".com"}


def _prefer_windows_executable(candidates: list[Path]) -> Path | None:
    """Choose the best candidate path, preferring executable suffixes on Windows.

    On non-Windows platforms the first candidate is returned unchanged. On Windows, paths with
    a known executable suffix are preferred over extensionless paths.

    Args:
        candidates: Candidate paths in priority order.

    Returns:
        The selected path, or ``None`` if no candidates were given.
    """
    if platform.system() != "Windows":
        return candidates[0] if candidates else None
    no_ext: list[Path] = []
    has_ext: list[Path] = []
    suffixes = _windows_executable_suffixes()
    for c in candidates:
        (has_ext if c.suffix.lower() in suffixes else no_ext).append(c)
    return (has_ext[0] if has_ext else (no_ext[0] if no_ext else None))


def _candidate_from_root(root: Path, spec: AdapterSpec) -> Path | None:
    """Resolve an adapter's executable or directory from a candidate root.

    A file root is returned directly. Otherwise the spec's root markers and commands (under
    the root and its ``bin`` subdirectory, with a ``.exe`` fallback on Windows) are searched.

    Args:
        root: Directory or file to resolve from.
        spec: Adapter specification providing root markers and commands.

    Returns:
        The resolved path, the root itself for directory/toolchain adapters, or ``None`` when
        nothing satisfies the spec.
    """
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
        for base in (root, root / "bin"):
            candidate = base / command
            if candidate.exists():
                return candidate
            if platform.system() == "Windows" and not candidate.suffix:
                with_ext = base / f"{command}.exe"
                if with_ext.exists():
                    return with_ext
    return root if spec.kind in {AdapterKind.DIRECTORY, AdapterKind.TOOLCHAIN} and root.exists() else None


def _known_windows_msvc_roots() -> list[Path]:
    """Collect likely MSVC installation roots on Windows.

    Reads the ``VCINSTALLDIR`` and ``VSINSTALLDIR`` environment variables and, when available,
    queries ``vswhere.exe`` for the latest install providing the x86/x64 VC tools.

    Returns:
        Candidate installation root paths, possibly empty.
    """
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
    """Search a directory tree for the first file matching any of the given names.

    Matching is case-insensitive and limited to the given depth below the root.

    Args:
        root: Directory to search.
        names: File names to look for.
        max_depth: Maximum directory depth below the root to descend.

    Returns:
        The first matching file path, or ``None`` if none is found or the walk fails.
    """
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


def _with_capabilities(spec: AdapterSpec, installed: bool, path: str | None = None, version: str | None = None, source: str | None = None, diagnostics: list[str] | None = None) -> ProbeResult:
    """Build a probe result, attaching the spec's capabilities only when installed.

    Args:
        spec: Adapter specification being probed.
        installed: Whether the adapter was detected.
        path: Resolved adapter path, if any.
        version: Detected version string, if any.
        source: Label describing how the adapter was found.
        diagnostics: Diagnostic messages accumulated during detection.

    Returns:
        The assembled :class:`ProbeResult`; capabilities are empty unless ``installed``.
    """
    return ProbeResult(
        spec.adapter_id,
        installed=installed,
        path=path,
        version=version,
        source=source,
        diagnostics=list(diagnostics or []),
        capabilities=list(spec.capabilities) if installed else [],
    )


def _detect_http_endpoint(spec: AdapterSpec, config: TestConfig) -> ProbeResult:
    """Probe an OpenAI-compatible HTTP endpoint adapter from config and environment.

    Configured endpoints are tried first, then each declared environment variable; the first
    reachable endpoint wins.

    Args:
        spec: HTTP-endpoint adapter specification.
        config: Test configuration providing adapter paths and probe settings.

    Returns:
        An installed result for the first reachable endpoint, otherwise an uninstalled result
        carrying diagnostics.
    """
    diagnostics: list[str] = []
    configured = config.adapter_paths.get(spec.adapter_id)
    endpoint_values: list[tuple[str, str]] = []
    if configured:
        endpoint_values.append((configured, "configured-endpoint"))
    for variable in spec.environment_variables:
        value = os.environ.get(variable)
        if value:
            endpoint_values.append((value, f"environment:{variable}"))
    for value, source in endpoint_values:
        ok, endpoint, notes = probe_openai_compatible_endpoint(value, config)
        diagnostics.extend(notes)
        if ok and endpoint:
            return _with_capabilities(spec, True, path=endpoint, version="OpenAI-compatible HTTP", source=source, diagnostics=diagnostics)
    if not endpoint_values:
        diagnostics.append("no configured endpoint or declared endpoint environment variable found")
    return _with_capabilities(spec, False, diagnostics=diagnostics)


def detect_adapter(spec: AdapterSpec, config: TestConfig) -> ProbeResult:
    """Detect a single adapter according to its kind and resolution rules.

    HTTP-endpoint adapters are delegated to the endpoint probe and Python adapters are checked
    by importing their modules in a subprocess. Other kinds are resolved from configured paths,
    environment variables, ``PATH``, and adapter-specific known locations (MSVC via Visual
    Studio discovery, Ghidra via common install directories).

    Args:
        spec: Adapter specification to detect.
        config: Test configuration providing paths, the Python executable, and probe settings.

    Returns:
        A :class:`ProbeResult` describing whether and how the adapter was found.
    """
    diagnostics: list[str] = []

    if spec.kind == AdapterKind.HTTP_ENDPOINT:
        return _detect_http_endpoint(spec, config)

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
            return _with_capabilities(
                spec,
                installed=installed,
                path=config.python_executable if installed else None,
                version=", ".join(f"{name}={versions[name]}" for name in spec.python_modules if name in versions) or None,
                source="python-subprocess" if installed else None,
                diagnostics=diagnostics,
            )
        except (OSError, subprocess.SubprocessError, ValueError) as exc:
            diagnostics.append(f"Python probe failed using {config.python_executable!r}: {exc}")
            return _with_capabilities(spec, False, diagnostics=diagnostics)

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
            return _with_capabilities(spec, True, str(candidate), version, "configured-path", diagnostics)
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
            return _with_capabilities(spec, True, str(candidate), version, f"environment:{variable}", diagnostics)

    for command in spec.commands:
        value = shutil.which(command)
        if value:
            path = Path(value).absolute()
            version, error = _run_version(path, spec.version_args)
            if error:
                diagnostics.append(error)
            return _with_capabilities(spec, True, str(path), version, "PATH", diagnostics)

    if spec.adapter_id == "msvc" and platform.system() == "Windows":
        for root in _known_windows_msvc_roots():
            candidate = _find_recursive(root, ("cl.exe",), max_depth=12)
            if candidate:
                version, error = _run_version(candidate, ())
                if error:
                    diagnostics.append(error)
                return _with_capabilities(spec, True, str(candidate), version, "visual-studio-discovery", diagnostics)

    if spec.adapter_id == "ghidra":
        known = [Path.home() / "ghidra", Path("/opt/ghidra"), Path("/usr/local/ghidra")]
        if platform.system() == "Windows":
            known.extend([Path("C:/ghidra"), Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Ghidra"])
        for root in known:
            if root.exists():
                candidate = _candidate_from_root(root, spec) or _find_recursive(root, spec.commands, max_depth=4)
                if candidate and candidate.exists():
                    return _with_capabilities(spec, True, str(candidate), None, "known-location", diagnostics)

    diagnostics.append("not found in configuration, environment variables, PATH, or known locations")
    return _with_capabilities(spec, False, diagnostics=diagnostics)


def detect_all(catalog: dict[str, AdapterSpec], config: TestConfig) -> list[ProbeResult]:
    """Detect every adapter in a catalog, ordered by adapter id.

    Args:
        catalog: Mapping of adapter id to specification.
        config: Test configuration passed to each detection.

    Returns:
        Probe results for all catalog entries, sorted by key.
    """
    return [detect_adapter(catalog[key], config) for key in sorted(catalog)]
