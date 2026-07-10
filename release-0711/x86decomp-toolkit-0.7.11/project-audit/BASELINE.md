# Audit Baseline — x86decomp-toolkit 0.7.11

Recorded: 2026-07-10 05:07 UTC (audit start)

## Repository identity
- Repository root (user machine): `C:\Users\SeanS\Downloads\x86decomp\release-0711\x86decomp-toolkit-0.7.11`
- Repository root (audit sandbox mount): `/sessions/hopeful-admiring-shannon/mnt/x86decomp-toolkit-0.7.11`
- Intended purpose (derived from README.md and pyproject.toml, per owner instruction): an evidence-governed toolkit for authorized x86 / x86-64 Windows binary analysis, reconstruction, validation, and reproducible release work. Single CLI entry point `x86decomp` (README claims 59 capability groups, 239 canonical routes) plus a separately packaged verification harness `x86decomp-test`.
- Package: `x86decomp-toolkit` version 0.7.11, license Apache-2.0, `requires-python >= 3.11`.

## Version control state
- **Not a git repository.** `git rev-parse` fails; there is no `.git` directory. This is an extracted release tree.
- Branch / commit hash: not applicable — recorded as `Blocked from verification` for any git-based claims.
- Working-tree cleanliness at audit start: cannot be established via git. Substitute evidence: the repo ships `MANIFEST.sha256` (449 entries). Verification at audit start: **381 OK, 68 FAILED** (see RUN_LOG.md entry R-003 and finding REPO-001). The tree therefore does NOT match its own shipped integrity manifest at audit start.
- File mtimes suggest bulk timestamp 2026-07-06 18:44 with later modifications to at least `x86decomp-test.json` (23:32), `CODE_AUDIT_REPORT.md` (19:27), and directories `src` (18:48), `scripts` (18:57), `test-suite` (18:56), `tests` (19:54).

## Environment
- Audit sandbox: Ubuntu 22.04 (kernel 6.8.0-124-generic), x86_64, isolated Linux VM; project mounted read-write. Auditor policy: no writes outside `project-audit/`.
- Python 3.10.12, pip 25.3, Node v22.22.3.
- **Limitation:** project requires Python >= 3.11; sandbox has 3.10.12. Some runtime checks (imports using 3.11-only syntax, strict pyright settings) may fail for environment reasons rather than product defects. Any such failure will be attributed carefully.
- Host OS of record: Windows (user machine); audit executes on the Linux sandbox against the same files.
- Network: restricted/allowlisted. No package installation planned without need; any installs recorded in RUN_LOG.md.

## Build / test tooling detected
- Build system: setuptools >= 75 (pyproject.toml), `python -m build` via Makefile `package` target.
- Test: pytest via `scripts/run-pytest-partitions.py` (Makefile `test`), plus separate `test-suite/` package (`x86decomp_testkit`, CLI `x86decomp-test`).
- Static checks configured: ruff (line-length 100, py311), pyright (strict). Neither tool is a declared dependency of the sandbox; availability to be checked in Phase 10.
- Other Make targets: verify, compile, contracts (`scripts/validate-contracts.py`), verify-hashes / hashes (`scripts/source_hashes.py`), package, install, editable, clean.
- Optional dependency groups: disassembly (capstone), dynamic (unicorn), symbolic (z3), angr, service (fastapi/uvicorn), full, pe (lief), dev.
- Runtime dependencies: **none required** (`dependencies = []`) — core is stdlib-only by design.

## Repository composition (from FILE_INVENTORY.csv, built 2026-07-10)
- 694 first-party files (7.8 MB) + vendored `.x86decomp-test-tools/` (5,227 files, 1.4 GB: Ghidra 12.1.2 install + distribution zip + objdiff.exe) inventoried as 3 component-level rows per agreed scope.
- No symlinks found. No nested git repositories or submodules found (no `.git` anywhere; verified during walk).
- Ignored-file categories present despite `.gitignore` listing them: `.pytest_cache/` (5 files), `dist/` (2 files). `.x86decomp-test-tools/` at repo root is NOT the gitignored path (`test-suite/.x86decomp-test-tools/` is the ignored one) — location discrepancy noted for review.
- Prior audit artifacts ship in the repo root: CODE_AUDIT_REPORT.md, DOCSTRING_AUDIT_0.7.11.{md,json}, SECOND_AUDIT_FIX_REPORT_0.7.11.md, SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json, RELEASE_VERIFICATION.{md,json}, ALL_FILE_MANIFEST_0.7.11.json, MANIFEST.sha256.

## Environmental limitations (standing)
1. No git metadata — provenance claims limited to shipped manifests and mtimes.
2. Python 3.10 vs required 3.11 — runtime verification may be partially blocked; will attempt and attribute failures precisely.
3. 45-second cap per shell command — long test runs will be partitioned.
4. Vendored Ghidra tree reviewed at component level only (owner decision, 2026-07-10).
5. Sandbox disk: 9.6 GB total, ~4.5 GB free — full `python -m build` of the 1.4 GB tree will not be attempted.

## Authorization constraints honored
- Review-only: no project file edits, no formatter/linter fix modes, no dependency updates, no commits (n/a — no git), no branch changes (n/a).
- Audit artifacts written only under `project-audit/`.
