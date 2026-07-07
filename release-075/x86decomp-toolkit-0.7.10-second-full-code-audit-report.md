# x86decomp-toolkit 0.7.10 second full code audit report

## Executive summary

This audit used the current 0.7.10 audit-fix release bundle as the source of truth:

- Bundle: `x86decomp-toolkit-0.7.10-audit-fix-release-bundle.zip`
- Bundle SHA-256: `413f37a9d5c2ff36ffece96cff78a6d9154a21d5bbfce195b9b9e0115ca970b2`
- Clean extraction root: `x86decomp-toolkit-0.7.10`

I read and hashed every file in the extracted bundle before judging issues. The bundle contains **452 files** total. Of those, **396 are code/config candidate files** by extension or role. The project source manifest verifier separately covers **446 root source files** and **63 test-suite source files**, because the release manifest intentionally ignores build outputs such as `dist/` artifacts and manifest files.

The audit did **not** produce an all-clear. The most important findings are real runtime command failures in the 0.7.10 command surface that are missed by Python compilation, import checks, source hashes, and the selected existing tests:

1. `x86decomp plugin validate ...` crashes with `NameError: name 'json' is not defined`.
2. `x86decomp llm prompt ...` crashes with `NameError: name 'writeparse_json_arg' is not defined`.
3. The production tree fails `pyflakes` with eight findings, including the two command-breaking defects above.

No source edits were made in this audit. This report is an evidence report only.

## Audit coverage

### File inventory

| Category | Count |
|---|---:|
| Total files read and SHA-256 hashed from clean extraction | 452 |
| Code/config candidate files reviewed | 396 |
| Python files parsed with `ast.parse` | 211 |
| JSON files parsed | 123 |
| TOML files parsed | 2 |
| YAML files parsed | 1 |
| Java files parsed with `javalang` | 3 |
| Shell scripts checked with `bash -n` | 3 |

Extension counts from the clean extraction:

| Extension/type | Count |
|---|---:|
| `.py` | 211 |
| `.json` | 123 |
| `.md` | 39 |
| `.c` | 33 |
| `.cpp` | 16 |
| `[noext]` | 5 |
| `.bin` | 3 |
| `.java` | 3 |
| `.sh` | 3 |
| `.cfg` | 2 |
| `.gz` | 2 |
| `.in` | 2 |
| `.sha256` | 2 |
| `.toml` | 2 |
| `.txt` | 2 |
| `.whl` | 2 |
| `.ps1` | 1 |
| `.yml` | 1 |

### Verification commands run

| Check | Result |
|---|---|
| `python -m compileall -q src test-suite/src tests scripts` | PASS |
| `scripts/source_hashes.py verify --root .` | PASS: root `446/446`, test-suite `63/63` |
| `scripts/validate-contracts.py` after installing declared dev dependency `javalang>=0.13,<1` | PASS |
| Java syntax parse with `javalang` over `ghidra_scripts/*.java` | PASS: `3/3` |
| `bash -n` over shell scripts | PASS: `3/3` |
| Import walk over `x86decomp` and `x86decomp_testkit`, excluding `__main__` modules | PASS: `145` modules imported, `0` import errors |
| Pytest collection over root tests, test-suite tests, and toolkit contract tests | PASS: `241` tests collected |
| Selected regression tests: `test_audit_fixes.py`, `test_release_contract.py`, `test_docstring_audit.py`, `test_documentation.py` | PASS: `20` tests |
| Standalone `test-suite/tests/test_inventory_reports_process.py` | PASS: `4` tests |
| `pyflakes src scripts test-suite/src` | FAIL: 8 production/static findings |

I am **not** claiming that the entire monolithic test suite passed in this audit. The audit used collection, syntax, source-hash, static-analysis, command probes, selected regression tests, and targeted direct evidence.

## Confirmed issues

### CR-0710-001 — `plugin validate` crashes because `governance/cli.py` uses `json` without importing it

