from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "mkdocs-site"
DOCS = OUT / "docs"
ARCHIVE = OUT / "archive-original-site"


def frontmatter(title: str, description: str) -> str:
    return "---\n" + yaml.safe_dump({"title": title, "description": description}, sort_keys=False).strip() + "\n---\n\n"


def site_href(href: str, current_dir: str = "") -> str:
    split = urlsplit(href)
    path = split.path
    fragment = f"#{split.fragment}" if split.fragment else ""
    if not path:
        return fragment or href
    if path.endswith("index.html"):
        path = path[: -len("index.html")]
    elif path.endswith(".html"):
        path = path[: -len(".html")] + "/"
    if current_dir and path.startswith(current_dir + "/"):
        path = path[len(current_dir) + 1 :]
    return path + fragment


def original_soup(relative_html: str) -> BeautifulSoup:
    return BeautifulSoup((ROOT / relative_html).read_text(encoding="utf-8"), "html.parser")


def cards_from_html(relative_html: str, current_dir: str = "") -> list[dict[str, str]]:
    soup = original_soup(relative_html)
    cards = []
    for card in soup.select("a.card"):
        title = card.select_one(".card-title")
        title_text = title.get_text(" ", strip=True) if title else card.get_text(" ", strip=True)
        paragraphs = [p.get_text(" ", strip=True) for p in card.select("p")]
        tags = [tag.get_text(" ", strip=True) for tag in card.select(".tag")]
        cards.append(
            {
                "title": title_text,
                "description": paragraphs[0] if paragraphs else "",
                "tag": " · ".join(tags),
                "href": site_href(card.get("href", "#"), current_dir),
            }
        )
    return cards


def card_grid(cards: list[dict[str, str]]) -> str:
    lines = ['<div class="doc-card-grid">']
    for card in cards:
        tag = f'<small>{card["tag"]}</small>' if card["tag"] else ""
        desc = f'<span>{card["description"]}</span>' if card["description"] else ""
        lines.extend(
            [
                f'<a class="doc-card" href="{card["href"]}">',
                f"<strong>{card['title']}</strong>",
                desc,
                tag,
                "</a>",
            ]
        )
    lines.append("</div>")
    return "\n".join(line for line in lines if line)


def cards_by_heading(relative_html: str, current_dir: str = "") -> dict[str, list[dict[str, str]]]:
    soup = original_soup(relative_html)
    groups: dict[str, list[dict[str, str]]] = {}
    current = "Reference"
    main = soup.select_one("main") or soup
    for node in main.find_all(["h2", "a"], recursive=True):
        if node.name == "h2":
            current = node.get_text(" ", strip=True)
            groups.setdefault(current, [])
        elif node.name == "a" and "card" in node.get("class", []):
            title = node.select_one(".card-title")
            paragraphs = [p.get_text(" ", strip=True) for p in node.select("p")]
            tags = [tag.get_text(" ", strip=True) for tag in node.select(".tag")]
            groups.setdefault(current, []).append(
                {
                    "title": title.get_text(" ", strip=True) if title else node.get_text(" ", strip=True),
                    "description": paragraphs[0] if paragraphs else "",
                    "tag": " · ".join(tags),
                    "href": site_href(node.get("href", "#"), current_dir),
                }
            )
    return {k: v for k, v in groups.items() if v}


def write_home() -> None:
    cards = [
        {"title": "Install and verify", "description": "Set up the 0.7.4 toolkit, initialize a project, and run the verifier.", "tag": "Start here", "href": "getting-started/"},
        {"title": "Choose a workflow", "description": "Follow task-oriented paths for analysis, reconstruction, evidence, assembly, and release checks.", "tag": "Guides", "href": "workflows/"},
        {"title": "Use project examples", "description": "Walk through matching, functional, hybrid, and support workflows with bounded claims.", "tag": "Examples", "href": "project-examples/"},
        {"title": "Find a command", "description": "Browse exact command syntax, arguments, examples, and source basis.", "tag": "Reference", "href": "commands/"},
        {"title": "Check schemas", "description": "Inspect every JSON schema contract shipped with the release.", "tag": "Reference", "href": "schemas/"},
        {"title": "Review release evidence", "description": "See the sealed verification result, source coverage, and current release boundary.", "tag": "Evidence", "href": "verification/"},
    ]
    body = frontmatter("x86decomp 0.7.4 Documentation", "End-user documentation for installing, running, and verifying x86decomp-toolkit 0.7.4.")
    body += """# x86decomp 0.7.4 Documentation

Use this site to install the toolkit, create projects, run workflows, and verify release evidence. The reference pages remain source-derived, but the main path through the docs is organized around what an end user is trying to do.

<div class="doc-hero-metrics">
<div><strong>145</strong><span>command choices</span></div>
<div><strong>285</strong><span>runnable paths</span></div>
<div><strong>137</strong><span>Python modules</span></div>
<div><strong>93</strong><span>JSON schemas</span></div>
</div>

## Start Here

"""
    body += card_grid(cards)
    body += """

## Scope

x86decomp-toolkit is an evidence-governed x86 and x86-64 decompilation toolkit. The release exposes the `x86decomp` toolkit executable and the `x86decomp-test` verification executable.

> Analyze only binaries and systems you are authorized to inspect. Native execution and integration scenarios require appropriate isolation and explicit consent.
"""
    (DOCS / "index.md").write_text(body, encoding="utf-8", newline="\n")


