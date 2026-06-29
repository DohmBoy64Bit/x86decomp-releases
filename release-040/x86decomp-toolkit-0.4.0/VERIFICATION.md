# Verification record — x86decomp-toolkit 0.4.0

## Scope and truth boundary

This record covers the 0.4.0 production-pilot release of x86decomp-toolkit and
its integrated, separately packaged verification harness under `test-suite/`.
The release preserves the retained 0.3.1 surface while adding target packs,
grounded project templates, durable orchestration, transactional project state,
content-addressed artifacts, bounded workers, linker-convergence planning,
reproducibility, security, release gates, generated corpora, and expanded
symbolic semantics.

A passing record means the declared finite tests and contracts passed in the
recorded environment. It does not prove arbitrary-program equivalence, recover
erased source information, establish an unknown compiler identity, or make an
unavailable external adapter count as tested.

## Source and compatibility contracts

The pinned 0.4.0 inventory is:

```text
60 Python modules
514 defined functions and methods
106 CLI commands
52 JSON Schemas
3 Ghidra Java scripts
31 adapter contracts
```

The compatibility gate preserves the public 0.3.1 command, schema, module,
adapter, workflow-state, and Ghidra-script surface. Legacy schema-v1 and
schema-v2 project records have explicit migration coverage into project schema
v3. No retained command or mode was removed.

The four maintained architecture artifacts are:

- `docs/ARCHITECTURE_MAP.md`
- `docs/ARCHITECTURE_MAP_ASCII.txt`
- `test-suite/docs/ARCHITECTURE_MAP.md`
- `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`

Their version, cross-links, matching/functional states, trust boundaries, and
major subsystem coverage are regression-tested.

## Contract validation

Executed from the repository root:

```bash
PYTHONPATH=src:test-suite/src python scripts/validate-contracts.py
```

Result:

```text
contract, example, Java syntax, and skill frontmatter validation passed
```

This checks schemas and examples, Ghidra Java syntax, evidence-engineering
skill frontmatter/version 4.0.0, release contract 0.4.0, and active examples.

## Repository regression suite

