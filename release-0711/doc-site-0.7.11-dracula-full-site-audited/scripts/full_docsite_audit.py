from __future__ import annotations
import ast, gzip, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def subparsers(parser):
    import argparse
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return action.choices
    return {}

def load_toolkit(toolkit_root: Path):
    sys.path.insert(0, str(toolkit_root / "src"))
    from x86decomp.cli import _build_parser
    from x86decomp.canonical import canonical_groups, canonical_routes
    return _build_parser, canonical_groups, canonical_routes

def read_manifest(path: Path, prefix: str = ""):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split(None, 1)
        target = path.parent / rel.strip()
        rows.append({"path": prefix + rel.strip(), "sha256": digest, "verified": target.is_file() and sha256_file(target) == digest})
    return rows

def ast_symbols(path: Path):
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except Exception:
        return []
    result = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            result.append({"name": node.name, "kind": "class" if isinstance(node, ast.ClassDef) else "function", "line": node.lineno})
    return result

def module_name(root: Path, path: Path) -> str:
    return ".".join(path.relative_to(root).with_suffix("").parts)

def slug_module(module: str) -> str:
    return module.replace("_", "-").replace(".", "-")

def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        _, _, rest = text.partition("\n---\n")
        return rest
    return text

def slugify(text: str) -> str:
    cleaned = re.sub(r"`([^`]*)`", r"\1", text)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    slug = re.sub(r"[^a-z0-9 _-]", "", cleaned.lower()).strip()
    return re.sub(r"\s+", "-", slug)

def anchors_in_markdown(path: Path) -> set[str]:
    text = strip_frontmatter(path.read_text(encoding="utf-8"))
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
    for _, heading in re.findall(r"^(#{1,6})\s+(.+)$", text, re.MULTILINE):
        slug = slugify(heading)
        if slug:
            anchors.add(slug)
    return anchors

def resolve_link(source: Path, href: str, *, html_href: bool = False) -> Path | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or href.startswith(("mailto:", "tel:", "#")):
        return None
    path = unquote(split.path)
    if not path:
        return None
    base = source.parent
    if html_href and source.name != "index.md":
        base = source.parent / source.stem
    if path.endswith("/"):
        stripped = path.rstrip("/")
        candidate = (base / f"{stripped}.md").resolve()
        if candidate.exists():
            return candidate
        return (base / stripped / "index.md").resolve()
    if not Path(path).suffix:
        candidate = (base / f"{path}.md").resolve()
        if candidate.exists():
            return candidate
        return (base / path / "index.md").resolve()
    return (base / path).resolve()

def public_page_for_markdown(path: Path) -> Path:
    rel = path.relative_to(DOCS)
    if rel.name == "index.md":
        return SITE / rel.parent / "index.html"
    return SITE / rel.with_suffix("") / "index.html"

def search_index_paths() -> set[str]:
    for candidate in [SITE / "search" / "search_index.json", SITE / "search_index.json"]:
        if candidate.exists():
            data = json.loads(candidate.read_text(encoding="utf-8"))
            docs = data.get("docs", data if isinstance(data, list) else [])
            return {str((item.get("location") or item.get("url") or "")).split("#", 1)[0].strip("/") for item in docs}
    return set()