**Severity:** High  
**Type:** Runtime command failure, robust error handling failure, test coverage gap  
**Files/lines:** `src/x86decomp/governance/cli.py:212`, `src/x86decomp/governance/cli.py:232`

**What I found**

`pyflakes` reports:

```text
src/x86decomp/governance/cli.py:212:66: undefined name 'json'
src/x86decomp/governance/cli.py:232:15: undefined name 'json'
```

The code at line 212 dispatches the governance plugin validation command using `json.loads(...)`, but `json` is not imported in the module. The error-handling path at line 232 also tries to call `json.dumps(...)` without importing `json`.

I confirmed the runtime failure through the canonical root command:

```text
PYTHONPATH=src python -m x86decomp.cli plugin --project /tmp/probes validate /tmp/probes/plugin.json
```

Observed result:

```text
exit=1
NameError: name 'json' is not defined. Did you forget to import 'json'?
```

**Why this is wrong or needs modification**

`plugin validate` is a canonical command route. It should return a structured validation result for a plugin manifest. Instead, it crashes with an uncaught `NameError`, so the command does not satisfy the toolkit’s JSON-error-output and no-fabricated-success rules. The same missing import also weakens the module’s generic error handler: if a handled `ContractError`, `KeyError`, `OSError`, or `ValueError` occurs, the handler itself can crash while trying to serialize the error.

**How I would modify it**

Add `import json` near the other imports in `src/x86decomp/governance/cli.py`, or better, use the already shared `load_json` / JSON helper style consistently. Then add a regression test that exercises both:

1. `x86decomp plugin validate <manifest>` through the root canonical CLI.
2. A failure path that proves the CLI returns structured JSON instead of raising a traceback.

The fix is small, but it must be tested through the actual command surface, not only by importing the module or building the parser.

---

### CR-0710-002 — `llm prompt`, `llm generate --report`, and `llm cpp-generate --report` crash because `reconstruction/cli.py` calls undefined `writeparse_json_arg`

**Severity:** High  
**Type:** Runtime command failure, command implementation defect, test coverage gap  
**Files/lines:** `src/x86decomp/reconstruction/cli.py:368`, `src/x86decomp/reconstruction/cli.py:371`, `src/x86decomp/reconstruction/cli.py:376`

**What I found**

`pyflakes` reports:

```text
src/x86decomp/reconstruction/cli.py:368:69: undefined name 'writeparse_json_arg'
src/x86decomp/reconstruction/cli.py:371:29: undefined name 'writeparse_json_arg'
src/x86decomp/reconstruction/cli.py:376:29: undefined name 'writeparse_json_arg'
```

The typo appears in these paths:

- `llm prompt`
- `llm generate --report`
- `llm cpp-generate --report`

I confirmed the runtime failure through the root canonical command with a valid minimal local-LLM job:

```text
PYTHONPATH=src python -m x86decomp.cli llm --project /tmp/probes prompt /tmp/probes/job.json /tmp/probes/prompt.json
```

Observed result:

```text
exit=1
NameError: name 'writeparse_json_arg' is not defined. Did you mean: 'parse_json_arg'?
```

No prompt output file was created.

**Why this is wrong or needs modification**

`llm prompt` is supposed to materialize the deterministic prompt without contacting a model. That is an important safety boundary because it lets analysts inspect the exact prompt before model use. The current route computes the prompt record, then crashes before writing it. The `generate --report` and `cpp-generate --report` report-writing paths have the same typo, so report emission is also broken for those commands.

This is not a theoretical lint-only issue. It is a directly reproduced command failure.

**How I would modify it**

Replace `writeparse_json_arg(...)` with the correct JSON writer, most likely `x86decomp.util.write_json(...)`, and import it explicitly:

```python
from x86decomp.util import write_json
```

Then change the three call sites to:

```python
write_json(Path(args.output), record)
write_json(Path(args.report), result)
```

Add command-level tests for:

