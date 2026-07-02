from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "mkdocs-site"
DOCS = OUT / "docs"


REQUIRED_DOCS = [
    "index.md",
    "getting-started.md",
    "workflows.md",
    "project-examples.md",
    "reference.md",
    "release-evidence.md",
    "commands/index.md",
    "features/index.md",
    "functions/index.md",
    "tests/index.md",
    "schemas.md",
    "integrations.md",
    "verification.md",
    "source-coverage.md",
    "changelog.md",
    "about.md",
]

FORBIDDEN_PUBLISHED_DOCS = [
    "migration-report.md",
    "original-site-files.md",
    "search.md",
]

REQUIRED_RELEASE_ARTIFACTS = [
    "release-artifacts/FULL_DOCSITE_AUDIT.md",
    "release-artifacts/FULL_DOCSITE_AUDIT.json",
    "release-artifacts/PROJECT_EXAMPLES_SOURCE_AUDIT.json",
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        _, _, rest = text.partition("\n---\n")
        return rest
    return text


def anchors_in_markdown(path: Path) -> set[str]:
    text = strip_frontmatter(path.read_text(encoding="utf-8"))
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
    for heading in re.findall(r"^(#{1,6})\s+(.+)$", text, re.MULTILINE):
        cleaned = re.sub(r"`([^`]*)`", r"\1", heading[1])
        cleaned = re.sub(r"<[^>]+>", "", cleaned)
        slug = re.sub(r"[^a-z0-9 _-]", "", cleaned.lower()).strip()
        slug = re.sub(r"\s+", "-", slug)
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
    # Markdown links are resolved in source-file space. Raw HTML hrefs are
    # resolved in public URL space because MkDocs does not rewrite them.
    base = source.parent
    if html_href:
        base = source.parent if source.name == "index.md" else source.parent / source.stem
    if path.endswith("/"):
        stripped = path.rstrip("/")
        page_form = (base / f"{stripped}.md").resolve()
        if page_form.exists():
            return page_form
        return (base / stripped / "index.md").resolve()
    if not Path(path).suffix:
        page_form = (base / f"{path}.md").resolve()
        if page_form.exists():
            return page_form
        return (base / path / "index.md").resolve()
    return (base / path).resolve()


def link_errors() -> list[str]:
    errors: list[str] = []
    for source in DOCS.rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        markdown_links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        html_links = re.findall(r'href="([^"]+)"', text)
        for href in markdown_links:
            target = resolve_link(source, href, html_href=False)
            if target is None:
                continue
            split = urlsplit(href)
            if not target.exists():
                errors.append(f"Broken link in {source.relative_to(DOCS).as_posix()}: {href}")
                continue
            if split.fragment and target.suffix == ".md":
                if split.fragment not in anchors_in_markdown(target):
                    errors.append(f"Broken fragment in {source.relative_to(DOCS).as_posix()}: {href}")
        for href in html_links:
            target = resolve_link(source, href, html_href=True)
            if target is None:
                continue
            split = urlsplit(href)
            if not target.exists():
                errors.append(f"Broken link in {source.relative_to(DOCS).as_posix()}: {href}")
                continue
            if split.fragment and target.suffix == ".md":
                if split.fragment not in anchors_in_markdown(target):
                    errors.append(f"Broken fragment in {source.relative_to(DOCS).as_posix()}: {href}")
    return errors


def main() -> int:
    errors: list[str] = []
    config = yaml.safe_load((OUT / "mkdocs.yml").read_text(encoding="utf-8"))
    nav_text = json.dumps(config.get("nav", []))
    for required in REQUIRED_DOCS:
        if not (DOCS / required).exists():
            errors.append(f"Missing required doc: {required}")
    for forbidden in FORBIDDEN_PUBLISHED_DOCS:
        if (DOCS / forbidden).exists():
            errors.append(f"Forbidden migration/static page is still published: {forbidden}")
        if forbidden in nav_text:
            errors.append(f"Forbidden page remains in nav: {forbidden}")
    if (DOCS / "original-site-files").exists():
        errors.append("original-site-files/ should not be inside docs_dir")
    for artifact in REQUIRED_RELEASE_ARTIFACTS:
        if not (DOCS / artifact).exists():
            errors.append(f"Missing release artifact: {artifact}")
    if "migration-report" in nav_text or "Original Site Files" in nav_text:
        errors.append("Migration/archive labels remain in the user navigation")
    errors.extend(link_errors())
    if errors:
        print("FAIL")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"... {len(errors) - 200} additional errors omitted")
        return 1
    print("PASS")
    print(f"Published Markdown pages: {len(list(DOCS.rglob('*.md')))}")
    print("End-user nav, retained release artifacts, and local links verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
