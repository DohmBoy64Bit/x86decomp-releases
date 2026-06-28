# Verification record — x86decomp comprehensive test suite 0.3.0

## Test target

The full harness was executed against a clean extraction of `x86decomp-toolkit-0.3.0.zip`, not against a modified working directory.

## Harness self-tests

```text
17 passed
0 failed
0 skipped
```

The self-tests cover configuration round trips, strict exit behavior, adapter detection, no-prompt behavior for installed adapters, custom-path prompting for missing adapters, custom Python interpreter resolution, non-interactive unresolved behavior, symlink/argv0 preservation, safe ZIP/TAR extraction, traversal/link rejection, installer command construction, inventory drift, function coverage correlation, JUnit parsing, process logging, reports, and CLI behavior.

## Complete toolkit run

```text
120 PASS
0 FAIL
0 ERROR
6 BLOCKED
```

The run used non-strict mode only because six external installations were unavailable in the execution environment. Strict mode would return exit code `2` for the same blocked set.

Blocked integrations:

- DynamoRIO
- Ghidra
- LIEF
- LLVM `llvm-readobj`
- user-owned MSVC toolchain
- objdiff CLI

They were explicitly listed in `adapters.json`, `results.json`, Markdown/HTML reports, and JSONL events. They were not skipped or counted as passing.

## Surface and coverage results

```text
45 Python modules inventoried
394/394 function and method bodies executed
72/72 CLI commands parse-tested
38/38 JSON Schemas inventoried and meta-validated
3/3 Ghidra Java scripts syntax-validated
75 toolkit + supplemental pytest tests passed
0 pytest tests skipped
statement coverage: 75.87738146397365%
branch coverage: 52.03313253012048%
```

The configured floors were 70% statements and 50% branches.

## Packaging verification

- Source package byte-compilation passed.
- Wheel and source distribution built successfully.
- Wheel installed into a separate virtual environment.
- Installed CLI help and packaged feature catalog were accessible.
- Packaged harness self-tests passed when dependencies were provided from the controlled test environment.

## Important interpretation

Executing every function body does not prove correctness for every possible input or every path. This suite provides a no-omission surface contract plus targeted regressions, branch/statement coverage, schemas, artifact integrity, package installation, and live external-tool probes. New behavior still requires new targeted assertions.
