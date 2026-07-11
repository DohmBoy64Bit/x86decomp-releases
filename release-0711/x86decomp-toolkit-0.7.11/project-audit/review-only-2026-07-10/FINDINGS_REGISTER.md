# Findings register

Open findings: **9** — Critical 0, High 1, Medium 4, Low 3, Informational 1.

## REL-001 — Documented verification sequence rewrites sealed reports before hash verification

- **Category:** Release integrity
- **Severity:** High
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `ALL_FILE_MANIFEST_0.7.11.json`, `DOCSTRING_AUDIT_0.7.11.json`, `DOCSTRING_AUDIT_0.7.11.md`, `MANIFEST.sha256`, `Makefile`, `README.md`, `docs/build-and-verification.md`, `scripts/audit-docstrings.py`, `scripts/source_hashes.py`
- **Affected symbols/commands:** Makefile verify/docstrings/verify-hashes; audit-docstrings.main; source_hashes.verify_all
- **Direct evidence:** Makefile line 3 orders docstrings before verify-hashes. scripts/audit-docstrings.py lines 85-86 generate a current timestamp and lines 138-143 overwrite the two root reports by default. A disposable-clone replay changed both report hashes; the immediately following source_hashes.py verify returned exit 2 with exactly those two hash mismatches.
- **Corroborating evidence:** README.md lines 81-93 and docs/build-and-verification.md lines 3-16 direct users to make verify and state that it verifies committed manifests. The pristine archive manifest verification passed before the docstring command was run.
- **Consistency check:** The behavior conflicts with the repository’s deterministic-manifest contract: a verification-only sequence should not invalidate a previously valid sealed source state.
- **User/technical impact:** The documented release gate cannot complete against an otherwise pristine release without an intentional manifest regeneration.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Add a check-only mode that writes to a temporary location or compares generated content while excluding volatile timestamps; make verify should use that mode. Keep report regeneration as an explicit release action.
- **Verification needed:** After remediation, run make verify in a fresh extracted archive and prove all original file hashes remain unchanged.
- **Related/duplicate findings:** DOC-001, DOC-002
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## COR-001 — Declared Python 3.11 minimum includes patch releases unsupported by backup restore

- **Category:** Correctness / compatibility
- **Severity:** Medium
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `.github/workflows/ci.yml`, `pyproject.toml`, `src/x86decomp/project_state.py`, `tests/test_production.py`
- **Affected symbols/commands:** project.requires-python; restore_project_backup
- **Direct evidence:** pyproject.toml line 10 declares >=3.11. restore_project_backup unconditionally passes filter="data" to TarFile.extractall at project_state.py line 557. Python’s 3.11 documentation records that the filter parameter was added in 3.11.4.
- **Corroborating evidence:** CI tests only the latest patch selected by actions/setup-python for the 3.11 channel; no job pins 3.11.0–3.11.3. The restore tests therefore do not exercise the declared minimum patch level.
- **Consistency check:** Package metadata promises installability and operation for every version satisfying >=3.11, including 3.11.0–3.11.3.
- **User/technical impact:** On Python 3.11.0–3.11.3, project backup restoration raises TypeError before extraction.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Either require Python >=3.11.4 or feature-detect/filter safely with a compatibility path and add a minimum-version CI job.
- **Verification needed:** Execute the restore contract on Python 3.11.0 and 3.11.4 (or the newly declared minimum).
- **Related/duplicate findings:** None
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## LIC-001 — Distributed LICENSE files contain abbreviated notices rather than the full Apache-2.0 text

