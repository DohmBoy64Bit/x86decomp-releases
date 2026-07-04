# End-User Site Audit — x86decomp 0.7.8 Docs

Date: 2026-07-04 · Scope: full coverage, formatting, and UX audit of the Dracula-themed doc site. Site rebuilt with `mkdocs build` (zero warnings).

## 1. Coverage audit — 100% verified

- 500/500 markdown pages build to HTML; every page is reachable from the home page (crawl-verified).
- 102/102 CLI commands from the 0.7.8 parser (`src/x86decomp/cli.py`) have documentation pages; the remaining command pages are group/route pages.
- All 145 source modules, 1,299 function symbols, 100 schemas, and 59 test source files are linked from their section indexes.
- Fixed: 60 orphaned duplicate pages (50 older-generation `tests/` pages, 10 duplicate `features/` `__init__` pages) were unreachable dead weight — deleted; the linked canonical versions remain.
- Fixed: stale counts on Home and Reference (modules 114→145, schemas 97→100, symbols 983→1,299, test stats corrected).

## 2. Formatting audit — internal noise removed, theme untouched

Removed content end users don't need, across 492 pages (see `end-user-cleanup-report.json` for per-file log):

- SHA-256 hash lines, rows, and table columns on command, schema, module, and test pages.
- "Source basis" and "Verification boundary" boilerplate sections on all 167 command pages.
- Parser internals in argument tables (`parser destination: …`, `type: _path`), and "No help text declared." filler — replaced with clean types and em dashes.
- "This page is generated from the exact schema file…" and "The schema audit verifies…" boilerplate on all 100 schema pages; `Not declared` cells → —.
- Migration debris: `original_path:` frontmatter and stray `Section:` lines on 13 pages.
- Fixed a double-H1 on the Decompilation Acceleration page; every page now has exactly one H1 and no heading-level jumps.

Dev/internal pages removed from the end-user site (per your instruction): Release Evidence, Verification, Source Coverage, the `release-artifacts/` audit bundle (strict audits, hash manifests), and the project-examples source-audit ledger. All inbound links to them were removed or rewritten. Changelog and About are kept under a "Project" nav section.

## 3. UX audit — results

- Links: 0 broken internal links across 502 HTML files (the 404 page uses root-absolute links, correct when served).
- Navigation: 4 top-level sections + Home; full nav renders on every page including deep command/schema pages.
- Titles: every page has a unique `<title>` ("Page – x86decomp 0.7.8 Docs"); descriptions simplified ("Command reference for…", "Schema reference for…").
- Search: index built with 2,223 entries covering all pages.
- Mobile: viewport meta present on all pages; Dracula theme's responsive layout unchanged.
- Theme: Dracula CSS + `x86decomp-dracula-overrides.css` intact; stat grid and card grids render as before.

## 4. Rendered-output display pass (code-level visual audit)

Scanned all 502 rendered HTML pages for display defects:

- Fixed: all 12 project-example pages had a broken "Related examples" block — multiline markdown links that rendered as literal `](file.md)` text on the page. Rewritten as clean link lists; verified they now render as proper `<ul>` navigation.
- Verified: no literal markdown (bold markers, pipes, headings, attr syntax) leaks anywhere; every heading has body content; no empty or mismatched table rows; no missing asset references at any nav depth.
- Verified: every custom class used in pages (`doc-card`, `doc-card-grid`, `doc-stat-grid`, `doc-step`, `doc-step-number`, `doc-workflow-step`) has rules in the shipped CSS, so cards, stat grids, and step numbers style correctly.
- Verified: theme CSS includes table `overflow-x` and `pre` overflow handling, so wide command tables and usage blocks scroll instead of breaking mobile layout.
- Known-fine: the 404 page uses root-absolute asset/link paths — correct when the site is served at the domain root (e.g. `mkdocs serve`).

## Notes

- Repo-root dev artifacts (`DOCSITE_MARKDOWN_HASHES.json`, `FULL_DOCSITE_AUDIT_VERIFICATION.md`, `SITE_UPDATE_VERIFICATION.*`) are now stale — they hash the pre-cleanup markdown. They are not part of the built site; regenerate them if you still use that tooling.
- To preview: `mkdocs serve` from this folder, or open `site/index.html` (search requires serving over HTTP).