1. `x86decomp llm prompt <job> <output>` creates a deterministic prompt JSON file.
2. `x86decomp llm generate ... --report <report>` writes a report in the mocked/loopback local-model test path.
3. `x86decomp llm cpp-generate ... --report <report>` writes a report or has a bounded mocked test equivalent.

---

### CR-0710-003 — `reconstruction/cli.py` error handling also references missing `json`

**Severity:** High  
**Type:** Robust error handling failure  
**File/line:** `src/x86decomp/reconstruction/cli.py:454`

**What I found**

`pyflakes` reports:

```text
src/x86decomp/reconstruction/cli.py:454:15: undefined name 'json'
```

The `main()` exception handler tries to print a structured JSON error, but `json` is not imported. As in the governance CLI, this means a handled exception can be replaced by a new `NameError` inside the handler.

**Why this is wrong or needs modification**

The CLI contract depends on predictable structured error output. A crash inside the exception handler prevents downstream scripts and the test-suite harness from distinguishing expected `ContractError` failures from internal crashes.

**How I would modify it**

Import `json`, or route all CLI JSON output through `emit_json` and a shared error-emission helper. Then add a regression test that intentionally triggers a `ContractError` in `x86decomp.reconstruction.cli.main()` and asserts that the process returns status `2` with a JSON error object.

---

### CR-0710-004 — The release lacks a static-analysis gate that would have caught the command-breaking undefined names

**Severity:** Medium  
**Type:** Release-gate/test-suite gap  
**Evidence:** `pyflakes src scripts test-suite/src` fails with 8 findings while compile/import/source-hash checks pass

**What I found**

The following checks passed even though command-breaking undefined names are present:

- Python compilation with `compileall`
- Full package import walk, excluding executable `__main__` modules
- Source hash verification
- Existing selected release-contract and audit-fix tests

`pyflakes` immediately found the production failures:

```text
src/x86decomp/target_pack.py:371:5: local variable 'project' is assigned to but never used
src/x86decomp/governance/cli.py:212:66: undefined name 'json'
src/x86decomp/governance/cli.py:232:15: undefined name 'json'
src/x86decomp/reconstruction/acceleration.py:457:5: local variable 'db' is assigned to but never used
src/x86decomp/reconstruction/cli.py:368:69: undefined name 'writeparse_json_arg'
src/x86decomp/reconstruction/cli.py:371:29: undefined name 'writeparse_json_arg'
src/x86decomp/reconstruction/cli.py:376:29: undefined name 'writeparse_json_arg'
src/x86decomp/reconstruction/cli.py:454:15: undefined name 'json'
```

**Why this is wrong or needs modification**

The prior audit-fix release explicitly removed unused imports and claimed a custom import-use check. However, a basic undefined-name/static-lint gate was not strong enough to catch new undefined names. Because the failed names live in command dispatch branches, import checks do not execute them.

**How I would modify it**

Add a static-analysis step to the release gates. Either:

- add `pyflakes` or `ruff check --select F` to `scripts/validate-contracts.py`, or
- add a dedicated `tests/test_static_lint.py` that runs the same check over `src`, `scripts`, and `test-suite/src`.

The gate should fail on undefined names in production code. The unused-local findings can be configured as warnings if desired, but undefined names should be hard failures.

---

### CR-0710-005 — Two production dead assignments remain

**Severity:** Low  
**Type:** Dead code / cleanup  
**Files/lines:** `src/x86decomp/target_pack.py:371`, `src/x86decomp/reconstruction/acceleration.py:457`

**What I found**

`pyflakes` reports:

```text
src/x86decomp/target_pack.py:371:5: local variable 'project' is assigned to but never used
src/x86decomp/reconstruction/acceleration.py:457:5: local variable 'db' is assigned to but never used
```

In `target_pack.py`, `initialize_project(...)` is assigned to `project` but that variable is never read. In `reconstruction/acceleration.py`, `db = project.resolve()/"reconstruction.sqlite"` is computed but never read.

**Why this is wrong or needs modification**

