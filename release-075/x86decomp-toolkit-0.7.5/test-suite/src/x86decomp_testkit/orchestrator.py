from __future__ import annotations

import json
import uuid
from pathlib import Path

from .adapters import adapter_catalog, resolve_missing_adapters
from .config import TestConfig
from .live_adapters import run_live_adapter_tests
from .logging_utils import configure_logging
from .models import RunSummary
from .reports import write_adapter_report, write_html_report, write_json_report, write_markdown_report
from .suites import (
    run_cli_surface_tests,
    run_inventory_tests,
    run_harness_self_tests,
    run_packaging_tests,
    run_pytest_and_coverage,
    run_structural_tests,
)
from .timeutil import utc_now


def package_root() -> Path:
    return Path(__file__).resolve().parent


def suite_root() -> Path:
    # Source checkout: <root>/src/x86decomp_testkit. Installed wheel: package dir.
    candidate = package_root().parents[1]
    return candidate if (candidate / "pyproject.toml").is_file() else package_root()


def feature_catalog_path() -> Path:
    return package_root() / "data" / "feature_catalog.json"


def run_all(config: TestConfig, *, config_path: Path | None = None, verbose: bool = False) -> RunSummary:
    if not config.toolkit_root.is_dir():
        raise FileNotFoundError(f"toolkit root does not exist: {config.toolkit_root}")
    if not (config.toolkit_root / "pyproject.toml").is_file():
        raise FileNotFoundError(f"toolkit root has no pyproject.toml: {config.toolkit_root}")

    run_id = f"run-{utc_now().replace(':', '').replace('-', '').replace('.', '')}-{uuid.uuid4().hex[:8]}"
    output_directory = config.output_root / run_id
    output_directory.mkdir(parents=True, exist_ok=False)
    logger, event_logger = configure_logging(output_directory, verbose=verbose)
    event_logger.emit("run.started", run_id=run_id, configuration=config.to_dict())
    started_at = utc_now()

    catalog = adapter_catalog()
    adapter_results = resolve_missing_adapters(
        catalog,
        config,
        config_path=config_path,
        event_logger=event_logger,
    )
    write_adapter_report(adapter_results, output_directory / "adapters.json")
    tests = []

    logger.info("building toolkit inventory and enforcing the feature catalog")
    inventory, inventory_tests = run_inventory_tests(config, output_directory, feature_catalog_path())
    tests.extend(inventory_tests)

    logger.info("running structural and contract tests")
    tests.extend(run_structural_tests(config, suite_root(), output_directory, event_logger, adapter_results))

    logger.info("parse-testing every discovered CLI command")
    tests.extend(run_cli_surface_tests(config, inventory, output_directory, event_logger))

    logger.info("running the verification harness self-tests")
    tests.extend(run_harness_self_tests(config, suite_root(), output_directory, event_logger, adapter_results))

    logger.info("running toolkit and supplemental pytest suites under branch coverage")
    tests.extend(run_pytest_and_coverage(config, package_root(), output_directory, event_logger, adapter_results))

    logger.info("building and clean-installing toolkit distributions")
    tests.extend(run_packaging_tests(config, output_directory, event_logger, adapter_results))

    logger.info("running installed-adapter tests; unresolved adapters become BLOCKED")
    tests.extend(run_live_adapter_tests(catalog, adapter_results, config, output_directory, event_logger))

    summary = RunSummary(
        run_id=run_id,
        toolkit_root=str(config.toolkit_root),
        output_directory=str(output_directory),
        strict=config.strict,
        started_at=started_at,
        finished_at=utc_now(),
        adapter_results=adapter_results,
        test_results=tests,
        inventory=inventory,
        configuration=config.to_dict(),
    )
    write_json_report(summary, output_directory / "results.json")
    write_markdown_report(summary, output_directory / "REPORT.md")
    write_html_report(summary, output_directory / "report.html")
    event_logger.emit("run.finished", run_id=run_id, counts=summary.counts(), exit_code=summary.exit_code())
    logger.info("run complete: %s", json.dumps(summary.counts(), sort_keys=True))
    return summary
