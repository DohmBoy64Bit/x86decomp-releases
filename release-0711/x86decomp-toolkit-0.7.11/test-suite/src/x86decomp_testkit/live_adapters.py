"""Provide live adapters support for the standalone verification harness."""
from __future__ import annotations

import importlib
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .config import TestConfig
from .adapters.capabilities import probe_openai_compatible_endpoint
from .adapters.detection import _prefer_windows_executable
from .fixtures import build_minimal_pe32
from .logging_utils import JsonlEventLogger
from .models import AdapterKind, AdapterSpec, ProbeResult, Status, TestResult
from .process import blocked_result, run_process_test
from .timeutil import utc_now


def _path_for(result: ProbeResult, spec: AdapterSpec) -> Path | None:
    """Resolve the executable or installation path associated with an adapter result."""
    if not result.path:
        return None
    path = Path(result.path)
    if path.is_file():
        return path
    root_matches: list[Path] = []
    for marker in spec.root_markers:
        candidate = path / marker
        if candidate.is_file():
            root_matches.append(candidate)
    if root_matches:
        preferred = _prefer_windows_executable(root_matches)
        if preferred:
            return preferred
    for command in spec.commands:
        for base in (path, path / "bin"):
            candidate = base / command
            if candidate.is_file():
                return candidate
            if platform.system() == "Windows" and not candidate.suffix:
                with_ext = base / f"{command}.exe"
                if with_ext.is_file():
                    return with_ext
    return None


def _python_adapter_test(spec: AdapterSpec, result: ProbeResult) -> TestResult:
    """Return the python adapter test derived from `spec`, `result`."""
    started = utc_now()
    details: dict[str, Any] = {}
    try:
        for module_name in spec.python_modules:
            module = importlib.import_module(module_name)
            details[module_name] = str(getattr(module, "__version__", "unknown"))
        status = Status.PASS
        summary = "all declared Python modules imported"
    except Exception as exc:
        status = Status.FAIL
        summary = f"Python adapter import failed: {exc}"
        details["error"] = repr(exc)
    return TestResult(
        test_id=f"adapter:{spec.adapter_id}:import",
        suite="adapters",
        status=status,
        started_at=started,
        finished_at=utc_now(),
        duration_seconds=0.0,
        summary=summary,
        details=details,
        required_adapters=[spec.adapter_id],
    )


def _generic_executable_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> TestResult:
    """Return the generic executable test derived from `spec`, `result`, `config`, and additional options."""
    executable = _path_for(result, spec)
    if executable is None:
        return blocked_result(f"adapter:{spec.adapter_id}:version", "adapters", [spec.adapter_id], "detected adapter has no executable probe target")
    accepted = (0, 1, 2) if spec.adapter_id in {"java", "msvc"} else (0, 1)
    return run_process_test(
        test_id=f"adapter:{spec.adapter_id}:version",
        suite="adapters",
        command=[str(executable), *spec.version_args],
        cwd=config.toolkit_root,
        output_directory=output_directory,
        timeout=min(config.timeout_seconds, 60),
        event_logger=event_logger,
        required_adapters=[spec.adapter_id],
        accepted_return_codes=accepted,
    )


def _compiler_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> TestResult:
    """Return the compiler test derived from `spec`, `result`, `config`, and additional options."""
    executable = _path_for(result, spec)
    if executable is None:
        return blocked_result(f"adapter:{spec.adapter_id}:compile", "adapters", [spec.adapter_id])
    work = output_directory / "adapter-work" / spec.adapter_id
    work.mkdir(parents=True, exist_ok=True)
    source = work / ("probe.cpp" if spec.adapter_id in {"clangxx", "gxx"} else "probe.c")
    source.write_text("int probe(int x) { return x + 1; }\n", encoding="utf-8")
    output = work / "probe.o"
    command = [str(executable), "-c", str(source), "-o", str(output)]
    if spec.adapter_id in {"clang", "clangxx"}:
        command[1:1] = ["--target=i686-pc-windows-msvc"]
        output = work / "probe.obj"
        command[-1] = str(output)
    return run_process_test(
        test_id=f"adapter:{spec.adapter_id}:compile",
        suite="adapters",
        command=command,
        cwd=work,
        output_directory=output_directory,
        timeout=min(config.timeout_seconds, 120),
        event_logger=event_logger,
        required_adapters=[spec.adapter_id],
    )


