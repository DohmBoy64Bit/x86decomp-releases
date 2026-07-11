# Review audit finding closure

All nine findings from `project-audit/review-only-2026-07-10/FINDINGS_REGISTER.md` are closed by this remediation set. Historical audit files remain unchanged and continue to describe the pre-remediation state.

## Verification summary

- Source test inventory: **268/268 passed**, zero failures, errors, or skips.
- Packaged duplicate self-tests: **21/21 passed** independently.
- Live command examples: **405/405 passed**.
- Findings: **9/9 closed**, zero open.

## Finding-by-finding closure

### REL-001 — Documented verification sequence rewrites sealed reports before hash verification

- **Severity:** High
- **Status:** Closed — verified

**Implemented changes**

- scripts/audit-docstrings.py now emits deterministic content and separates --check from --write
- Makefile verify invokes the non-mutating check target; regeneration is explicit via docstrings-update
- README.md and docs/build-and-verification.md document the read-only gate
- tests/test_review_remediation.py hashes both reports before and after --check

**Verification**

- python scripts/audit-docstrings.py --check returned 0 and reported no mismatches
- Regression test proved the JSON and Markdown report bytes do not change
- Final source manifests are regenerated only after all intentional edits and verified separately

### COR-001 — Declared Python 3.11 minimum includes patch releases unsupported by backup restore

- **Severity:** Medium
- **Status:** Closed — verified by signature-contract tests

**Implemented changes**

- src/x86decomp/project_state.py feature-detects the TarFile.extractall filter parameter
- Runtimes with filter support use filter="data"; older 3.11 signatures extract only after the existing complete member/path/type validation
- CI now pins Python 3.11.0 in addition to 3.12 and 3.13
- Regression tests exercise both legacy and filtered extraction signatures

**Verification**

- test_backup_extraction_supports_pre_filter_python passed
- test_backup_extraction_uses_data_filter_when_available passed
- The entire 268-test source inventory passed

**Limits recorded without overclaiming**

- A CPython 3.11.0 binary was not available in the execution image; uv also reported no downloadable 3.11.0 build. The compatibility branch was verified with an exact legacy-signature test and is pinned for CI execution.

### LIC-001 — Distributed LICENSE files contain abbreviated notices rather than the full Apache-2.0 text

- **Severity:** Medium
- **Status:** Closed — source verified; package payload verified in final delivery report

**Implemented changes**

- Replaced both LICENSE files with the complete Apache License 2.0 text
- Added root and test-suite NOTICE files
- Updated both MANIFEST.in files to include NOTICE

**Verification**

- Both LICENSE files are byte-identical, exceed 10,000 bytes, and contain the complete terms headings
- Regression tests require the complete text and both NOTICE files

**Limits recorded without overclaiming**

- This is a technical packaging remediation, not legal advice.

### DOC-001 — Docstring quality gate passes 364 generic low-information docstrings

- **Severity:** Medium
- **Status:** Closed — verified

**Implemented changes**

- Replaced all 364 audit-identified generic docstrings across 128 files
- Refined 127 initially mechanical replacements into behavior-specific summaries
- Expanded scripts/audit-docstrings.py to detect every audited template family
- Made reports deterministic and source-state-bound

**Verification**

- 215 Python files audited
- 215/215 modules, 163/163 classes, and 1,522/1,522 functions or methods have docstrings
- Zero generic occurrences, zero missing docstrings, and zero repeated-leading-verb defects
- tests/test_audit_fixes.py and tests/test_docstring_audit.py passed

### DOC-002 — Detailed command documentation covers only a small fraction of the live command surface

- **Severity:** Medium
- **Status:** Closed — verified

**Implemented changes**

- Added scripts/generate_command_reference.py as the reproducible source of command documentation
- Generated JSON and Markdown references for 166 root commands, 239 canonical routes, and 405 parser nodes
- Each node records summary, arguments/options/defaults, usage/help, success and error contracts, safety classification/note, example, and real-world use case
- Added check/update Makefile targets, CI enforcement, and regression tests

**Verification**

- Generator --check reports 405/405 current records with no mismatches
- All 405 published --help examples parsed successfully against the live CLI
- Command reference coverage counters are 405/405 for every required field

**Limits recorded without overclaiming**

- Examples intentionally use non-mutating --help invocations; destructive or environment-dependent workflows are documented but were not executed merely to validate prose.

### TEST-001 — Six packaged self-test files duplicate source tests without an explicit synchronization gate

- **Severity:** Low
- **Status:** Closed — verified

**Implemented changes**

- Added scripts/verify_self_test_sync.py with a fixed six-pair inventory
- The gate strips docstrings and compares normalized ASTs, preserving documentation freedom while enforcing executable equivalence
- Added Makefile and CI enforcement

**Verification**

- All six pairs pass the synchronization gate
- A regression test mutates a packaged copy and proves the gate reports the exact mismatch
- 21/21 packaged self-tests pass independently

### MAINT-001 — Strict lint/type configurations are not installable or enforced by the declared development workflow

- **Severity:** Low
- **Status:** Closed — verified

**Implemented changes**

- Added bounded Ruff and Pyright versions to the dev extra
- Added lint and typecheck Makefile targets and verify dependencies
- Added Ruff and Pyright CI steps
- Set an enforced Pyright basic source scope instead of an aspirational unenforced strict configuration
- Corrected type-contract defects exposed in CLI claim serialization, COFF archive symbol access, metadata handling, SQL arguments, PE checksum typing, and related paths

**Verification**

- Ruff completed with no findings
- Pyright completed with zero errors, warnings, or information diagnostics
- The tools were installed from the declared version ranges in an isolated target directory

### UX-001 — Primary CLI exposes no version-reporting option

- **Severity:** Low
- **Status:** Closed — verified

**Implemented changes**

- Registered argparse version action using x86decomp.__version__
- Documented x86decomp --version in README.md

**Verification**

- Parser regression test confirms exit status 0 and exact output: x86decomp 0.7.11

### REPO-001 — Forty-five trailing-whitespace lines remain in seventeen text files

- **Severity:** Informational
- **Status:** Closed — verified

**Implemented changes**

- Removed all 45 audited trailing-whitespace occurrences from active release files
- Preserved the immutable historical review-only evidence subtree rather than rewriting audit evidence
- Added a repository-wide regression scan outside that historical evidence subtree
- Removed 116 compiled Python cache files present in the working baseline

**Verification**

- Regression scan reports zero trailing-whitespace lines in active release text
- No __pycache__, .pyc, .pytest_cache, .ruff_cache, build, or dist artifacts remain in the sealed source tree

**Limits recorded without overclaiming**

- The original review named 17 files while its explicit affected-file list contained 14 active files; every listed active file and every reproducibly detected occurrence was cleaned.
