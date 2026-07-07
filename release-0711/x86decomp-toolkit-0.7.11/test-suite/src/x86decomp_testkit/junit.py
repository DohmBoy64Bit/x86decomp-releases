"""Parse JUnit XML result files into aggregate counts and case name lists."""
from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


def parse_junit(path: Path) -> dict[str, Any]:
    """Parse a JUnit XML report into aggregate counts and per-case name lists.

    Handles both a single ``<testsuite>`` root and a ``<testsuites>`` root containing
    multiple suites, summing the ``tests``, ``failures``, ``errors``, and ``skipped``
    attributes across all suites.

    Args:
        path: Filesystem path to the JUnit XML file to parse.

    Returns:
        A mapping with the summed count keys plus ``"skipped_cases"`` and
        ``"failed_cases"``, each a list of ``"classname::name"`` identifiers.
    """
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.findall("testsuite"))
    counts = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    skipped_cases: list[str] = []
    failed_cases: list[str] = []
    for suite in suites:
        for key in counts:
            counts[key] += int(suite.attrib.get(key, 0))
        for case in suite.findall(".//testcase"):
            name = f"{case.attrib.get('classname', '')}::{case.attrib.get('name', '')}"
            if case.find("skipped") is not None:
                skipped_cases.append(name)
            if case.find("failure") is not None or case.find("error") is not None:
                failed_cases.append(name)
    return {**counts, "skipped_cases": skipped_cases, "failed_cases": failed_cases}