def write_reference() -> None:
    cards = [
        {"title": "Commands", "description": "Exact parser-derived syntax, arguments, examples, and command provenance.", "tag": "285 runnable paths", "href": "../commands/"},
        {"title": "Schemas", "description": "All JSON schema contracts with required fields, properties, and hashes.", "tag": "93 schemas", "href": "../schemas/"},
        {"title": "Integrations", "description": "External adapters, optional tools, and their documented boundaries.", "tag": "Adapters", "href": "../integrations/"},
        {"title": "Source modules", "description": "Module and symbol references copied from source names, signatures, and docstrings.", "tag": "137 modules", "href": "../features/"},
        {"title": "Function index", "description": "All generated function and method references in one index.", "tag": "983 symbols", "href": "../functions/"},
        {"title": "Tests", "description": "The current release test inventory and public-surface contract coverage.", "tag": "215 tests", "href": "../tests/"},
    ]
    body = frontmatter("Reference", "Command, schema, module, function, integration, and test references.")
    body += "# Reference\n\nUse these pages when you need exact command syntax, schema fields, source modules, or verification coverage.\n\n"
    body += card_grid(cards)
    (DOCS / "reference.md").write_text(body, encoding="utf-8", newline="\n")


def write_release_evidence() -> None:
    cards = [
        {"title": "Verification", "description": "Authenticated release results and what the evidence does and does not claim.", "tag": "Release gate", "href": "../verification/"},
        {"title": "Source coverage", "description": "Manifest-backed coverage for packaged source files, hashes, schemas, and mappings.", "tag": "411 files", "href": "../source-coverage/"},
        {"title": "Changelog", "description": "Release notes and provenance for x86decomp-toolkit 0.7.4.", "tag": "0.7.4", "href": "../changelog/"},
        {"title": "About", "description": "Documentation scope, current-release boundary, and support notes.", "tag": "Scope", "href": "../about/"},
    ]
    body = frontmatter("Release Evidence", "Verification, source coverage, changelog, and documentation scope.")
    body += "# Release Evidence\n\nThese pages preserve the release evidence that matters to an end user evaluating the 0.7.4 package.\n\n"
    body += card_grid(cards)
    (DOCS / "release-evidence.md").write_text(body, encoding="utf-8", newline="\n")


def write_project_examples() -> None:
    cards = [c for c in cards_from_html("project-examples.html", current_dir="project-examples") if "source-audit" not in c["href"]]
    body = frontmatter("Project Examples", "Source-verified example workflows for official project modes and supporting tasks.")
    body += """# Project Examples

Pick the example closest to your project goal. The examples preserve the original bounded claims: they do not assume a compiler, linker, ABI, function size, tool availability, passing result, or execution safety for your target.

> **Mode model.** The 0.7.4 project schema permits only `matching` and `functional` in `selected_modes`. A target decision of `preferred_mode: both` enables both; “hybrid” describes their build/workflow composition, not a third enum.

## Example Catalog

"""
    body += card_grid(cards)
    body += """

## Command-line Notation

Examples use one command per line so they paste cleanly in PowerShell and POSIX shells. Replace uppercase placeholder values such as digests, pipeline IDs, and stage IDs with values measured or returned by your project.
"""
    (DOCS / "project-examples.md").write_text(body, encoding="utf-8", newline="\n")


