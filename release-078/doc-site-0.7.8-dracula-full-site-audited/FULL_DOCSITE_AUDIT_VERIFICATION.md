# Full Docsite Audit Verification

Status: **PASS**

## Inputs

- Toolkit baseline: `x86decomp-toolkit-0.7.8-complete-release-bundle.zip`
- Site baseline: latest Dracula MkDocs docsite in this workspace
- Theme/style preservation: `theme.name: dracula`

## Results

- Markdown pages: **569**
- Markdown SHA-256 entries: **569**
- Built HTML pages: **571**
- Root commands: **166**
- Canonical groups: **59**
- Canonical routes: **239**
- JSON Schemas: **97**
- Unique source-manifest paths: **433**
- Root manifest entries verified: **433**
- Test-suite manifest entries verified: **63**
- Python modules documented: **145**
- Python AST symbols documented: **1299**
- Test source files documented: **59**

## Commands run

- `python -m mkdocs build --strict`
- `python scripts/full_docsite_audit.py <toolkit-root> docs/release-artifacts/FULL_DOCSITE_HASH_PARITY_AUDIT.json`
- `python scripts/verify_markdown_hashes.py`
- `python scripts/verify_end_user_site.py`
- `python -m py_compile scripts/*.py`
- `bash build.sh`

No errors were reported. This verification is documentation/source parity only and does not claim a full optional adapter-aware runtime harness pass.
