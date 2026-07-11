#!/usr/bin/env python3
"""Generate or verify deterministic docstring coverage and quality reports."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
RELEASE = "0.7.11"
PYTHON_ROOTS = (
    ROOT / "src",
    ROOT / "tests",
    ROOT / "test-suite" / "src",
    ROOT / "test-suite" / "tests",
    ROOT / "scripts",
    ROOT / "ghidra_scripts",
)
IGNORED_PARTS = {"build", "dist", ".pytest_cache", "__pycache__"}
GENERIC_DOCSTRING_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("perform_operation", re.compile(r"^Perform the .+ operation\.$", re.IGNORECASE)),
    ("run_requested", re.compile(r"^Run the requested operation\.$", re.IGNORECASE)),
    (
        "initialize_component",
        re.compile(r"^Initialize the instance with validated constructor state\.$", re.IGNORECASE),
    ),
    (
        "provide_implementation",
        re.compile(r"^Provide the current runtime implementation for .+\.$", re.IGNORECASE),
    ),
    (
        "represent_data_behavior",
        re.compile(r"^Represent .+ data and behavior\.$", re.IGNORECASE),
    ),
    (
        "legacy_template_phrase",
        re.compile(
            r"^(?:.+ for the current toolkit workflow\.|.+ processing for internal toolkit callers\.)$",
            re.IGNORECASE,
        ),
    ),
)


def python_files() -> list[Path]:
    """Return every release-controlled Python source file in audit scope."""
    result: list[Path] = []
    for base in PYTHON_ROOTS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.py")):
            if any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts):
                continue
            result.append(path)
    return result


def sha256(path: Path) -> str:
    """Return the SHA-256 digest for one audited source file."""
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def _source_state_digest(file_hashes: dict[str, str]) -> str:
    """Hash the sorted path-and-digest map that defines the audited source state."""
    payload = "".join(f"{path}\0{digest}\n" for path, digest in sorted(file_hashes.items()))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _generic_pattern(first_line: str) -> str | None:
    """Return the matching low-information docstring pattern name, if any."""
    for name, pattern in GENERIC_DOCSTRING_PATTERNS:
        if pattern.fullmatch(first_line.strip()):
            return name
    return None


def audit() -> dict[str, Any]:
    """Inspect docstring presence and reject documented low-information patterns."""
    totals = {"modules": 0, "classes": 0, "functions": 0}
    present = {"modules": 0, "classes": 0, "functions": 0}
    missing: list[str] = []
    generic: list[dict[str, str]] = []
    repeated: list[str] = []
    files = python_files()

    def inspect_docstring(doc: str, key: str) -> None:
        """Record generic-pattern and repeated-verb findings for one symbol."""
        first_line = doc.splitlines()[0].strip() if doc else ""
        pattern = _generic_pattern(first_line)
        if pattern is not None:
            generic.append({"symbol": key, "pattern": pattern, "first_line": first_line})
        words = re.findall(r"[A-Za-z]+", first_line.lower())
        if len(words) >= 2 and words[0] == words[1]:
            repeated.append(key)

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
        totals["modules"] += 1
        module_doc = ast.get_docstring(tree) or ""
        if module_doc:
            present["modules"] += 1
        else:
            missing.append(f"{relative}:<module>")
        inspect_docstring(module_doc, f"{relative}:<module>")

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                category = "classes"
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                category = "functions"
            else:
                continue
            totals[category] += 1
            doc = ast.get_docstring(node) or ""
            key = f"{relative}:{node.lineno}:{node.name}"
            if doc:
                present[category] += 1
            else:
                missing.append(key)
            inspect_docstring(doc, key)

    file_hashes = {path.relative_to(ROOT).as_posix(): sha256(path) for path in files}
    pattern_counts = {
        name: sum(1 for item in generic if item["pattern"] == name)
        for name, _ in GENERIC_DOCSTRING_PATTERNS
    }
    return {
        "schema_version": 2,
        "release": RELEASE,
        "scope": [path.relative_to(ROOT).as_posix() for path in PYTHON_ROOTS],
        "audited_file_count": len(files),
        "audited_files_sha256": file_hashes,
        "source_state_sha256": _source_state_digest(file_hashes),
        "python_docstring_coverage": {
            "modules_total": totals["modules"],
            "modules_with_docstrings": present["modules"],
            "classes_total": totals["classes"],
            "classes_with_docstrings": present["classes"],
            "functions_total": totals["functions"],
            "functions_with_docstrings": present["functions"],
        },
        "missing_docstrings": missing,
        "quality_checks": {
            "generic_docstring_occurrences": len(generic),
            "generic_docstring_patterns": pattern_counts,
            "generic_docstring_symbols": generic,
            "repeated_leading_verb_occurrences": len(repeated),
            "repeated_leading_verb_symbols": repeated,
            # Retained for consumers of the previous schema.
            "template_phrase_occurrences": len(generic),
            "template_phrase_symbols": [item["symbol"] for item in generic],
        },
        "passed": not missing and not generic and not repeated,
    }


def render_markdown(report: dict[str, Any]) -> str:
    """Render the deterministic human-readable companion to the JSON audit."""
    coverage = report["python_docstring_coverage"]
    quality = report["quality_checks"]
    status = "PASS" if report["passed"] else "FAIL"
    patterns = quality["generic_docstring_patterns"]
    pattern_lines = "\n".join(f"  - `{name}`: {count}" for name, count in sorted(patterns.items()))
    return f"""# Docstring audit — {report['release']}