def write_grouped_index(relative_html: str, output_md: str, title: str, description: str, intro: str, current_dir: str = "") -> None:
    groups = cards_by_heading(relative_html, current_dir=current_dir)
    body = frontmatter(title, description)
    body += f"# {title}\n\n{intro}\n\n"
    for heading, cards in groups.items():
        clean_heading = re.sub(r"¶$", "", heading).strip()
        body += f"## {clean_heading}\n\n"
        body += card_grid(cards)
        body += "\n\n"
    (DOCS / output_md).write_text(body, encoding="utf-8", newline="\n")


def archive_non_user_pages() -> None:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for item in ["migration-report.md", "original-site-files.md", "search.md"]:
        src = DOCS / item
        if src.exists():
            dst = ARCHIVE / "removed-from-published-site" / item
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
    src_dir = DOCS / "original-site-files"
    if src_dir.exists():
        dst_dir = ARCHIVE / "original-site-files"
        if dst_dir.exists():
            shutil.rmtree(dst_dir)
        shutil.move(str(src_dir), str(dst_dir))


def publish_release_artifacts() -> None:
    artifact_dir = DOCS / "release-artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    source_dir = ARCHIVE / "original-site-files"
    for name in [
        "FULL_DOCSITE_AUDIT.md",
        "FULL_DOCSITE_AUDIT.json",
        "PROJECT_EXAMPLES_SOURCE_AUDIT.json",
    ]:
        src = source_dir / name
        if src.exists():
            shutil.copy2(src, artifact_dir / name)

    replacements = {
        "original-site-files/FULL_DOCSITE_AUDIT.md": "release-artifacts/FULL_DOCSITE_AUDIT.md",
        "original-site-files/FULL_DOCSITE_AUDIT.json": "release-artifacts/FULL_DOCSITE_AUDIT.json",
        "../original-site-files/PROJECT_EXAMPLES_SOURCE_AUDIT.json": "../release-artifacts/PROJECT_EXAMPLES_SOURCE_AUDIT.json",
    }
    for path in [DOCS / "verification.md", DOCS / "project-examples" / "source-audit.md"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8", newline="\n")


def write_mkdocs_config() -> None:
    config = {
        "site_name": "x86decomp 0.7.4 Docs",
        "site_description": "End-user documentation for x86decomp-toolkit 0.7.4",
        "docs_dir": "docs",
        "site_dir": "site",
        "use_directory_urls": True,
        "theme": {"name": "dracula"},
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
            {"toc": {"permalink": False}},
        ],
        "extra_css": ["assets/x86decomp-dracula-overrides.css"],
        "validation": {"nav": {"omitted_files": "ignore"}},
        "nav": [
            {"Home": "index.md"},
            {"Getting Started": "getting-started.md"},
            {"Workflows": "workflows.md"},
            {"Project Examples": "project-examples.md"},
            {
                "Reference": [
                    {"Overview": "reference.md"},
                    {"Commands": "commands/index.md"},
                    {"Schemas": "schemas.md"},
                    {"Integrations": "integrations.md"},
                    {"Source Modules": "features/index.md"},
                    {"Function Index": "functions/index.md"},
                    {"Tests": "tests/index.md"},
                ]
            },
            {
                "Release Evidence": [
                    {"Overview": "release-evidence.md"},
                    {"Verification": "verification.md"},
                    {"Source Coverage": "source-coverage.md"},
                    {"Changelog": "changelog.md"},
                    {"About": "about.md"},
                ]
            },
        ],
    }
    (OUT / "mkdocs.yml").write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8", newline="\n")


