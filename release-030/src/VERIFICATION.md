# Verification record — x86decomp-toolkit 0.3.0

This record separates checks actually executed in the release environment from checks
that require operator-specific installations or proprietary target artifacts. It does
not claim arbitrary-binary decompilation correctness, original-source recovery, or
all-input semantic equivalence.

## Release environment

- Date: 2026-06-28 UTC.
- Host: Linux x86-64.
- Python: 3.13.5.
- OpenJDK/Javac: 21.0.10.
- GCC: 14.2.0.
- Clang/LLD/LLVM ar: 17.0.0, Swift LLVM build
  `10999b6d034fe318f3d56c83bddb6572593a8bb0`.
- Capstone: 5.0.6.
- Unicorn: 2.1.4.
- angr: 9.2.222.
- FastAPI: 0.128.2.
- Uvicorn: 0.48.0.
- jsonschema: 4.26.0.
- javalang: 0.13.0.
- PyYAML: 6.0.3.
- build: 1.5.0.

## Regression baseline

Before v0.3 changes, the complete v0.2 suite was executed:

```text
33 passed
```

No prior command was removed. An automated compatibility contract now checks that all
17 v0.2 command names remain present, all seven legacy schema filenames remain present,
and representative schema-v1 project/function documents remain valid.

## Complete source verification

Executed:

```text
make verify
```

Final result:

```text
contract, example, Java syntax, and skill frontmatter validation passed
56 passed
```

The command performs:

1. Python bytecode compilation for `src`, `tests`, and `scripts`.
2. Draft 2020-12 self-validation of every JSON Schema.
3. Schema validation of all representative shipped examples.
4. Java syntax parsing of all Ghidra scripts.
5. YAML parsing and release-contract validation of the skill frontmatter.
6. The complete Python regression suite.

No test was skipped in the final release run.

## v0.3 depth checks executed

### COFF, bigobj, COMDAT, and archives

The tests cover:

- classic COFF and `ANON_OBJECT_HEADER_BIGOBJ`;
- i386 and AMD64 relocation naming, width, PC-relative behavior, addends, overflow,
  section alignment, string-table names, and auxiliary records;
- real Clang weak-external records;
- all seven COMDAT selection policies, associative parents, winners, discards, and
  explicit conflicts;
- multi-section and COMDAT synthetic objects;
- real `llvm-ar` Windows static libraries, both linker-member indexes, embedded COFF
  objects, and COMDAT inventory;
- a real `lld-link` import library and import-object records.

### Linker layout and complete-image comparison

The tests and smoke runs cover:

- MSVC/LLD map headers, segments, public symbols, contribution records, object
  ownership/order, preferred base, and entry point;
- the distinction between public-derived object order and byte-accurate contribution
  evidence;
- target-bound image profiles;
- raw equality, checksum normalization, real CodeView debug normalization, section
  layout comparison, and supported base-relocation rebasing;
- manifest-driven `lld-link` execution and complete-image comparison.

### Microsoft C++ metadata and PDB

Real Clang/LLD C++ artifacts were built and checked for:

- RTTI TypeDescriptors, CompleteObjectLocators, class hierarchy/base records, PMD
  metadata, vftable address points, and function slots;
- x64 runtime functions, UNWIND_INFO, handlers, and chained records;
- x86 SafeSEH parser paths and bounded EH FuncInfo candidate handling;
- linked TLS, object `.tls$*`/`.CRT$XL*` records, and `.CRT$X*` initializers;
- MSF 7.0 superblock and discontiguous stream directory parsing;
- PDB GUID/age identity, TPI/IPI headers, DBI modules, section contributions, source
  mappings, and PE RSDS identity matching.

The real PDB regression produced non-empty TPI/IPI records, identified the contributing
object and source file, and matched both GUID and age to its linked PE.

### Ground-truth compiler corpus

The bundled corpus was built outside pytest with the release compiler matrix:

```text
24 C/C++ cases
2 architectures: x86 and x86-64
4 optimization levels: O0, O1, O2, Os
2 frame-pointer variants
384 total COFF builds
384 succeeded
0 failed
192 x86 outputs
192 x86-64 outputs
all source/output hashes reverified
```

Each build record contains source hash, compiler executable hash, complete compiler
version output, exact argument array, environment policy, output hash, and parsed COFF
metadata. Cross-report comparison is tested without inferring compiler identity or
semantic equivalence from byte appearance.

### Richer symbolic memory and functional validation

Executed tests cover:

- Unicorn target/candidate execution with explicit register, stack, memory, and
  deterministic external-call summaries;
- built-in Capstone/Z3 equal and counterexample cases;
- angr comparative execution with symbolic byte regions, finite base slots, and
  equal/distinct/disjoint/may-alias constraints;
- memory-observation counterexamples where instruction ordering matters only under
  aliasing;
- DynamoRIO drcov text parsing and unavailable-tool failure behavior;
- explicit-consent integration scenarios comparing process exit code, stdout, stderr,
  and generated files;