def audit(toolkit_root: Path) -> dict:
    errors: list[str] = []
    _build_parser, canonical_groups, canonical_routes = load_toolkit(toolkit_root)
    parser = _build_parser()
    root_commands = sorted(subparsers(parser))
    groups = sorted(canonical_groups())
    routes = list(canonical_routes())
    command_pages = sorted(p.stem for p in (DOCS / "commands").glob("*.md"))
    for command in root_commands:
        if command not in command_pages:
            errors.append(f"missing command page: {command}")
    for group in groups:
        page = DOCS / "commands" / f"{group}.md"
        if not page.exists():
            errors.append(f"missing canonical command group page: {group}")
            continue
        text = page.read_text(encoding="utf-8")
        for route in [r for r in routes if r["group"] == group]:
            if route["action"] not in text:
                errors.append(f"missing canonical route action mention: {group} {route['action']}")
    schema_doc = (DOCS / "schemas.md").read_text(encoding="utf-8")
    schemas = sorted((toolkit_root / "schemas").rglob("*.json"))
    for schema in schemas:
        rel = schema.relative_to(toolkit_root).as_posix()
        if rel not in schema_doc or sha256_file(schema) not in schema_doc:
            errors.append(f"schema not fully documented: {rel}")
    root_manifest_entries = read_manifest(toolkit_root / "MANIFEST.sha256")
    test_suite_manifest_entries = read_manifest(toolkit_root / "test-suite" / "MANIFEST.sha256", "test-suite/")
    combined_manifest = {}
    for item in root_manifest_entries + test_suite_manifest_entries:
        combined_manifest[item["path"]] = item
    manifest_entries = [combined_manifest[key] for key in sorted(combined_manifest)]
    source_doc = (DOCS / "source-coverage.md").read_text(encoding="utf-8")
    for row in manifest_entries:
        if row["path"] not in source_doc or row["sha256"] not in source_doc:
            errors.append(f"source manifest entry missing from docs: {row['path']}")
        if not row["verified"]:
            errors.append(f"source manifest hash mismatch: {row['path']}")
    py_roots = [(toolkit_root / "src", "toolkit"), (toolkit_root / "test-suite" / "src", "test-suite")]
    modules = []
    symbol_count = 0
    for root, area in py_roots:
        for path in sorted(root.rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            mod = module_name(root, path)
            symbols = ast_symbols(path)
            symbol_count += len(symbols)
            modules.append({"module": mod, "path": path.relative_to(toolkit_root).as_posix(), "symbols": len(symbols)})
            page = DOCS / "features" / f"{slug_module(mod)}.md"
            if not page.exists():
                errors.append(f"missing module page: {mod}")
            else:
                text = page.read_text(encoding="utf-8")
                if mod not in text or path.relative_to(toolkit_root).as_posix() not in text or sha256_file(path) not in text:
                    errors.append(f"module page not source-current: {mod}")
    test_sources = []
    for base in [toolkit_root / "tests", toolkit_root / "test-suite" / "tests", toolkit_root / "test-suite" / "src" / "x86decomp_testkit" / "self_tests", toolkit_root / "test-suite" / "src" / "x86decomp_testkit" / "toolkit_tests"]:
        if base.exists():
            test_sources.extend(sorted(base.rglob("test*.py")))
    test_sources = sorted(set(test_sources))
    test_index = (DOCS / "tests" / "index.md").read_text(encoding="utf-8")
    for path in test_sources:
        rel = path.relative_to(toolkit_root).as_posix()
        if rel not in test_index or sha256_file(path) not in test_index:
            errors.append(f"test source missing from docs: {rel}")
    stale = []
    for path in [ROOT / "mkdocs.yml", ROOT / "README.md"] + sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"(?<![0-9A-Fa-f])0\.7\.[0-8](?![0-9A-Fa-f])", text):
            stale.append(f"{path.relative_to(ROOT).as_posix()}:{text.count(chr(10), 0, m.start()) + 1}:{m.group(0)}")
    errors.extend(f"stale version reference: {item}" for item in stale)
    md_files = sorted(DOCS.rglob("*.md"))
    for source in md_files:
        text = source.read_text(encoding="utf-8")
        for href in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = resolve_link(source, href, html_href=False)
            if target is None:
                continue
            split = urlsplit(href)
            if not target.exists():
                errors.append(f"broken local link in {source.relative_to(DOCS).as_posix()}: {href}")
            elif split.fragment and target.suffix == ".md" and split.fragment not in anchors_in_markdown(target):
                errors.append(f"broken local fragment in {source.relative_to(DOCS).as_posix()}: {href}")
        for href in re.findall(r'href="([^"]+)"', text):
            target = resolve_link(source, href, html_href=True)
            if target is None:
                continue
            split = urlsplit(href)
            if not target.exists():
                errors.append(f"broken local link in {source.relative_to(DOCS).as_posix()}: {href}")
            elif split.fragment and target.suffix == ".md" and split.fragment not in anchors_in_markdown(target):
                errors.append(f"broken local fragment in {source.relative_to(DOCS).as_posix()}: {href}")
    if SITE.exists():
        for page in md_files:
            built = public_page_for_markdown(page)
            if not built.exists():
                errors.append(f"missing built page: {built.relative_to(SITE).as_posix()}")
        paths = search_index_paths()
        if not paths:
            errors.append("missing MkDocs search index")
        for page in md_files:
            built = public_page_for_markdown(page).relative_to(SITE).as_posix()
            public = built[:-len("index.html")].rstrip("/") or "index.html"
            alternates = {public, built, public + "/", public + "/index.html", "" if page.relative_to(DOCS).as_posix()=="index.md" else public}
            if not (paths & alternates):
                errors.append(f"page absent from search index: {page.relative_to(DOCS).as_posix()}")
    if (SITE / "sitemap.xml.gz").exists():
        with gzip.open(SITE / "sitemap.xml.gz", "rt", encoding="utf-8") as handle:
            handle.read(1)
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    if config.get("theme", {}).get("name") != "dracula":
        errors.append("theme.name changed from dracula")
    markdown_hashes_path = ROOT / "DOCSITE_MARKDOWN_HASHES.json"
    markdown_hashes = []
    if markdown_hashes_path.exists():
        try:
            markdown_hashes = json.loads(markdown_hashes_path.read_text(encoding="utf-8")).get("files", [])
        except Exception:
            markdown_hashes = []
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "toolkit_root": str(toolkit_root.resolve()),
        "status": "pass" if not errors else "fail",
        "error_count": len(errors),
        "errors": errors,
        "counts": {
            "markdown_pages": len(md_files),
            "markdown_hash_entries": len(markdown_hashes),
            "root_commands": len(root_commands),
            "canonical_groups": len(groups),
            "canonical_routes": len(routes),
            "schemas": len(schemas),
            "source_manifest_entries": len(manifest_entries),
            "root_manifest_entries": len(root_manifest_entries),
            "test_suite_manifest_entries": len(test_suite_manifest_entries),
            "python_modules": len(modules),
            "python_symbols": symbol_count,
            "test_sources": len(test_sources),
            "built_html_pages": len(list(SITE.rglob("*.html"))) if SITE.exists() else 0,
        },
        "details": {
            "root_commands": root_commands,
            "canonical_groups": groups,
            "canonical_routes": routes,
            "schemas": [{"path": s.relative_to(toolkit_root).as_posix(), "sha256": sha256_file(s)} for s in schemas],
            "source_manifest_entries": manifest_entries,
            "python_modules": modules,
            "test_sources": [{"path": t.relative_to(toolkit_root).as_posix(), "sha256": sha256_file(t)} for t in test_sources],
            "markdown_hashes": markdown_hashes,
        },
    }

def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: full_docsite_audit.py TOOLKIT_ROOT [OUTPUT_JSON]", file=sys.stderr)
        return 2
    report = audit(Path(argv[0]))
    if len(argv) > 1:
        Path(argv[1]).parent.mkdir(parents=True, exist_ok=True)
        Path(argv[1]).write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "pass" else 1

if __name__ == "__main__":
    raise SystemExit(main())