- **Category:** Licensing / repository hygiene
- **Severity:** Medium
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `LICENSE`, `MANIFEST.in`, `pyproject.toml`, `test-suite/LICENSE`, `test-suite/MANIFEST.in`, `test-suite/pyproject.toml`
- **Affected symbols/commands:** Distribution license files
- **Direct evidence:** The root LICENSE is 428 bytes and replaces the terms with a URL; test-suite/LICENSE is 587 bytes and contains only the short boilerplate notice. Neither includes the complete Apache License 2.0 terms.
- **Corroborating evidence:** Both package metadata files declare Apache-2.0 and package manifests include their respective LICENSE files, so the abbreviated files are what source and wheel recipients receive.
- **Consistency check:** Apache’s official application guidance instructs distributors to place the entire LICENSE-2.0 text in LICENSE; the license’s redistribution conditions require recipients to receive a copy of the license.
- **User/technical impact:** The repository and built distributions do not carry a self-contained full license copy; legal compliance consequences require counsel and were not adjudicated by this technical audit.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Replace both abbreviated files with the official complete Apache-2.0 text and retain project copyright/NOTICE information separately as appropriate.
- **Verification needed:** Rebuild wheel and sdist, inspect their license payloads, and obtain legal review if required.
- **Related/duplicate findings:** None
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## DOC-001 — Docstring quality gate passes 364 generic low-information docstrings

- **Category:** Documentation quality
- **Severity:** Medium
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `DOCSTRING_AUDIT_0.7.11.json`, `DOCSTRING_AUDIT_0.7.11.md`, `scripts/audit-docstrings.py`, `scripts/run-pytest-partitions.py`, `scripts/sync-release-contracts.py`, `src/x86decomp/abi.py`, `src/x86decomp/analysis_db.py`, `src/x86decomp/artifacts.py`, `src/x86decomp/assembly/annotation.py`, `src/x86decomp/assembly/cli.py`, `src/x86decomp/assembly/materialize.py`, `src/x86decomp/assembly/pipeline.py`, `src/x86decomp/assembly/relocations.py`, `src/x86decomp/assembly/store.py`, `src/x86decomp/benchmarks.py`, `src/x86decomp/cli.py`, `src/x86decomp/coff.py`, `src/x86decomp/compiler.py`, `src/x86decomp/compiler_lab.py`, `src/x86decomp/content_store.py`, `src/x86decomp/convergence.py`, `src/x86decomp/cpp_recovery.py`, `src/x86decomp/disassembly.py`, `src/x86decomp/evidence.py`, `src/x86decomp/exe_diff.py`, `src/x86decomp/governance/campaigns.py`, `src/x86decomp/governance/candidates.py`, `src/x86decomp/governance/changesets.py`, `src/x86decomp/governance/cli.py`, `src/x86decomp/governance/consensus.py`, `src/x86decomp/governance/counterexamples.py`, `src/x86decomp/governance/family.py`, `src/x86decomp/governance/hypotheses.py`, `src/x86decomp/governance/knowledge_graph.py`, `src/x86decomp/governance/plugins.py`, `src/x86decomp/governance/proofs.py`, `src/x86decomp/governance/reviews.py`, `src/x86decomp/governance/store.py`, `src/x86decomp/governance/workers.py`, `src/x86decomp/ground_truth.py`, `src/x86decomp/harness_generator.py`, `src/x86decomp/hybrid.py`, `src/x86decomp/integration.py`, `src/x86decomp/linker_layout.py`, `src/x86decomp/local_llm/matching.py`, `src/x86decomp/local_llm/profiles.py`, `src/x86decomp/local_llm/prompts.py`, `src/x86decomp/mcp.py`, `src/x86decomp/memory.py`, `src/x86decomp/native/closed_loop.py`, `src/x86decomp/native/hybrid_composer.py`, `src/x86decomp/native/matching.py`, `src/x86decomp/native/pe_reconstruction.py`, `src/x86decomp/native/runtime.py`, `src/x86decomp/native/slots.py`, `src/x86decomp/native/staging.py`, `src/x86decomp/native/store.py`, `src/x86decomp/native/windows_tools.py`, `src/x86decomp/orchestrator.py`, `src/x86decomp/patching.py` … (complete set in per-file ledger/evidence)
- **Affected symbols/commands:** 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json
- **Direct evidence:** A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”.
- **Corroborating evidence:** The shipped audit reports PASS because audit-docstrings.py lines 25-28 check only two older exact phrases, and lines 81-83 check only a repeated first word. The generic patterns occur across 128 files.
- **Consistency check:** The repository’s documentation standard calls for specific, symbol-appropriate explanations rather than syntactically present but low-information text.
- **User/technical impact:** API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions.
- **Verification needed:** Repeat the full AST scan and manually sample each pattern family after remediation.
- **Related/duplicate findings:** REL-001
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## DOC-002 — Detailed command documentation covers only a small fraction of the live command surface

