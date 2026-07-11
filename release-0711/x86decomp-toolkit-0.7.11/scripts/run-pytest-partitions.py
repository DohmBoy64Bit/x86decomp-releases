#!/usr/bin/env python3
"""Run the exact current test inventory in isolated, fully reconciled processes."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Any

ISOLATED_TEST_FILES = {
    "tests/test_linker_metadata_corpus.py",
    "tests/test_production.py",
}


def _environment(root: Path) -> dict[str, str]:
    """Build the isolated environment inherited by each pytest subprocess."""
    environment = os.environ.copy()
    values = [str(root / "src"), str(root / "test-suite/src")]
    if environment.get("PYTHONPATH"):
        values.append(environment["PYTHONPATH"])
    environment["PYTHONPATH"] = os.pathsep.join(values)
    environment["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return environment


def _collect(root: Path, environment: dict[str, str]) -> list[str]:
    """Collect the requested operation."""
    completed = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q", "tests", "test-suite/tests", "test-suite/src/x86decomp_testkit/toolkit_tests"],
        cwd=root,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=300,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError("test collection failed:\n" + completed.stdout[-8000:])
    node_ids = [line.strip() for line in completed.stdout.splitlines() if "::" in line and not line.startswith("<")]
    if not node_ids:
        raise RuntimeError("test collection returned no node identifiers")
    return node_ids


def _partitions(node_ids: list[str]) -> list[tuple[str, list[str]]]:
    """Group collected test node identifiers into the exact isolated execution partitions."""
    grouped: dict[str, list[str]] = defaultdict(list)
    for node_id in node_ids:
        grouped[node_id.split("::", 1)[0]].append(node_id)
    partitions: list[tuple[str, list[str]]] = []
    for file_name in sorted(grouped):
        if file_name in ISOLATED_TEST_FILES:
            partitions.extend((node_id, [node_id]) for node_id in grouped[file_name])
        else:
            partitions.append((file_name, [file_name]))
    return partitions


def _junit_counts(path: Path) -> dict[str, int]:
    """Read test, failure, error, and skip totals from a JUnit XML report."""
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.findall(".//testsuite"))
    return {
        name: sum(int(suite.attrib.get(name, 0)) for suite in suites)
        for name in ("tests", "failures", "errors", "skipped")
    }


def run(root: Path, *, timeout_seconds: int, report_path: Path | None = None) -> dict[str, Any]:
    """Collect, execute, and reconcile every test partition without accepting skips."""
    root = root.resolve()
    environment = _environment(root)
    node_ids = _collect(root, environment)
    partitions = _partitions(node_ids)
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    records: list[dict[str, Any]] = []

    with tempfile.TemporaryDirectory(prefix="x86decomp-current-tests-") as temporary:
        temp_root = Path(temporary)
        for index, (name, targets) in enumerate(partitions, start=1):
            junit = temp_root / f"{index:03d}.xml"
            log_path = temp_root / f"{index:03d}.log"
            command = [sys.executable, "-m", "pytest", "-q", *targets, f"--junitxml={junit}"]
            with log_path.open("w", encoding="utf-8") as log:
                try:
                    completed = subprocess.run(
                        command,
                        cwd=root,
                        env=environment,
                        stdout=log,
                        stderr=subprocess.STDOUT,
                        text=True,
                        timeout=timeout_seconds,
                        check=False,
                    )
                except subprocess.TimeoutExpired as exc:
                    raise RuntimeError(f"test partition timed out: {name}") from exc
            output = log_path.read_text(encoding="utf-8", errors="replace")
            if not junit.is_file():
                raise RuntimeError(f"test partition produced no JUnit report: {name}\n{output[-4000:]}")
            counts = _junit_counts(junit)
            for key in totals:
                totals[key] += counts[key]
            records.append({
                "partition": name,
                "targets": targets,
                "returncode": completed.returncode,
                **counts,
                "output_tail": output[-2000:],
            })
            if completed.returncode != 0 or counts["failures"] or counts["errors"] or counts["skipped"]:
                raise RuntimeError(f"test partition failed or skipped tests: {name}\n{output[-8000:]}")

    expected = len(node_ids)
    if totals["tests"] != expected:
        raise RuntimeError(f"test inventory mismatch: executed {totals['tests']}, collected {expected}")

    report: dict[str, Any] = {
        "schema_version": 1,
        "runner": "x86decomp-current-exact-inventory",
        "collected": expected,
        "partition_count": len(partitions),
        **totals,
        "passed": totals["tests"] - totals["failures"] - totals["errors"] - totals["skipped"],
        "partitions": records,
    }
    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    """Run the command-line entry point and return its process status."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--timeout", type=int, default=600, help="timeout for each isolated partition")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    try:
        report = run(args.root, timeout_seconds=args.timeout, report_path=args.report)
    except (OSError, RuntimeError, subprocess.SubprocessError, ET.ParseError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(
        f"{report['passed']} passed, {report['failures']} failed, "
        f"{report['errors']} errors, {report['skipped']} skipped "
        f"across {report['partition_count']} current partitions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
