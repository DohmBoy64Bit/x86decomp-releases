# x86decomp 0.7.8 Full Docsite Audit Verification

Status: **PASS**

This package preserves the Dracula MkDocs theme/template configuration and updates the documentation content, coverage manifests, and verification scripts only.

## Verified counts

| Area | Count |
| --- | ---: |
| Markdown pages | 465 |
| Built HTML pages | 467 |
| Markdown files with SHA-256 checks | 465 |
| Root commands documented | 166 |
| Canonical groups documented | 59 |
| Canonical routes documented | 239 |
| JSON Schemas documented | 97 |
| Unique source-manifest paths documented | 433 |
| Root manifest entries verified | 433 |
| Test-suite manifest entries verified | 63 |
| Python modules documented | 145 |
| Python AST symbols documented | 1299 |
| Test source files documented | 59 |

## Checks run

- `python -m mkdocs build --strict`
- `python scripts/full_docsite_audit.py <toolkit-root> docs/release-artifacts/FULL_DOCSITE_HASH_PARITY_AUDIT.json`
- `python scripts/verify_end_user_site.py`
- `python scripts/verify_markdown_hashes.py`
- `python -m py_compile scripts/*.py`
- `bash build.sh`

## Content corrections made

- Added a full end-to-end text-swap project example at `docs/project-examples/text-swap-project.md`.
- Added `DOCSITE_MARKDOWN_HASHES.json` and `scripts/verify_markdown_hashes.py` so every published Markdown file has a SHA-256 check.
- Added `scripts/full_docsite_audit.py` for source-to-docsite parity checks.
- Regenerated command pages from the live parser surface.
- Regenerated schema, source-coverage, feature/module, function, and test indexes from the toolkit source tree.
- Removed the stale pre-current version tag from active Markdown.

## Boundary

This is a full documentation/source parity audit. It does not claim a new full optional adapter-aware runtime harness pass.