def write_css() -> None:
    css = """
html,
body {
  max-width: 100%;
  overflow-x: hidden !important;
  font-size: 16px;
}

main,
.content,
.container,
.container-fluid {
  max-width: 100%;
}

.section-content {
  padding-top: 2rem !important;
}

.section-content article {
  max-width: 74rem;
}

.section-content h1,
.section-content h2,
.section-content h3,
.section-content h4 {
  letter-spacing: 0;
  overflow-wrap: anywhere;
}

.section-content h1 {
  font-size: 2rem !important;
  line-height: 1.18 !important;
  margin-bottom: 1rem;
}

.section-content h2 {
  font-size: 1.45rem !important;
  line-height: 1.25 !important;
  margin-top: 2rem;
  margin-bottom: 0.85rem;
}

.section-content h3 {
  font-size: 1.18rem !important;
  line-height: 1.3 !important;
  margin-top: 1.45rem;
  margin-bottom: 0.65rem;
}

.section-content h4 {
  font-size: 1rem !important;
  line-height: 1.35 !important;
  margin-top: 1.2rem;
}

.section-content p,
.section-content li,
.section-content td,
.section-content th {
  font-size: 1rem;
  line-height: 1.58;
}

.section-content p {
  max-width: 68rem;
}

.section-content ul,
.section-content ol {
  padding-left: 1.35rem;
}

.section-content li {
  margin: 0.28rem 0;
}

.section-content li::marker {
  color: #8be9fd;
  font-size: 1rem;
  font-weight: 700;
}

.section-content a.headerlink {
  display: none !important;
}

.section-content h1 code,
.section-content h2 code,
.section-content h3 code {
  font-size: 0.92em;
  line-height: inherit;
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
  border-collapse: collapse;
  border: 1px solid rgba(248, 248, 242, 0.14);
  border-radius: 8px;
  background: rgba(40, 42, 54, 0.28);
}

main pre {
  position: relative;
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
  margin: 1rem 0 1.35rem;
  padding: 1.1rem 1.2rem;
  border: 1px solid rgba(139, 233, 253, 0.18);
  border-radius: 8px;
  background:
    linear-gradient(180deg, rgba(54, 57, 73, 0.96), rgba(39, 41, 54, 0.96)) !important;
  box-shadow: 0 14px 30px rgba(15, 16, 24, 0.22);
  scrollbar-width: thin;
  scrollbar-color: rgba(139, 233, 253, 0.45) rgba(40, 42, 54, 0.2);
}

main pre::before {
  content: "";
  position: absolute;
  inset: 0 0 auto;
  height: 3px;
  background: linear-gradient(90deg, #8be9fd, #50fa7b, #ffb86c);
  opacity: 0.88;
}

main pre::-webkit-scrollbar {
  height: 8px;
  width: 8px;
}

main pre::-webkit-scrollbar-track {
  background: rgba(40, 42, 54, 0.25);
}

main pre::-webkit-scrollbar-thumb {
  background: rgba(139, 233, 253, 0.42);
  border-radius: 999px;
}

main pre code {
  display: block;
  padding: 0 !important;
  border: 0 !important;
  color: #f8f8f2;
  background: transparent !important;
  font-size: 0.95rem !important;
  line-height: 1.62 !important;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: normal;
}

main :not(pre) > code {
  font-size: 0.9em;
  line-height: inherit;
  padding: 0.08rem 0.25rem;
  border-radius: 4px;
  color: #f8f8f2;
  background: rgba(40, 42, 54, 0.5);
}

main td,
main th {
  overflow-wrap: anywhere;
}

main td,
main th {
  min-width: 8rem;
  vertical-align: top;
}

main th {
  color: #f8f8f2;
  background: rgba(68, 71, 90, 0.72);
}

main tr:nth-child(even) td {
  background: rgba(68, 71, 90, 0.2);
}

main blockquote {
  border-left-color: #bd93f9;
}

.section-content h2.doc-step {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-top: 2.2rem;
  margin-bottom: 0.95rem;
  font-size: 1.28rem !important;
  line-height: 1.32 !important;
}

.section-content h2.doc-workflow-step {
  margin-top: 1.85rem;
  margin-bottom: 0.65rem;
  color: #f8f8f2;
  font-size: 1.28rem !important;
  line-height: 1.32 !important;
}

.doc-step-number {
  display: inline-grid;
  flex: 0 0 auto;
  width: 2.05rem;
  height: 2.05rem;
  place-items: center;
  border: 1px solid rgba(248, 248, 242, 0.28);
  border-radius: 999px;
  color: #282a36;
  background: linear-gradient(135deg, #8be9fd 0%, #50fa7b 100%);
  box-shadow: 0 8px 18px rgba(80, 250, 123, 0.18);
  font-size: 1rem;
  font-weight: 800;
  line-height: 1;
}

.doc-hero-metrics,
.doc-card-grid {
  display: grid;
  gap: 0.9rem;
}

.doc-hero-metrics {
  grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr));
  margin: 1.5rem 0;
}

.doc-hero-metrics div,
.doc-card {
  border: 1px solid rgba(248, 248, 242, 0.16);
  background: rgba(68, 71, 90, 0.42);
  border-radius: 8px;
}

.doc-hero-metrics div {
  padding: 0.9rem 1rem;
}

.doc-hero-metrics strong {
  display: block;
  color: #50fa7b;
  font-size: 1.6rem;
  line-height: 1.1;
}

.doc-hero-metrics span {
  display: block;
  margin-top: 0.25rem;
  color: #f8f8f2;
}

.doc-card-grid {
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  margin: 1rem 0 2rem;
}

.doc-card {
  display: flex;
  min-height: 8.5rem;
  padding: 1rem;
  color: #f8f8f2;
  flex-direction: column;
  gap: 0.55rem;
  text-decoration: none !important;
  overflow-wrap: anywhere;
}

.doc-card:hover,
.doc-card:focus {
  border-color: #bd93f9;
  background: rgba(98, 114, 164, 0.35);
}

.doc-card strong {
  color: #8be9fd;
  font-size: 1rem;
}

.doc-card span {
  color: #f8f8f2;
}

.doc-card small {
  color: #ffb86c;
  margin-top: auto;
}

@media (min-width: 1200px) {
  .section-content h1 {
    font-size: 2.15rem !important;
  }

  .doc-card-grid {
    grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  }
}

@media (max-width: 768px) {
  .section-content {
    padding: 1.25rem !important;
  }

  .section-content h1 {
    font-size: 1.65rem !important;
  }

  .section-content h2 {
    font-size: 1.28rem !important;
  }

  .section-content h3 {
    font-size: 1.08rem !important;
  }

  .section-content h2.doc-step {
    gap: 0.65rem;
    align-items: flex-start;
    font-size: 1.08rem !important;
    line-height: 1.28 !important;
  }

  .section-content h2.doc-workflow-step {
    font-size: 1.08rem !important;
    line-height: 1.28 !important;
  }

  .doc-step-number {
    width: 1.85rem;
    height: 1.85rem;
    margin-top: 0.05rem;
    font-size: 0.95rem;
  }

  .doc-hero-metrics,
  .doc-card-grid {
    grid-template-columns: 1fr;
  }

  .doc-card {
    min-height: auto;
  }
}

@media (max-width: 430px) {
  body {
    font-size: 15px;
  }

  .section-content {
    padding: 1rem !important;
  }

  .section-content h1 {
    font-size: 1.45rem !important;
  }

  main pre code {
    font-size: 0.9rem !important;
  }
}

.doc-section-label,
.doc-meta {
  color: #8be9fd;
  font-size: 0.92rem;
}
""".strip()
    (DOCS / "assets" / "x86decomp-dracula-overrides.css").write_text(css + "\n", encoding="utf-8", newline="\n")