def _lld_link_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
    adapter_results: dict[str, ProbeResult],
    catalog: dict[str, AdapterSpec],
) -> TestResult:
    """Return the lld link test derived from `spec`, `result`, `config`, and additional options."""
    clang_result = adapter_results.get("clang")
    if not clang_result or not clang_result.installed:
        return blocked_result("adapter:lld-link:link", "adapters", ["clang", "lld-link"])
    clang = _path_for(clang_result, catalog["clang"])
    linker = _path_for(result, spec)
    if clang is None or linker is None:
        return blocked_result("adapter:lld-link:link", "adapters", ["clang", "lld-link"])
    work = output_directory / "adapter-work" / "lld-link"
    work.mkdir(parents=True, exist_ok=True)
    source = work / "entry.c"
    source.write_text("void entry(void) {}\n", encoding="utf-8")
    obj = work / "entry.obj"
    compile_result = subprocess.run([str(clang), "--target=x86_64-pc-windows-msvc", "-c", str(source), "-o", str(obj)], capture_output=True, text=True)
    if compile_result.returncode != 0:
        return TestResult("adapter:lld-link:link", "adapters", Status.FAIL, utc_now(), utc_now(), 0.0, "fixture compilation failed", details={"stderr": compile_result.stderr}, required_adapters=["clang", "lld-link"])
    image = work / "probe.exe"
    return run_process_test(
        test_id="adapter:lld-link:link",
        suite="adapters",
        command=[str(linker), "/entry:entry", "/subsystem:console", "/nodefaultlib", f"/out:{image}", str(obj)],
        cwd=work,
        output_directory=output_directory,
        timeout=min(config.timeout_seconds, 120),
        event_logger=event_logger,
        required_adapters=["clang", "lld-link"],
    )


def _ghidra_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> TestResult:
    """Return the Ghidra test derived from `spec`, `result`, `config`, and additional options."""
    analyze = _path_for(result, spec)
    if analyze is None:
        return blocked_result("adapter:ghidra:headless-export", "adapters", ["ghidra"])
    work = output_directory / "adapter-work" / "ghidra"
    work.mkdir(parents=True, exist_ok=True)
    binary = build_minimal_pe32(work / "minimal.exe")
    project = work / "project"
    project.mkdir(parents=True, exist_ok=True)
    exports = work / "exports"
    command = [
        str(analyze), str(project), "probe", "-import", str(binary), "-overwrite",
        "-scriptPath", str(config.toolkit_root / "ghidra_scripts"),
        "-postScript", "ExportProjectManifest.java", str(exports),
        "-postScript", "ExportFunctionArtifacts.java", str(exports), "all",
    ]
    return run_process_test(
        test_id="adapter:ghidra:headless-export",
        suite="adapters",
        command=command,
        cwd=work,
        output_directory=output_directory,
        timeout=config.timeout_seconds,
        event_logger=event_logger,
        required_adapters=["ghidra"],
    )


def _dynamorio_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> TestResult:
    """Return the dynamorio test derived from `spec`, `result`, `config`, and additional options."""
    drrun = _path_for(result, spec)
    if drrun is None:
        return blocked_result("adapter:dynamorio:drcov", "adapters", ["dynamorio"])
    target = Path(shutil.which("true") or shutil.which("cmd") or "")
    if not target.is_file():
        return blocked_result("adapter:dynamorio:drcov", "adapters", ["dynamorio"], "no harmless host probe executable found")
    work = output_directory / "adapter-work" / "dynamorio"
    work.mkdir(parents=True, exist_ok=True)
    command = [str(drrun), "-t", "drcov", "-dump_text", "-logdir", str(work), "--", str(target)]
    return run_process_test(
        test_id="adapter:dynamorio:drcov",
        suite="adapters",
        command=command,
        cwd=work,
        output_directory=output_directory,
        timeout=min(config.timeout_seconds, 180),
        event_logger=event_logger,
        required_adapters=["dynamorio"],
    )