- **Category:** Command documentation
- **Severity:** Medium
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `README.md`, `docs/COMMAND_REFERENCE_0.7.11.json`, `docs/COMMAND_REFERENCE_0.7.11.md`, `src/x86decomp/canonical.py`, `src/x86decomp/cli.py`
- **Affected symbols/commands:** 166 root commands, 405 parser nodes, 239 canonical routes
- **Direct evidence:** Runtime parser introspection found help text for all 405 parser nodes. Cross-checking every command and route against Markdown code blocks and prose found explicit examples for 23/166 root commands, mentions for 31/405 parser nodes, and examples for 7/239 canonical routes.
- **Corroborating evidence:** docs/COMMAND_REFERENCE_0.7.11.md is 11 lines and delegates to a JSON inventory that lists names/counts rather than per-command arguments, outputs, errors, safety notes, examples, and use cases.
- **Consistency check:** Built-in discoverability is strong, but it does not satisfy the project’s own long-form analyst and automation documentation needs.
- **User/technical impact:** New users must infer workflows from --help and source; safety, output, and error contracts are not consistently explained outside the executable.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Generate or maintain a full command reference from parser metadata, augmented with human-authored examples, outputs, error behavior, and safety notes.
- **Verification needed:** Re-run the command-documentation matrix and manually execute every published example in a disposable workspace.
- **Related/duplicate findings:** REL-001
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## TEST-001 — Six packaged self-test files duplicate source tests without an explicit synchronization gate

- **Category:** Testing / duplication
- **Severity:** Low
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `scripts/run-pytest-partitions.py`, `test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py`, `test-suite/src/x86decomp_testkit/self_tests/test_adapter_detection_resolution.py`, `test-suite/src/x86decomp_testkit/self_tests/test_archive_security.py`, `test-suite/src/x86decomp_testkit/self_tests/test_cli_and_installation.py`, `test-suite/src/x86decomp_testkit/self_tests/test_config_models.py`, `test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py`, `test-suite/tests/test_adapter_capabilities.py`, `test-suite/tests/test_adapter_detection_resolution.py`, `test-suite/tests/test_archive_security.py`, `test-suite/tests/test_cli_and_installation.py`, `test-suite/tests/test_config_models.py`, `test-suite/tests/test_inventory_reports_process.py`
- **Affected symbols/commands:** Six test-suite/tests ↔ x86decomp_testkit/self_tests file pairs
- **Direct evidence:** Six pairs have different file hashes but identical AST behavior after docstrings are removed. The packaged copies are used when the source test tree is unavailable; the source copies are used in a checkout.
- **Corroborating evidence:** The exact 258-test runner intentionally excludes the packaged duplicate tree. The 21 packaged self-tests were run separately and all passed. No dedicated byte/AST synchronization script or CI assertion was found.
- **Consistency check:** Two maintained copies of the same executable test logic can drift even when both currently pass.
- **User/technical impact:** Future fixes may land in only one copy, producing checkout/package behavior differences.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Generate packaged self-tests from one canonical source or add a normalized-AST synchronization gate.
- **Verification needed:** Intentionally perturb one copy and prove the new gate fails.
- **Related/duplicate findings:** None
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## MAINT-001 — Strict lint/type configurations are not installable or enforced by the declared development workflow

