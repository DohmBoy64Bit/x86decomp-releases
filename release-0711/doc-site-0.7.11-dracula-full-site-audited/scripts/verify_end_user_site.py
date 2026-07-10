from __future__ import annotations

import gzip
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

REQUIRED_DOCS = [
    "index.md",
    "getting-started.md",
    "workflows.md",
    "local-llm.md",
    "project-examples.md",
    "reference.md",
    "architecture.md",
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
    "release-artifacts/AUDIT_FIX_REPORT_0.7.11.md",
    "release-artifacts/AUDIT_FIX_VERIFICATION_0.7.11.json",
    "release-artifacts/COMMAND_REFERENCE_0.7.11.md",
    "release-artifacts/COMMAND_REFERENCE_0.7.11.json",
    "release-artifacts/DOCSTRING_AUDIT_0.7.11.md",
    "release-artifacts/DOCSTRING_AUDIT_0.7.11.json",
    "release-artifacts/RELEASE_VERIFICATION_0.7.11.md",
    "release-artifacts/RELEASE_VERIFICATION_0.7.11.json",
    "release-artifacts/DOCSITE_MARKDOWN_HASHES.json",
]


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
    for heading in re.findall(r"^(#{1,6})\s+(.+)$", text, re.MULTILINE):
        slug = slugify(heading[1])
        if slug:
            anchors.add(slug)
    return anchors


def public_page_for_markdown(path: Path) -> Path:
    rel = path.relative_to(DOCS)
    if rel.name == "index.md":
        return SITE / rel.parent / "index.html"
    return SITE / rel.with_suffix("") / "index.html"


def resolve_link(source: Path, href: str, *, html_href: bool = False) -> Path | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or href.startswith(("mailto:", "tel:", "#")):
        return None
    path = unquote(split.path)
    if not path:
        return None
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
            if split.fragment and target.suffix == ".md" and split.fragment not in anchors_in_markdown(target):
                errors.append(f"Broken fragment in {source.relative_to(DOCS).as_posix()}: {href}")
        for href in html_links:
            target = resolve_link(source, href, html_href=True)
            if target is None:
                continue
            split = urlsplit(href)
            if not target.exists():
                errors.append(f"Broken link in {source.relative_to(DOCS).as_posix()}: {href}")
                continue
            if split.fragment and target.suffix == ".md" and split.fragment not in anchors_in_markdown(target):
                errors.append(f"Broken fragment in {source.relative_to(DOCS).as_posix()}: {href}")
    return errors


def search_index_paths() -> set[str]:
    candidates = [SITE / "search" / "search_index.json", SITE / "search_index.json"]
    for candidate in candidates:
        if candidate.exists():
            data = json.loads(candidate.read_text(encoding="utf-8"))
            docs = data.get("docs", data if isinstance(data, list) else [])
            paths = set()
            for item in docs:
                loc = item.get("location") or item.get("url") or ""
                if loc:
                    paths.add(loc.split("#", 1)[0].strip("/"))
            return paths
    return set()


def built_site_errors() -> list[str]:
    errors: list[str] = []
    if not SITE.exists():
        return ["site directory is missing; run mkdocs build --strict first"]
    if not (SITE / "index.html").exists():
        errors.append("missing built site/index.html")
    if not (SITE / "sitemap.xml").exists():
        errors.append("missing generated sitemap.xml")
    if not (SITE / "sitemap.xml.gz").exists():
        errors.append("missing generated sitemap.xml.gz")
    else:
        try:
            with gzip.open(SITE / "sitemap.xml.gz", "rt", encoding="utf-8") as fh:
                fh.read(32)
        except Exception as exc:  # pragma: no cover - diagnostic
            errors.append(f"sitemap.xml.gz is not readable gzip: {exc}")
    markdown_pages = list(DOCS.rglob("*.md"))
    for page in markdown_pages:
        built = public_page_for_markdown(page)
        if not built.exists():
            errors.append(f"missing built page: {built.relative_to(SITE).as_posix()}")
    search_paths = search_index_paths()
    if not search_paths:
        errors.append("missing MkDocs search index")
    else:
        for page in markdown_pages:
            built = public_page_for_markdown(page).relative_to(SITE).as_posix()
            public = built[:-len("index.html")].rstrip("/") or "index.html"
            alternates = {public, built, public + "/", public + "/index.html"}
            if page.relative_to(DOCS).as_posix() == "index.md":
                alternates.update({"", "#x86decomp-0711-documentation"})
            if not (search_paths & alternates):
                errors.append(f"page absent from search index: {page.relative_to(DOCS).as_posix()}")
    return errors


def main() -> int:
    errors: list[str] = []
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    nav_text = json.dumps(config.get("nav", []))
    if config.get("theme", {}).get("name") != "dracula":
        errors.append("theme.name must remain dracula for the supplied site style")
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
    root_text_files = [ROOT / "mkdocs.yml", ROOT / "README.md"]
    docs_text_files = list(DOCS.rglob("*.md"))
    stale = []
    for path in root_text_files + docs_text_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"(?<![0-9A-Fa-f])0\.7\.[0-8](?![0-9A-Fa-f])", text):
            stale.append(path.relative_to(ROOT).as_posix())
    if stale:
        errors.append("stale pre-0.7.10 references in current site source: " + ", ".join(stale[:20]))
    errors.extend(link_errors())
    errors.extend(built_site_errors())
    if errors:
        print("FAIL")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"... {len(errors) - 200} additional errors omitted")
        return 1
    print("PASS")
    print(f"Published Markdown pages: {len(list(DOCS.rglob('*.md')))}")
    print(f"Built HTML pages: {len(list(SITE.rglob('*.html')))}")
    print("Dracula-styled 0.7.11 docs, release artifacts, built pages, search index, and local links verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