These do not appear to break runtime behavior. They are still real dead assignments. They make review harder because a reader expects the assigned values to matter. They also reduce confidence in the prior “unused code removed” claim.

**How I would modify it**

- In `target_pack.py`, either drop the assignment and call `initialize_project(...)` for its side effects, or use the returned project object if it contains needed state.
- In `reconstruction/acceleration.py`, remove `db` unless it is meant to be included in the observation scan.

Add a static lint test so this does not drift again.

---

### CR-0710-006 — Three Python example files are outside the claimed 100% module-docstring coverage

**Severity:** Low  
**Type:** Documentation/audit-scope drift  
**Files:**

- `examples/integration/candidate.py`
- `examples/integration/candidate_mismatch.py`
- `examples/integration/target.py`

**What I found**

The extracted bundle contains **211 Python files**. AST inspection found module docstrings in **208/211**. The three missing files are Python example/integration fixtures. Classes and functions are fully covered where present: **160/160 classes** and **1442/1442 functions/methods** have docstrings.

**Why this is wrong or needs modification**

This is not a runtime defect. It is a documentation/audit-scope mismatch. The previous docstring release evidence counted 208 Python modules, which appears to exclude these examples. Since the project rules and the user request treat every code file as in scope, these example modules should either receive short module docstrings or the docstring audit should explicitly document why example scripts are excluded.

**How I would modify it**

Add concise module docstrings to the three example files. For example, describe that `candidate.py` and `target.py` are deterministic integration-command fixtures and that `candidate_mismatch.py` intentionally produces a mismatch for negative evidence tests. Then update the docstring audit to report 211/211 Python modules if examples remain in scope.

---

### CR-0710-007 — Duplicate binary-reader/helper logic remains across PE/COFF parsers

**Severity:** Low  
**Type:** Duplicated code / maintainability  
**Files/examples:**

- `src/x86decomp/coff.py:_Reader.require`
- `src/x86decomp/pe32.py:_Reader.require`
- `src/x86decomp/coff.py:_Reader.unpack`
- `src/x86decomp/pe32.py:_Reader.unpack`
- duplicated little-endian helper closures in `src/x86decomp/pe.py` and `src/x86decomp/pe32.py`

**What I found**

Normalized AST duplicate-body detection found repeated non-trivial parser helper bodies, including duplicate `_Reader.require` and `_Reader.unpack` implementations across COFF and PE32 parsing code.

**Why this is wrong or needs modification**

This is not currently a runtime bug. It is a real redundancy risk. These helpers perform bounds checks and structured unpacking. If one parser gets a bounds-check or diagnostics improvement and the other does not, the parsers can diverge in behavior and error quality.

**How I would modify it**

Move the common reader functionality into a small shared internal module, for example `x86decomp.binary_reader`, with methods for bounded `require`, `unpack`, and little-endian integer reads. Then update PE32/PE64/COFF parsers to use it while preserving their format-specific error messages. Add parser regression tests for truncated input in each format so centralization does not weaken diagnostics.

---

### CR-0710-008 — Several action-named reconstruction commands are explicitly plan-only, but the CLI contract should make that obvious

**Severity:** Low  
**Type:** Command semantics / user-facing clarity  
**Files/examples:** `src/x86decomp/reconstruction/acceleration.py`

**What I found**

Some commands intentionally return plans rather than performing the action their name may suggest. Examples:

- `type_propagate(...)` returns a `type_propagation_plan` with `source_edits_performed: False` and `claim: "plan_only_no_silent_overwrite"`.
- `candidate_search(...)` returns `claim: "ordered_candidate_search_plan_only"`.
- `triage_next(...)` returns `claim: "planning_only"`.

**Why this is wrong or needs modification**

This is not a placeholder by itself; the functions are honest about plan-only behavior in their returned payloads. The concern is command-contract clarity. A user invoking `type propagate` may reasonably expect propagation to be applied, not only planned, unless the help text and documentation make the plan-only boundary explicit.

**How I would modify it**

