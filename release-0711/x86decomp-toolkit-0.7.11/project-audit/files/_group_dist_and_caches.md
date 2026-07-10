# Grouped audit — generated artifacts and caches (B02g)

Grouped per owner-approved scope: generated/cache files receive identity + purpose + hygiene review, not line-level review.

## dist/x86decomp_toolkit-0.7.11-py3-none-any.whl (369,957 B, binary zip)
- Purpose: built wheel of this release. Hash in FILE_INVENTORY.csv.
- Belongs in repo? A release folder may legitimately carry its wheel, but it is BUILT FROM THE PRE-FIX SOURCE: the 68 post-release source edits (REPO-001) are not in this wheel (mtime 18:44, predates edits; Strongly supported). Anyone installing this wheel gets code that differs from the shipped sources — reproducibility violation. Escalates REPO-003.
- Full source-level review not applicable: generated archive; contents derive from src/ which is audited directly.

## dist/x86decomp_toolkit-0.7.11.tar.gz (529,267 B, binary archive)
- Same assessment as the wheel; sdist predates post-release edits (Strongly supported via mtime + manifest logic).

## .pytest_cache/ (5 files: .gitignore, CACHEDIR.TAG, README.md, v/cache/lastfailed, v/cache/nodeids)
- Purpose: pytest state from local runs on the owner's machine. lastfailed = {} (no cached failures); nodeids lists test-suite public-API contract tests — evidence those tests were executed locally.
- Belongs in repo? No — transient cache; is gitignored but present because tree is not a git checkout. Part of REPO-003 (working-state contamination). No security concerns; no secrets found (read fully — they are tiny text files).

## Verdict
All 7 files: Audited — generated file. Findings: REPO-003 (contamination), REPO-005 (stale dist artifacts diverge from post-fix sources).
