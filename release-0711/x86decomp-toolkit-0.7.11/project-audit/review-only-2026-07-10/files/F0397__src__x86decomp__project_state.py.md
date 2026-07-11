# Per-file audit: `src/x86decomp/project_state.py`

## A. File Identity

- **Inventory ID:** `F0397`
- **Relative path:** `src/x86decomp/project_state.py`
- **SHA-256:** `75d110ea45d0a708e2f8d87c07a96f2c593ea70491590c2f28e22ac6c405fa89`
- **File size:** 24176 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Transactional project-state database, migrations, backup, and recovery.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/cli.py`, `src/x86decomp/orchestrator.py`, `src/x86decomp/project.py`, `src/x86decomp/release_gate.py`, `src/x86decomp/reproducibility.py`, `src/x86decomp/service.py`, `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`, `tests/test_production.py`
- **Key imports/dependencies:** `.content_store`, `.errors`, `.util`, `__future__`, `contextlib`, `dataclasses`, `gzip`, `json`, `os`, `pathlib`, `shutil`, `sqlite3`, `tarfile`, `tempfile`, `typing`

## B. Functional Summary

Transactional project-state database, migrations, backup, and recovery. Major symbols: ProjectCheck, ProjectStateDatabase, state_database_path, create_project_backup, migrate_project, check_project_state, repair_project_state, project_gc, restore_project_backup, ProjectCheck.to_dict, ProjectStateDatabase.close, ProjectStateDatabase.transaction. Static analysis recorded 22 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 22 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: self.connection.execute×13, database.connection.execute×2, output.parent.mkdir×1, destination.parent.mkdir×1, self.path.parent.mkdir×1, sqlite3.connect×1, os.replace×1, destination.mkdir×1, shutil.rmtree×1. 3 broad exception handler(s) were inspected in context; no blanket finding was created without a demonstrated failure path.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 21/21. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: restore_project_backup (branches=18, AST nodes=478), check_project_state (branches=10, AST nodes=369), repair_project_state (branches=10, AST nodes=318), create_project_backup (branches=7, AST nodes=354), migrate_project (branches=6, AST nodes=368). 1 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 3. Global/nonlocal declarations: 0. Pass statements: 2. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Boilerplate/duplication indicator: 2 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

22 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: ProjectCheck(1), ProjectStateDatabase(12), artifact_digests(2), check_project_state(4), close(11), create_project_backup(5), integrity_check(1), migrate_project(4), project_gc(3), record_migration(1). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: COR-001.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 1: src/x86decomp/analysis_db.py:AnalysisDatabase.close, src/x86decomp/orchestrator.py:Orchestrator.close, src/x86decomp/project_state.py:ProjectStateDatabase.close. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 11: src/x86decomp/mcp.py:StdioMCPClient.__exit__, src/x86decomp/orchestrator.py:Orchestrator.__exit__, src/x86decomp/project_state.py:ProjectStateDatabase.__exit__. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| COR-001 | Medium | Verified | project.requires-python; restore_project_backup | Declared Python 3.11 minimum includes patch releases unsupported by backup restore | pyproject.toml line 10 declares >=3.11. restore_project_backup unconditionally passes filter="data" to TarFile.extractall at project_state.py line 557. Python’s 3.11 documentation records that the filter parameter was added in 3.11.4. | On Python 3.11.0–3.11.3, project backup restoration raises TypeError before extraction. | Either require Python >=3.11.4 or feature-detect/filter safely with a compatibility path and add a minimum-version CI job. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** Proportionate to file type, subject to repository-wide documentation findings.
- **Correctness confidence:** Reduced by an open verified finding.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: ProjectCheck(1), ProjectStateDatabase(12), artifact_digests(2), check_project_state(4), close(11), create_project_backup(5), integrity_check(1), migrate_project(4), project_gc(3), record_migration(1). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Execute the restore contract on Python 3.11.0 and 3.11.4 (or the newly declared minimum).
- **Related follow-up:** COR-001
- **Final audit status:** **Audited — complete**