Keep the conservative no-silent-edit behavior, but make the command contract explicit in CLI help and docs. Options:

1. Rename or alias these commands to `type propagation-plan`, `candidate search-plan`, etc., while preserving compatibility aliases.
2. Add help text that says “emit plan only; no source edits performed.”
3. Add tests that assert the plan-only claim is present and documented.

---

### CR-0710-009 — `validate-contracts.py` is correct with declared dev dependencies installed, but the missing-dependency error path is not robust

**Severity:** Low  
**Type:** Tooling error-message robustness  
**File:** `scripts/validate-contracts.py`

**What I found**

Before installing `javalang`, `scripts/validate-contracts.py` failed with a raw `ModuleNotFoundError`. After installing the declared dev dependency `javalang>=0.13,<1`, the same script passed:

```text
current contracts, examples, Java syntax, schemas, skill, and release shape passed
```

The dependency itself is declared in `pyproject.toml` under `dev`, so this is not dependency drift.

**Why this is wrong or needs modification**

A release validation script should give a clear operator-facing error when a declared validation dependency is missing. A raw traceback is less useful and can be mistaken for a source failure.

**How I would modify it**

Catch `ModuleNotFoundError` around the `javalang` import and raise or print a clear validation error such as: `missing validation dependency: install the dev extra that provides javalang>=0.13,<1`. Keep the process nonzero.

## Reviewed items that did not become confirmed issues

### Canonical command taxonomy

The command catalog still reports:

- Root commands: **166**
- Canonical groups: **59**
- Canonical routes: **239**

I did not find duplicate canonical routes in the command catalog. The retained flat compatibility aliases are marked explicitly in tests. `project-check` remains separate because it is not byte-for-byte equivalent to the assembly project check route.

### Intentional mirrored corpus files

The audit found duplicate file hashes for mirrored corpus files under both:

- `corpus/ground_truth_sources/...`
- `src/x86decomp/corpus/ground_truth_sources/...`

This is expected packaging/mirroring behavior, and the files are covered by the source hash manifest. I am not treating those mirrored corpus duplicates as dead or redundant code.

### `innerHTML`, `eval`, `NotImplementedError`, and placeholder scans

Text scans found `innerHTML` only in the audit-fix report and tests that assert the UI does not use it. I did not find a production `innerHTML` use.

`eval` scan hits were `solver.eval(...)` calls in the angr backend, not Python `eval(...)` execution.

`NotImplementedError` hits were in release-contract tests that scan for forbidden placeholder implementations, not production placeholder code.

`TODO`/`FIXME` text hits were policy/prompts/tests that reject unfinished markers, not implementation TODO branches.

### Shell command execution

I did not find `shell=True` in the scanned code/config files. The shell scripts parsed successfully with `bash -n`.

### Java/Ghidra scripts

All three Java scripts parsed with `javalang` after installing the declared validation dependency. No Java syntax issue was confirmed.

## Recommended fix order

1. Fix `governance/cli.py` missing `json` import and add command-level `plugin validate` tests.
2. Fix `reconstruction/cli.py` missing `json` import and `writeparse_json_arg` typo; add command-level `llm prompt` and report-writing tests.
3. Add a static undefined-name gate using `pyflakes` or `ruff F` over production code.
4. Remove the two dead local assignments.
5. Add docstrings to the three Python example modules or explicitly include/exclude examples in docstring audit scope.
6. Consider centralizing duplicated parser reader helpers.
7. Clarify plan-only command semantics in CLI help and docs.
8. Improve `validate-contracts.py` missing-dependency diagnostics.

## Final assessment

0.7.10 is improved over 0.7.9, but it is not clean. The source manifests, command catalog, docstring coverage for production/test modules, Java syntax, JSON/TOML/YAML parsing, shell syntax, import walk, and selected release tests are healthy. However, the confirmed undefined-name failures in governance and reconstruction CLI dispatch are release-blocking for a proper 0.7.11 fix transaction because they break real canonical commands.
