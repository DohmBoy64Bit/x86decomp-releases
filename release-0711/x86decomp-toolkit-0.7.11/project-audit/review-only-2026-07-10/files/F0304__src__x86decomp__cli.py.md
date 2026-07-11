# Per-file audit: `src/x86decomp/cli.py`

## A. File Identity

- **Inventory ID:** `F0304`
- **Relative path:** `src/x86decomp/cli.py`
- **SHA-256:** `12b849e573b008c7a615a679b4f119f714ff037847afb86b4ca442a767ba68ea`
- **File size:** 55097 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Command-line interface for all toolkit architecture components.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `scripts/sync-release-contracts.py`, `src/x86decomp/__main__.py`, `src/x86decomp/canonical.py`, `test-suite/src/x86decomp_testkit/__main__.py`, `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`, `tests/assembly/test_pipeline_cli_schemas.py`, `tests/governance/test_governance_cli_schemas.py`, `tests/native/test_cli_schemas.py`
- **Key imports/dependencies:** `.abi`, `.analysis_db`, `.angr_backend`, `.artifacts`, `.benchmarks`, `.canonical`, `.cli_utils`, `.coff`, `.coff_archive`, `.compiler`, `.compiler_lab`, `.compiler_worker`, `.content_store`, `.convergence`, `.cpp_recovery`, `.decompme`, `.diffing`, `.disassembly`, `.dynamic`, `.dynamorio`, `.evidence`, `.exe_diff`, `.ghidra`, `.ground_truth`, `.harness_generator`, `.image_match`, `.integration`, `.linker_layout`, `.linker_reconstruction`, `.mcp`

## B. Functional Summary

Command-line interface for all toolkit architecture components. Major symbols: main. Static analysis recorded 2 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 2 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: args.output.parent.mkdir×1, args.output.write_bytes×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 8/8. 3 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: _run (branches=134, AST nodes=3578), _build_parser (branches=10, AST nodes=5281), _mcp_client (branches=5, AST nodes=99), _json_object (branches=1, AST nodes=47), main (branches=0, AST nodes=37). 129 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship. Boilerplate/duplication indicator: 2 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

_run has 134 branch/compound nodes; treat this as a profiling and maintainability target, not a confirmed performance defect.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

2 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: main(57). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001, DOC-002, UX-001.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 2: src/x86decomp/assembly/cli.py:_int, src/x86decomp/cli.py:_int. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 5: src/x86decomp/cli.py:_path, test-suite/src/x86decomp_testkit/cli.py:_path. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |
| DOC-002 | Medium | Verified | 166 root commands, 405 parser nodes, 239 canonical routes | Detailed command documentation covers only a small fraction of the live command surface | Runtime parser introspection found help text for all 405 parser nodes. Cross-checking every command and route against Markdown code blocks and prose found explicit examples for 23/166 root commands, mentions for 31/405 parser nodes, and examples for 7/239 canonical routes. | New users must infer workflows from --help and source; safety, output, and error contracts are not consistently explained outside the executable. | Generate or maintain a full command reference from parser metadata, augmented with human-authored examples, outputs, error behavior, and safety notes. | Open |
| UX-001 | Low | Verified | x86decomp root parser; __version__ | Primary CLI exposes no version-reporting option | x86decomp --version exits 2 as an unrecognized argument and prints the full root usage; the package exports version 0.7.11. | Users and automation cannot query the installed executable version without importing Python metadata or package internals. | Add argparse’s version action and test its exact stdout and zero exit status. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: main(57). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.; Re-run the command-documentation matrix and manually execute every published example in a disposable workspace.; Run installed wheel entry point with --version on supported platforms.
- **Related follow-up:** DOC-001, DOC-002, UX-001
- **Final audit status:** **Audited — complete**
