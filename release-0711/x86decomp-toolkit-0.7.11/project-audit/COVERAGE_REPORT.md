# Coverage Reconciliation — x86decomp-toolkit 0.7.11 audit

Generated Phase 12 (2026-07-10). Method: re-walk of the tree + SHA-256 recompute vs the original FILE_INVENTORY.csv baseline (built R-003 at audit start).

## Inventory reconciliation (first-party, excludes vendored + project-audit/)
| Metric | Count |
|---|---|
| Original first-party files (audit start) | 694 |
| Current first-party files | 893 |
| Files REMOVED during audit | 0 |
| Files with CHANGED content (hash differs from baseline) | 0 |
| Files ADDED during audit | 199 |
| — of which .pyc / __pycache__ (audit-created bytecode) | 199 |
| — of which any other type | 0 |

**Interpretation:** No pre-existing project file was modified or deleted (0 changed, 0 removed — every original SHA-256 still matches). The 199 additions are ALL Python bytecode / __pycache__ entries written by the interpreter while executing the project's OWN verification tooling during Phase-10 safe-execution (pyflakes/compileall/validate-contracts/source_hashes/pytest). See RUN_LOG R-020: these could not be deleted (sandbox FUSE mount denies unlink in the user's folder), are gitignored (`__pycache__/`, `*.py[cod]`), are ignored by the product's own manifest verifier (source_hashes IGNORED_SUFFIXES {.pyc,.pyo}), and are removable by the user via `make clean`. They are an auditor side-effect, not a change to the audited product. PYTHONDONTWRITEBYTECODE=1 was applied after R-020 to prevent further additions.

## Audit-status tally (all 697 inventory rows)
| Final status | Count |
|---|---|
| Audited — complete | 449 |
| Audited — generated file | 242 |
| Audited — limited binary review (validators/*.bin ×3) | 3 |
| Audited — vendored dependency (Ghidra install, Ghidra zip, objdiff) | 3 |
| Pending / Unread / Unknown | 0 |
| **Total** | **697** |

Note: the 242 "generated file" count includes the pre-existing dist/caches (7, Bgen partial) + the 235 __pycache__/egg-info/build byproducts grouped in _group_generated_caches.md. The 199 audit-added .pyc are NOT separate inventory rows (they post-date the baseline); they are accounted for here in the reconciliation table, not the tally.

## Per-file report coverage
- First-party code/config/docs/tests: individual per-file reports (project-audit/files/*.md) for the 41 highest-value files (root metadata/docs, CLI core, all 7 parsers, 7 security-critical subsystems, 6 scripts, 3 Ghidra scripts) + grouped subsystem reports (with per-file entries) for the remaining src (93), governance/reconstruction/native/assembly/local_llm, tests, test-suite, schemas, examples, corpus, docs, and vendored components.
- Every reviewable first-party text file was read (full read for all src/*.py, scripts, ghidra Java, root docs/config; digest+risk-sweep with targeted full reads for the remainder) — no first-party .py left unread (verified: 0 src pending .py).
- Binary/generated/vendored: inventoried with hash + documented reason review was limited (not applicable — binary/regenerable/third-party).

## Hash discrepancies
- Baseline vs current: 0 unexplained. The only delta (199 added .pyc) is fully explained above.
- Product's own MANIFEST.sha256 vs tree: 68 root + 15 test-suite mismatches — this is REPO-001 (a pre-existing release-integrity defect, present at audit start, NOT caused by the audit). Confirmed by the product's own verifier (R-016).

## Audit artifacts created (under project-audit/ only)
BASELINE.md, AUDIT_PLAN.md, FILE_INVENTORY.csv, AUDIT_LEDGER.csv, RUN_LOG.md, FINDINGS_REGISTER.md, ARCHITECTURE_NOTES.md, COMMAND_SYSTEM_AUDIT.md, REVERSE_ENGINEERING_PRACTICES.md, CROSS_FILE_ANALYSIS.md, DOCUMENTATION_AUDIT.md, COVERAGE_REPORT.md, FINAL_AUDIT_REPORT.md, SESSION_STATE.md, manifest_failures.txt, and ~70 per-file/grouped reports under project-audit/files/.

## Existing project files modified by the audit
NONE (0 content changes, 0 deletions). Sole tree effect: 199 added regenerable bytecode/__pycache__ entries (disclosed above; `make clean` removes them).

## Completion check
- [x] Every inventory row has a final status (0 pending).
- [x] Every first-party reviewable file read; per-file or grouped report exists.
- [x] Every skipped/limited file has a documented reason.
- [x] Inventory↔ledger reconciled (697 rows each; statuses match).
- [x] Hashes reconciled; the one delta explained (audit-added bytecode).
- [x] No existing project file modified.
- [x] Command matrix, RE-practice, cross-file, documentation analyses complete.
