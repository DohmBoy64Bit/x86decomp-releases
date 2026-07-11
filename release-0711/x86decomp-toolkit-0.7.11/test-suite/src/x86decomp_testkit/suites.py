"""Provide suites support for the standalone verification harness."""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Any

from .config import TestConfig
from .coverage_audit import audit_public_symbol_execution
from .inventory import audit_catalog, build_inventory, load_feature_catalog
from .junit import parse_junit
from .logging_utils import JsonlEventLogger
from .models import ProbeResult, Status, TestResult
from .process import blocked_result, run_process_test
from .timeutil import utc_now



def _missing(adapter_results: list[ProbeResult], required: tuple[str, ...]) -> list[str]:
    """Return the required capabilities not satisfied by any installed adapter.

    Args:
        adapter_results: Adapter probe results carrying install state and capabilities.
        required: The capability or adapter identifiers a suite depends on.

    Returns:
        The subset of ``required`` that is neither an installed adapter nor a
        capability provided by one.
    """
    installed = {item.adapter_id: item.installed for item in adapter_results}
    satisfied_capabilities = {capability for item in adapter_results if item.installed for capability in item.capabilities}
    missing: list[str] = []
    for requirement in required:
        if installed.get(requirement, False) or requirement in satisfied_capabilities:
            continue
        missing.append(requirement)
    return missing

def _result(test_id: str, suite: str, passed: bool, summary: str, *, details: dict[str, Any] | None = None) -> TestResult:
    """Build a zero-duration :class:`TestResult` with the current timestamp.

    Args:
        test_id: The unique test identifier.
        suite: The suite the test belongs to.
        passed: Whether the test passed.
        summary: A human-readable summary line.
        details: Optional structured details attached to the result.

    Returns:
        The constructed :class:`TestResult`.
    """
    now = utc_now()
    return TestResult(
        test_id=test_id,
        suite=suite,
        status=Status.PASS if passed else Status.FAIL,
        started_at=now,
        finished_at=now,
        duration_seconds=0.0,
        summary=summary,
        details=details or {},
    )


def run_inventory_tests(
    config: TestConfig,
    output_directory: Path,
    feature_catalog_path: Path,
) -> tuple[dict[str, Any], list[TestResult]]:
    """Build the toolkit inventory and audit it against the feature catalog.

    Writes ``inventory.json`` and ``catalog-audit.json``, then checks that the catalog
    matches discovered commands, that cataloged workflow states appear in ``workflow.py``,
    and that the adapter catalog matches the pinned feature catalog.

    Args:
        config: The test configuration, providing toolkit root and Python executable.
        output_directory: Directory to write inventory and audit artifacts into.
        feature_catalog_path: Path to the pinned feature catalog.

    Returns:
        A ``(inventory, results)`` tuple with the discovered inventory and the catalog,
        workflow-state, and adapter-catalog test results.
    """
    inventory = build_inventory(config.toolkit_root, config.python_executable)
    (output_directory / "inventory.json").write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    catalog = load_feature_catalog(feature_catalog_path)
    audit = audit_catalog(inventory, catalog)
    (output_directory / "catalog-audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result = _result(
        "inventory:feature-catalog",
        "inventory",
        bool(audit["passed"]),
        "feature catalog exactly matches discovered commands, modules, schemas, and Ghidra scripts" if audit["passed"] else "feature catalog is stale or incomplete",
        details=audit,
    )
    expected_states = catalog.get("workflow_states", {})
    workflow_source = (config.toolkit_root / "src" / "x86decomp" / "workflow.py").read_text(encoding="utf-8")
    missing_states = [state for states in expected_states.values() for state in states if f'"{state}"' not in workflow_source]
    state_result = _result(
        "inventory:workflow-states",
        "inventory",
        not missing_states,
        "all cataloged matching and functional states are present" if not missing_states else "workflow states are missing",
        details={"missing_states": missing_states},
    )
    from .adapters import adapter_catalog
    expected_adapters = set(catalog.get("adapters", []))
    actual_adapters = set(adapter_catalog())
    adapter_details = {
        "uncataloged_adapters": sorted(actual_adapters - expected_adapters),
        "stale_adapters": sorted(expected_adapters - actual_adapters),
    }
    adapter_result = _result(
        "inventory:adapter-catalog",
        "inventory",
        not adapter_details["uncataloged_adapters"] and not adapter_details["stale_adapters"],
        "adapter catalog exactly matches the pinned feature catalog" if not adapter_details["uncataloged_adapters"] and not adapter_details["stale_adapters"] else "adapter catalog drift detected",
        details=adapter_details,
    )
    return inventory, [result, state_result, adapter_result]


