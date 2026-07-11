# Audit remediation changelog — x86decomp-toolkit 0.7.11

## Scope and evidence integrity

Every one of the 83 pre-existing files in `project-audit/` was read in full and SHA-256 hashed before remediation. `AUDIT_READ_RECEIPT_0.7.11.json` records the path, byte count, line count, original digest, current digest, and read-complete flag for each file; all 83 original hashes still match. The findings registry received special review and is explicitly marked complete in that receipt.

The register and cross-file audit artifacts contain 24 unique finding identifiers. This remediation closes and mechanically verifies all 24. “100%” below means 24/24 audit findings, not an invented code-coverage result.

## Finding-by-finding changelog

| Finding | Result | Change | Verification evidence |
|---|---|---|---|
| REPO-001 | Closed—verified | Regenerated deterministic root and standalone test-suite SHA-256 manifests after all remediation artifacts were written. | scripts/source_hashes.py generate/verify; MANIFEST.sha256; test-suite/MANIFEST.sha256; ALL_FILE_MANIFEST_0.7.11.json |
| REPO-002 | Closed—verified | Removed the machine-local root harness configuration that exposed absolute user paths and environment data. | x86decomp-test.json absent; root ignore rule added |
| REPO-003 | Closed—verified | Kept build outputs, caches, downloaded tools, and harness results outside the release tree and expanded clean rules. | .gitignore; Makefile; final hygiene scan |
| REPO-004 | Closed—verified | Aligned root-level harness output/config/install paths with ignore and clean rules. | .gitignore; README/CI invocation paths are now safely ignored |
| REPO-005 | Closed—verified | Kept distribution artifacts out of the source tree, rebuilt wheel/sdist externally, byte-compared packaged source to the current tree, and clean-installed both entry points. | external build verification; 141 wheel and 141 sdist package files matched |
| TEST-001 | Closed—verified | Completed the entire collected test inventory both in isolated partitions and monolithically with no failures, errors, or skips. | FINAL_TEST_GROUP_REPORT_0.7.11.json: 258/258 post-packaging final-tree replay; FINAL_TEST_PARTITION_REPORT_0.7.11.json: 258/258 isolated; prior monolithic 258/258 |
| DOC-001 | Closed—verified | Replaced audited template and repeated-verb docstrings and added a reproducible quality-aware docstring audit. | 212 modules, 160 classes, 1,474 functions/methods; zero missing/template/repeated defects |
| DOC-002 | Closed—verified | Added a source-controlled MkDocs Material site, docs dependency, navigation, strict build gate, and CI step. | mkdocs.yml; docs/index.md; strict build PASS |
| DUP-001 | Closed—verified | Moved the repeated adapter-capability statement to one canonical page and replaced copied prose with context-specific references. | docs/adapter-capabilities.md; README.md; PROJECT_MEMORY.md; VERIFICATION.md |
| DUP-002 | Closed—verified | Made contracts.py the canonical implementation for hashing, JSON, time, path containment, and atomic writes; util.py now preserves compatibility through delegation. | src/x86decomp/contracts.py; src/x86decomp/util.py |
| DUP-003 | Closed—verified | Routed PDB and MSVC metadata bounded reads through BinaryReader, including bounded string reads with returned end offsets. | binary_reader.py; pdb.py; msvc_metadata.py |
| DUP-004 | Closed—verified | Extracted width-parameterized import-thunk and TLS-callback walkers shared by PE32 and PE32+ parsers. | pe32.py::_parse_thunk_symbols/_parse_tls_callbacks; pe.py consumers |
| DUP-005 | Closed—verified | Added an executable hash-based synchronization gate for all 24 duplicated package-data corpus sources. | scripts/verify-corpus-sync.py; exact package/repository equality PASS |
| UX-001 | Closed—verified | Added an explicit private vulnerability-reporting address, subject convention, required evidence, and disclosure flow. | SECURITY.md |
| MAINT-001 | Closed—verified | Did not restore the stale prior audit report; added this disposition/remediation report tied to current verification evidence. | project-audit/AUDIT_REMEDIATION_REPORT.md |
| MAINT-002 | Closed—verified | Made VerificationStatus a runtime output of claim verification. | evidence.py verification_status; regression test |
| CLI-001 | Closed—verified | Unified expected CLI failures around X86DecompError so domain errors emit structured JSON instead of tracebacks. | cli_utils.py CLI_ERROR_TYPES; CLI regression tests |
| CLI-002 | Closed—verified | Migrated the root CLI to shared run_cli handling, including OSError and subprocess errors with exit status 2. | cli.py main; missing-file JSON regression test |
| CLI-003 | Closed—verified | Added a specific help summary for every root command, including dynamically registered MCP commands. | 166/166 parser choices have help actions |
| ARC-001 | Closed—verified | Collapsed the two ContractError definitions into one class that remains compatible with X86DecompError and ValueError catches. | errors.py canonical class; contracts.py import; identity regression test |
| PERF-001 | Closed—verified | Memoized canonical parser discovery, route generation, and group generation with process-local LRU caches. | canonical.py cache decorators and cache-hit regression test |
| SEC-002 | Closed—verified | Runs ad-hoc SELECT statements on a dedicated read-only SQLite connection with wall-clock interruption and a 10,000-row default cap. | analysis_db.py; mutation and row-bound regression tests |
| SEC-003 | Closed—verified | Rejects every workflow function identifier outside the exact pe-rva:XXXXXXXX grammar before path construction. | workflow.py anchored regex; traversal regression test |
| SEC-004 | Closed—verified | Requires explicit --allow-remote authorization before binding the unauthenticated read-only service to a non-loopback address. | service.py and CLI flag; remote-bind regression test |

