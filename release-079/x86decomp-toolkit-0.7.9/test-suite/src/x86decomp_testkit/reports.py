"""Provide test-suite.x86decomp_testkit.reports functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

from .models import RunSummary, Status


def write_json_report(summary: RunSummary, path: Path) -> None:
    """Write json report.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary.to_dict(), indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def write_adapter_report(adapter_results: list[Any], path: Path) -> None:
    """Write adapter report.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "adapters": [item.to_dict() for item in adapter_results],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _status_icon(status: Status) -> str:
    """Implement status icon.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return {
        Status.PASS: "PASS",
        Status.FAIL: "FAIL",
        Status.BLOCKED: "BLOCKED",
        Status.ERROR: "ERROR",
    }[status]


def write_markdown_report(summary: RunSummary, path: Path) -> None:
    """Write markdown report.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    counts = summary.counts()
    lines = [
        "# x86decomp comprehensive test report",
        "",
        f"- Run ID: `{summary.run_id}`",
        f"- Toolkit: `{summary.toolkit_root}`",
        f"- Started: `{summary.started_at}`",
        f"- Finished: `{summary.finished_at}`",
        f"- Strict mode: `{summary.strict}`",
        f"- Exit code: `{summary.exit_code()}`",
        "",
        "## Result counts",
        "",
        "| PASS | FAIL | BLOCKED | ERROR |",
        "|---:|---:|---:|---:|",
        f"| {counts['pass']} | {counts['fail']} | {counts['blocked']} | {counts['error']} |",
        "",
        "## Adapter inventory",
        "",
        "| Adapter | Installed | Capabilities | Version | Path/source | Diagnostics |",
        "|---|---:|---|---|---|---|",
    ]
    for adapter in summary.adapter_results:
        location = " / ".join(item for item in (adapter.path, adapter.source) if item)
        diagnostics = "<br>".join(adapter.diagnostics)
        capability_text = ", ".join(adapter.capabilities)
        lines.append(
            f"| `{adapter.adapter_id}` | {'yes' if adapter.installed else 'no'} | {capability_text} | "
            f"{adapter.version or ''} | {location} | {diagnostics} |"
        )
    lines.extend(["", "## Capability inventory", "", "| Capability | Satisfied | Providers | Diagnostics |", "|---|---:|---|---|"])
    for capability in summary.capability_results:
        providers = ", ".join(getattr(capability, "providers", ()) or capability.get("providers", ())) if hasattr(capability, "providers") else ", ".join(capability.get("providers", ()))
        diagnostics = "<br>".join(getattr(capability, "diagnostics", ()) or capability.get("diagnostics", ())) if hasattr(capability, "diagnostics") else "<br>".join(capability.get("diagnostics", ()))
        capability_id = getattr(capability, "capability_id", None) or capability.get("capability_id")
        satisfied = getattr(capability, "satisfied", None)
        if satisfied is None:
            satisfied = capability.get("satisfied")
        lines.append(f"| `{capability_id}` | {'yes' if satisfied else 'no'} | {providers} | {diagnostics} |")
    lines.extend(["", "## Tests", "", "| Status | Suite | Test | Duration | Summary | Logs |", "|---|---|---|---:|---|---|"])
    for result in summary.test_results:
        logs = []
        if result.stdout_path:
            logs.append(f"stdout: `{result.stdout_path}`")
        if result.stderr_path:
            logs.append(f"stderr: `{result.stderr_path}`")
        lines.append(
            f"| {_status_icon(result.status)} | `{result.suite}` | `{result.test_id}` | "
            f"{result.duration_seconds:.3f}s | {result.summary.replace('|', '\\|')} | {'<br>'.join(logs)} |"
        )
    blocked = [item for item in summary.test_results if item.status == Status.BLOCKED]
    if blocked:
        lines.extend(["", "## Blocked tests", ""])
        for item in blocked:
            lines.append(f"- `{item.test_id}`: {item.summary}")
    lines.extend(
        [
            "",
            "## Coverage contract",
            "",
            "This suite treats unresolved external dependencies as **BLOCKED**, not skipped. In strict mode, any BLOCKED result produces a non-zero exit code. Public Python functions and methods are audited against coverage data, every CLI command is parse-tested, every schema is checked, and every Ghidra script is syntax-checked. Live integrations run only when their adapters are resolved.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_html_report(summary: RunSummary, path: Path) -> None:
    """Write html report.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    counts = summary.counts()
    rows = []
    for result in summary.test_results:
        rows.append(
            "<tr>"
            f"<td class='{result.status.value}'>{html.escape(result.status.value.upper())}</td>"
            f"<td>{html.escape(result.suite)}</td>"
            f"<td><code>{html.escape(result.test_id)}</code></td>"
            f"<td>{result.duration_seconds:.3f}</td>"
            f"<td>{html.escape(result.summary)}</td>"
            "</tr>"
        )
    adapter_rows = []
    for item in summary.adapter_results:
        adapter_rows.append(
            "<tr>"
            f"<td><code>{html.escape(item.adapter_id)}</code></td>"
            f"<td>{'yes' if item.installed else 'no'}</td>"
            f"<td>{html.escape(item.version or '')}</td>"
            f"<td>{html.escape(item.path or '')}</td>"
            f"<td>{html.escape('; '.join(item.diagnostics))}</td>"
            "</tr>"
        )
    document = f"""<!doctype html>
<html><head><meta charset='utf-8'><title>x86decomp test report</title>
<style>
body{{font:14px system-ui;margin:2rem;max-width:1500px}} table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #bbb;padding:.4rem;vertical-align:top}} th{{background:#eee}}
.pass{{color:#087f23;font-weight:700}} .fail,.error{{color:#b00020;font-weight:700}} .blocked{{color:#a05a00;font-weight:700}}
code{{white-space:nowrap}}
</style></head><body>
<h1>x86decomp comprehensive test report</h1>
<p><b>Run:</b> <code>{html.escape(summary.run_id)}</code><br>
<b>Toolkit:</b> <code>{html.escape(summary.toolkit_root)}</code><br>
<b>Strict:</b> {summary.strict}<br><b>Exit code:</b> {summary.exit_code()}</p>
<h2>Counts</h2><p>PASS {counts['pass']} · FAIL {counts['fail']} · BLOCKED {counts['blocked']} · ERROR {counts['error']}</p>
<h2>Adapters</h2><table><thead><tr><th>Adapter</th><th>Installed</th><th>Version</th><th>Path</th><th>Diagnostics</th></tr></thead><tbody>{''.join(adapter_rows)}</tbody></table>
<h2>Tests</h2><table><thead><tr><th>Status</th><th>Suite</th><th>Test</th><th>Seconds</th><th>Summary</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
</body></html>"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8")
