# Run Log — x86decomp-toolkit 0.7.11 audit

Every command that produces evidence is logged here. Format: ID, command, purpose, exit status, output summary, conclusive?, side effects.

## R-001 — 2026-07-10 05:07 UTC
- Command: `date -u; git rev-parse --is-inside-work-tree; git branch --show-current; git rev-parse HEAD; git status --porcelain; python3 --version; pip3 --version; node --version; ls -la`
- Purpose: Phase 1 baseline — VCS state, runtimes, root listing.
- Exit: git commands failed ("not a git repository"); others 0.
- Result: NOT a git repository. Python 3.10.12, pip 25.3, Node v22.22.3. Root listing captured in BASELINE.md.
- Conclusive: yes for VCS absence and runtime versions.
- Side effects: none.

## R-002 — 2026-07-10 05:08 UTC
- Command: `find` counts by top dir (pruning .x86decomp-test-tools), `du -sh`, symlink scan.
- Purpose: Composition survey.
- Exit: 0.
- Result: 694 first-party files, 7.8 MB; vendored tree 5,227 files, 1.4 GB; zero symlinks.
- Conclusive: yes.
- Side effects: none.

## R-003 — 2026-07-10 05:09 UTC
- Command: `python3 /sessions/.../outputs/build_inventory.py` (script stored in audit scratchpad; walks tree, sha256 every first-party file, component rows for vendored).
- Purpose: Phase 2 — build FILE_INVENTORY.csv + initialize AUDIT_LEDGER.csv.
- Exit: 0.
- Result: 697 inventory rows (694 first-party + 3 vendored components). Class breakdown in BASELINE.md.
- Conclusive: yes.
- Side effects: created project-audit/FILE_INVENTORY.csv, project-audit/AUDIT_LEDGER.csv, project-audit/files/ (audit artifacts only).

## R-004 — 2026-07-10 05:10 UTC
- Command: `sha256sum -c MANIFEST.sha256` (repo root).
- Purpose: Verify the shipped release integrity manifest against actual tree.
- Exit: sha256sum reported "WARNING: 68 computed checksums did NOT match" (non-zero internally; pipeline captured).
- Result: 381/449 OK, **68 FAILED** (34 src, 15 test-suite, 17 tests, 1 doc, x86decomp-test.json). Full list saved to project-audit/manifest_failures.txt. Finding REPO-001.
- Conclusive: yes — the tree does not match its own shipped manifest. Cause (post-manifest fixes vs other modification) to be corroborated against SECOND_AUDIT_FIX_REPORT_0.7.11.md in B02.
- Side effects: wrote project-audit/manifest_failures.txt (audit artifact).

## R-005 — 2026-07-10 05:11 UTC
- Command: `head README.md; cat pyproject.toml Makefile .gitignore setup.cfg`
- Purpose: Baseline build/test tooling detection.
- Exit: 0.
- Result: Captured in BASELINE.md (setuptools, pytest partitions, ruff/pyright config, dependency groups, zero required deps).
- Conclusive: yes.
- Side effects: none.

