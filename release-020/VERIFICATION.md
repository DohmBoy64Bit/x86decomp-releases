# Verification record — x86decomp-toolkit 0.2.0

This record distinguishes checks actually executed in the release environment from
integration checks that require software or target artifacts not present there. It is
not a claim that arbitrary binaries can be decompiled correctly or proven equivalent.

## Release environment

- Date: 2026-06-27/28 UTC.
- Host: Linux x86-64.
- Python: 3.13.5.
- OpenJDK/Javac: 21.0.10.
- GCC: 14.2.0.
- `lld-link`: LLD 17.0.0.
- Capstone: 5.0.6.
- Unicorn: 2.1.4.
- angr: 9.2.222.
- FastAPI: 0.128.2.
- Uvicorn: 0.48.0.
- jsonschema: 4.26.0.
- javalang: 0.13.0.

## Complete source verification

Executed:

```text
make verify
```

Result:

```text
contract, example, Java syntax, and skill frontmatter validation passed
33 passed
```

The command performed:

1. Python bytecode compilation of `src`, `tests`, and `scripts`.
2. Draft 2020-12 validation of every schema document.
3. Schema validation of all representative examples.
4. Java syntax parsing of all bundled Ghidra scripts.
5. YAML parsing and required-field validation of the skill frontmatter.
6. The complete Python test suite.

The 33 tests cover:

- PE32/i386 and PE32+/AMD64 parsing and malformed-input rejection;
- project initialization and original-binary tamper detection;
- independent matching/functional workflow state transitions;
- immutable evidence copies, evidence independence, contradiction gates and hashes;
- append-only memory-chain validation and tamper detection;
- function-artifact import, path traversal and symlink protections;
- i386/AMD64 COFF parsing, symbol extraction and synthetic objects;
- Capstone decode, CFG normalization and ABI observations;
- PE-to-COFF and exact-byte comparison behavior;
- real GCC `-m32` object compilation and compiler reports;
- exact-byte hybrid project generation and real Make/assembler execution;
- PE patching and checksum regeneration;
- real `lld-link` invocation producing a minimal AMD64 PE image;
- Unicorn equal/different concrete execution cases;
- Z3 equal/different bounded symbolic cases with counterexample generation;
- DynamoRIO drcov text parsing and optional dependency behavior;
- real stdio JSON-RPC/MCP initialization, reads, signed mutation proposals and commits;
- type-constraint conflicts and validator-gated work queue behavior;
- explicit-consent integration scenario equality and mismatch detection;
- local decomp.me packet generation;
- manifest-driven external objdiff adapter execution and parsed output capture.

No test was skipped in the final run.

## Representative end-to-end commands

The following release checks were also executed outside pytest.

### Compiler and compiler laboratory

```text
x86decomp compile examples/compiler-profiles/gcc-i686-object.json \
  examples/sample_source/add.c add.o --cache cache --report compile.json
```

Result: success. `file` identified the output as a 32-bit Intel i386 relocatable ELF
object. The report contains compiler path/hash/version, exact argument array, source
hash, output hash, stdout/stderr, timeout state and cache identity.

```text
x86decomp compiler-lab examples/labs/gcc-optimization-matrix.json
```

Result: two declared experiments executed.

### Functional validators

```text
x86decomp dynamic-validate add_stack_target.bin add_stack_candidate.bin \
  add_stack_harness.json
```

Result: `equivalent_for_harness=true` for the declared Unicorn state.

```text
x86decomp symbolic-validate add_stack_target.bin add_stack_candidate.bin \
  --architecture x86 --stack-argument-words 2 --output-register eax \
  --max-steps 64 --max-paths 16
```

Result: `equivalent_within_model=true` for the built-in Capstone/Z3 model.

```text
x86decomp angr-validate add_stack_target.bin add_stack_candidate.bin \
  --architecture x86 --stack-argument-words 2 --output-register eax \
  --max-steps 64 --max-paths 16
```

Result: `equivalent_within_completed_model=true`; both blobs completed within one
bounded path and one step. This is not an all-program proof.

```text
x86decomp integration-run examples/integration/bounded-demo.json \
  --allow-host-execution
```

Result: one scenario passed. Exit code, stdout, stderr and generated file observations
matched. Host execution required the explicit manifest acknowledgement and CLI flag.

### Benchmark corpus

```text
x86decomp benchmark-run examples/benchmarks/bounded-demo.json
```

Result: four cases completed, zero failed. The report separately records one exact byte
match, one Unicorn pass, one bounded symbolic pass, one integration-scenario pass and
three recorded human interventions.

## Package build and installation

The release process builds both:

```text
x86decomp_toolkit-0.2.0-py3-none-any.whl
x86decomp_toolkit-0.2.0.tar.gz
```

The final wheel is installed into a clean virtual environment and checked with:

```text
x86decomp --help
x86decomp coff-synthesize ...
x86decomp coff-inspect ...
```

The source distribution includes the Python source, tests, Ghidra scripts, schemas,
examples, docs, skill, security policy, project memory and verification record through
`MANIFEST.in`.

## Environment-dependent checks not executable here

### Ghidra runtime

A Ghidra distribution was not installed. Java syntax was parsed, but the exporters were
not executed against the live Ghidra API in this environment. Run:

```bash
export GHIDRA_HOME=/path/to/ghidra_12.1.2_PUBLIC
./scripts/verify-ghidra.sh path/to/authorized-sample.exe /tmp/x86decomp-ghidra-check
```

That performs headless import/analysis, executes project and function exporters, and
validates generated JSON/JSONL. Preserve the Ghidra distribution hash, sample hash,
command and exported artifact hashes in project memory.

### DynamoRIO runtime

`drrun` was not installed. The drcov parser is tested with a representative log, but a
live target trace was not captured. Execute `x86decomp drcov-run` only in an isolated,
disposable environment.

### Real objdiff binary

`objdiff-cli` was not installed. The adapter was exercised with a real subprocess that
accepted target/candidate/output paths and emitted parsed JSON. A release-specific
objdiff invocation must be tested against the operator's installed objdiff version and
manifest because CLI/configuration details may vary.

### Historical MSVC toolchains

No proprietary historical MSVC installation was present or bundled. Registry and hash
verification are implemented and tested with available executables. Matching against a
specific historical compiler requires a legally obtained user-owned installation.

## Claims deliberately not made

This verification does not claim:

- recovery of original source text, comments, names, types or translation units;
- correctness of every Ghidra analysis result;
- complete reconstruction of consumed COFF relocations, COMDATs or linker decisions;
- safety of host execution for unknown binaries;
- universal semantic equivalence from finite tests or bounded solvers;
- that external-wrapper isolation is independently certified by the toolkit;
- that the three-source evidence gate guarantees truth;
- generic byte-identical whole-image reconstruction for arbitrary programs.

The 0.2.0 package provides runnable implementations for every discussed architecture
box and named workflow boundary. Each implementation retains explicit scope, failure
and unsupported-case reporting instead of pretending that open reverse-engineering
problems are universally solved.
