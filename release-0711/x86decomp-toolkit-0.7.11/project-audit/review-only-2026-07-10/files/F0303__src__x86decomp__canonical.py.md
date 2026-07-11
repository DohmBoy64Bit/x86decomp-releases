# Per-file audit: `src/x86decomp/canonical.py`

## A. File Identity

- **Inventory ID:** `F0303`
- **Relative path:** `src/x86decomp/canonical.py`
- **SHA-256:** `8c3ec3a4bc45c53e198249f12b84117c49be63df96160f0c552e82c570e26ef1`
- **File size:** 11870 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Unified canonical CLI surface that merges the governance, reconstruction, native,
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `scripts/sync-release-contracts.py`, `src/x86decomp/cli.py`, `tests/test_docstring_audit.py`, `tests/test_release_contract.py`
- **Key imports/dependencies:** `__future__`, `argparse`, `collections`, `functools`, `subprocess`, `typing`, `x86decomp.assembly.cli`, `x86decomp.cli_utils`, `x86decomp.contracts`, `x86decomp.governance.cli`, `x86decomp.native.cli`, `x86decomp.reconstruction.cli`

## B. Functional Summary

Unified canonical CLI surface that merges the governance, reconstruction, native, Major symbols: canonical_routes, canonical_groups, command_catalog, register_canonical_commands, dispatch, build_parser, main. No side-effect-relevant call matched the audit scanner’s rule set.

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 12/12. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: command_catalog (branches=8, AST nodes=155), _route_owner (branches=5, AST nodes=154), register_canonical_commands (branches=4, AST nodes=224), canonical_routes (branches=3, AST nodes=157), _leaf_parsers (branches=2, AST nodes=109).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Boilerplate/duplication indicator: 1 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: build_parser(19), canonical_groups(9), canonical_routes(9), command_catalog(1), dispatch(6), main(57), register_canonical_commands(1). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-002.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 4: src/x86decomp/canonical.py:main, src/x86decomp/native/cli.py:main. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-002 | Medium | Verified | 166 root commands, 405 parser nodes, 239 canonical routes | Detailed command documentation covers only a small fraction of the live command surface | Runtime parser introspection found help text for all 405 parser nodes. Cross-checking every command and route against Markdown code blocks and prose found explicit examples for 23/166 root commands, mentions for 31/405 parser nodes, and examples for 7/239 canonical routes. | New users must infer workflows from --help and source; safety, output, and error contracts are not consistently explained outside the executable. | Generate or maintain a full command reference from parser metadata, augmented with human-authored examples, outputs, error behavior, and safety notes. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: build_parser(19), canonical_groups(9), canonical_routes(9), command_catalog(1), dispatch(6), main(57), register_canonical_commands(1). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Re-run the command-documentation matrix and manually execute every published example in a disposable workspace.
- **Related follow-up:** DOC-002
- **Final audit status:** **Audited — complete**
