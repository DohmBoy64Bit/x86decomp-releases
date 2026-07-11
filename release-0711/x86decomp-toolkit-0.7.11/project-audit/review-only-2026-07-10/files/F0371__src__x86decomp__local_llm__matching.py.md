# Per-file audit: `src/x86decomp/local_llm/matching.py`

## A. File Identity

- **Inventory ID:** `F0371`
- **Relative path:** `src/x86decomp/local_llm/matching.py`
- **SHA-256:** `f8ded8441592fbbc8705df6c0b8c087b58ff30edc437782d371c24ce7132a5f6`
- **File size:** 19052 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Local-model C generation and deterministic byte-match verification loop.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/local_llm/__init__.py`, `src/x86decomp/native/cli.py`, `src/x86decomp/native/closed_loop.py`, `src/x86decomp/native/hybrid_composer.py`, `src/x86decomp/reconstruction/acceleration.py`, `tests/native/test_inventory_and_loops.py`, `tests/native/test_pe_hybrid.py`, `tests/native/test_slots_matching.py`
- **Key imports/dependencies:** `.profiles`, `.prompts`, `.transport`, `__future__`, `json`, `pathlib`, `re`, `shutil`, `typing`, `x86decomp.assembly.relocations`, `x86decomp.coff`, `x86decomp.compiler`, `x86decomp.contracts`, `x86decomp.diffing`, `x86decomp.errors`, `x86decomp.util`

## B. Functional Summary

Local-model C generation and deterministic byte-match verification loop. Major symbols: generate_candidate, run_match_loop, verify_match_report. Static analysis recorded 8 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 8 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: resolved.parent.mkdir×1, resolved.mkdir×1, output.parent.mkdir×1, output.write_text×1, attempts_root.mkdir×1, shutil.rmtree×1, attempt_root.mkdir×1, source_path.write_text×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 7/7. 2 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: verify_match_report (branches=21, AST nodes=474), _parse_candidate (branches=19, AST nodes=377), run_match_loop (branches=13, AST nodes=1316), _prepare_output (branches=3, AST nodes=86), generate_candidate (branches=2, AST nodes=235).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

8 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: generate_candidate(4), run_match_loop(3), verify_match_report(4). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001.

## K. Redundancy and Consolidation Opportunities

No exact normalized-function duplicate involving this file was identified by the AST scan.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: generate_candidate(4), run_match_loop(3), verify_match_report(4). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.
- **Related follow-up:** DOC-001
- **Final audit status:** **Audited — complete**
