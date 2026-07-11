# Per-file audit: `tests/assembly/test_pipeline_cli_schemas.py`

## A. File Identity

- **Inventory ID:** `F0496`
- **Relative path:** `tests/assembly/test_pipeline_cli_schemas.py`
- **SHA-256:** `7e3b3f40f5a85f6a5c3591eb375fa5a045a24f5de688e143fcaf55fe13ea39e8`
- **File size:** 9179 bytes
- **Language/format:** Python source
- **Classification:** Test code
- **Apparent responsibility:** Executable regression tests for the behavior indicated by the filename and test symbols.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** No direct relationship established beyond directory and manifest context.
- **Key imports/dependencies:** `__future__`, `importlib.util`, `json`, `jsonschema`, `pathlib`, `pytest`, `x86decomp.assembly.cli`, `x86decomp.assembly.pipeline`, `x86decomp.assembly.relocations`, `x86decomp.assembly.store`, `x86decomp.cli`, `x86decomp.contracts`, `x86decomp.errors`, `x86decomp.hybrid`

## B. Functional Summary

Executable regression tests for the behavior indicated by the filename and test symbols. Major symbols: test_pipeline_all_three_formats_and_durable_reports, test_assembly_project_cli_and_all_leaf_help, test_main_cli_exposes_assembly_capabilities, test_assembly_schemas_and_symbol_map_contracts, test_store_keeps_all_prior_schema_layers, test_pipeline_persists_relocation_evidence, test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes, test_failed_batch_is_recorded_durably, _leaf_commands.walk. Static analysis recorded 5 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 5 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: raw.write_bytes×1, path.write_text×1, artifact.mkdir×1, manifest.write_text×1, connection.execute×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 12/12. 3 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: test_pipeline_all_three_formats_and_durable_reports (branches=5, AST nodes=248), _leaf_commands (branches=5, AST nodes=106), _leaf_commands.walk (branches=5, AST nodes=87), test_pipeline_persists_relocation_evidence (branches=3, AST nodes=149), test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes (branches=2, AST nodes=246).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship. Boilerplate/duplication indicator: 3 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

5 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Executed in the exact inventory: 8 collected test(s), all passing.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 44: tests/assembly/test_annotation_materialize.py:_capstone_available, tests/assembly/test_pipeline_cli_schemas.py:_capstone_available. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 45: tests/assembly/test_pipeline_cli_schemas.py:_leaf_commands, tests/native/test_cli_schemas.py:_leaf_commands. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 46: tests/assembly/test_pipeline_cli_schemas.py:_leaf_commands.walk, tests/native/test_cli_schemas.py:_leaf_commands.walk. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Executed in the exact inventory: 8 collected test(s), all passing.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.
- **Related follow-up:** DOC-001
- **Final audit status:** **Audited — complete**
