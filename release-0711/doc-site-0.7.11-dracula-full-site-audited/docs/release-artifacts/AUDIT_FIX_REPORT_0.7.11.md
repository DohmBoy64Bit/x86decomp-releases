# x86decomp-toolkit 0.7.11 second-audit fix report

## Source of truth

This release was derived from `x86decomp-toolkit-0.7.10-audit-fix-release-bundle.zip` and fixes the concrete findings in the second 0.7.10 audit report. It is a forward release transaction; it does not rewrite the sealed 0.7.10 artifacts.

## Issue-by-issue fixes

### CR-0710-001 — plugin validate missing json import

**Fix:** Fixed by importing json in governance/cli.py and adding a root command regression that validates a plugin manifest without NameError.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-002 — llm prompt/generate report undefined writeparse_json_arg

**Fix:** Fixed by importing write_json and replacing all typo call sites; root command tests cover llm prompt, llm generate --report, and llm cpp-generate --report.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-003 — reconstruction CLI error handler missing json

**Fix:** Fixed by importing json and adding a process-level reconstruction CLI error-handler test that parses stderr as JSON.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-004 — missing static-analysis gate

**Fix:** Fixed by adding pyflakes to dev dependencies and scripts/validate-contracts.py; pyflakes over src, scripts, and test-suite/src is now a hard gate.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-005 — two production dead assignments

**Fix:** Fixed by removing unused project assignment in target_pack.py and unused db assignment in reconstruction/acceleration.py.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-006 — three example Python files outside docstring coverage

**Fix:** Fixed by adding module docstrings to examples/integration/candidate.py, candidate_mismatch.py, and target.py; all Python files parse with module docstrings.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-007 — duplicate PE/COFF binary-reader helper logic

**Fix:** Fixed by adding x86decomp.binary_reader.BinaryReader and wiring COFF/PE32/PE32+ parser helpers through the shared bounded reader methods.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-008 — plan-only command contract clarity

**Fix:** Fixed by updating candidate search, type propagate, and triage next CLI descriptions plus docs/command reference/architecture notes; a regression asserts help text exposes the plan-only boundary.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

### CR-0710-009 — validate-contracts missing javalang diagnostic

**Fix:** Fixed by catching ModuleNotFoundError and raising an explicit missing-dev-extra message; a regression simulates the missing dependency.

**Verification:** source inspection plus targeted regression tests and static validation are recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.

## Additional hardening completed

- Added command-level coverage for `llm cpp-generate --report`, because the audit identified the same broken report writer path as `llm generate --report`.
- Added `pyflakes>=3.3,<4` to toolkit and test-suite dev extras so the static lint gate is installable from declared release dependencies.
- Updated the four architecture artifacts to include the shared bounded PE/COFF binary-reader boundary and static lint gate.
- Regenerated the feature catalog and public/command surface contracts from the live parser and inventory.

## Verification summary

- Files read and hashed before packaging: 450
- Code/config candidate files reviewed by inventory: 439
- Python files parsed from the full release tree, including examples: 213
- Python parse errors: 0
- Module docstrings across all Python files: 213/213
- Class docstrings across all Python files: 160/160
- Function/method docstrings across all Python files: 1451/1451
- `python -m compileall -q src test-suite/src tests scripts`: PASS
- `pyflakes src scripts test-suite/src`: PASS
- `scripts/validate-contracts.py`: PASS
- Toolkit and test-suite wheels/sdists: PASS
- Clean wheel install and `pip check`: PASS
- Final extracted ZIP source-manifest verification: PASS; root 449/449 and test-suite 63/63
- Targeted second-audit regression tests: 7/7 PASS
- Root toolkit tests were run file-by-file in this sandbox and passed for the files recorded in the verification JSON.
- Test-suite/self-test/toolkit-test files were run file-by-file in this sandbox and passed for the files recorded in the verification JSON.

## Not claimed

- I am not claiming that a single monolithic `pytest tests` invocation completed in this sandbox; repeated all-at-once/sequential loops timed out despite the same files passing when run individually.
- I am not claiming live LM Studio/Ollama/llama.cpp/vLLM/LocalAI model quality or availability tests.
