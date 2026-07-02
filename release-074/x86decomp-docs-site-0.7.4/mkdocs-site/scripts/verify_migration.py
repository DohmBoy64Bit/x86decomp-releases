from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "mkdocs-site"
DOCS = OUT / "docs"
MANIFEST = OUT / "migration-manifest.json"
SKIP_DIRS = {"mkdocs-site", "__pycache__", ".git"}


def original_html_pages() -> list[str]:
    pages = []
    for path in ROOT.rglob("*.html"):
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        pages.append(relative.as_posix())
    return sorted(pages)


def original_non_html_files() -> list[str]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.suffix.lower() == ".html":
            continue
        files.append(relative.as_posix())
    return sorted(files)


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        _, _, rest = text.partition("\n---\n")
        return rest
    return text


def anchors_in_markdown(path: Path) -> set[str]:
    text = strip_frontmatter(path.read_text(encoding="utf-8"))
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
    headings = re.findall(r"^(#{1,6})\s+(.+)$", text, re.MULTILINE)
    for _, heading in headings:
        cleaned = re.sub(r"`([^`]*)`", r"\1", heading)
        cleaned = re.sub(r"<[^>]+>", "", cleaned)
        slug = re.sub(r"[^a-z0-9 _-]", "", cleaned.lower()).strip()
        slug = re.sub(r"\s+", "-", slug)
        if slug:
            anchors.add(slug)
    return anchors


def html_ids(path: Path) -> set[str]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    main = soup.select_one("main#main")
    if not main:
        return set()
    return {tag["id"] for tag in main.find_all(id=True)}


def verify_links() -> list[str]:
    errors: list[str] = []
    anchors_cache: dict[Path, set[str]] = {}
    for md_path in DOCS.rglob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            href = match.group(1).strip()
            if not href or href.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            split = urlsplit(href)
            if split.scheme or split.netloc:
                continue
            target_path = unquote(split.path)
            if not target_path:
                continue
            target = (md_path.parent / target_path).resolve()
            if not target.exists():
                errors.append(f"Broken link in {md_path.relative_to(DOCS).as_posix()}: {href}")
                continue
            if split.fragment and target.suffix == ".md":
                if target not in anchors_cache:
                    anchors_cache[target] = anchors_in_markdown(target)
                if split.fragment not in anchors_cache[target]:
                    errors.append(f"Broken fragment in {md_path.relative_to(DOCS).as_posix()}: {href}")
    return errors


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected_pages = original_html_pages()
    converted_pages = sorted(data["pages"])
    expected_files = original_non_html_files()
    copied_files = sorted(data["copied_original_files"])
    errors: list[str] = []

    if expected_pages != converted_pages:
        errors.append(f"HTML coverage mismatch: expected {len(expected_pages)}, manifest has {len(converted_pages)}")
        missing = sorted(set(expected_pages) - set(converted_pages))
        extra = sorted(set(converted_pages) - set(expected_pages))
        if missing:
            errors.append("Missing pages: " + ", ".join(missing[:20]))
        if extra:
            errors.append("Extra pages: " + ", ".join(extra[:20]))

    for html_page in expected_pages:
        md_page = DOCS / Path(html_page).with_suffix(".md")
        if not md_page.exists():
            errors.append(f"Missing Markdown page for {html_page}")
            continue
        missing_ids = html_ids(ROOT / html_page) - anchors_in_markdown(md_page)
        if missing_ids:
            errors.append(f"Missing anchors in {md_page.relative_to(DOCS).as_posix()}: {', '.join(sorted(missing_ids)[:20])}")

    if expected_files != copied_files:
        errors.append(f"Original file copy mismatch: expected {len(expected_files)}, manifest has {len(copied_files)}")
        missing = sorted(set(expected_files) - set(copied_files))
        extra = sorted(set(copied_files) - set(expected_files))
        if missing:
            errors.append("Missing copied files: " + ", ".join(missing[:20]))
        if extra:
            errors.append("Extra copied files: " + ", ".join(extra[:20]))

    errors.extend(verify_links())

    if errors:
        print("FAIL")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"... {len(errors) - 200} additional errors omitted")
        return 1

    print("PASS")
    print(f"Converted HTML pages: {len(converted_pages)}")
    print(f"Copied original non-HTML files: {len(copied_files)}")
    print("Local Markdown links and original anchors verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
