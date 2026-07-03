from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value for key, value in attrs if value is not None}
        if "id" in values:
            self.ids.add(values["id"])
        if "name" in values:
            self.ids.add(values["name"])
        if tag in {"a", "link"} and "href" in values:
            self.refs.append(("href", values["href"]))
        if tag in {"script", "img", "source"} and "src" in values:
            self.refs.append(("src", values["src"]))


def output_for_markdown(path: Path) -> Path:
    rel = path.relative_to(DOCS)
    if rel.name == "index.md":
        return SITE / rel.parent / "index.html"
    return SITE / rel.with_suffix("") / "index.html"


def resolve_reference(source: Path, value: str) -> tuple[Path | None, str]:
    split = urlsplit(value)
    if split.scheme or split.netloc or value.startswith(("mailto:", "tel:", "data:", "javascript:")):
        return None, ""
    fragment = unquote(split.fragment)
    raw_path = unquote(split.path)
    if not raw_path:
        return source, fragment
    if raw_path.startswith("/"):
        candidate = SITE / raw_path.lstrip("/")
    else:
        candidate = source.parent / raw_path
    candidate = candidate.resolve()
    if raw_path.endswith("/"):
        candidate = candidate / "index.html"
    elif candidate.is_dir():
        candidate = candidate / "index.html"
    elif not candidate.suffix:
        candidate = candidate / "index.html"
    return candidate, fragment


def main() -> int:
    errors: list[str] = []
    markdown = sorted(DOCS.rglob("*.md"))
    expected_outputs = {output_for_markdown(path).resolve() for path in markdown}
    missing_outputs = sorted(path for path in expected_outputs if not path.is_file())
    errors.extend(f"missing built page: {path.relative_to(SITE)}" for path in missing_outputs)

    html_pages = sorted(SITE.rglob("*.html"))
    parsed: dict[Path, PageParser] = {}
    checked_refs = 0
    external_refs = 0
    external_runtime_assets: list[str] = []
    for page in html_pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        parser = PageParser()
        parser.feed(html)
        parsed[page.resolve()] = parser
        for match in re.findall(r'<(?:script|img|source)\b[^>]*\bsrc=["\'](https?://[^"\']+)', html, re.IGNORECASE):
            external_runtime_assets.append(f"{page.relative_to(SITE)} -> {match}")
        for match in re.findall(r'<link\b[^>]*\bhref=["\'](https?://[^"\']+)', html, re.IGNORECASE):
            external_runtime_assets.append(f"{page.relative_to(SITE)} -> {match}")
    for page, parser in parsed.items():
        for kind, value in parser.refs:
            target, fragment = resolve_reference(page, value)
            if target is None:
                external_refs += 1
                continue
            checked_refs += 1
            if not target.exists():
                errors.append(f"broken {kind}: {page.relative_to(SITE)} -> {value}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed.get(target.resolve())
                if target_parser is None:
                    target_parser = PageParser()
                    target_parser.feed(target.read_text(encoding="utf-8", errors="replace"))
                    parsed[target.resolve()] = target_parser
                if fragment not in target_parser.ids:
                    errors.append(f"broken fragment: {page.relative_to(SITE)} -> {value}")

    search_path = SITE / "search/search_index.json"
    if not search_path.is_file():
        errors.append("missing Material search index")
        search_locations: set[str] = set()
    else:
        search = json.loads(search_path.read_text(encoding="utf-8"))
        docs = search.get("docs", []) if isinstance(search, dict) else []
        search_locations = {str(item.get("location", "")).split("#", 1)[0] for item in docs if isinstance(item, dict)}
    missing_search: list[str] = []
    for path in markdown:
        rel = path.relative_to(DOCS)
        if rel.as_posix() == "index.md":
            location = ""
        elif rel.name == "index.md":
            location = rel.parent.as_posix().rstrip("/") + "/"
        else:
            location = rel.with_suffix("").as_posix() + "/"
        if location not in search_locations:
            missing_search.append(rel.as_posix())
    errors.extend(f"page absent from search index: {item}" for item in missing_search)

    stale_patterns = {
        "stale 0.7.4 marker": re.compile(r"(?<![0-9])0\\.7\\.4(?![0-9])"),
        "unfinished TODO marker": re.compile(r"\\bTODO\\b", re.IGNORECASE),
        "unfinished FIXME marker": re.compile(r"\\bFIXME\\b", re.IGNORECASE),
        "placeholder marker": re.compile(r"\\bPLACEHOLDER\\b", re.IGNORECASE),
    }
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        for label, pattern in stale_patterns.items():
            if pattern.search(text):
                errors.append(f"{label}: {path.relative_to(DOCS)}")

    if external_runtime_assets:
        errors.extend(f"external runtime asset: {item}" for item in external_runtime_assets)

    report = {
        "schema_version": 1,
        "passed": not errors,
        "markdown_pages": len(markdown),
        "expected_built_pages": len(expected_outputs),
        "built_html_pages": len(html_pages),
        "built_files": len([path for path in SITE.rglob("*") if path.is_file()]),
        "checked_local_references": checked_refs,
        "external_references": external_refs,
        "external_runtime_assets": external_runtime_assets,
        "search_locations": len(search_locations),
        "missing_search_pages": missing_search,
        "errors": errors,
    }
    (ROOT / "BUILT_SITE_VERIFICATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
