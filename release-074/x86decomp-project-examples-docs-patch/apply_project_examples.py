#!/usr/bin/env python3
"""Apply the x86decomp Project Examples documentation overlay.

Usage:
    python apply_project_examples.py /path/to/extracted/x86decomp-docs-site-0.7.4
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html.parser
import json
import os
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit


PATCH_ID = "x86decomp-project-examples-v1"
NAV_LABEL = "Project examples"
NEW_PAGE = "project-examples.html"


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value for key, value in attrs}
        ident = data.get("id")
        if ident:
            self.ids.add(ident)
        if tag == "a" and data.get("name"):
            self.ids.add(data["name"] or "")
        for attr in ("href", "src"):
            value = data.get(attr)
            if value:
                self.links.append((attr, value))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def safe_write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def backup_files(root: Path, paths: list[Path]) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    backup = root / f".project-examples-backup-{stamp}"
    backup.mkdir(parents=True)
    for path in paths:
        if not path.exists() or not path.is_file():
            continue
        rel = path.relative_to(root)
        target = backup / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    return backup


def patch_navigation(text: str) -> tuple[str, bool]:
    if re.search(r'href="(?:\.\./)*project-examples\.html"', text):
        return text, False

    pattern = re.compile(
        r'(<a href="(?P<prefix>(?:\.\./)*)workflows\.html"[^>]*>Workflows</a>)'
    )

    def repl(match: re.Match[str]) -> str:
        prefix = match.group("prefix")
        return (
            match.group(1)
            + f'<a href="{prefix}project-examples.html">Project examples</a>'
        )

    updated, count = pattern.subn(repl, text, count=1)
    return updated, bool(count)


def patch_index(text: str) -> tuple[str, bool]:
    if 'href="project-examples.html"' in text and "See a complete hybrid project" in text:
        return text, False

    workflow_card = re.compile(
        r'(<a class="card link-card" href="workflows\.html">.*?</a>)',
        re.DOTALL,
    )
    card = (
        '\n<a class="card link-card" href="project-examples.html">'
        '<div class="card-title">See a complete hybrid project</div>'
        '<p>Follow one function from target evidence through matching, functional '
        'validation, hybrid integration, and release evidence.</p></a>'
    )
    updated, count = workflow_card.subn(lambda m: m.group(1) + card, text, count=1)
    return updated, bool(count)


def patch_workflows(text: str) -> tuple[str, bool]:
    marker = "Complete hybrid project example"
    if marker in text:
        return text, False
    block = (
        '\n<section class="callout success">'
        '<strong>Complete hybrid project example.</strong> '
        'See <a href="project-examples.html">Project examples</a> for a full '
        'target-to-release walkthrough with matching and functional validation '
        'lanes, state records, and diagrams.'
        '</section>\n'
    )
    updated, count = re.subn(
        r'(\s*<footer class="page-footer">)', block + r'\1', text, count=1
    )
    return updated, bool(count)


def patch_search_index(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "search index not present"
    text = safe_read(path)
    if "project-examples.html" in text:
        return False, "search entry already present"

    entry = {
        "title": "Project examples: end-to-end hybrid project",
        "href": "project-examples.html",
        "url": "project-examples.html",
        "kind": "guide",
        "type": "guide",
        "section": "Project examples",
        "summary": (
            "A complete hybrid reconstruction walkthrough from target evidence "
            "through matching, functional validation, image integration, and "
            "evidence-backed project status."
        ),
        "text": (
            "hybrid project target pack Ghidra assembly fallback source candidate "
            "compile ABI diff function byte match dynamic validation symbolic "
            "validation integration validation relink image match"
        ),
        "content": (
            "End-to-end hybrid project with independent matching and functional "
            "validation lanes, buildable assembly fallback, candidate promotion, "
            "bounded claims, and release evidence."
        ),
        "keywords": [
            "hybrid project",
            "matching",
            "functional validation",
            "target pack",
            "Ghidra",
            "assembly fallback",
            "byte matched",
            "integration validated",
        ],
    }
    serialized = json.dumps(entry, ensure_ascii=False, separators=(",", ":"))

    # The generated site stores a JSON-compatible array in search-index.js.
    # Insert before the final array terminator while preserving the existing variable name.
    match = re.search(r'\]\s*;\s*$', text)
    if not match:
        return False, "search-index.js did not end with a JSON-compatible array"
    before = text[: match.start()].rstrip()
    comma = "" if before.endswith("[") else ","
    updated = before + comma + "\n" + serialized + "\n" + text[match.start():]
    safe_write(path, updated)
    return True, "search entry appended"


def iter_site_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part.startswith(".project-examples-backup-") for part in path.parts):
            continue
        if path.name in {"SHA256SUMS.txt", "MANIFEST.sha256", "SITE_MANIFEST.sha256"}:
            continue
        yield path


def existing_hash_manifests(root: Path) -> list[str]:
    return [
        name
        for name in ("SHA256SUMS.txt", "MANIFEST.sha256", "SITE_MANIFEST.sha256")
        if (root / name).exists()
    ]


def refresh_hash_manifests(root: Path, names: list[str]) -> list[str]:
    files = sorted(iter_site_files(root), key=lambda p: p.relative_to(root).as_posix())
    lines = [
        f"{sha256(path)}  {path.relative_to(root).as_posix()}"
        for path in files
    ]
    payload = "\n".join(lines) + "\n"
    for name in names:
        safe_write(root / name, payload)
    return list(names)


def collect_ids(path: Path) -> set[str]:
    parser = LinkParser()
    parser.feed(safe_read(path))
    return parser.ids


def validate_local_links(root: Path) -> list[dict[str, str]]:
    html_files = sorted(root.rglob("*.html"))
    ids_cache: dict[Path, set[str]] = {}
    errors: list[dict[str, str]] = []

    for page in html_files:
        if any(part.startswith(".project-examples-backup-") for part in page.parts):
            continue
        parser = LinkParser()
        parser.feed(safe_read(page))
        for attr, raw in parser.links:
            parsed = urlsplit(raw)
            if parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}:
                continue
            if raw.startswith("//"):
                continue

            path_part = unquote(parsed.path)
            fragment = unquote(parsed.fragment)

            if not path_part:
                target = page
            elif path_part.startswith("/"):
                target = root / path_part.lstrip("/")
            else:
                target = (page.parent / path_part).resolve()

            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append({
                    "page": page.relative_to(root).as_posix(),
                    "attribute": attr,
                    "value": raw,
                    "error": "link escapes site root",
                })
                continue

            if path_part and not target.exists():
                errors.append({
                    "page": page.relative_to(root).as_posix(),
                    "attribute": attr,
                    "value": raw,
                    "error": "target does not exist",
                })
                continue

            if fragment and target.suffix.lower() in {".html", ".htm"} and target.exists():
                if target not in ids_cache:
                    ids_cache[target] = collect_ids(target)
                if fragment not in ids_cache[target]:
                    errors.append({
                        "page": page.relative_to(root).as_posix(),
                        "attribute": attr,
                        "value": raw,
                        "error": "fragment does not exist",
                    })
    return errors


def write_verification(
    root: Path,
    backup: Path,
    changed: list[str],
    search_message: str,
    refreshed: list[str],
    link_errors: list[dict[str, str]],
) -> None:
    html_count = sum(
        1 for p in root.rglob("*.html")
        if not any(part.startswith(".project-examples-backup-") for part in p.parts)
    )
    report = {
        "format": "x86decomp-project-examples-docs-patch-v1",
        "patch_id": PATCH_ID,
        "applied_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "target_release": "0.7.4",
        "status": "pass" if not link_errors else "fail",
        "new_page": NEW_PAGE,
        "html_pages_after_patch": html_count,
        "changed_files": sorted(changed),
        "search_index": search_message,
        "refreshed_hash_manifests": refreshed,
        "backup_directory": backup.name,
        "checks": {
            "new_page_present": (root / NEW_PAGE).is_file(),
            "project_examples_stylesheet_present": (
                root / "assets" / "project-examples.css"
            ).is_file(),
            "navigation_link_present_on_all_html_pages": all(
                "project-examples.html" in safe_read(p)
                for p in root.rglob("*.html")
                if not any(part.startswith(".project-examples-backup-") for part in p.parts)
            ),
            "local_links_and_fragments_valid": not link_errors,
            "zero_placeholder_markers_in_new_page": not re.search(
                r"\b(TODO|TBD|FIXME|COMING SOON)\b",
                safe_read(root / NEW_PAGE),
                flags=re.IGNORECASE,
            ),
        },
        "link_errors": link_errors,
        "truth_boundary": (
            "This report verifies the documentation overlay and its local site links. "
            "It does not re-run the toolkit's parser, test suite, external adapters, "
            "or sealed 0.7.4 release verification."
        ),
    }
    safe_write(
        root / "PROJECT_EXAMPLES_VERIFICATION.json",
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
    )

    markdown = [
        "# Project Examples documentation patch verification",
        "",
        f"- Patch: `{PATCH_ID}`",
        "- Target documentation release: `0.7.4`",
        f"- Status: **{report['status'].upper()}**",
        f"- HTML pages after patch: **{html_count}**",
        f"- Backup: `{backup.name}`",
        f"- Search index: {search_message}",
        f"- Refreshed checksum manifests: {', '.join(refreshed) if refreshed else 'none found'}",
        "",
        "## Checks",
        "",
    ]
    for name, value in report["checks"].items():
        markdown.append(f"- {'PASS' if value else 'FAIL'} — `{name}`")
    markdown.extend([
        "",
        "## Truth boundary",
        "",
        report["truth_boundary"],
        "",
    ])
    if link_errors:
        markdown.extend(["## Link errors", "", "```json", json.dumps(link_errors, indent=2), "```", ""])
    safe_write(root / "PROJECT_EXAMPLES_VERIFICATION.md", "\n".join(markdown))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_root", type=Path, help="Extracted x86decomp docs site root")
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Do not create a timestamped backup of touched files",
    )
    args = parser.parse_args()

    bundle_root = Path(__file__).resolve().parent
    payload = bundle_root / "payload"
    root = args.site_root.expanduser().resolve()

    required = [root / "index.html", root / "assets", root / "assets" / "styles.css"]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        parser.error("not an x86decomp docs site root; missing: " + ", ".join(missing))

    html_files = [
        p for p in root.rglob("*.html")
        if not any(part.startswith(".project-examples-backup-") for part in p.parts)
    ]
    candidates = html_files + [
        root / "assets" / "search-index.js",
        root / NEW_PAGE,
        root / "assets" / "project-examples.css",
        root / "PROJECT_EXAMPLES_VERIFICATION.json",
        root / "PROJECT_EXAMPLES_VERIFICATION.md",
    ]
    backup = (
        backup_files(root, candidates)
        if not args.no_backup
        else root / ".project-examples-backup-disabled"
    )

    shutil.copy2(payload / NEW_PAGE, root / NEW_PAGE)
    shutil.copy2(
        payload / "assets" / "project-examples.css",
        root / "assets" / "project-examples.css",
    )

    changed: list[str] = [NEW_PAGE, "assets/project-examples.css"]

    for page_path in html_files:
        text = safe_read(page_path)
        updated, nav_changed = patch_navigation(text)
        if page_path == root / "index.html":
            updated, index_changed = patch_index(updated)
        else:
            index_changed = False
        if page_path == root / "workflows.html":
            updated, workflows_changed = patch_workflows(updated)
        else:
            workflows_changed = False

        if nav_changed or index_changed or workflows_changed:
            safe_write(page_path, updated)
            changed.append(page_path.relative_to(root).as_posix())

    search_changed, search_message = patch_search_index(root / "assets" / "search-index.js")
    if search_changed:
        changed.append("assets/search-index.js")

    link_errors = validate_local_links(root)
    manifest_names = existing_hash_manifests(root)
    changed.extend([
        "PROJECT_EXAMPLES_VERIFICATION.json",
        "PROJECT_EXAMPLES_VERIFICATION.md",
        *manifest_names,
    ])

    write_verification(
        root=root,
        backup=backup,
        changed=changed,
        search_message=search_message,
        refreshed=manifest_names,
        link_errors=link_errors,
    )
    refreshed = refresh_hash_manifests(root, manifest_names)

    if link_errors:
        print(f"Applied {PATCH_ID}, but local-link validation found {len(link_errors)} error(s).")
        print("See PROJECT_EXAMPLES_VERIFICATION.json.")
        return 2

    print(f"Applied {PATCH_ID} successfully.")
    print(f"New page: {root / NEW_PAGE}")
    print(f"Backup: {backup}")
    print("Verification: PROJECT_EXAMPLES_VERIFICATION.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
