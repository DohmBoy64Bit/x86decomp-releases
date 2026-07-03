from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

SITE = Path(__file__).resolve().parents[1]
DOCS = SITE / "docs"
VERSION = "0.7.5"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def frontmatter(title: str, description: str) -> str:
    return "---\n" + yaml.safe_dump(
        {"title": title, "description": description},
        sort_keys=False,
        allow_unicode=True,
    ).strip() + "\n---\n\n"


def anchor(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or "item"


def module_name(base: Path, path: Path, prefix: str) -> str:
    rel = path.relative_to(base).with_suffix("")
    parts = list(rel.parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    return ".".join((prefix, *parts)) if parts else prefix


def expression_text(node: ast.AST | None) -> str:
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return "<source expression unavailable>"


def function_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
    arguments = expression_text(node.args)
    result = f"{prefix} {node.name}({arguments})"
    if node.returns is not None:
        result += f" -> {expression_text(node.returns)}"
    return result


def direct_symbols(path: Path, module: str) -> list[dict[str, Any]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    symbols: list[dict[str, Any]] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            symbols.append(
                {
                    "id": f"{module}:{node.name}",
                    "qualname": node.name,
                    "line": node.lineno,
                    "signature": function_signature(node),
                    "docstring": ast.get_docstring(node),
                    "visibility": "internal" if node.name.startswith("_") else "public",
                }
            )
        elif isinstance(node, ast.ClassDef):
            for member in node.body:
                if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    symbols.append(
                        {
                            "id": f"{module}:{node.name}.{member.name}",
                            "qualname": f"{node.name}.{member.name}",
                            "line": member.lineno,
                            "signature": function_signature(member).replace(
                                f" {member.name}(", f" {node.name}.{member.name}(", 1
                            ),
                            "docstring": ast.get_docstring(member),
                            "visibility": "internal" if member.name.startswith("_") else "public",
                        }
                    )
    return symbols


def discover_modules(toolkit: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    specs = [
        (toolkit / "src/x86decomp", "x86decomp", "Toolkit"),
        (toolkit / "test-suite/src/x86decomp_testkit", "x86decomp_testkit", "Verification harness"),
    ]
    modules: list[dict[str, Any]] = []
    functions: list[dict[str, Any]] = []
    for base, prefix, area in specs:
        for path in sorted(base.rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            module = module_name(base, path, prefix)
            rel = path.relative_to(toolkit).as_posix()
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            symbols = direct_symbols(path, module)
            modules.append(
                {
                    "module": module,
                    "area": area,
                    "path": rel,
                    "sha256": sha256(path),
                    "docstring": ast.get_docstring(tree),
                    "functions": symbols,
                }
            )
            functions.extend({**symbol, "path": rel, "module": module, "area": area} for symbol in symbols)
    return modules, functions


def subparsers(parser: argparse.ArgumentParser) -> argparse._SubParsersAction | None:
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return action
    return None


def action_metadata(action: argparse.Action) -> str:
    parts: list[str] = []
    if not action.option_strings:
        parts.append("required" if getattr(action, "required", True) else "optional")
    elif getattr(action, "required", False):
        parts.append("required")
    if action.default is not argparse.SUPPRESS and action.default is not None:
        parts.append(f"default: `{action.default!r}`")
    if action.choices is not None:
        parts.append("choices: " + ", ".join(f"`{choice}`" for choice in action.choices))
    if getattr(action, "type", None) is not None:
        typ = action.type
        parts.append(f"type: `{getattr(typ, '__name__', str(typ))}`")
    if getattr(action, "nargs", None) not in (None, 1):
        parts.append(f"nargs: `{action.nargs}`")
    return " · ".join(parts) or "declared"


def parser_arguments(parser: argparse.ArgumentParser) -> list[argparse.Action]:
    return [
        action
        for action in parser._actions
        if not isinstance(action, (argparse._HelpAction, argparse._SubParsersAction))
        and action.dest not in {"command", "action"}
    ]


def format_usage(parser: argparse.ArgumentParser) -> str:
    usage = parser.format_usage().strip()
    if usage.lower().startswith("usage:"):
        usage = usage.split(":", 1)[1].strip()
    return usage


def render_parser_section(title: str, parser: argparse.ArgumentParser, source_rows: list[tuple[str, str]]) -> str:
    lines = [f"## `{title}`", ""]
    description = parser.description or parser.format_help().splitlines()[0].strip()
    if description:
        lines.extend([description, ""])
    lines.extend(["### Usage", "", "```text", format_usage(parser), "```", ""])
    actions = parser_arguments(parser)
    if actions:
        lines.extend(["### Arguments", "", "| Argument | Exact parser declaration |", "| --- | --- |"]) 
        for action in actions:
            label = ", ".join(f"`{item}`" for item in action.option_strings) if action.option_strings else f"`{action.dest}`"
            help_text = action.help if action.help not in (None, argparse.SUPPRESS) else f"No help text is declared; parser destination is `{action.dest}`."
            lines.append(f"| {label} | {action_metadata(action)}. {str(help_text).replace('|', '\\|')} |")
        lines.append("")
    else:
        lines.extend(["No route-specific arguments are declared.", ""])
    lines.extend(["### Source basis", "", "| Parser owner | Source file and SHA-256 |", "| --- | --- |"]) 
    for owner, source in source_rows:
        lines.append(f"| `{owner}` | `{source}` · `{sha256(TOOLKIT / source)}` |")
    lines.append("")
    return "\n".join(lines)


def generate_commands(toolkit: Path) -> dict[str, Any]:
    global TOOLKIT
    TOOLKIT = toolkit
    sys.path[:0] = [str(toolkit / "src"), str(toolkit / "test-suite/src")]
    from x86decomp.cli import _build_parser
    from x86decomp.canonical import canonical_groups, canonical_routes
    from x86decomp_testkit.cli import _base_parser

    parser = _build_parser()
    root = subparsers(parser)
    assert root is not None
    groups = set(canonical_groups())
    route_owner = {(item["group"], item["action"]): item["owner"] for item in canonical_routes()}
    owner_source = {
        "governance": "src/x86decomp/governance/cli.py",
        "reconstruction": "src/x86decomp/reconstruction/cli.py",
        "native": "src/x86decomp/native/cli.py",
        "assembly": "src/x86decomp/assembly/cli.py",
    }
    command_dir = DOCS / "commands"
    command_dir.mkdir(parents=True, exist_ok=True)
    for path in command_dir.glob("*.md"):
        if path.name != "index.md":
            path.unlink()
    documented_paths: list[str] = []
    command_records: list[dict[str, Any]] = []
    for name, command_parser in sorted(root.choices.items()):
        nested = subparsers(command_parser)
        page = frontmatter(f"x86decomp {name}", f"Exact parser-derived reference for x86decomp {name} in {VERSION}.")
        page += f"# `x86decomp {name}`\n\n"
        if name in groups and nested is not None:
            routes = sorted(nested.choices.items())
            page += f"Canonical capability group with {len(routes)} routes. Shared group options are shown in every exact usage string.\n\n"
            for action_name, action_parser in routes:
                owner = route_owner[(name, action_name)]
                title = f"x86decomp {name} {action_name}"
                page += render_parser_section(title, action_parser, [(owner, owner_source[owner])])
                documented_paths.append(f"{name} {action_name}")
                command_records.append({"path": f"{name} {action_name}", "owner": owner, "usage": format_usage(action_parser)})
        else:
            source = "src/x86decomp/canonical.py" if name == "commands" else "src/x86decomp/cli.py"
            page += render_parser_section(f"x86decomp {name}", command_parser, [("core", source)])
            documented_paths.append(name)
            command_records.append({"path": name, "owner": "core", "usage": format_usage(command_parser)})
        write(command_dir / f"{name}.md", page)

    suite_parser = _base_parser()
    suite_root = subparsers(suite_parser)
    assert suite_root is not None
    page = frontmatter("x86decomp-test", f"Exact parser-derived reference for the {VERSION} verification executable.")
    page += "# `x86decomp-test`\n\nThe independent verification executable.\n\n"
    for action_name, action_parser in sorted(suite_root.choices.items()):
        page += render_parser_section(
            f"x86decomp-test {action_name}",
            action_parser,
            [("verification harness", "test-suite/src/x86decomp_testkit/cli.py")],
        )
        documented_paths.append(f"x86decomp-test {action_name}")
        command_records.append({"path": f"x86decomp-test {action_name}", "owner": "verification", "usage": format_usage(action_parser)})
    write(command_dir / "x86decomp-test.md", page)

    root_names = sorted(root.choices)
    cards = []
    for name in root_names:
        nested = subparsers(root.choices[name])
        count = len(nested.choices) if nested is not None and name in groups else 1
        cards.append(f"| [`x86decomp {name}`]({name}.md) | {count} |")
    index = frontmatter("Command reference", "Complete parser-derived command reference for both installed executables.")
    index += (
        "# Command reference\n\n"
        f"This reference is regenerated from the live {VERSION} argparse trees. It covers **{len(root_names)} toolkit root commands**, "
        f"**{len(groups)} canonical groups**, **{len(canonical_routes())} canonical routes**, and **{len(suite_root.choices)} test-suite actions**. "
        "Descriptions and argument tables use only parser-declared metadata; missing help text is identified explicitly.\n\n"
        "| Toolkit command | Documented paths |\n| --- | ---: |\n" + "\n".join(cards) +
        "\n| [`x86decomp-test`](x86decomp-test.md) | " + str(len(suite_root.choices)) + " |\n"
    )
    write(command_dir / "index.md", index)
    return {
        "root_commands": root_names,
        "canonical_groups": sorted(groups),
        "canonical_routes": [f"{item['group']} {item['action']}" for item in canonical_routes()],
        "documented_paths": documented_paths,
        "records": command_records,
        "test_suite_actions": sorted(suite_root.choices),
    }


def generate_modules(toolkit: Path) -> dict[str, Any]:
    modules, functions = discover_modules(toolkit)
    feature_dir = DOCS / "features"
    feature_dir.mkdir(parents=True, exist_ok=True)
    for path in feature_dir.glob("*.md"):
        if path.name != "index.md":
            path.unlink()
    for module in modules:
        slug = module["module"].replace("_", "-").replace(".", "-")
        doc = module["docstring"] or f"No module docstring is declared in the {VERSION} source."
        text = frontmatter(module["module"], doc.splitlines()[0])
        text += f"# `{module['module']}`\n\n{doc}\n\n"
        text += f"**Area:** {module['area']}  \n**Source:** `{module['path']}`  \n**SHA-256:** `{module['sha256']}`  \n**Functions/methods:** {len(module['functions'])}\n\n"
        text += "> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.\n\n"
        if module["functions"]:
            text += "## Functions and methods\n\n"
            for symbol in module["functions"]:
                text += f"<a id=\"function-{anchor(symbol['qualname'])}\"></a>\n\n### `{symbol['qualname']}`\n\n"
                text += (symbol["docstring"] or f"No function or method docstring is declared in the {VERSION} source.") + "\n\n"
                text += f"```python\n{symbol['signature']}\n```\n\n"
                text += f"**Catalog symbol:** `{symbol['id']}`  \n**Visibility:** {symbol['visibility']}  \n**Source line:** {symbol['line']}\n\n"
        else:
            text += "No direct module functions or class methods are declared.\n"
        write(feature_dir / f"{slug}.md", text)

    index = frontmatter("Source modules", "Complete AST-derived module inventory for toolkit and verification harness.")
    index += f"# Source modules\n\nThe current release contains **{len(modules)} Python modules**: "
    counts = defaultdict(int)
    for module in modules:
        counts[module["area"]] += 1
    index += ", ".join(f"{count} {area.lower()}" for area, count in sorted(counts.items())) + ".\n\n"
    index += "| Module | Area | Functions/methods | Source SHA-256 |\n| --- | --- | ---: | --- |\n"
    for module in modules:
        slug = module["module"].replace("_", "-").replace(".", "-")
        index += f"| [`{module['module']}`]({slug}.md) | {module['area']} | {len(module['functions'])} | `{module['sha256']}` |\n"
    write(feature_dir / "index.md", index)

    function_index = frontmatter("All functions and methods", "Complete AST-derived function and method inventory.")
    toolkit_count = sum(1 for item in functions if item["area"] == "Toolkit")
    harness_count = len(functions) - toolkit_count
    function_index += f"# All functions and methods\n\nThe complete **{len(functions)}-symbol** inventory: **{toolkit_count} toolkit** and **{harness_count} verification-harness** functions/methods.\n\n"
    function_index += "| Catalog symbol | Source location | Visibility |\n| --- | --- | --- |\n"
    for item in functions:
        slug = item["module"].replace("_", "-").replace(".", "-")
        function_index += f"| [`{item['id']}`](../features/{slug}.md#function-{anchor(item['qualname'])}) | `{item['path']}:{item['line']}` | {item['visibility']} |\n"
    write(DOCS / "functions/index.md", function_index)
    return {"modules": modules, "functions": functions}


def collect_tests(toolkit: Path, python: Path) -> list[dict[str, Any]]:
    env = {**os.environ, "PYTHONPATH": os.pathsep.join([str(toolkit / "src"), str(toolkit / "test-suite/src")])}
    targets = [
        ("Toolkit behavior", toolkit, "tests", ""),
        ("Standalone verification harness", toolkit / "test-suite", "tests", "test-suite/"),
        ("Bundled public contract", toolkit / "test-suite", "src/x86decomp_testkit/toolkit_tests", "test-suite/"),
    ]
    items: list[dict[str, Any]] = []
    for area, cwd, target, source_prefix in targets:
        completed = subprocess.run(
            [str(python), "-m", "pytest", "--collect-only", "-q", target],
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=300,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(f"pytest collection failed for {target}: {completed.stderr}")
        for line in completed.stdout.splitlines():
            if "::" not in line or line.startswith(("=", "<")):
                continue
            nodeid = line.strip()
            collected_source = nodeid.split("::", 1)[0]
            source = source_prefix + collected_source
            path = toolkit / source
            if not path.is_file():
                continue
            function = nodeid.split("::")[-1].split("[")[0]
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            found = next((n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == function), None)
            calls: list[str] = []
            if found is not None:
                for call in [n for n in ast.walk(found) if isinstance(n, ast.Call)]:
                    try:
                        calls.append(ast.unparse(call.func))
                    except Exception:
                        pass
            items.append(
                {
                    "nodeid": nodeid,
                    "area": area,
                    "source": source,
                    "line": found.lineno if found is not None else None,
                    "docstring": ast.get_docstring(found) if found is not None else None,
                    "calls": sorted(dict.fromkeys(calls)),
                    "sha256": sha256(path),
                }
            )
    return items


def generate_tests(toolkit: Path, python: Path) -> dict[str, Any]:
    items = collect_tests(toolkit, python)
    test_dir = DOCS / "tests"
    test_dir.mkdir(parents=True, exist_ok=True)
    for path in test_dir.glob("*.md"):
        if path.name != "index.md":
            path.unlink()
    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        by_source[item["source"]].append(item)
    for source, source_items in sorted(by_source.items()):
        slug = source.replace("/", "-").replace("_", "-").replace(".py", "")
        text = frontmatter(source, f"Source-derived reference for {len(source_items)} collected test nodes.")
        text += f"# `{source}`\n\n**Collected nodes:** {len(source_items)}  \n**Source SHA-256:** `{source_items[0]['sha256']}`\n\n"
        text += "> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.\n\n"
        for item in source_items:
            name = item["nodeid"].split("::")[-1]
            text += f"## `{name}`\n\n"
            text += (item["docstring"] or "No test docstring is declared.") + "\n\n"
            if item["calls"]:
                text += "**Direct call names in source:** " + ", ".join(f"`{call}`" for call in item["calls"]) + "  \n"
            text += f"**Node ID:** `{item['nodeid']}`  \n**Area:** {item['area']}"
            if item["line"] is not None:
                text += f"  \n**Source line:** {item['line']}"
            text += "\n\n"
        write(test_dir / f"{slug}.md", text)
    counts = defaultdict(int)
    for item in items:
        counts[item["area"]] += 1
    index = frontmatter("Test inventory", "Complete collected release-test inventory.")
    index += f"# Test inventory\n\nThe current release collects **{len(items)} distinct test nodes**: " + ", ".join(f"**{count}** {area.lower()}" for area, count in sorted(counts.items())) + ".\n\n"
    index += "| Test source | Area | Collected nodes | SHA-256 |\n| --- | --- | ---: | --- |\n"
    for source, source_items in sorted(by_source.items()):
        slug = source.replace("/", "-").replace("_", "-").replace(".py", "")
        index += f"| [`{source}`]({slug}.md) | {source_items[0]['area']} | {len(source_items)} | `{source_items[0]['sha256']}` |\n"
    write(test_dir / "index.md", index)
    return {"items": items, "counts": dict(counts)}


def generate_schemas(toolkit: Path) -> dict[str, Any]:
    schemas: list[dict[str, Any]] = []
    for path in sorted((toolkit / "schemas").rglob("*.schema.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        schemas.append(
            {
                "path": path.relative_to(toolkit / "schemas").as_posix(),
                "sha256": sha256(path),
                "title": data.get("title"),
                "description": data.get("description"),
                "$schema": data.get("$schema"),
                "$id": data.get("$id"),
                "type": data.get("type"),
                "required": data.get("required", []),
                "properties": sorted(data.get("properties", {})),
            }
        )
    text = frontmatter("JSON Schemas", "Complete source-derived JSON Schema inventory.")
    text += f"# All {len(schemas)} JSON Schemas\n\nEach entry is read from the current schema file. Missing titles or descriptions are identified rather than inferred.\n\n"
    for item in schemas:
        text += f"<a id=\"schema-{anchor(item['path'])}\"></a>\n\n## `{item['path']}`\n\n"
        text += (item["title"] or "No schema title is declared.") + "\n\n"
        if item["description"]:
            text += item["description"] + "\n\n"
        text += f"- **Meta-schema:** `{item['$schema'] or 'not declared'}`\n- **$id:** `{item['$id'] or 'not declared'}`\n- **Top-level type:** `{item['type'] or 'not declared'}`\n"
        text += "- **Required fields:** " + (", ".join(f"`{v}`" for v in item["required"]) if item["required"] else "none declared") + "\n"
        text += "- **Top-level properties:** " + (", ".join(f"`{v}`" for v in item["properties"]) if item["properties"] else "none declared") + "\n\n"
        text += f"SHA-256: `{item['sha256']}`\n\n"
    write(DOCS / "schemas.md", text)
    return {"schemas": schemas}


def generate_integrations(toolkit: Path) -> dict[str, Any]:
    sys.path[:0] = [str(toolkit / "src"), str(toolkit / "test-suite/src")]
    from x86decomp.local_llm import provider_catalog
    from x86decomp_testkit.adapters import adapter_catalog

    adapters = []
    for adapter_id, spec in sorted(adapter_catalog().items()):
        adapters.append(
            {
                "id": adapter_id,
                "display_name": spec.display_name,
                "kind": spec.kind.value,
                "required_for": list(spec.required_for),
                "commands": list(spec.commands),
                "python_modules": list(spec.python_modules),
                "environment_variables": list(spec.environment_variables),
                "optional": spec.optional,
                "pip_requirement": spec.pip_requirement,
                "manual_install_note": spec.manual_install_note,
            }
        )
    providers = provider_catalog()["providers"]
    text = frontmatter("Integrations", "Exact adapter and local-inference provider declarations.")
    text += f"# Integrations\n\nThe verification harness declares **{len(adapters)} adapters**. Unresolved adapters are `BLOCKED`; they are never passed or silently skipped.\n\n"
    text += "## Adapter catalog\n\n| ID | Display name | Kind | Required for | Discovery declarations | Optional |\n| --- | --- | --- | --- | --- | --- |\n"
    for item in adapters:
        discovery = []
        if item["commands"]:
            discovery.append("commands: " + ", ".join(f"`{v}`" for v in item["commands"]))
        if item["python_modules"]:
            discovery.append("modules: " + ", ".join(f"`{v}`" for v in item["python_modules"]))
        if item["environment_variables"]:
            discovery.append("environment: " + ", ".join(f"`{v}`" for v in item["environment_variables"]))
        text += f"| `{item['id']}` | {item['display_name']} | `{item['kind']}` | {', '.join(f'`{v}`' for v in item['required_for'])} | {'; '.join(discovery) or 'none declared'} | {'yes' if item['optional'] else 'no'} |\n"
    text += "\n**Source:** `test-suite/src/x86decomp_testkit/adapters/catalog.py`  \n**SHA-256:** `" + sha256(toolkit / "test-suite/src/x86decomp_testkit/adapters/catalog.py") + "`\n\n"
    text += f"## Local-model provider profiles\n\nThe `llm` capability implements **{len(providers)} provider presets**. Provider support means the declared HTTP contract is implemented; it is not a claim that every served model can produce matching C.\n\n"
    text += "| Provider | Protocol | Default base URL | Models path | Chat path | Structured output |\n| --- | --- | --- | --- | --- | --- |\n"
    for provider in providers:
        text += f"| `{provider['id']}` | `{provider['protocol']}` | `{provider['base_url']}` | `{provider['models_path']}` | `{provider['chat_path']}` | `{provider['structured_output']}` |\n"
    text += "\n**Source:** `src/x86decomp/local_llm/profiles.py`  \n**SHA-256:** `" + sha256(toolkit / "src/x86decomp/local_llm/profiles.py") + "`\n\n"
    text += "Profiles are loopback-only by default. Remote endpoints require explicit opt-in, and secrets are referenced by environment-variable name rather than stored in profile JSON.\n"
    write(DOCS / "integrations.md", text)
    return {"adapters": adapters, "providers": providers}


def parse_manifest(path: Path) -> list[dict[str, str]]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        digest, sep, rel = line.partition("  ")
        if sep:
            entries.append({"path": rel, "sha256": digest})
    return entries


PROJECT_SOURCES = {
    "matching-project.md": ["src/x86decomp/cli.py", "src/x86decomp/compiler.py", "src/x86decomp/exe_diff.py", "src/x86decomp/image_match.py", "src/x86decomp/workflow.py", "tests/test_modes_and_db.py"],
    "functional-project.md": ["src/x86decomp/cli.py", "src/x86decomp/dynamic.py", "src/x86decomp/symbolic.py", "src/x86decomp/integration.py", "src/x86decomp/workflow.py", "tests/test_dynamic_symbolic.py"],
    "hybrid-project.md": ["src/x86decomp/cli.py", "src/x86decomp/hybrid.py", "src/x86decomp/workflow.py", "src/x86decomp/dynamic.py", "src/x86decomp/symbolic.py", "tests/test_pe64_patch_hybrid.py"],
    "static-analysis-evidence.md": ["src/x86decomp/cli.py", "src/x86decomp/pe.py", "src/x86decomp/ghidra.py", "src/x86decomp/disassembly.py", "src/x86decomp/evidence.py", "src/x86decomp/analysis_db.py", "tests/test_ghidra.py"],
    "compiler-laboratory.md": ["src/x86decomp/cli.py", "src/x86decomp/compiler.py", "src/x86decomp/compiler_lab.py", "src/x86decomp/toolchains.py", "tests/test_compiler.py"],
    "patch-image-integration.md": ["src/x86decomp/cli.py", "src/x86decomp/patching.py", "src/x86decomp/pe32.py", "tests/test_pe64_patch_hybrid.py"],
    "full-relink-convergence.md": ["src/x86decomp/cli.py", "src/x86decomp/linker_reconstruction.py", "src/x86decomp/relink.py", "src/x86decomp/image_match.py", "src/x86decomp/convergence.py", "tests/test_relink.py"],
    "abi-type-recovery.md": ["src/x86decomp/cli.py", "src/x86decomp/abi.py", "src/x86decomp/cpp_recovery.py", "src/x86decomp/harness_generator.py", "src/x86decomp/analysis_db.py", "tests/test_abi_disassembly.py"],
    "target-release-reproducibility.md": ["src/x86decomp/cli.py", "src/x86decomp/reproducibility.py", "src/x86decomp/security_audit.py", "src/x86decomp/release_gate.py", "src/x86decomp/project_state.py", "tests/test_production.py"],
    "benchmark-validation-corpus.md": ["src/x86decomp/cli.py", "src/x86decomp/benchmarks.py", "src/x86decomp/ground_truth.py", "src/x86decomp/dynamic.py", "src/x86decomp/symbolic.py", "src/x86decomp/integration.py", "tests/test_linker_metadata_corpus.py"],
    "project-operations-recovery.md": ["src/x86decomp/cli.py", "src/x86decomp/project_state.py", "src/x86decomp/orchestrator.py", "src/x86decomp/content_store.py", "src/x86decomp/security_audit.py", "tests/test_project.py"],
}


def update_project_examples(toolkit: Path) -> dict[str, Any]:
    audit = {"schema_version": 1, "toolkit_version": VERSION, "pages": {}}
    project_dir = DOCS / "project-examples"
    for name, sources in PROJECT_SOURCES.items():
        path = project_dir / name
        text = path.read_text(encoding="utf-8").replace("0.7.4", VERSION).replace("v0.7.4", f"v{VERSION}")
        heading = re.search(r"\n## (?:v?0\.7\.5 )?source basis\n", text, re.IGNORECASE)
        if not heading:
            heading = re.search(r"\n## v0\.7\.5 source basis\n", text, re.IGNORECASE)
        if not heading:
            raise RuntimeError(f"source basis heading missing: {path}")
        start = heading.start()
        related = text.find("\n## Related examples", heading.end())
        end = related if related >= 0 else len(text)
        rows = []
        basis = "\n## v0.7.5 source basis\n\n> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.\n\n| Evidence file | SHA-256 |\n| --- | --- |\n"
        for rel in sources:
            source_path = toolkit / rel
            if not source_path.is_file():
                raise FileNotFoundError(source_path)
            digest = sha256(source_path)
            rows.append({"path": rel, "sha256": digest})
            basis += f"| `{rel}` | `{digest}` |\n"
        basis += "\n"
        text = text[:start] + basis + text[end:]
        write(path, text)
        audit["pages"][name] = {"sources": rows}
    landing = DOCS / "project-examples.md"
    text = landing.read_text(encoding="utf-8").replace("0.7.4", VERSION).replace("v0.7.4", f"v{VERSION}")
    write(landing, text)
    source_audit = frontmatter("Project Examples source audit", "Current source hashes for every Project Example evidence ledger.")
    source_audit += f"# Project Examples source audit\n\nThis ledger is regenerated from the {VERSION} source tree. Each listed digest is a full SHA-256 of the referenced current file.\n\n"
    for name, page in audit["pages"].items():
        source_audit += f"## `{name}`\n\n| Source | SHA-256 |\n| --- | --- |\n"
        for row in page["sources"]:
            source_audit += f"| `{row['path']}` | `{row['sha256']}` |\n"
        source_audit += "\n"
    write(project_dir / "source-audit.md", source_audit)
    write(DOCS / "release-artifacts/PROJECT_EXAMPLES_SOURCE_AUDIT.json", json.dumps(audit, indent=2, sort_keys=True))
    return audit


def extract_commands_from_project_examples() -> list[tuple[str, str]]:
    commands: list[tuple[str, str]] = []
    for path in sorted((DOCS / "project-examples").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for block in re.findall(r"^```[^\n]*\n(.*?)^```\s*$", text, flags=re.DOTALL | re.IGNORECASE | re.MULTILINE):
            logical: list[str] = []
            current = ""
            for raw in block.splitlines():
                line = raw.strip()
                if not line:
                    continue
                if current:
                    current += " " + line
                else:
                    current = line
                if current.endswith(("\\", "`")):
                    current = current[:-1].rstrip()
                    continue
                logical.append(current)
                current = ""
            if current:
                logical.append(current)
            for line in logical:
                if line.startswith("x86decomp ") or line.startswith("x86decomp-test "):
                    commands.append((path.relative_to(DOCS).as_posix(), line))
    return commands


def audit_project_commands(toolkit: Path) -> dict[str, Any]:
    sys.path[:0] = [str(toolkit / "src"), str(toolkit / "test-suite/src")]
    from x86decomp.cli import _build_parser
    from x86decomp_testkit.cli import _base_parser
    toolkit_parser = _build_parser()
    suite_parser = _base_parser()
    failures = []
    checked = []
    for page, line in extract_commands_from_project_examples():
        audit_line = re.sub(r"\$\{?[A-Za-z_][A-Za-z0-9_]*\}?", "1", line)
        audit_line = re.sub(r"%[A-Za-z_][A-Za-z0-9_]*%", "1", audit_line)
        try:
            tokens = shlex.split(audit_line, posix=True)
        except ValueError as exc:
            failures.append({"page": page, "command": line, "error": str(exc)})
            continue
        parser = toolkit_parser if tokens[0] == "x86decomp" else suite_parser
        try:
            parser.parse_args(tokens[1:])
            checked.append({"page": page, "command": line})
        except SystemExit as exc:
            failures.append({"page": page, "command": line, "error": f"argparse exit {exc.code}"})
    return {"checked": checked, "failures": failures, "passed": not failures}


def generate_source_coverage(toolkit: Path, data: dict[str, Any]) -> dict[str, Any]:
    root_entries = parse_manifest(toolkit / "MANIFEST.sha256")
    suite_entries = parse_manifest(toolkit / "test-suite/MANIFEST.sha256")
    report = {
        "schema_version": 1,
        "toolkit_version": VERSION,
        "source_manifest": {"path": "MANIFEST.sha256", "entries": root_entries},
        "test_suite_manifest": {"path": "test-suite/MANIFEST.sha256", "entries": suite_entries},
        "reference_counts": {
            "toolkit_root_commands": len(data["commands"]["root_commands"]),
            "canonical_groups": len(data["commands"]["canonical_groups"]),
            "canonical_routes": len(data["commands"]["canonical_routes"]),
            "python_modules": len(data["modules"]["modules"]),
            "functions_and_methods": len(data["modules"]["functions"]),
            "test_nodes": len(data["tests"]["items"]),
            "schemas": len(data["schemas"]["schemas"]),
            "adapters": len(data["integrations"]["adapters"]),
            "provider_presets": len(data["integrations"]["providers"]),
        },
    }
    write(DOCS / "release-artifacts/FULL_DOCSITE_AUDIT.json", json.dumps(report, indent=2, sort_keys=True))
    text = frontmatter("Source coverage", "Manifest-backed source and documentation-reference coverage.")
    text += f"# Source coverage\n\nThe root source manifest contains **{len(root_entries)} entries** and the independently packaged test-suite manifest contains **{len(suite_entries)} entries**. Every digest below is taken from the current manifest.\n\n"
    text += "## Reference coverage\n\n| Surface | Count |\n| --- | ---: |\n"
    for key, value in report["reference_counts"].items():
        text += f"| {key.replace('_', ' ').title()} | {value} |\n"
    text += "\n## Root source manifest\n\n| Path | SHA-256 |\n| --- | --- |\n"
    for item in root_entries:
        text += f"| `{item['path']}` | `{item['sha256']}` |\n"
    text += "\n## Test-suite source manifest\n\n| Path | SHA-256 |\n| --- | --- |\n"
    for item in suite_entries:
        text += f"| `{item['path']}` | `{item['sha256']}` |\n"
    write(DOCS / "source-coverage.md", text)
    return report


def update_core_pages(toolkit: Path, data: dict[str, Any]) -> None:
    replacements = {
        "0.7.4": VERSION,
        "7.4.0": "7.5.0",
        "33-group": "34-group",
        "173-route": "181-route",
        "33 canonical groups": "34 canonical groups",
        "173 canonical routes": "181 canonical routes",
        "140 root commands": "141 root commands",
        "93 JSON schemas": "97 JSON schemas",
        "93 schemas": "97 schemas",
        "31 adapter": "36 adapter",
        "108 Python modules": "113 toolkit Python modules",
        "843 toolkit functions/methods": "879 toolkit functions/methods",
    }
    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        write(path, text)

    local_source = toolkit / "docs/local-llm.md"
    local_text = frontmatter("Local LLM C generation", "Bounded local-model C proposals with deterministic exact-byte acceptance.") + local_source.read_text(encoding="utf-8")
    write(DOCS / "local-llm.md", local_text)
    arch_source = toolkit / "docs/ARCHITECTURE_MAP.md"
    write(DOCS / "architecture.md", frontmatter("Architecture map", "Current toolkit and verification architecture.") + arch_source.read_text(encoding="utf-8"))
    changelog = frontmatter("Changelog", f"Current {VERSION} release entry.") + toolkit.joinpath("CHANGELOG.md").read_text(encoding="utf-8")
    changelog += f"\n> **Source basis.** `CHANGELOG.md` SHA-256 `{sha256(toolkit / 'CHANGELOG.md')}`.\n"
    write(DOCS / "changelog.md", changelog)

    counts = data["source_coverage"]["reference_counts"] if "source_coverage" in data else {
        "toolkit_root_commands": len(data["commands"]["root_commands"]),
        "canonical_routes": len(data["commands"]["canonical_routes"]),
        "python_modules": len(data["modules"]["modules"]),
        "schemas": len(data["schemas"]["schemas"]),
    }
    home = frontmatter(f"x86decomp {VERSION} Documentation", "Evidence-governed x86/x86-64 decompilation toolkit documentation.")
    home += f"# x86decomp {VERSION} Documentation\n\nUse this Material for MkDocs site to install the toolkit, create projects, run matching and functional workflows, use bounded local-model C generation, and verify release evidence.\n\n"
    home += '<div class="doc-stat-grid">\n'
    for value, label in [
        (len(data["commands"]["root_commands"]), "toolkit root commands"),
        (len(data["commands"]["canonical_routes"]), "canonical routes"),
        (len(data["modules"]["modules"]), "Python modules"),
        (len(data["schemas"]["schemas"]), "JSON Schemas"),
        (len(data["tests"]["items"]), "distinct tests"),
        (len(data["integrations"]["adapters"]), "adapter declarations"),
    ]:
        home += f"<div><strong>{value}</strong><span>{label}</span></div>\n"
    home += "</div>\n\n## Start here\n\n- [Getting started](getting-started.md)\n- [Workflows](workflows.md)\n- [Local LLM C generation](local-llm.md)\n- [Project Examples](project-examples.md)\n- [Complete command reference](commands/index.md)\n- [Release verification](verification.md)\n\n## Scope\n\nThe model is a proposal engine only. Exact byte acceptance comes from deterministic compilation, COFF extraction, complete relocation resolution, and raw byte identity. Analyze and execute only authorized targets in appropriately isolated environments.\n"
    write(DOCS / "index.md", home)

    about = frontmatter("About", f"Source-of-truth policy for the {VERSION} documentation.")
    about += f"# About x86decomp and this site\n\nThis site documents x86decomp-toolkit {VERSION} and is regenerated from the release parser, source AST, schemas, adapters, manifests, tests, and maintained project examples.\n\n## Documentation policy\n\n- Parser metadata comes from the live command trees.\n- Module names, signatures, lines, and docstrings come from the source AST.\n- Test node IDs come from pytest collection.\n- Schema facts come from the JSON files.\n- Adapter and provider facts come from their declaration catalogs.\n- Missing docstrings and help text are stated explicitly rather than replaced with inferred behavior.\n- Unavailable integrations remain `BLOCKED`.\n- No unfinished implementation markers are permitted.\n\n## Authorization and safety\n\nUse the toolkit only on binaries, systems, and environments you are permitted to analyze. Review model-generated source and isolate native execution.\n"
    write(DOCS / "about.md", about)


def configure_material() -> None:
    config = {
        "site_name": f"x86decomp {VERSION} Docs",
        "site_description": f"End-user and source-derived documentation for x86decomp-toolkit {VERSION}",
        "docs_dir": "docs",
        "site_dir": "site",
        "use_directory_urls": True,
        "theme": {
            "name": "material",
            "font": False,
            "features": [
                "navigation.instant",
                "navigation.tabs",
                "navigation.sections",
                "navigation.top",
                "search.highlight",
                "search.suggest",
                "content.code.copy",
                "content.code.annotate",
                "toc.follow",
            ],
            "palette": [
                {"scheme": "default", "primary": "deep purple", "accent": "indigo", "toggle": {"icon": "material/brightness-7", "name": "Switch to dark mode"}},
                {"scheme": "slate", "primary": "deep purple", "accent": "indigo", "toggle": {"icon": "material/brightness-4", "name": "Switch to light mode"}},
            ],
        },
        "plugins": [{"search": {"lang": "en"}}],
        "markdown_extensions": [
            "admonition", "attr_list", "def_list", "footnotes", "md_in_html", "tables",
            {"toc": {"permalink": True}},
            {"pymdownx.highlight": {"anchor_linenums": True}},
            "pymdownx.inlinehilite", "pymdownx.snippets", "pymdownx.superfences", "pymdownx.details", "pymdownx.tabbed",
        ],
        "extra_css": ["assets/x86decomp-material-overrides.css"],
        "validation": {"nav": {"omitted_files": "ignore"}, "links": {"absolute_links": "relative_to_docs"}},
        "nav": [
            {"Home": "index.md"},
            {"Getting Started": "getting-started.md"},
            {"Workflows": [
                {"Workflow Guide": "workflows.md"},
                {"Local LLM C Generation": "local-llm.md"},
                {"Project Examples": "project-examples.md"},
            ]},
            {"Reference": [
                {"Overview": "reference.md"},
                {"Architecture": "architecture.md"},
                {"Commands": "commands/index.md"},
                {"Schemas": "schemas.md"},
                {"Integrations": "integrations.md"},
                {"Source Modules": "features/index.md"},
                {"Function Index": "functions/index.md"},
                {"Tests": "tests/index.md"},
            ]},
            {"Release Evidence": [
                {"Overview": "release-evidence.md"},
                {"Verification": "verification.md"},
                {"Source Coverage": "source-coverage.md"},
                {"Changelog": "changelog.md"},
                {"About": "about.md"},
            ]},
        ],
    }
    write(SITE / "mkdocs.yml", yaml.safe_dump(config, sort_keys=False, allow_unicode=True))
    write(SITE / "requirements.txt", "mkdocs==1.6.1\nmkdocs-material==9.7.6\nbeautifulsoup4>=4.13,<5\nPyYAML>=6,<7\n")
    css = """
:root { --md-text-font: system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif; --md-code-font: \"Cascadia Code\", \"SFMono-Regular\", Consolas, monospace; }
.md-grid { max-width: 92rem; }
.doc-stat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(9rem,1fr)); gap:.8rem; margin:1.2rem 0 2rem; }
.doc-stat-grid > div { border:1px solid var(--md-default-fg-color--lightest); border-radius:.6rem; padding:1rem; background:var(--md-code-bg-color); }
.doc-stat-grid strong { display:block; font-size:1.55rem; }
.doc-stat-grid span { color:var(--md-default-fg-color--light); font-size:.82rem; }
.doc-card-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(18rem,1fr)); gap:1rem; }
a.doc-card { display:flex; flex-direction:column; gap:.4rem; border:1px solid var(--md-default-fg-color--lightest); border-radius:.65rem; padding:1rem; color:inherit; }
a.doc-card:hover { border-color:var(--md-accent-fg-color); text-decoration:none; }
.md-typeset table:not([class]) { display:table; width:100%; }
.md-typeset code { overflow-wrap:anywhere; }
"""
    write(DOCS / "assets/x86decomp-material-overrides.css", css)
    old = DOCS / "assets/x86decomp-dracula-overrides.css"
    if old.exists():
        old.unlink()


def verify_generated(toolkit: Path, data: dict[str, Any], command_audit: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    command_pages = {p.stem for p in (DOCS / "commands").glob("*.md") if p.name != "index.md"}
    expected_command_pages = set(data["commands"]["root_commands"]) | {"x86decomp-test"}
    if command_pages != expected_command_pages:
        errors.append(f"command page drift: missing={sorted(expected_command_pages-command_pages)} extra={sorted(command_pages-expected_command_pages)}")
    feature_pages = {p.stem for p in (DOCS / "features").glob("*.md") if p.name != "index.md"}
    expected_features = {m["module"].replace("_", "-").replace(".", "-") for m in data["modules"]["modules"]}
    if feature_pages != expected_features:
        errors.append(f"feature page drift: missing={len(expected_features-feature_pages)} extra={len(feature_pages-expected_features)}")
    if command_audit["failures"]:
        errors.append(f"project example parser failures: {len(command_audit['failures'])}")
    all_text = "\n".join(path.read_text(encoding="utf-8") for path in DOCS.rglob("*.md"))
    for stale in ("0.7.4", "v0.7.4", "mkdocs-dracula-theme"):
        if stale in all_text or stale in (SITE / "mkdocs.yml").read_text(encoding="utf-8"):
            errors.append(f"stale documentation marker: {stale}")
    unfinished = []
    pattern = re.compile(r"\b(TODO|FIXME|XXX|NOT IMPLEMENTED)\b", re.IGNORECASE)
    for path in DOCS.rglob("*.md"):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                unfinished.append(f"{path.relative_to(SITE)}:{line_no}")
    if unfinished:
        errors.append("unfinished markers: " + ", ".join(unfinished[:20]))
    report = {
        "schema_version": 1,
        "toolkit_version": VERSION,
        "passed": not errors,
        "errors": errors,
        "counts": {
            "toolkit_root_commands": len(data["commands"]["root_commands"]),
            "canonical_groups": len(data["commands"]["canonical_groups"]),
            "canonical_routes": len(data["commands"]["canonical_routes"]),
            "documented_command_paths": len(data["commands"]["documented_paths"]),
            "modules": len(data["modules"]["modules"]),
            "functions_and_methods": len(data["modules"]["functions"]),
            "tests": len(data["tests"]["items"]),
            "schemas": len(data["schemas"]["schemas"]),
            "adapters": len(data["integrations"]["adapters"]),
            "provider_presets": len(data["integrations"]["providers"]),
            "project_example_commands": len(command_audit["checked"]),
        },
        "project_example_command_audit": command_audit,
    }
    write(DOCS / "release-artifacts/DOCSITE_SYNC_AUDIT.json", json.dumps(report, indent=2, sort_keys=True))
    if errors:
        raise RuntimeError("; ".join(errors))
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("toolkit_root", type=Path)
    parser.add_argument("--python", type=Path, default=Path(sys.executable))
    args = parser.parse_args()
    toolkit = args.toolkit_root.resolve()
    configure_material()
    data: dict[str, Any] = {}
    data["commands"] = generate_commands(toolkit)
    data["modules"] = generate_modules(toolkit)
    data["tests"] = generate_tests(toolkit, args.python)
    data["schemas"] = generate_schemas(toolkit)
    data["integrations"] = generate_integrations(toolkit)
    data["project_examples"] = update_project_examples(toolkit)
    update_core_pages(toolkit, data)
    data["source_coverage"] = generate_source_coverage(toolkit, data)
    command_audit = audit_project_commands(toolkit)
    report = verify_generated(toolkit, data, command_audit)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