def _objdiff_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> TestResult:
    """Return the objdiff test derived from `spec`, `result`, `config`, and additional options."""
    executable = _path_for(result, spec)
    if executable is None:
        return blocked_result("adapter:objdiff:help", "adapters", ["objdiff"])
    return run_process_test(
        test_id="adapter:objdiff:help",
        suite="adapters",
        command=[str(executable), "--help"],
        cwd=config.toolkit_root,
        output_directory=output_directory,
        timeout=min(config.timeout_seconds, 60),
        event_logger=event_logger,
        required_adapters=["objdiff"],
        accepted_return_codes=(0, 1, 2),
    )


def _http_endpoint_test(
    spec: AdapterSpec,
    result: ProbeResult,
    config: TestConfig,
    event_logger: JsonlEventLogger,
) -> TestResult:
    """Probe an HTTP endpoint adapter by hitting its OpenAI-compatible /v1/models."""
    started = utc_now()
    if not result.path:
        return blocked_result(f"adapter:{spec.adapter_id}:probe", "adapters", [spec.adapter_id], "no endpoint URL")
    ok, endpoint, diagnostics = probe_openai_compatible_endpoint(result.path, config, timeout=10)
    details: dict[str, Any] = {"endpoint": endpoint, "diagnostics": diagnostics}
    if ok:
        status = Status.PASS
        summary = f"OpenAI-compatible endpoint reachable at {endpoint}"
    else:
        status = Status.FAIL
        summary = f"endpoint probe failed: {'; '.join(diagnostics) if diagnostics else 'unreachable'}"
    return TestResult(
        test_id=f"adapter:{spec.adapter_id}:probe",
        suite="adapters",
        status=status,
        started_at=started,
        finished_at=utc_now(),
        duration_seconds=0.0,
        summary=summary,
        details=details,
        required_adapters=[spec.adapter_id],
    )


def run_live_adapter_tests(
    catalog: dict[str, AdapterSpec],
    probe_results: list[ProbeResult],
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> list[TestResult]:
    """Run live adapter tests."""
    results_by_id = {item.adapter_id: item for item in probe_results}
    tests: list[TestResult] = []
    for adapter_id in sorted(catalog):
        spec = catalog[adapter_id]
        probe = results_by_id[adapter_id]
        if not probe.installed:
            tests.append(blocked_result(f"adapter:{adapter_id}:live", "adapters", [adapter_id]))
            continue
        if spec.kind == AdapterKind.HTTP_ENDPOINT:
            tests.append(_http_endpoint_test(spec, probe, config, event_logger))
        elif spec.kind.value == "python":
            tests.append(_python_adapter_test(spec, probe))
        elif adapter_id in {"clang", "clangxx", "gcc", "gxx"}:
            tests.append(_compiler_test(spec, probe, config, output_directory, event_logger))
        elif adapter_id == "lld-link":
            tests.append(_lld_link_test(spec, probe, config, output_directory, event_logger, results_by_id, catalog))
        elif adapter_id == "ghidra":
            tests.append(_ghidra_test(spec, probe, config, output_directory, event_logger))
        elif adapter_id == "dynamorio":
            tests.append(_dynamorio_test(spec, probe, config, output_directory, event_logger))
        elif adapter_id == "objdiff":
            tests.append(_objdiff_test(spec, probe, config, output_directory, event_logger))
        else:
            tests.append(_generic_executable_test(spec, probe, config, output_directory, event_logger))
    return tests