- **Category:** Maintainability / tooling
- **Severity:** Low
- **Confidence:** Verified
- **Status:** Open — remediation recommended
- **Affected files:** `.github/workflows/ci.yml`, `Makefile`, `pyproject.toml`
- **Affected symbols/commands:** [tool.ruff], [tool.pyright], project.optional-dependencies.dev
- **Direct evidence:** pyproject.toml defines Ruff and strict Pyright settings at lines 45-51, but neither ruff nor pyright is listed in the dev extra, Makefile targets, or CI workflow.
- **Corroborating evidence:** The active CI runs contracts, docs, pytest, packaging, and the comprehensive harness, but no Ruff or Pyright command.
- **Consistency check:** Checked-in strict configuration suggests intended quality gates, while the documented install/verification path cannot invoke them.
- **User/technical impact:** Type and lint regressions covered only by those tools can enter releases unnoticed; users cannot reproduce an implied strict check from the declared dev extra.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Either add pinned tools and read-only CI targets or remove/label the configurations as optional local guidance.
- **Verification needed:** Install only the documented dev extra in a clean environment and run the declared lint/type targets.
- **Related/duplicate findings:** None
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## UX-001 — Primary CLI exposes no version-reporting option

- **Category:** CLI usability
- **Severity:** Low
- **Confidence:** Verified
- **Status:** Open — optional improvement
- **Affected files:** `README.md`, `pyproject.toml`, `src/x86decomp/__init__.py`, `src/x86decomp/cli.py`
- **Affected symbols/commands:** x86decomp root parser; __version__
- **Direct evidence:** x86decomp --version exits 2 as an unrecognized argument and prints the full root usage; the package exports version 0.7.11.
- **Corroborating evidence:** Parser introspection found no --version action among root options; README identifies the release but documents no runtime version command.
- **Consistency check:** A version flag is conventional and useful for reproducible evidence records, though it is not currently promised by documentation.
- **User/technical impact:** Users and automation cannot query the installed executable version without importing Python metadata or package internals.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Add argparse’s version action and test its exact stdout and zero exit status.
- **Verification needed:** Run installed wheel entry point with --version on supported platforms.
- **Related/duplicate findings:** None
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.

## REPO-001 — Forty-five trailing-whitespace lines remain in seventeen text files

- **Category:** Repository hygiene
- **Severity:** Informational
- **Confidence:** Verified
- **Status:** Open — optional cleanup
- **Affected files:** `docs/ARCHITECTURE_MAP.md`, `project-audit/files/_group_schemas_examples_corpus.md`, `project-audit/files/scripts__validate-contracts.py.md`, `project-audit/files/src__x86decomp__coff_archive.py.md`, `setup.cfg`, `test-suite/docs/ARCHITECTURE_MAP.md`, `test-suite/setup.cfg`, `test-suite/tests/test_adapter_capabilities.py`, `test-suite/tests/test_adapter_detection_resolution.py`, `test-suite/tests/test_architecture_maps.py`, `test-suite/tests/test_archive_security.py`, `test-suite/tests/test_cli_and_installation.py`, `test-suite/tests/test_config_models.py`, `test-suite/tests/test_inventory_reports_process.py`
- **Affected symbols/commands:** Exact lines listed in FILE_INVENTORY.csv notes and per-file reports
- **Direct evidence:** A byte-preserving line scan found 45 lines ending in spaces or tabs across 17 files; no files were modified.
- **Corroborating evidence:** The findings are reproducible from evidence/repo_analysis.json and include intentional Markdown hard-break lines as well as whitespace-only test lines.
- **Consistency check:** This does not affect runtime behavior; it is a formatting/review-noise issue and is therefore informational.
- **User/technical impact:** Minor diff noise and possible editor/linter churn.
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** Classify intentional Markdown hard breaks, then remove only unintended trailing whitespace in a separate reviewed change.
- **Verification needed:** Run a format-aware trailing-whitespace check after cleanup.
- **Related/duplicate findings:** TEST-001
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.
