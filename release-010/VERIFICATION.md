# Verification record

This record describes checks performed on the packaged source tree. It distinguishes
checks actually executed from integration checks that require software unavailable in
the build environment.

## Executed checks

Environment used for this record:

- Python 3.13.5.
- OpenJDK/Javac 21.0.10.
- GCC 14.2.0.
- Linux x86-64 host.

Commands and results:

```text
make verify
```

Result: Python bytecode compilation succeeded and all 14 unit/integration tests passed.
The tests cover PE32 parsing, malformed input rejection, project initialization,
binary tamper detection, evidence independence, evidence copying, memory hash-chain
tamper detection, exact byte comparison, function-artifact integrity and path
traversal, safe Ghidra command construction, and a real GCC `-m32` compile.

```text
python3 -m pip wheel . --no-deps
```

Result: built `x86decomp_toolkit-0.1.0-py3-none-any.whl` successfully.

The wheel was installed into a clean virtual environment. `x86decomp --help` ran
successfully, and the installed CLI compiled `examples/sample_source/add.c` into a
real 32-bit i386 relocatable ELF object using the example profile. The emitted
compiler report recorded success, executable identity/hash, command arguments,
source hash, and output hash.

All JSON Schema files parsed as JSON. Representative project, compiler profile,
verification, memory-event, evidence, and claim documents were validated with a
Draft 2020-12 validator. The skill YAML frontmatter parsed and contained all required
metadata fields.

The Java compiler parsed all three Ghidra script source files without reporting Java
syntax errors. A normal standalone `javac` compilation cannot resolve Ghidra API
classes because a Ghidra distribution is not installed in this environment.

## Integration check requiring Ghidra

The Ghidra scripts have not been represented as runtime-verified here. Run the
included check against the supported Ghidra baseline and a legally usable PE32 test
binary:

```bash
export GHIDRA_HOME=/path/to/ghidra_12.1.2_PUBLIC
./scripts/verify-ghidra.sh path/to/sample.exe /tmp/x86decomp-ghidra-check
```

That command performs headless import/analysis, executes both exporters, and parses
the generated JSON. A successful local run should be committed to project memory with
the Ghidra version, distribution hash, input hash, command, and resulting artifact
hashes.

## Claims deliberately not made

This verification does not claim that:

- Ghidra analysis is always correct;
- decompiler output is original source;
- three-source review guarantees truth;
- byte similarity proves semantic equivalence;
- the toolkit currently reconstructs consumed COFF link-time relocations;
- the example GCC ELF object is a Windows COFF matching toolchain;
- dynamic or symbolic equivalence checking is implemented.

Those boundaries are enforced in the documentation and skill rather than hidden
behind empty APIs.
