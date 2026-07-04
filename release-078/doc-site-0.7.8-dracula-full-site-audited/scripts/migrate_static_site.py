from __future__ import annotations

import json
import os
import re
import shutil
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import yaml
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import markdownify as md


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "mkdocs-site"
DOCS = OUT / "docs"
ORIGINAL_FILES = DOCS / "original-site-files"

TOP_NAV_ORDER = [
    "index.html",
    "getting-started.html",
    "workflows.html",
    "project-examples.html",
    "commands/index.html",
    "features/index.html",
    "tests/index.html",
    "schemas.html",
    "integrations.html",
    "source-coverage.html",
    "verification.html",
    "changelog.html",
    "about.html",
    "search.html",
]

GROUPS = {
    "project-examples": "Project Examples",
    "commands": "Commands",
    "features": "Features & Functions",
    "tests": "Tests",
}

SKIP_DIRS = {"mkdocs-site", "__pycache__", ".git"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def html_pages() -> list[Path]:
    pages = []
    for path in ROOT.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        pages.append(path)
    return sorted(pages, key=lambda p: rel(p))


def md_path_for_html(path: Path) -> Path:
    relative = path.relative_to(ROOT).with_suffix(".md")
    return DOCS / relative


def docs_ref_for_html(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix(".md").as_posix()


def page_title(path: Path, soup: BeautifulSoup) -> str:
    h1 = soup.select_one("main h1")
    if h1:
        text = h1.get_text(" ", strip=True)
        if text:
            return text
    if soup.title and soup.title.string:
        return soup.title.string.replace(" · x86decomp 0.7.4 Docs", "").strip()
    return path.stem.replace("-", " ").title()


def rewrite_href(current: Path, href: str | None) -> str | None:
    if not href:
        return href
    if href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
        return href
    split = urlsplit(href)
    if split.scheme or split.netloc:
        return href
    target = split.path
    if not target:
        return href
    if target.endswith(".html"):
        resolved = (current.parent / target).resolve()
        try:
            relative_to_root = resolved.relative_to(ROOT).with_suffix(".md")
        except ValueError:
            return href
        target_md = DOCS / relative_to_root
        current_md_dir = md_path_for_html(current).parent
        new_path = os.path.relpath(target_md, current_md_dir).replace("\\", "/")
        return urlunsplit(("", "", new_path, split.query, split.fragment))
    resolved_file = (current.parent / target).resolve()
    if resolved_file.exists() and resolved_file.is_file():
        try:
            original_relative = resolved_file.relative_to(ROOT)
        except ValueError:
            return href
        copied_target = ORIGINAL_FILES / original_relative
        current_md_dir = md_path_for_html(current).parent
        new_path = os.path.relpath(copied_target, current_md_dir).replace("\\", "/")
        return urlunsplit(("", "", new_path, split.query, split.fragment))
    return href


def replace_with_text(tag: Tag, text: str) -> None:
    tag.clear()
    tag.append(NavigableString(text))


def normalize_main(current: Path, soup: BeautifulSoup) -> tuple[BeautifulSoup, list[str]]:
    changes: list[str] = []
    main = soup.select_one("main#main")
    if main is None:
        main = soup.new_tag("main")
        body = soup.body or soup
        for child in list(body.children):
            main.append(child.extract())
        changes.append("No <main id=\"main\"> wrapper found; converted full body.")

    for selector, note in [
        (".breadcrumbs", "Removed generated breadcrumb chrome; MkDocs provides navigation context."),
        (".page-footer", "Removed generated page footer; MkDocs owns page footer rendering."),
        (".search-dialog", "Removed custom static search dialog; MkDocs search plugin is enabled."),
    ]:
        for tag in main.select(selector):
            tag.decompose()
            if note not in changes:
                changes.append(note)

    for tag in main.select(".eyebrow"):
        text = tag.get_text(" ", strip=True)
        if text:
            tag.name = "p"
            tag["class"] = "doc-section-label"
            replace_with_text(tag, f"Section: {text}")

    for tag in main.select(".meta-row"):
        labels = [item.get_text(" ", strip=True) for item in tag.select(".tag")]
        labels = [item for item in labels if item]
        if labels:
            tag.name = "p"
            tag["class"] = "doc-meta"
            replace_with_text(tag, "Metadata: " + " · ".join(labels))

    for tag in main.select(".stats"):
        rows = []
        for stat in tag.select(".stat"):
            value = stat.select_one("strong")
            label = stat.select_one("span")
            rows.append((value.get_text(" ", strip=True) if value else "", label.get_text(" ", strip=True) if label else ""))
        if rows:
            table = soup.new_tag("table")
            thead = soup.new_tag("thead")
            head_row = soup.new_tag("tr")
            for heading in ["Value", "Meaning"]:
                th = soup.new_tag("th")
                th.string = heading
                head_row.append(th)
            thead.append(head_row)
            tbody = soup.new_tag("tbody")
            for value, label in rows:
                tr = soup.new_tag("tr")
                td_value = soup.new_tag("td")
                td_value.string = value
                td_label = soup.new_tag("td")
                td_label.string = label
                tr.append(td_value)
                tr.append(td_label)
                tbody.append(tr)
            table.append(thead)
            table.append(tbody)
            tag.replace_with(table)

    for tag in main.select(".callout"):
        tag.name = "blockquote"
        tag.attrs = {}

    for tag in main.select(".table-wrap"):
        tag.unwrap()

    for tag in main.find_all(["article", "section", "div"]):
        tag.attrs.pop("class", None)

    for tag in main.find_all(id=True):
        anchor = soup.new_tag("a")
        anchor["id"] = tag["id"]
        tag.insert_before(anchor)

    for link in main.find_all("a", href=True):
        link["href"] = rewrite_href(current, link["href"])

    return main, changes


def markdown_for_page(path: Path) -> tuple[str, str, list[str]]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    title = page_title(path, soup)
    description = ""
    meta = soup.find("meta", attrs={"name": "description"})
    if isinstance(meta, Tag):
        description = str(meta.get("content", "")).strip()
    main, changes = normalize_main(path, soup)
    original_ids = []
    for tag in main.find_all(id=True):
        tag_id = str(tag["id"])
        if tag_id not in original_ids:
            original_ids.append(tag_id)
    body = md(
        str(main),
        heading_style="ATX",
        bullets="-",
        code_language_callback=lambda el: (el.get("class", [""])[0].replace("language-", "") if el.get("class") else ""),
    ).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = body.replace("\\_", "_")
    if original_ids:
        anchor_block = "\n".join(f'<a id="{escape(tag_id, quote=True)}"></a>' for tag_id in original_ids)
        body = anchor_block + "\n\n" + body
    frontmatter = {
        "title": title,
        "description": description,
        "original_path": rel(path),
    }
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False).strip() + "\n---\n\n" + body + "\n", title, changes


def write_pages() -> dict[str, dict[str, object]]:
    manifest: dict[str, dict[str, object]] = {}
    for page in html_pages():
        output = md_path_for_html(page)
        output.parent.mkdir(parents=True, exist_ok=True)
        text, title, changes = markdown_for_page(page)
        output.write_text(text, encoding="utf-8", newline="\n")
        manifest[rel(page)] = {
            "markdown": output.relative_to(OUT).as_posix(),
            "title": title,
            "structural_changes": changes,
        }
    return manifest


def copy_original_files() -> list[str]:
    if ORIGINAL_FILES.exists():
        shutil.rmtree(ORIGINAL_FILES)
    copied: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.suffix.lower() == ".html":
            continue
        target = ORIGINAL_FILES / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied.append(relative.as_posix())
    return sorted(copied)


def nav_entry(path: str, title: str) -> dict[str, str]:
    return {title: Path(path).with_suffix(".md").as_posix()}


def build_nav(manifest: dict[str, dict[str, object]]) -> list[object]:
    nav: list[object] = []
    included: set[str] = set()
    for item in TOP_NAV_ORDER:
        if item in manifest and "/" not in item:
            nav.append(nav_entry(item, str(manifest[item]["title"])))
            included.add(item)
    for group_dir, group_title in GROUPS.items():
        pages = [p for p in manifest if p.startswith(group_dir + "/")]
        if not pages:
            continue
        pages = sorted(pages, key=lambda p: (p != f"{group_dir}/index.html", p))
        group_items = [nav_entry(p, str(manifest[p]["title"])) for p in pages]
        nav.append({group_title: group_items})
        included.update(pages)
    remaining = [p for p in manifest if p not in included]
    for p in sorted(remaining):
        if p not in TOP_NAV_ORDER:
            nav.append(nav_entry(p, str(manifest[p]["title"])))
    nav.append({"Migration Report": "migration-report.md"})
    nav.append({"Original Site Files": "original-site-files.md"})
    return nav


def write_migration_report(manifest: dict[str, dict[str, object]], copied: list[str]) -> None:
    page_count = len(manifest)
    original_search = ROOT / "assets" / "search-index.js"
    search_entries = "unknown"
    if original_search.exists():
        text = original_search.read_text(encoding="utf-8")
        search_entries = str(text.count('"title"'))
    report = f"""---
title: Migration Report
description: Static HTML to MkDocs migration notes for x86decomp 0.7.4.
---

# Migration Report

This MkDocs project was generated from the original static `x86decomp-docs-site-0.7.4` bundle.

## Coverage

- Original HTML pages converted to Markdown: {page_count}
- Original non-HTML files copied under `original-site-files/`: {len(copied)}
- Original search-index entries observed: {search_entries}

## Intentional Structural Changes

- The original custom header, sidebar, theme toggle, page footer, and search overlay were removed from converted pages because MkDocs and the Dracula theme provide site chrome.
- Original local `.html` links were rewritten to `.md` source links so MkDocs can resolve and validate them during build.
- Original card grids, stat strips, metadata tags, and callout blocks were converted into Markdown-friendly lists, tables, paragraphs, or blockquotes.
- The original static search JavaScript was not used as runtime UI. MkDocs' built-in search plugin is enabled instead, while the original JavaScript asset is retained under `original-site-files/assets/`.

## Content Policy

No discretionary end-user documentation content was removed. The changes above are format and platform changes required for MkDocs.
"""
    (DOCS / "migration-report.md").write_text(report, encoding="utf-8", newline="\n")


def write_original_files_page(copied: list[str]) -> None:
    lines = [
        "---",
        "title: Original Site Files",
        "description: Preserved non-HTML files from the original static documentation bundle.",
        "---",
        "",
        "# Original Site Files",
        "",
        "The files below are copied from the original static site bundle for auditability.",
        "",
    ]
    for item in copied:
        link = "original-site-files/" + item.replace(" ", "%20")
        lines.append(f"- [`{item}`]({link})")
    (DOCS / "original-site-files.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_support_files(manifest: dict[str, dict[str, object]], copied: list[str]) -> None:
    legacy_css = DOCS / "assets" / "overrides.css"
    if legacy_css.exists():
        legacy_css.unlink()
    (OUT / "requirements.txt").write_text(
        "mkdocs==1.6.1\nmkdocs-dracula-theme==1.0.9\nmarkdownify==1.2.3\nbeautifulsoup4>=4.13,<5\nPyYAML>=6,<7\n",
        encoding="utf-8",
        newline="\n",
    )
    (DOCS / "assets" / "x86decomp-dracula-overrides.css").write_text(
        """
html,
body {
  max-width: 100%;
  overflow-x: hidden !important;
}

main,
.content,
.container,
.container-fluid {
  max-width: 100%;
}

@media (min-width: 769px) {
  .content {
    width: calc(100vw - 294px) !important;
    max-width: calc(100vw - 294px) !important;
  }

  .content > header,
  .content > section,
  .content > footer,
  .content > footer > div,
  .content .container-fluid {
    max-width: 100% !important;
    width: 100% !important;
  }
}

@media (max-width: 768px) {
  .content {
    width: 100vw !important;
    max-width: 100vw !important;
  }
}

main table {
  display: block;
  overflow-x: auto;
  width: 100%;
  max-width: 100%;
}

main pre {
  max-width: 100%;
  overflow-x: auto;
}

main code,
main td,
main th {
  overflow-wrap: anywhere;
}

main blockquote {
  border-left-color: #bd93f9;
}

.doc-section-label,
.doc-meta {
  color: #8be9fd;
  font-size: 0.92rem;
}
""".strip()
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    config = {
        "site_name": "x86decomp 0.7.4 Docs",
        "site_description": "Source-audited x86decomp-toolkit 0.7.4 documentation",
        "docs_dir": "docs",
        "site_dir": "site",
        "use_directory_urls": True,
        "theme": {
            "name": "dracula",
        },
        "plugins": ["search"],
        "markdown_extensions": [
            "admonition",
            "attr_list",
            "def_list",
            "fenced_code",
            "footnotes",
            "md_in_html",
            "sane_lists",
            "tables",
            {"toc": {"permalink": True}},
        ],
        "extra_css": ["assets/x86decomp-dracula-overrides.css"],
        "nav": build_nav(manifest),
    }
    (OUT / "mkdocs.yml").write_text(yaml.safe_dump(config, sort_keys=False, allow_unicode=True), encoding="utf-8", newline="\n")
    (OUT / "migration-manifest.json").write_text(
        json.dumps({"pages": manifest, "copied_original_files": copied}, indent=2, sort_keys=True),
        encoding="utf-8",
        newline="\n",
    )
    readme = """# x86decomp MkDocs site

This folder contains the MkDocs conversion of the original static x86decomp 0.7.4 documentation site.

## Build

```bash
pip install -r requirements.txt
mkdocs build --strict
```

## Serve locally

```bash
mkdocs serve -a 127.0.0.1:8001
```

## Verify migration coverage

```bash
python scripts/verify_migration.py
```
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8", newline="\n")


def main() -> None:
    for child in DOCS.iterdir() if DOCS.exists() else []:
        if child.name == "assets":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
    manifest = write_pages()
    copied = copy_original_files()
    write_migration_report(manifest, copied)
    write_original_files_page(copied)
    write_support_files(manifest, copied)
    print(f"Converted {len(manifest)} HTML pages.")
    print(f"Copied {len(copied)} non-HTML original files.")
    print(f"Wrote {OUT / 'mkdocs.yml'}.")


if __name__ == "__main__":
    main()