The suite is run with unrelated host pytest plugins disabled. This environment
contains an automatically loaded `ddtrace` plugin that can hang interpreter
shutdown after pytest has completed; plugin isolation is therefore part of the
reproducible test contract rather than a test omission.

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=src:test-suite/src \
pytest -q
```

Result:

```text
140 passed
0 failed
0 skipped
```

Collected layers:

```text
tests/:                                             82
test-suite/tests/:                                  21
test-suite/src/x86decomp_testkit/self_tests/:       17
test-suite/src/x86decomp_testkit/toolkit_tests/:    20
```

The tests include 0.2/0.3.1 compatibility, project migrations, deterministic
backup/restore, crash/stale-run recovery, active cancellation, concurrency,
content sealing, tamper invalidation, worker bounds, target/template generation,
linker plans, convergence, release gates, symbolic flags, generated corpus
provenance, service visibility, and architecture/document synchronization.

## Function, command, schema, and coverage audit

The native plus supplemental coverage run executes at least one body line from
every cataloged toolkit function or method:

```text
514 / 514 function and method bodies executed
106 / 106 CLI commands inventoried and parser-tested
60 / 60 Python modules inventoried
52 / 52 JSON Schemas inventoried
3 / 3 Ghidra scripts inventoried
0 pytest/JUnit skips
line coverage:   76.54071314529004%
branch coverage: 52.312464749012975%
```

This is a no-omission surface contract. It is not a claim that every branch,
input combination, target ABI, or external-tool version has been proven.

## End-to-end target/template exercise

A generated PE fixture was used to exercise:

1. target-pack inference and hash sealing;
2. observation/decision separation;
3. target-project generation;
4. matching/functional/hybrid template derivation;
5. project materialization without fabricated source;
6. project-helper execution when the console-script is present;
7. project-helper fallback to `python -m x86decomp` when it is absent;
8. project integrity checking;
9. durable pipeline creation and status handling.

Unknown compiler, linker, language, and execution-authorization facts remain
explicit blockers. The generator does not emit fake decompiled C/C++, invented
compiler profiles, or inferred target facts without evidence.

## Compiler corpus exercise

The deterministic corpus generator and verifier preserve exact seeds, source
hashes, family metadata, and non-claims. A release exercise generated twelve
representative source cases and compiled a bounded Windows-target matrix:

```text
12 generated C/C++ cases
x86 and x86-64 targets
O0 and O2 profiles
48 COFF object builds completed
```

The packaged hand-authored 24-case compiler corpus and its broader matrix remain
covered by the existing corpus tests. A byte appearance is never promoted to a
compiler/version identity without independent evidence.

## Comprehensive harness

The integrated harness is run non-interactively and non-strictly for this host.
Missing adapters therefore remain explicit `BLOCKED` records while all available
operations must pass. Strict release mode would return exit code 2 until every
required adapter is resolved.

Final sealed-source result:

```text
154 PASS
0 FAIL
0 ERROR
8 BLOCKED
```

Blocked integrations on this host:

- container runtime (Docker/Podman);
- DynamoRIO;
- Ghidra;
- LIEF;
- llvm-readobj;
- user-owned MSVC;
- objdiff CLI;
- pip-audit.

These were not silently skipped and are not represented as live-tested. Detected
compilers, linkers, Python libraries, build tools, schemas, package builders, and
bounded validators are exercised by real probes.

## Project-state and orchestration reliability

Verified behaviors include:

- v1/v2-to-v3 project migration with history;
- deterministic backup and bounded restore;
- SQLite integrity/repair checks and dry-run-first garbage collection;
- immutable SHA-256 content storage and reference tracking;
- durable pipeline IDs, dependencies, retries, cancellation, heartbeats, and
  stale-run recovery;
- idempotent stage reuse only when recorded outputs still exist and match hashes;
- persistent materialization of successful outputs outside ephemeral workspaces;
- automatic invalidation and rerun after output tampering;
- lease/concurrency behavior without weakening the race regression.

## Worker and execution security

Verified local worker behavior includes command-array execution, bounded timeout,
workspace confinement, output-size checks, exact input/output hashes, cancellation,
and provenance. Docker/Podman command generation includes read-only roots,
network-disabled defaults, dropped capabilities, no-new-privileges, resource
limits, and explicit mounts; a live container runtime was not available here.

Source-tree security auditing, release-manifest verification, archive confinement,
CycloneDX SBOM generation, and dependency-audit output parsing have tests. A live
`pip-audit` executable was not available and remains blocked.

## Packaging

The release builds four artifacts:

```text
x86decomp_toolkit-0.4.0-py3-none-any.whl
x86decomp_toolkit-0.4.0.tar.gz
x86decomp_test_suite-0.4.0-py3-none-any.whl
x86decomp_test_suite-0.4.0.tar.gz
```

Both wheels and both source distributions are installed in clean virtual
environments. Installed CLI entry points, packaged schemas/data, corpus files,
and the test-suite feature catalog are probed. The toolkit source distribution
contains the clean integrated `test-suite/`; its runtime wheel remains focused on
the toolkit package.

## Source hygiene and manifests

The final source archive excludes:

- `__pycache__`, `.pyc`, and `.pytest_cache`;
- coverage/JUnit/test-result products;
- `build/`, `dist/`, `.egg-info`, and virtual environments;
- downloaded adapters and proprietary toolchains;
- machine-specific configuration, credentials, and absolute user paths.

`test-suite/MANIFEST.sha256` independently seals the harness. The root
`MANIFEST.sha256` seals the complete source tree including the nested manifest.
Both are regenerated only after documentation and source are final and are
verified again from the extracted release archive.

## Claims deliberately not made

Version 0.4.0 does not claim:

- original-source recovery;
- reliable reconstruction of erased names or source boundaries;
- universal C++/RTTI/exception reconstruction;
- generic historical linker reproduction for every target;
- semantic proof beyond a validator's declared finite model;
- generic whole-image identity;
- safe ordinary-host execution of unknown native programs;
- that three independent evidence groups mathematically guarantee truth.

The accurate release claim is a regression-preserving, production-pilot platform
for authorized target-specific decompilation projects, with explicit blockers
and bounded acceptance evidence.