Status: **{status}**

Source state SHA-256: `{report['source_state_sha256']}`

- Python files audited: {report['audited_file_count']}
- Modules with docstrings: {coverage['modules_with_docstrings']} / {coverage['modules_total']}
- Classes with docstrings: {coverage['classes_with_docstrings']} / {coverage['classes_total']}
- Functions and methods with docstrings: {coverage['functions_with_docstrings']} / {coverage['functions_total']}
- Missing docstrings: {len(report['missing_docstrings'])}
- Generic low-information docstrings: {quality['generic_docstring_occurrences']}
- Repeated leading-verb stubs: {quality['repeated_leading_verb_occurrences']}

Generic-pattern counts:
{pattern_lines}

The JSON companion records a SHA-256 digest for every audited Python file. Both reports are
deterministic for a given source state; verification mode compares them without rewriting files.
"""


def _expected_bytes(report: dict[str, Any]) -> tuple[bytes, bytes]:
    """Return the canonical JSON and Markdown report bytes for an audit result."""
    json_bytes = (json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8")
    markdown_bytes = render_markdown(report).encode("utf-8")
    return json_bytes, markdown_bytes


def _check_file(path: Path, expected: bytes) -> str | None:
    """Return a deterministic mismatch message when a persisted report is stale."""
    if not path.is_file():
        return f"missing report: {path}"
    if path.read_bytes() != expected:
        return f"stale report: {path}"
    return None


def main(argv: Iterable[str] | None = None) -> int:
    """Generate reports or verify them without modifying the source tree."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, default=ROOT / f"DOCSTRING_AUDIT_{RELEASE}.json")
    parser.add_argument("--markdown", type=Path, default=ROOT / f"DOCSTRING_AUDIT_{RELEASE}.md")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="compare reports without writing files")
    mode.add_argument("--write", action="store_true", help="write deterministic reports (default)")
    args = parser.parse_args(list(argv) if argv is not None else None)

    report = audit()
    json_bytes, markdown_bytes = _expected_bytes(report)
    mismatches: list[str] = []
    if args.check:
        for path, expected in ((args.json, json_bytes), (args.markdown, markdown_bytes)):
            mismatch = _check_file(path, expected)
            if mismatch is not None:
                mismatches.append(mismatch)
    else:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_bytes(json_bytes)
        args.markdown.write_bytes(markdown_bytes)

    summary = {
        "passed": report["passed"] and not mismatches,
        "mode": "check" if args.check else "write",
        "source_state_sha256": report["source_state_sha256"],
        "audited_file_count": report["audited_file_count"],
        "missing_docstrings": len(report["missing_docstrings"]),
        "generic_docstring_occurrences": report["quality_checks"]["generic_docstring_occurrences"],
        "repeated_leading_verb_occurrences": report["quality_checks"]["repeated_leading_verb_occurrences"],
        "report_mismatches": mismatches,
    }
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
