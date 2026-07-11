# Per-file audit: `pyproject.toml`

## A. File Identity

- **Inventory ID:** `F0180`
- **Relative path:** `pyproject.toml`
- **SHA-256:** `141e8829c0aaefbd084d7a60ead3f8a07e049682e80043e1b3f1b86c55d691cf`
- **File size:** 1615 bytes
- **Language/format:** TOML
- **Classification:** Configuration or packaging
- **Apparent responsibility:** Build metadata, package dependencies, entry points, and tool configuration.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** No direct relationship established beyond directory and manifest context.
- **Key imports/dependencies:** None or not applicable.

## B. Functional Summary

Build metadata, package dependencies, entry points, and tool configuration.

- **Inputs:** The file itself is consumed as repository content, configuration, documentation, evidence, or test data.
- **Outputs:** Format-specific content for readers, build tools, tests, or package consumers.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

The complete content was reviewed for internal consistency and format-specific defects; no file-specific correctness defect was verified.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Documentation expectations were assessed proportionally to the file type; no large docstring requirement was imposed on data or binary fixtures.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

1 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

No executable file-specific test relationship applies or was established; repository-wide checks are recorded in RUN_LOG.md.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: COR-001, LIC-001, MAINT-001, UX-001.

## K. Redundancy and Consolidation Opportunities

No exact normalized-function duplicate involving this file was identified by the AST scan.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| COR-001 | Medium | Verified | project.requires-python; restore_project_backup | Declared Python 3.11 minimum includes patch releases unsupported by backup restore | pyproject.toml line 10 declares >=3.11. restore_project_backup unconditionally passes filter="data" to TarFile.extractall at project_state.py line 557. Python’s 3.11 documentation records that the filter parameter was added in 3.11.4. | On Python 3.11.0–3.11.3, project backup restoration raises TypeError before extraction. | Either require Python >=3.11.4 or feature-detect/filter safely with a compatibility path and add a minimum-version CI job. | Open |
| LIC-001 | Medium | Verified | Distribution license files | Distributed LICENSE files contain abbreviated notices rather than the full Apache-2.0 text | The root LICENSE is 428 bytes and replaces the terms with a URL; test-suite/LICENSE is 587 bytes and contains only the short boilerplate notice. Neither includes the complete Apache License 2.0 terms. | The repository and built distributions do not carry a self-contained full license copy; legal compliance consequences require counsel and were not adjudicated by this technical audit. | Replace both abbreviated files with the official complete Apache-2.0 text and retain project copyright/NOTICE information separately as appropriate. | Open |
| MAINT-001 | Low | Verified | [tool.ruff], [tool.pyright], project.optional-dependencies.dev | Strict lint/type configurations are not installable or enforced by the declared development workflow | pyproject.toml defines Ruff and strict Pyright settings at lines 45-51, but neither ruff nor pyright is listed in the dev extra, Makefile targets, or CI workflow. | Type and lint regressions covered only by those tools can enter releases unnoticed; users cannot reproduce an implied strict check from the declared dev extra. | Either add pinned tools and read-only CI targets or remove/label the configurations as optional local guidance. | Open |
| UX-001 | Low | Verified | x86decomp root parser; __version__ | Primary CLI exposes no version-reporting option | x86decomp --version exits 2 as an unrecognized argument and prints the full root usage; the package exports version 0.7.11. | Users and automation cannot query the installed executable version without importing Python metadata or package internals. | Add argparse’s version action and test its exact stdout and zero exit status. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** Proportionate to file type, subject to repository-wide documentation findings.
- **Correctness confidence:** Reduced by an open verified finding.
- **Maintainability assessment:** Open maintainability or duplication concern.
- **Test confidence:** No executable file-specific test relationship applies or was established; repository-wide checks are recorded in RUN_LOG.md.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Execute the restore contract on Python 3.11.0 and 3.11.4 (or the newly declared minimum).; Rebuild wheel and sdist, inspect their license payloads, and obtain legal review if required.; Install only the documented dev extra in a clean environment and run the declared lint/type targets.; Run installed wheel entry point with --version on supported platforms.
- **Related follow-up:** COR-001, LIC-001, MAINT-001, UX-001
- **Final audit status:** **Audited — complete**
