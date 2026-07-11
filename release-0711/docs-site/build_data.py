"""Extract structured documentation data from x86decomp-toolkit-0.7.11.

Reads every Python source file, every schema, the command reference,
and produces a single comprehensive JSON data file for the docs site.
Computes SHA-256 of every file read as proof of coverage.
"""
import ast
import hashlib
import json
import os
import sys
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parent.parent / "x86decomp-toolkit-0.7.11"
SRC = TOOLKIT / "src" / "x86decomp"
SCHEMAS = TOOLKIT / "schemas"
DOCS = TOOLKIT / "docs"
OUTPUT = Path(__file__).resolve().parent / "js" / "data.js"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_python_module(path):
    """Extract docstring, functions, classes from a .py file via AST."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as e:
        return {"_parse_error": str(e), "functions": [], "classes": [], "docstring": None}

    result = {"docstring": ast.get_docstring(tree), "functions": [], "classes": [], "imports": []}

    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [alias.name for alias in node.names]
            module = getattr(node, 'module', None)
            result["imports"].append({"module": module, "names": names})

        elif isinstance(node, ast.FunctionDef):
            func = {
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "args": [arg.arg for arg in node.args.args if arg.arg != "self" and arg.arg != "cls"],
                "decorators": [ast.unparse(d) if hasattr(ast, 'unparse') else str(d) for d in node.decorator_list],
                "line": node.lineno,
                "is_async": isinstance(node, ast.AsyncFunctionDef),
            }
            if node.returns and hasattr(ast, 'unparse'):
                func["returns"] = ast.unparse(node.returns)
            result["functions"].append(func)

        elif isinstance(node, ast.AsyncFunctionDef):
            func = {
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "args": [arg.arg for arg in node.args.args if arg.arg != "self" and arg.arg != "cls"],
                "decorators": [ast.unparse(d) if hasattr(ast, 'unparse') else str(d) for d in node.decorator_list],
                "line": node.lineno,
                "is_async": True,
            }
            result["functions"].append(func)

        elif isinstance(node, ast.ClassDef):
            cls = {
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "methods": [],
                "bases": [ast.unparse(b) if hasattr(ast, 'unparse') else str(b) for b in node.bases],
                "line": node.lineno,
            }
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method = {
                        "name": child.name,
                        "docstring": ast.get_docstring(child),
                        "args": [arg.arg for arg in child.args.args if arg.arg not in ("self", "cls")],
                        "decorators": [ast.unparse(d) if hasattr(ast, 'unparse') else str(d) for d in child.decorator_list],
                        "line": child.lineno,
                    }
                    cls["methods"].append(method)
            result["classes"].append(cls)

    return result


def extract_schemas():
    """Read all JSON schema files."""
    schemas = {}
    if SCHEMAS.exists():
        for f in sorted(SCHEMAS.rglob("*.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                rel = str(f.relative_to(SCHEMAS)).replace("\\", "/")
                schemas[rel] = {
                    "title": data.get("title", ""),
                    "description": data.get("description", ""),
                    "type": data.get("type", ""),
                    "properties": list(data.get("properties", {}).keys()) if data.get("properties") else [],
                    "required": data.get("required", []),
                    "path": rel,
                }
            except (json.JSONDecodeError, UnicodeDecodeError):
                schemas[str(f.relative_to(SCHEMAS)).replace("\\", "/")] = {"_error": "parse failed"}
    return schemas


def extract_modules():
    """Walk every .py file, extract AST data, compute hash."""
    modules = {}
    file_hashes = {}
    for pyfile in sorted(SRC.rglob("*.py")):
        rel = str(pyfile.relative_to(SRC)).replace("\\", "/")
        file_hashes[rel] = sha256(pyfile)
        mod_data = extract_python_module(pyfile)
        mod_data["_hash"] = file_hashes[rel]
        mod_data["_size"] = pyfile.stat().st_size
        modules[rel] = mod_data
    return modules, file_hashes


def load_command_reference():
    """Load and restructure the command reference JSON."""
    ref_path = DOCS / "COMMAND_REFERENCE_0.7.11.json"
    if not ref_path.exists():
        return None

    raw = json.loads(ref_path.read_text(encoding="utf-8"))
    result = {
        "_meta": {
            "canonical_group_count": raw["canonical_group_count"],
            "canonical_groups": raw["canonical_groups"],
            "canonical_route_count": raw["canonical_route_count"],
            "parser_node_count": raw["parser_node_count"],
        },
    }

    groups = {}
    root_commands = []

    for node in raw["parser_nodes"]:
        if node["kind"] == "root-command":
            root_commands.append(node)
            group_name = node["path"][0] if node["path"] else "root"
            if group_name not in groups:
                groups[group_name] = {"_command": node, "routes": []}
            else:
                groups[group_name]["_command"] = node

        elif node["kind"] == "canonical-route":
            group_name = node["path"][0] if node["path"] else "root"
            if group_name not in groups:
                groups[group_name] = {"_command": None, "routes": []}
            groups[group_name]["routes"].append(node)

    result["groups"] = groups
    result["root_commands"] = root_commands
    return result


def load_extra_docs():
    """Load README, CHANGELOG, and architecture docs."""
    extra = {}
    for name in ["README.md", "CHANGELOG.md"]:
        p = TOOLKIT / name
        if p.exists():
            extra[name] = {"content": p.read_text(encoding="utf-8"), "_hash": sha256(p)}

    arch_map = DOCS / "ARCHITECTURE_MAP.md"
    if arch_map.exists():
        extra["ARCHITECTURE_MAP.md"] = {"content": arch_map.read_text(encoding="utf-8"), "_hash": sha256(arch_map)}

    contracts = DOCS / "contracts.md"
    if contracts.exists():
        extra["contracts.md"] = {"content": contracts.read_text(encoding="utf-8"), "_hash": sha256(contracts)}

    return extra


def extract_examples(file_hashes):
    """Read every example file from the toolkit examples/ directory."""
    EXAMPLES = TOOLKIT / "examples"
    examples = {}
    if not EXAMPLES.exists():
        return examples

    for f in sorted(EXAMPLES.rglob("*")):
        if f.is_dir():
            continue
        rel = str(f.relative_to(EXAMPLES)).replace("\\", "/")
        h = sha256(f)
        file_hashes[f"examples/{rel}"] = h
        ext = f.suffix.lower()
        size = f.stat().st_size
        try:
            if ext == ".json":
                content = json.loads(f.read_text(encoding="utf-8"))
                examples[rel] = {"kind": "json", "content": content, "_hash": h, "_size": size}
            elif ext == ".py" or ext == ".c":
                examples[rel] = {"kind": "code", "language": "python" if ext == ".py" else "c", "content": f.read_text(encoding="utf-8"), "_hash": h, "_size": size}
            elif ext == ".bin":
                examples[rel] = {"kind": "binary", "_hash": h, "_size": size}
            else:
                examples[rel] = {"kind": "text", "content": f.read_text(encoding="utf-8"), "_hash": h, "_size": size}
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            examples[rel] = {"kind": "error", "_error": str(e), "_hash": h, "_size": size}

    return examples


def main():
    print("Extracting modules from Python source...")
    modules, file_hashes = extract_modules()
    print(f"  {len(modules)} Python modules indexed")

    print("Extracting schemas...")
    schemas = extract_schemas()
    print(f"  {len(schemas)} schemas indexed")

    print("Loading command reference...")
    commands = load_command_reference()
    if commands:
        print(f"  {commands['_meta']['parser_node_count']} parser nodes loaded")

    print("Loading extra docs...")
    extra = load_extra_docs()
    print(f"  {len(extra)} docs loaded")

    print("Extracting examples...")
    examples = extract_examples(file_hashes)
    print(f"  {len(examples)} example files indexed")

    if commands:
        ref_path = DOCS / "COMMAND_REFERENCE_0.7.11.json"
        file_hashes["docs/COMMAND_REFERENCE_0.7.11.json"] = sha256(ref_path)

    data = {
        "meta": {
            "version": "0.7.11",
            "generated_from": str(TOOLKIT),
            "python_modules": len(modules),
            "schemas": len(schemas),
            "examples": len(examples),
            "files_hashed": len(file_hashes),
        },
        "modules": modules,
        "commands": commands,
        "schemas": schemas,
        "examples": examples,
        "extra_docs": extra,
        "file_hashes": file_hashes,
    }

    output_js = f"// x86decomp 0.7.11 documentation data — auto-generated\n// {len(modules)} modules, {len(schemas)} schemas, {len(examples)} examples, {len(file_hashes)} files hashed\nvar DOCS_DATA = {json.dumps(data, indent=2, ensure_ascii=False)};\n"

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(output_js, encoding="utf-8")
    print(f"\nDone. Written to {OUTPUT} ({len(output_js):,} bytes)")
    print(f"File hash coverage: {len(file_hashes)} files")


if __name__ == "__main__":
    main()
