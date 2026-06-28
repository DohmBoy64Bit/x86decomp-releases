# Comprehensive test plan for x86decomp-toolkit 0.3.0

## Release surface

The pinned 0.3.0 contract contains:

- 45 Python modules;
- 394 defined functions and methods, including private/internal helpers;
- 72 CLI subcommands;
- 38 JSON Schemas;
- 3 Ghidra Java scripts;
- matching and functional workflow state machines;
- 29 external or Python adapter contracts.

The exact names live in `src/x86decomp_testkit/data/feature_catalog.json`.

## Test phases

### 1. Adapter inventory

Every adapter is detected and versioned. Installed adapters are never prompted for. Missing adapters enter the custom-path flow and then, if consented, an installer flow. Unresolved adapters create explicit blocked live tests.

### 2. Surface drift

Dynamic discovery must exactly match the pinned catalog. Uncataloged additions and stale catalog entries fail independently for commands, modules, functions, schemas, Ghidra scripts, and adapters.

### 3. Structural integrity

- source SHA-256 manifest;
- JSON Schema meta-validation;
- Ghidra Java syntax;
- skill YAML frontmatter;
- Python byte compilation;
- toolkit's own contract validator.

### 4. CLI parser surface

Each of the 72 commands runs as a separate process with `--help`. This catches parser construction errors, missing imports, argument conflicts, and command removal.

### 5. Native and supplemental behavioral regression

The toolkit's own tests run together with supplemental tests that exercise API areas not reached by the native suite. The current combined suite exercises all 394 function/method bodies.

### 6. No-skip gate

Pytest emits JUnit XML. Any skipped testcase fails the gate. External dependencies are handled as blocked adapter tests rather than pytest skips.

### 7. Coverage

- all 394 function/method bodies execute at least one direct line;
- statement floor defaults to 70%;
- branch floor defaults to 50%;
- full JSON/XML/HTML coverage reports are retained.

### 8. Packaging

- build exactly one wheel and one source distribution;
- create a fresh virtual environment;
- install the wheel without source-tree imports;
- execute installed `x86decomp --help`.

### 9. Adapter live tests

Resolved adapters are used, not merely version-checked. Compilers compile fixtures, `lld-link` links a PE, Ghidra runs exporters, DynamoRIO runs drcov, and Python libraries import.

### 10. Harness self-verification

The harness's own tests run in every full run and must have zero skips.

## Result semantics

- `PASS`: the declared bounded contract executed successfully.
- `FAIL`: the test executed and contradicted its expectation.
- `ERROR`: the harness could not execute the test due to an unexpected internal problem.
- `BLOCKED`: a declared external prerequisite is unresolved. This is never equivalent to pass.

Strict mode treats every blocked result as a non-zero release gate.