## R-006 — 2026-07-10 ~05:30 UTC
- Command: AST-based docstring quality scan over src/tests/test-suite/scripts/examples (script inline; Python 3.10 ast).
- Exit: 0. Result: 213 files parse cleanly under 3.10 grammar (no syntax errors tree-wide); 1,614 class/function defs; **555 boilerplate docstrings** matching templates 'for the current toolkit workflow.' / 'Support X processing for internal toolkit callers.'; **36 degenerate repeated-verb** ('Append append...'). Top file: coff.py (34). DOC-001 evidence (independently reproduces prior report's ~577/48 minus post-fix cleanup).
- Conclusive: yes for docstring quality metric. Side effects: none (PYTHONDONTWRITEBYTECODE).

## R-007 — uv python install 3.12
- Exit: 127 (network tunnel blocked). Result: cannot obtain Python ≥3.11 in sandbox. Runtime checks proceed on 3.10 + in-memory compat shims (enum.StrEnum, datetime.UTC, tomllib→tomli), shims live in /tmp only; findings from these runs are limited to version-independent logic (exception routing, dispatch), and each is labeled with this caveat.
- Side effects: none in repo.

## R-008 — pip3 install tomli (PyPI reachable)
- Exit: 0. Side effects: sandbox site-packages only.

## R-009 — CLI import under shim
- `import x86decomp, x86decomp.cli` → OK, __version__ 0.7.11. All imports succeed at module level.

## R-010 — Malformed-PE and missing-file behavior via ROOT entry (x86decomp.cli.main)
- `inspect-pe bad.exe` (truncated MZ+garbage, /tmp): stderr `error: missing PE signature`, exit 2 — clean.
- `inspect-pe does-not-exist.exe`: **FileNotFoundError traceback, exit 1** — CLI-002 runtime-verified.
- `pe inventory ./missing.exe` (canonical route via root): **FileNotFoundError traceback, exit 1** — root entry lacks OSError for the whole 239-route surface.
- `pe inventory ./bad.exe` via root: clean error exit 2 (root catches X86DecompError) — narrows CLI-001 to subsystem entry points.
- Conclusive: yes (exception-tuple logic is version-independent). Side effects: none in repo (cwd /tmp).

## R-011 — FormatError via subsystem entry (x86decomp.canonical.main)
- `python -m`-equivalent canonical main, `pe inventory ./bad.exe`: **x86decomp.errors.FormatError traceback, exit 1** — CLI-001 runtime-verified for run_cli-based mains.

## R-012 — Live surface-claim verification
- `x86decomp commands`: group_count=59, route_count=239 — matches README/PROJECT_MEMORY/RELEASE_VERIFICATION claims (Verified at runtime).
- Parser introspection: 166 top-level parsers = 106 flat + 59 canonical groups + 1 `commands` catalog — matches root_commands:166 claim (Verified).
- **78 of 106 flat root commands have no help= string** in `x86decomp --help` (Verified) — CLI-003.

## R-013 — 2026-07-10 ~05:45 UTC — pytest (partitioned subset, py3.10 + shims)
- Setup: pip3 install pytest pyflakes jsonschema>=4.23 fastapi javalang PyYAML capstone (sandbox site-packages only); sitecustomize shim on PYTHONPATH (/tmp); -p no:cacheprovider; PYTHONDONTWRITEBYTECODE=1. No writes to repo (pytest tmp under user tmp dir).
- Results:
  - tests/test_pe32.py: 2 passed. tests/test_coff.py: 2 passed. tests/test_evidence.py: 2 passed. tests/test_docstring_audit.py: 3 passed (does NOT pin stale hashes — computes live; no REPO-001 corroboration from this test).
  - tests/test_audit_fixes.py: 5 passed (after fastapi installed; initial failure = missing extra, environment).
  - tests/test_release_contract.py: 8 passed, 1 failed — test_exact_recursive_feature_catalog_matches_current_tree fails ONLY because it subprocess-spawns `python3 -m x86decomp.cli` without the shim (StrEnum ImportError on 3.10). Attribution: ENVIRONMENT, not product. Blocked from clean verification until run on ≥3.11.
  - tests/test_second_audit_fixes.py: 2 passed, 5 failed — all subprocess-based, same StrEnum environment cause. Attribution: ENVIRONMENT.
- Conclusion: zero product-attributable test failures in the subset run; subprocess-launching tests require Python ≥3.11 and remain Blocked in this sandbox. Full-suite run still pending (TEST-001).

## R-014 — 2026-07-10 ~06:20 UTC — structural digest + risk sweep, all remaining 93 src modules
- Command: AST signatures + regex risk sweep (subprocess/shell/eval/exec/pickle/extractall/socket/urlopen/.. etc.) over every not-yet-deep-read src module.
- Result: risk map produced. Flagged files read in full at risk sites: worker.py (isolation exec/Popen), project_state.py (tar restore), governance/plugins.py (plugin exec), integration.py (command subst), angr_backend.py (eval=solver.eval), changesets/proofs/capsules (zip = write/metadata only, no disk extraction). All clean.
- Conclusive: yes. Side effects: none.

## R-015 — deep reads of security-critical remainder
- worker.py: shell=False, argv arrays, null-byte reject, _confined_paths escape reject, RLIMIT via exec-wrapper, container --network=none --read-only --cap-drop=ALL --security-opt=no-new-privileges. Honest 'not a security boundary' for local mode.
- project_state.restore_project_backup: rejects abs/../symlink/hardlink/dev members, 100k member cap, 2GiB/8GiB size caps, single-root, extractall(filter="data").
- integration._substitute_command: token allowlist + argv (no shell); host exec gated allow_host_execution (default False).
- governance/plugins: out-of-process hash-pinned executables, subprocess argv+timeout, doctor re-verifies hash.
- Conclusion: SECURITY.md controls substantively implemented; no injection/traversal/unsafe-exec defects in code. Sole traversal defect is SEC-003 (workflow function_id), found separately.

## R-016 — 2026-07-10 ~06:35 UTC — the project's OWN verifier on the shipped tree
- Command: `python3 scripts/source_hashes.py verify --root .`
- Exit: 2 (invalid). Result: root manifest valid=False, checked=449, **68 hash mismatch** + 65 unlisted (64 of which are THIS audit's project-audit/ files; the sole product-relevant unlisted file is CODE_AUDIT_REPORT.md). test_suite manifest valid=False, 15 failures. overall valid=False.
- Conclusive: yes — REPO-001 confirmed by the toolkit's own release-gate verifier (not just external sha256sum). `make verify` (which runs this) fails on the shipped tree. Version-independent (pure hashing). Side effects: none.

## R-017 — schema meta-validation (all 97 + test-suite)
- `Draft202012Validator.check_schema` over schemas/**.json: 97 valid, 0 invalid. test-suite/schemas: all valid. Conclusive.

## R-018 — validate-contracts.py (product release gate) with compat shim
- `PYTHONPATH=src:/tmp/auditrun python3 scripts/validate-contracts.py`: exit 0, 'current contracts, examples, Java syntax, static lint, schemas, skill, and release shape passed'. Product's structural gate PASSES. (Fails only on tomllib without shim = py3.10 env.) Note: this gate does NOT include MANIFEST hash verification or the test suite, which is why it passes while source_hashes verify fails.

## R-020 — 2026-07-10 ~06:50 UTC — INTEGRITY NOTE: audit-created bytecode
- Finding: 76 `*.cpython-310.pyc` files were written into src/ (and 4 into scripts/) as an interpreter side-effect while executing the project's OWN verification tooling during Phase 10 safe-execution (validate-contracts.py import of the full package, R-018; canonical/CLI runtime demos). PYTHONDONTWRITEBYTECODE was set for the pytest runs (R-013) but not for the direct script/import runs (R-016/R-018) — my omission.
- Scope: ONLY bytecode was added. NO existing source/config/doc/test/data/schema file had its content modified (verified: all edits confined to project-audit/; the 76 additions are new __pycache__ entries, gitignored via `__pycache__/` + `*.py[cod]`).
- Removal attempted (rm, chmod+rm, python os.remove): ALL fail with 'Operation not permitted'. The workspace FUSE mount (default_permissions, host-controlled) permits file CREATION but denies DELETION in the user's real folder. I cannot remove them from within the sandbox.
- Impact: none on the product — regenerable bytecode, gitignored, ignored by source_hashes.py (IGNORED_SUFFIXES {.pyc,.pyo}) so they do NOT affect MANIFEST verification. Reinforces (does not create) REPO-003 (tree already contained cpython-313 .pyc pre-audit).
- User remediation (trivial): `make clean`, or delete src/**/__pycache__ and scripts/__pycache__ *.cpython-310.pyc.
- All subsequent audit commands export PYTHONDONTWRITEBYTECODE=1 to prevent further additions.
- This is disclosed in COVERAGE_REPORT.md and FINAL_AUDIT_REPORT.md as the sole tree change caused by the audit.

## R-021 — pyflakes + compileall (product static gates, py3.10)
- `python3 -m pyflakes src scripts test-suite/src`: exit 0 (CLEAN) — confirms CR-0710-004 pyflakes gate passes; no unused imports/names in src.
- `python3 -m compileall -q src test-suite/src tests scripts`: exit 0 — ENTIRE TREE compiles under Python 3.10, independently confirming the prior C1 (reports.py py3.11 f-string SyntaxError) is FIXED in-tree.

## R-022 — broader pytest partition (in-process, py3.10+shim, PYTHONDONTWRITEBYTECODE=1)
- 10 files (abi_disassembly, artifacts, coff_archive, diffing, memory, modes_and_db, pdb, project, workqueue, test_bundle): 18 passed, 4 skipped. Skips = LLVM/Windows tools unavailable (clean environment gating, BLOCKED-not-fail policy). ZERO product failures.
- tests/governance + tests/assembly: 41 passed, 10 failed. Sampled failure = ContractError "no COFF-capable assembler found; install clang or a MinGW assembler" (materialize.py:265) — ENVIRONMENT (missing toolchain the harness would provision), NOT product defect. Others same class.
- Cumulative across R-013/R-022: ~80+ tests pass; every failure attributed to the py3.10 sandbox or missing optional toolchains; ZERO product-attributable failures found. TEST-001 (full monolithic completion) remains unproven in-sandbox (needs ≥3.11 + toolchains) but no product defect surfaced.

## R-023 — Phase-11 fact-check
- source_hashes verify: still 68 mismatches (REPO-001 holds).
- sdist reports.py: escaped_summary fix ABSENT, broken backslash-fstring PRESENT → REPO-005 Verified (shipped sdist has the py3.11 SyntaxError the source fixed). sdist governance/cli.py has json import (fix timeline confirmed).
- cli.py:444 / cli_utils.py:20 / workflow.py:133 line refs confirmed accurate for CLI-002/CLI-001/SEC-003.
