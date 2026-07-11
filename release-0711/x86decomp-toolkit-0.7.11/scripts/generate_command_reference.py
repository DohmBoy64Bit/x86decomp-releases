#!/usr/bin/env python3
"""Generate the complete deterministic CLI and canonical-route reference."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from x86decomp.canonical import canonical_groups, canonical_routes  # noqa: E402
from x86decomp.cli import _build_parser  # noqa: E402

RELEASE = "0.7.11"
JSON_PATH = ROOT / "docs" / f"COMMAND_REFERENCE_{RELEASE}.json"
MARKDOWN_PATH = ROOT / "docs" / f"COMMAND_REFERENCE_{RELEASE}.md"


def _choice_help(action: argparse._SubParsersAction[Any], name: str) -> str | None:
    """Return the help text registered for one subparser choice."""
    for choice in action._choices_actions:
        if choice.dest == name:
            return choice.help
    return None


def _json_value(value: Any) -> Any:
    """Convert argparse metadata into deterministic JSON-compatible values."""
    if value is argparse.SUPPRESS:
        return "SUPPRESS"
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _json_value(item) for key, item in sorted(value.items(), key=lambda item: str(item[0]))}
    return repr(value)


def _argument_record(action: argparse.Action) -> dict[str, Any]:
    """Serialize one positional argument or option from an argparse parser."""
    choices = None if action.choices is None else [_json_value(item) for item in action.choices]
    action_name = type(action).__name__.removeprefix("_")
    type_name = None
    if action.type is not None:
        type_name = getattr(action.type, "__name__", repr(action.type))
    return {
        "destination": action.dest,
        "flags": list(action.option_strings),
        "kind": "option" if action.option_strings else "positional",
        "action": action_name,
        "required": bool(action.required),
        "nargs": _json_value(action.nargs),
        "default": _json_value(action.default),
        "choices": choices,
        "metavar": _json_value(action.metavar),
        "type": type_name,
        "help": None if action.help is argparse.SUPPRESS else action.help,
    }


def _safety_class(path: tuple[str, ...]) -> str:
    """Classify whether a command name signals possible state or file mutation."""
    mutating_tokens = {
        "accept", "add", "annotate", "assemble", "attach", "backup", "batch", "build",
        "cancel", "claim", "commit", "compile", "compose", "contradict", "create", "delete",
        "export", "extract", "gc", "generate", "import", "init", "install", "invoke", "lock",
        "materialize", "migrate", "patch", "promote", "propose", "put", "recover", "register",
        "repair", "restore", "retry", "run", "save", "set", "shim", "swap", "update", "write",
    }
    tokens = {token for part in path for token in part.replace("_", "-").split("-")}
    if tokens & mutating_tokens:
        return "potentially-mutating"
    read_only_tokens = {
        "audit", "capabilities", "check", "compare", "diff", "doctor", "explain", "inspect",
        "inventory", "list", "mismatches", "plan", "read", "report", "show", "status", "verify",
    }
    if tokens & read_only_tokens:
        return "apparently-read-only-by-name"
    return "review-required"


def _node_record(
    parser: argparse.ArgumentParser,
    path: tuple[str, ...],
    choice_help: str | None,
) -> dict[str, Any]:
    """Build one complete reference record for a parser node."""
    defaults = {key: _json_value(value) for key, value in sorted(parser._defaults.items())}
    owner = defaults.get("_canonical_owner")
    summary = (parser.description or choice_help or "").strip()
    if owner:
        group = str(defaults.get("_canonical_group", path[-2] if len(path) > 1 else ""))
        action = str(defaults.get("_canonical_action", path[-1]))
        summary = f"Execute the `{action}` action in the canonical `{group}` capability group."
    elif not summary:
        summary = f"Execute the `{' '.join(path)}` command."

    arguments = [
        _argument_record(action)
        for action in parser._actions
        if not isinstance(action, argparse._SubParsersAction)
    ]
    child_action = next(
        (action for action in parser._actions if isinstance(action, argparse._SubParsersAction)),
        None,
    )
    command = "x86decomp " + " ".join(path)
    safety_class = _safety_class(path)
    if safety_class == "potentially-mutating":
        safety_note = (
            "Operational execution can modify files, project state, or external-tool outputs. "
            "Review all arguments and use a disposable workspace when evaluating unfamiliar inputs."
        )
    elif safety_class == "apparently-read-only-by-name":
        safety_note = (
            "The command name indicates inspection or verification, but optional report paths or external "
            "tools can still create files; review the exact argument list before execution."
        )
    else:
        safety_note = (
            "Side effects are not provable from parser metadata alone. Review the implementation and run in "
            "a disposable workspace when processing untrusted inputs."
        )

    return {
        "path": list(path),
        "command": command,
        "kind": "canonical-route" if owner else "root-command",
        "is_leaf": child_action is None,
        "summary": summary,
        "description": parser.description,
        "owner": owner,
        "compatibility_alias": defaults.get("_compatibility_alias"),
        "defaults": defaults,
        "arguments": arguments,
        "required_positionals": [
            item["destination"]
            for item in arguments
            if item["kind"] == "positional" and item["required"]
        ],
        "options": [item["flags"] for item in arguments if item["kind"] == "option"],
        "usage": parser.format_usage().strip(),
        "help_text": parser.format_help().rstrip(),
        "success_output": (
            "Operational success is serialized as deterministic indented JSON on standard output by "
            "x86decomp.cli_utils.run_cli."
        ),
        "error_behavior": (
            "Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime "
            "errors exit with status 2 and a JSON object containing `error` and `message` on standard error."
        ),
        "safety_classification": safety_class,
        "safety_note": safety_note,
        "example": command + " --help",
        "example_expected_result": "Print this parser node's usage and argument reference, then exit with status 0.",
        "real_world_use_case": (
            f"Use this command when the task matches its registered purpose: {summary}"
        ),
    }


def parser_records() -> list[dict[str, Any]]:
    """Return one reference record for every root command and nested parser node."""
    root = _build_parser()
    records: list[dict[str, Any]] = []

    def walk(parser: argparse.ArgumentParser, path: tuple[str, ...]) -> None:
        """Traverse child parsers and append one record per registered node."""
        action = next(
            (item for item in parser._actions if isinstance(item, argparse._SubParsersAction)),
            None,
        )
        if action is None:
            return
        for name in sorted(action.choices):
            child = action.choices[name]
            child_path = (*path, name)
            records.append(_node_record(child, child_path, _choice_help(action, name)))
            walk(child, child_path)

    walk(root, ())
    return records


def build_reference() -> dict[str, Any]:
    """Build the complete command-reference payload from live parser metadata."""
    records = parser_records()
    roots = [record["path"][0] for record in records if len(record["path"]) == 1]
    routes = list(canonical_routes())
    return {
        "schema_version": 2,
        "release": RELEASE,
        "root_command_count": len(roots),
        "root_commands": roots,
        "parser_node_count": len(records),
        "parser_nodes": records,
        "canonical_group_count": len(canonical_groups()),
        "canonical_groups": list(canonical_groups()),
        "canonical_route_count": len(routes),
        "canonical_routes": routes,
        "plan_only_routes": sum(1 for route in routes if route.get("owner") == "plan-only"),
        "coverage": {
            "nodes_with_summary": sum(bool(record["summary"]) for record in records),
            "nodes_with_argument_reference": len(records),
            "nodes_with_output_contract": len(records),
            "nodes_with_error_contract": len(records),
            "nodes_with_safety_note": len(records),
            "nodes_with_valid_help_example": len(records),
            "nodes_with_use_case": len(records),
        },
    }


def render_markdown(reference: dict[str, Any]) -> str:
    """Render the complete command reference as deterministic Markdown."""
    lines = [
        f"# Command reference — {reference['release']}",
        "",
        "This document is generated from the live `argparse` tree. It covers every root command and canonical route without executing operational handlers.",
        "",
        f"- Root commands: **{reference['root_command_count']}**",
        f"- Canonical groups: **{reference['canonical_group_count']}**",
        f"- Canonical routes: **{reference['canonical_route_count']}**",
        f"- Total parser nodes: **{reference['parser_node_count']}**",
        "",
        "Every example below uses `--help`; it is concrete, valid, non-destructive, and exits with status 0.",
        "",
    ]
    for record in reference["parser_nodes"]:
        depth = len(record["path"])
        heading = "##" if depth == 1 else "###"
        lines.extend(
            [
                f"{heading} `{record['command']}`",
                "",
                record["summary"],
                "",
                f"- Kind: `{record['kind']}`",
                f"- Owner: `{record['owner'] or 'root CLI'}`",
                f"- Safety classification: `{record['safety_classification']}`",
                f"- Safety note: {record['safety_note']}",
                f"- Success output: {record['success_output']}",
                f"- Error behavior: {record['error_behavior']}",
                f"- Real-world use case: {record['real_world_use_case']}",
                "",
                "Example:",
                "",
                "```console",
                f"$ {record['example']}",
                "```",
                "",
                f"Expected result: {record['example_expected_result']}",
                "",
                "Generated help:",
                "",
                "```text",
                record["help_text"],
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _expected_bytes() -> tuple[bytes, bytes, dict[str, Any]]:
    """Return canonical JSON, Markdown, and structured command-reference values."""
    reference = build_reference()
    json_bytes = (json.dumps(reference, indent=2, sort_keys=True) + "\n").encode("utf-8")
    markdown_bytes = render_markdown(reference).encode("utf-8")
    return json_bytes, markdown_bytes, reference


def main(argv: Iterable[str] | None = None) -> int:
    """Write or verify the generated command-reference artifacts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, default=JSON_PATH)
    parser.add_argument("--markdown", type=Path, default=MARKDOWN_PATH)
    parser.add_argument("--check", action="store_true", help="compare artifacts without writing")
    args = parser.parse_args(list(argv) if argv is not None else None)
    json_bytes, markdown_bytes, reference = _expected_bytes()
    mismatches: list[str] = []
    if args.check:
        for path, expected in ((args.json, json_bytes), (args.markdown, markdown_bytes)):
            if not path.is_file():
                mismatches.append(f"missing reference: {path}")
            elif path.read_bytes() != expected:
                mismatches.append(f"stale reference: {path}")
    else:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_bytes(json_bytes)
        args.markdown.write_bytes(markdown_bytes)
    print(
        json.dumps(
            {
                "valid": not mismatches,
                "mode": "check" if args.check else "write",
                "root_commands": reference["root_command_count"],
                "canonical_routes": reference["canonical_route_count"],
                "parser_nodes": reference["parser_node_count"],
                "mismatches": mismatches,
            },
            sort_keys=True,
        )
    )
    return 0 if not mismatches else 1


if __name__ == "__main__":
    raise SystemExit(main())