def run_cli_surface_tests(
    config: TestConfig,
    inventory: dict[str, Any],
    output_directory: Path,
    event_logger: JsonlEventLogger,
) -> list[TestResult]:
    """Run a ``--help`` smoke test for every discovered CLI command.

    Args:
        config: The test configuration.
        inventory: The discovered inventory, providing ``cli_commands``.
        output_directory: Directory to write process output into.
        event_logger: Logger receiving per-process events.

    Returns:
        One :class:`TestResult` per CLI command.
    """
    environment = {"PYTHONPATH": str(config.toolkit_root / "src"), **config.custom_environment}
    results: list[TestResult] = []
    for command_name in inventory["cli_commands"]:
        results.append(
            run_process_test(
                test_id=f"cli-help:{command_name}",
                suite="cli-surface",
                command=[config.python_executable, "-m", "x86decomp", command_name, "--help"],
                cwd=config.toolkit_root,
                output_directory=output_directory,
                timeout=min(config.timeout_seconds, 60),
                environment=environment,
                event_logger=event_logger,
            )
        )
    return results


def _verify_manifest(toolkit_root: Path) -> tuple[bool, dict[str, Any]]:
    """Verify source files against the ``MANIFEST.sha256`` hash list.

    Args:
        toolkit_root: The toolkit root containing ``MANIFEST.sha256``.

    Returns:
        A ``(ok, details)`` tuple; ``details`` records the number of files checked and
        any missing files, hash mismatches, or malformed lines.
    """
    import hashlib

    manifest = toolkit_root / "MANIFEST.sha256"
    if not manifest.is_file():
        return False, {"error": "MANIFEST.sha256 is missing"}
    failures: list[str] = []
    checked = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, separator, relative = line.partition("  ")
        if not separator:
            failures.append(f"invalid manifest line: {line}")
            continue
        if relative == "MANIFEST.sha256":
            continue
        path = toolkit_root / relative
        if not path.is_file():
            failures.append(f"missing: {relative}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            failures.append(f"hash mismatch: {relative}")
        checked += 1
    return not failures, {"checked": checked, "failures": failures}


def _validate_schemas(toolkit_root: Path) -> tuple[bool, dict[str, Any]]:
    """Validate every ``*.schema.json`` under ``schemas`` against its meta-schema.

    Args:
        toolkit_root: The toolkit root containing the ``schemas`` directory.

    Returns:
        A ``(ok, details)`` tuple; ``ok`` requires at least one schema and no failures.
        If ``jsonschema`` is unavailable, returns ``(False, {"error": ...})``.
    """
    try:
        from jsonschema.validators import validator_for
    except ImportError as exc:
        return False, {"error": f"jsonschema unavailable: {exc}"}
    failures: list[str] = []
    checked = 0
    for path in sorted((toolkit_root / "schemas").rglob("*.schema.json")):
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            validator_for(schema).check_schema(schema)
        except Exception as exc:
            failures.append(f"{path.name}: {exc}")
        checked += 1
    return checked > 0 and not failures, {"checked": checked, "failures": failures}


def _validate_java(toolkit_root: Path) -> tuple[bool, dict[str, Any]]:
    """Parse every Ghidra ``*.java`` script to confirm it is syntactically valid.

    Args:
        toolkit_root: The toolkit root containing ``ghidra_scripts``.

    Returns:
        A ``(ok, details)`` tuple; ``ok`` requires at least one script and no parse
        failures. If ``javalang`` is unavailable, returns ``(False, {"error": ...})``.
    """
    try:
        import javalang
    except ImportError as exc:
        return False, {"error": f"javalang unavailable: {exc}"}
    failures: list[str] = []
    checked = 0
    for path in sorted((toolkit_root / "ghidra_scripts").glob("*.java")):
        try:
            javalang.parse.parse(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"{path.name}: {exc}")
        checked += 1
    return checked > 0 and not failures, {"checked": checked, "failures": failures}


def _validate_skill(toolkit_root: Path) -> tuple[bool, dict[str, Any]]:
    """Validate the presence and required frontmatter of the packaged skill.

    Checks that ``skills/x86decomp/SKILL.md`` exists and that its YAML frontmatter
    defines both ``name`` and ``description``.

    Args:
        toolkit_root: The toolkit root containing the ``skills`` directory.

    Returns:
        A ``(ok, details)`` tuple with the parsed frontmatter and any missing keys.
        If PyYAML is unavailable or the file is missing, returns ``(False, {"error": ...})``.
    """
    try:
        import yaml
    except ImportError as exc:
        return False, {"error": f"PyYAML unavailable: {exc}"}
    path = toolkit_root / "skills" / "x86decomp" / "SKILL.md"
    if not path.is_file():
        return False, {"error": "skills/x86decomp/SKILL.md is missing"}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False, {"error": "skill frontmatter opening delimiter is missing"}
    end = text.find("\n---\n", 4)
    if end < 0:
        return False, {"error": "skill frontmatter closing delimiter is missing"}
    frontmatter = yaml.safe_load(text[4:end])
    required = ["name", "description"]
    missing = [key for key in required if not isinstance(frontmatter, dict) or not frontmatter.get(key)]
    return not missing, {"frontmatter": frontmatter, "missing": missing}


def run_structural_tests(
    config: TestConfig,
    suite_root: Path,
    output_directory: Path,
    event_logger: JsonlEventLogger,
    adapter_results: list[ProbeResult],
) -> list[TestResult]:
    """Run structural integrity checks over the toolkit and suite sources.

    Covers manifest hashes, JSON schema validity, Ghidra Java syntax, skill
    frontmatter, ``compileall`` of both source trees, and the optional contract
    validator. Checks whose adapter capabilities are missing are reported as blocked.

    Args:
        config: The test configuration.
        suite_root: The test-suite root.
        output_directory: Directory to write process output into.
        event_logger: Logger receiving per-process events.
        adapter_results: Adapter probe results used to gate optional checks.

    Returns:
        The list of structural :class:`TestResult` entries.
    """
    results: list[TestResult] = []
    manifest_ok, manifest_details = _verify_manifest(config.toolkit_root)
    results.append(_result("structure:manifest-hashes", "structure", manifest_ok, "source manifest hashes verified" if manifest_ok else "source manifest verification failed", details=manifest_details))
    missing = _missing(adapter_results, ("jsonschema",))
    if missing:
        results.append(blocked_result("structure:json-schemas", "structure", missing))
    else:
        schema_ok, schema_details = _validate_schemas(config.toolkit_root)
        results.append(_result("structure:json-schemas", "structure", schema_ok, "all JSON schemas are valid" if schema_ok else "JSON schema validation failed", details=schema_details))
    missing = _missing(adapter_results, ("javalang",))
    if missing:
        results.append(blocked_result("structure:ghidra-java-syntax", "structure", missing))
    else:
        java_ok, java_details = _validate_java(config.toolkit_root)
        results.append(_result("structure:ghidra-java-syntax", "structure", java_ok, "all Ghidra Java scripts parse" if java_ok else "Ghidra Java syntax validation failed", details=java_details))
    missing = _missing(adapter_results, ("pyyaml",))
    if missing:
        results.append(blocked_result("structure:skill-frontmatter", "structure", missing))
    else:
        skill_ok, skill_details = _validate_skill(config.toolkit_root)
        results.append(_result("structure:skill-frontmatter", "structure", skill_ok, "skill frontmatter is valid" if skill_ok else "skill frontmatter validation failed", details=skill_details))
    results.append(
        run_process_test(
            test_id="structure:python-compileall-toolkit",
            suite="structure",
            command=[config.python_executable, "-m", "compileall", "-q", str(config.toolkit_root / "src")],
            cwd=config.toolkit_root,
            output_directory=output_directory,
            timeout=min(config.timeout_seconds, 120),
            event_logger=event_logger,
        )
    )
    results.append(
        run_process_test(
            test_id="structure:python-compileall-suite",
            suite="structure",
            command=[config.python_executable, "-m", "compileall", "-q", str((suite_root / "src") if (suite_root / "src").is_dir() else Path(__file__).resolve().parent)],
            cwd=suite_root,
            output_directory=output_directory,
            timeout=min(config.timeout_seconds, 120),
            event_logger=event_logger,
        )
    )
    validate_script = config.toolkit_root / "scripts" / "validate-contracts.py"
    if validate_script.is_file() and not _missing(adapter_results, ("jsonschema", "pyyaml")):
        results.append(
            run_process_test(
                test_id="structure:toolkit-contract-validator",
                suite="structure",
                command=[config.python_executable, str(validate_script)],
                cwd=config.toolkit_root,
                output_directory=output_directory,
                timeout=min(config.timeout_seconds, 180),
                environment={"PYTHONPATH": str(config.toolkit_root / "src")},
                event_logger=event_logger,
            )
        )
    return results



def run_harness_self_tests(
    config: TestConfig,
    suite_root: Path,
    output_directory: Path,
    event_logger: JsonlEventLogger,
    adapter_results: list[ProbeResult],
) -> list[TestResult]:
    """Run the harness' own pytest self-tests and assert no tests are skipped.

    Blocked when ``pytest`` or ``jsonschema`` is unavailable. Uses the source test
    directory when present, otherwise the packaged self-tests.

    Args:
        config: The test configuration.
        suite_root: The test-suite root.
        output_directory: Directory to write JUnit and process output into.
        event_logger: Logger receiving per-process events.
        adapter_results: Adapter probe results used to gate the run.

    Returns:
        The process result plus, when JUnit output exists, a no-skipped-tests result.
    """
    missing = _missing(adapter_results, ("pytest", "jsonschema"))
    if missing:
        return [blocked_result("harness:self-tests", "harness", missing)]
    source_tests = suite_root / "tests"
    packaged_tests = Path(__file__).resolve().parent / "self_tests"
    tests_dir = source_tests if source_tests.is_dir() else packaged_tests
    if not tests_dir.is_dir():
        return [_result("harness:self-tests-present", "harness", False, "harness self-test directory is missing")]
    junit = output_directory / "harness-junit.xml"
    environment = {"PYTHONPATH": str((suite_root / "src") if (suite_root / "src").is_dir() else Path(__file__).resolve().parent), "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1", **config.custom_environment}
    process_result = run_process_test(
        test_id="harness:self-tests",
        suite="harness",
        command=[
            config.python_executable, "-m", "pytest", "-q", str(tests_dir),
            f"--junitxml={junit}",
        ],
        cwd=suite_root,
        output_directory=output_directory,
        timeout=min(config.timeout_seconds, 600),
        environment=environment,
        event_logger=event_logger,
    )
    results = [process_result]
    if junit.is_file():
        data = parse_junit(junit)
        results.append(_result(
            "harness:no-skipped-tests",
            "harness",
            data["skipped"] == 0,
            "harness self-tests reported zero skipped tests" if data["skipped"] == 0 else "harness self-tests reported skipped tests",
            details=data,
        ))
    return results

def run_pytest_and_coverage(
    config: TestConfig,
    package_root: Path,
    output_directory: Path,
    event_logger: JsonlEventLogger,
    adapter_results: list[ProbeResult],
) -> list[TestResult]:
    """Run the toolkit and supplemental pytest suites under branch coverage.

    Blocked unless all required adapters are installed. On success, emits JSON, XML, and
    HTML coverage reports and asserts no skipped tests, full function-body execution, and
    the configured line and branch coverage floors.

    Args:
        config: The test configuration, providing floors and timeouts.
        package_root: The installed testkit package root, providing bundled tests.
        output_directory: Directory to write coverage and JUnit artifacts into.
        event_logger: Logger receiving per-process events.
        adapter_results: Adapter probe results used to gate the run.

    Returns:
        The list of pytest and coverage :class:`TestResult` entries.
    """
    results: list[TestResult] = []
    required = ("pytest", "coverage", "capstone", "unicorn", "z3", "angr", "fastapi", "uvicorn")
    missing = _missing(adapter_results, required)
    if missing:
        return [blocked_result("pytest:toolkit-and-supplemental", "pytest", missing)]
    junit = output_directory / "junit.xml"
    coverage_data = output_directory / ".coverage"
    coverage_json = output_directory / "coverage.json"
    coverage_xml = output_directory / "coverage.xml"
    coverage_html = output_directory / "coverage-html"
    test_directory = package_root / "toolkit_tests"
    environment = {
        "PYTHONPATH": os.pathsep.join([str(config.toolkit_root / "src"), str(package_root.parent)]),
        "COVERAGE_FILE": str(coverage_data),
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
        **config.custom_environment,
    }
    pytest_result = run_process_test(
        test_id="pytest:toolkit-and-supplemental",
        suite="pytest",
        command=[
            config.python_executable,
            "-m",
            "coverage",
            "run",
            "--branch",
            f"--source={config.toolkit_root / 'src' / 'x86decomp'}",
            "-m",
            "pytest",
            "-q",
            str(config.toolkit_root / "tests"),
            str(test_directory),
            f"--junitxml={junit}",
        ],
        cwd=config.toolkit_root,
        output_directory=output_directory,
        timeout=config.timeout_seconds,
        environment=environment,
        event_logger=event_logger,
    )
    results.append(pytest_result)
    if pytest_result.status != Status.PASS or not coverage_data.is_file():
        return results
    for test_id, command in (
        ("coverage:json", [config.python_executable, "-m", "coverage", "json", "-o", str(coverage_json)]),
        ("coverage:xml", [config.python_executable, "-m", "coverage", "xml", "-o", str(coverage_xml)]),
        ("coverage:html", [config.python_executable, "-m", "coverage", "html", "-d", str(coverage_html)]),
    ):
        results.append(
            run_process_test(
                test_id=test_id,
                suite="coverage",
                command=command,
                cwd=config.toolkit_root,
                output_directory=output_directory,
                timeout=min(config.timeout_seconds, 180),
                environment=environment,
                event_logger=event_logger,
            )
        )
    if junit.is_file():
        junit_data = parse_junit(junit)
        no_skips = junit_data["skipped"] == 0
        results.append(_result("pytest:no-skipped-tests", "pytest", no_skips, "pytest reported zero skipped tests" if no_skips else "pytest reported skipped tests", details=junit_data))
    if coverage_json.is_file():
        audit = audit_public_symbol_execution(config.toolkit_root, coverage_json)
        payload = json.dumps(audit, indent=2, sort_keys=True) + "\n"
        (output_directory / "all-function-coverage.json").write_text(payload, encoding="utf-8")
        results.append(_result("coverage:all-function-bodies", "coverage", bool(audit["passed"]), "every discovered function/method body executed" if audit["passed"] else "one or more function/method bodies were not executed", details={"missing_function_symbols": audit["missing_function_symbols"], "count": audit["function_symbol_count"]}))
        line_ok = audit["line_percent"] >= config.line_coverage_floor
        results.append(_result("coverage:line-floor", "coverage", line_ok, f"line coverage {audit['line_percent']:.2f}% meets floor {config.line_coverage_floor:.2f}%" if line_ok else f"line coverage {audit['line_percent']:.2f}% is below floor {config.line_coverage_floor:.2f}%", details={"line_percent": audit["line_percent"], "floor": config.line_coverage_floor}))
        branch_percent = 100.0 if audit["branch_count"] == 0 else 100.0 * audit["covered_branch_count"] / audit["branch_count"]
        branch_ok = branch_percent >= config.branch_coverage_floor
        results.append(_result("coverage:branch-floor", "coverage", branch_ok, f"branch coverage {branch_percent:.2f}% meets floor {config.branch_coverage_floor:.2f}%" if branch_ok else f"branch coverage {branch_percent:.2f}% is below floor {config.branch_coverage_floor:.2f}%", details={"branch_percent": branch_percent, "floor": config.branch_coverage_floor}))
    return results


def run_packaging_tests(
    config: TestConfig,
    output_directory: Path,
    event_logger: JsonlEventLogger,
    adapter_results: list[ProbeResult],
) -> list[TestResult]:
    """Build the distribution and smoke-test the wheel in a clean virtualenv.

    Blocked unless the ``build`` adapter is installed. Verifies that exactly one wheel
    and one sdist are produced, then creates a venv, installs the wheel, and runs the
    installed CLI's ``--help``.

    Args:
        config: The test configuration.
        output_directory: Directory to write the distribution and venv into.
        event_logger: Logger receiving per-process events.
        adapter_results: Adapter probe results used to gate the run.

    Returns:
        The list of packaging :class:`TestResult` entries.
    """
    missing = _missing(adapter_results, ("build",))
    if missing:
        return [blocked_result("packaging:build-wheel-and-sdist", "packaging", missing)]
    dist = output_directory / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir(parents=True)
    result = run_process_test(
        test_id="packaging:build-wheel-and-sdist",
        suite="packaging",
        command=[config.python_executable, "-m", "build", "--outdir", str(dist)],
        cwd=config.toolkit_root,
        output_directory=output_directory,
        timeout=config.timeout_seconds,
        event_logger=event_logger,
    )
    results = [result]
    if result.status != Status.PASS:
        return results
    wheels = sorted(dist.glob("*.whl"))
    sdists = sorted(dist.glob("*.tar.gz"))
    artifact_ok = len(wheels) == 1 and len(sdists) == 1
    results.append(_result("packaging:artifact-count", "packaging", artifact_ok, "exactly one wheel and one source distribution were produced" if artifact_ok else "unexpected distribution artifact count", details={"wheels": [str(p) for p in wheels], "sdists": [str(p) for p in sdists]}))
    if not wheels:
        return results
    venv = output_directory / "wheel-smoke-venv"
    if venv.exists():
        shutil.rmtree(venv)
    results.append(
        run_process_test(
            test_id="packaging:create-clean-venv",
            suite="packaging",
            command=[config.python_executable, "-m", "venv", str(venv)],
            cwd=config.toolkit_root,
            output_directory=output_directory,
            timeout=min(config.timeout_seconds, 180),
            event_logger=event_logger,
        )
    )
    python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    results.append(
        run_process_test(
            test_id="packaging:install-wheel",
            suite="packaging",
            command=[str(python), "-m", "pip", "install", "--no-deps", str(wheels[0])],
            cwd=config.toolkit_root,
            output_directory=output_directory,
            timeout=config.timeout_seconds,
            event_logger=event_logger,
        )
    )
    results.append(
        run_process_test(
            test_id="packaging:installed-cli-help",
            suite="packaging",
            command=[str(python), "-m", "x86decomp", "--help"],
            cwd=config.toolkit_root,
            output_directory=output_directory,
            timeout=min(config.timeout_seconds, 60),
            event_logger=event_logger,
        )
    )
    return results