def write_refactor_report() -> None:
    report = {
        "published_site_changes": [
            "Removed migration-report.md, original-site-files.md, search.md, and original-site-files/ from docs_dir.",
            "Moved removed migration/archive material to mkdocs-site/archive-original-site/ so it is retained outside the published site.",
            "Published only user-facing release artifacts under docs/release-artifacts/ for pages that link to audit evidence.",
            "Replaced huge global nav with end-user sections: Home, Getting Started, Workflows, Project Examples, Reference, Release Evidence.",
            "Rebuilt major index pages as responsive card grids rather than concatenated converted links.",
            "Kept command, feature, test, schema, source coverage, and release evidence pages published and searchable.",
        ],
        "major_content_deletions": [],
    }
    (OUT / "end-user-refactor-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")


def main() -> None:
    archive_non_user_pages()
    publish_release_artifacts()
    write_home()
    write_reference()
    write_release_evidence()
    write_project_examples()
    write_grouped_index(
        "commands/index.html",
        "commands/index.md",
        "Commands",
        "Exact command syntax and parser-derived command inventory.",
        "Commands are grouped by capability route and root command. Each detail page keeps the original parser-derived usage, arguments, examples, and source basis.",
        current_dir="commands",
    )
    write_grouped_index(
        "features/index.html",
        "features/index.md",
        "Source Modules",
        "Module and symbol references generated from source names, signatures, and docstrings.",
        "Use this reference when you need to locate a module or inspect public functions and methods. Missing source docstrings remain explicitly marked on detail pages.",
        current_dir="features",
    )
    write_grouped_index(
        "tests/index.html",
        "tests/index.md",
        "Tests",
        "Exact release test inventory.",
        "The test reference preserves the current test inventory and links each source file to its node list.",
        current_dir="tests",
    )
    write_mkdocs_config()
    write_css()
    write_refactor_report()
    print("End-user site refactor complete.")


if __name__ == "__main__":
    main()