## Test and quality results

- Final post-packaging inventory: **258 collected, 258 passed, 0 failed, 0 errors, 0 skipped** across six reconciled groups in `FINAL_TEST_GROUP_REPORT_0.7.11.json`.
- Exact isolated inventory: **258 collected, 258 passed, 0 failed, 0 errors, 0 skipped** across **86 partitions** in `FINAL_TEST_PARTITION_REPORT_0.7.11.json`.
- Monolithic run: **258 passed, 0 failed, 0 skipped** in **69.55 seconds**.
- Measured code coverage: **70.19% line/statements**, **43.93% branches**, and **63.28% combined line-plus-branch** over both shipped Python packages. No 100% code-coverage claim is made.
- Docstring audit: **212/212 modules**, **160/160 classes**, and **1,474/1,474 functions/methods** documented; zero missing docstrings, zero audited template phrases, and zero repeated-leading-verb stubs.
- Static/release gates: compileall PASS, contract/schema/Java validation PASS, pyflakes PASS, strict MkDocs Material build PASS, 24-file corpus synchronization PASS.
- Packaging rehearsal: toolkit and standalone test-suite wheels/sdists built externally; both clean-installed; both entry points launched; `pip check` passed; 141 packaged toolkit files in the wheel and 141 in the sdist were byte-identical to current source.

## Code changes by subsystem

### CLI and error contracts

`ContractError` now has one public identity, root and subsystem CLIs share the same structured error path, ordinary filesystem/domain failures return JSON on stderr with status 2, and all 166 root commands contribute help text.

### Security and containment

Workflow IDs are grammar-validated before any path is formed; service exposure beyond loopback requires explicit authorization; raw database queries use a separate read-only connection, timeout interruption, and bounded result collection.

### Architecture, duplication, and performance

Foundational utility behavior delegates to `contracts.py`; PDB/MSVC readers share `BinaryReader`; PE32/PE32+ share width-parameterized thunk/TLS walkers; canonical parser/route discovery is cached; corpus package-data duplication has a digest equality gate.

### Documentation and release hygiene

Template docstrings were replaced with symbol-specific descriptions, a reproducible quality audit was added, the Material for MkDocs site was created, duplicated adapter prose was centralized, the security channel was made actionable, and local harness/build byproducts are ignored and cleaned. Stale dist artifacts remain outside the source tree.

## Artifact policy

Final wheel/sdist and repaired source ZIP outputs are produced outside the source tree. The source tree itself contains no `dist/`, build directory, test cache, downloaded tool installation, machine-local harness configuration, or test-result directory. Deterministic root, standalone test-suite, and self-excluding all-release-file manifests are regenerated after every final report file is written.