- bounded benchmark reports and human-intervention counts.

Every functional/symbolic report retains its input model, path/step bounds, completion
counts, and `universal_equivalence=false` boundary.

### Authorized static upload bundle

A release smoke bundle containing eight synthetic, authorized artifacts was created and
inspected:

```text
primary PE
reference PE
candidate PE
PDB
linker map
COFF object
COFF static library
image profile
```

Result:

```text
bundle passed: true
PE images parsed: 3
COFF objects parsed: 1
COFF archives parsed: 1
PDB GUID/age identity match: true
whole-image classification: byte_identical
supplied code executed: false
errors: 0
```

ZIP path traversal, backslash/drive paths, duplicate members, symlinks, excessive
member/total size, compression expansion, missing authorization, and hash mismatch are
covered by rejection tests.

## Existing v0.2 features rechecked

The expanded suite still exercises:

- PE32/i386 and PE32+/AMD64 parsing and malformed-input rejection;
- project initialization, copied/external input handling, and binary tamper detection;
- independent matching and functional mode state machines with audited regressions;
- immutable evidence, independence groups, contradiction gates, and three-source claim
  verification;
- append-only hash-chained memory and tamper detection;
- safe function-artifact import, confinement, traversal, and symlink rejection;
- compiler profiles, executable/source/output hashes, cache identity, flag matrices,
  and user-owned toolchain registry;
- PE-function to COFF-symbol comparison, exact byte comparison, instruction/CFG
  similarity, and ABI observations;
- buildable assembly fallback projects and real assembler/Make execution;
- hash-gated PE patching and checksum regeneration;
- local decomp.me packets and manifest-driven objdiff adapters;
- SQLite analysis/type constraints, MCP stdio/HTTP policy, signed mutations, and
  validator-gated human/AI work queues;
- read-only service endpoints and benchmark contracts.

## Package build and clean-install checks

The release process builds:

```text
x86decomp_toolkit-0.3.0-py3-none-any.whl
x86decomp_toolkit-0.3.0.tar.gz
```

The wheel must be installed into a fresh virtual environment and checked with:

```text
x86decomp --help
x86decomp coff-synthesize ...
x86decomp coff-inspect ...
x86decomp lib-inspect ...
x86decomp pdb-inspect ... --pe ...
x86decomp corpus-create-manifest ...
```

The wheel includes the 24 packaged corpus sources. A regression test compares their
bytes to the repository corpus. The source distribution and repository ZIP include the
Python source, corpus, tests, Ghidra scripts, schemas, examples, docs, skill, policies,
project memory, parity matrix, and verification record.

## Environment-dependent checks not executed here

### Live Ghidra runtime

No Ghidra distribution was installed. Java syntax and command construction were tested,
but the scripts were not executed against a live Ghidra API. Run:

```bash
export GHIDRA_HOME=/path/to/ghidra
./scripts/verify-ghidra.sh path/to/authorized-sample.exe /tmp/x86decomp-ghidra-check
```

Record the exact Ghidra distribution hash/version, target hash, command, and exported
artifact hashes.

### Live DynamoRIO target trace

`drrun` was unavailable. The drcov parser and runner failure behavior are tested, but a
live native target trace was not captured. Run uploaded or unknown native code only in
an operator-controlled disposable environment.

### Operator-selected objdiff build

`objdiff-cli` was unavailable. The adapter was exercised with a real subprocess
implementing the declared manifest contract. A production project must verify the exact
operator-selected objdiff executable hash/version and arguments.

### Historical proprietary MSVC toolchains

No proprietary historical MSVC installation was present or bundled. Toolchain
registration and tamper verification are implemented. Compiler-version comparison
requires legally obtained user-owned installations.

### Complete CodeView records

The built-in PDB parser inventories MSF/PDB/TPI/IPI/DBI metadata and identity. It does
not fully decode every CodeView type, symbol, line, public/global hash, named-stream, or
fastlink record. Use a pinned external tool such as `llvm-pdbutil` or DIA where deeper
records are required, and retain that tool output as separate evidence.

## Claims deliberately not made

This release does not claim:

- recovery of original comments, identifiers, macros, templates, translation units, or
  compiler flags absent from the binary;
- correctness of every Ghidra/decompiler/type inference;
- complete reconstruction of all consumed relocations, archive directives, COMDAT
  decisions, linker-generated symbols, section ordering, padding, or linker scripts;
- generic whole-image byte identity for arbitrary targets;
- complete compiler-specific C++ exception semantics;
- safe native execution of unknown binaries;
- semantic equivalence outside declared finite harnesses/models/scenarios;
- that a three-source review gate guarantees truth.

Version 0.3.0 is a regression-tested, production-oriented bounded framework for
operator-authorized, target-specific decompilation work. Unsupported or unverified
conditions remain explicit report states rather than success shims.
