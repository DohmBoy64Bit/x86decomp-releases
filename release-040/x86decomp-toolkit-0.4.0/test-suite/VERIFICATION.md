# Verification record — x86decomp comprehensive test suite 0.4.0

## Scope

This record covers the integrated and independently packaged test harness under
`test-suite/` for x86decomp-toolkit 0.4.0. Generated results, downloaded
adapters, installation directories, virtual environments, coverage products,
and machine-specific configuration are excluded from the release source.

## Pinned surface

Dynamic discovery must exactly match:

```text
60 toolkit Python modules
514 defined functions and methods
106 CLI commands
52 JSON Schemas
3 Ghidra Java scripts
31 adapter contracts
```

Any uncataloged addition, stale catalog item, removed retained surface, or
uncovered function body fails the release contract.

## Harness layers

The complete repository run collected and passed:

```text
native toolkit tests:                         82
test-suite external tests:                    21
packaged harness self-tests:                  17
packaged toolkit supplemental tests:          20
total:                                       140
failed:                                        0
skipped:                                       0
```

Pytest plugin autoload is disabled for suite-owned subprocesses so unrelated
host plugins cannot alter collection or hang shutdown. This does not disable any
project test or adapter test.

## Coverage and no-omission contract

The coverage audit reported:

```text
514 / 514 cataloged function/method bodies executed
106 / 106 CLI commands parser-tested
line coverage:   76.54071314529004%
branch coverage: 52.312464749012975%
zero JUnit skips
```

Execution of each body is a no-omission guarantee, not exhaustive proof of every
branch or input. Focused behavior, malformed-input, migration, tamper,
concurrency, packaging, and adapter tests supply deeper evidence.

## Adapter resolution behavior

Resolution order is:

1. saved configured path;
2. environment variable;
3. system `PATH`;
4. known platform locations;
5. custom-path prompt only when still missing;
6. consent-gated installation only when unresolved;
7. explicit `BLOCKED` result.

Detected adapters never trigger a custom-path prompt. Noninteractive runs never
invent paths. Historical MSVC remains user-owned and custom-path-only. Network,
installation, container use, and host execution are disabled unless explicitly
authorized.

## Comprehensive run

The final sealed-source non-strict run reported:

```text
154 PASS
0 FAIL
0 ERROR
8 BLOCKED
```

Blocked in this host environment:

- container runtime;
- DynamoRIO;
- Ghidra;
- LIEF;
- llvm-readobj;
- MSVC;
- objdiff CLI;
- pip-audit.

Blocked integrations are retained in `results.json`, Markdown/HTML reports,
per-test logs, and `events.jsonl`. They are not converted to passes or omitted.
Strict mode returns exit code 2 while required adapter-backed tests are blocked.

## 0.4.0-specific coverage

The harness includes focused contracts for:

- target-pack inference/verification and grounded project templates;
- schema-v3 migrations, backup/restore/repair/GC, and compatibility from 0.3.1;
- immutable content storage;
- durable orchestration, cancellation, retries, heartbeat recovery, output
  sealing, and tamper invalidation;
- local/container worker policy and compiler workers;
- linker reconstruction, C++ recovery, convergence, harness generation, and
  symbolic flag behavior;
- reproducibility manifests, SBOM/security/dependency audits, and release gates;
- deterministic generated compiler corpora;
- read-only service/control-plane visibility;
- synchronized toolkit/test-suite Mermaid and ASCII maps;
- documentation/version/catalog consistency.

## Packaging and self-containment

The harness independently builds and installs as:

```text
x86decomp_test_suite-0.4.0-py3-none-any.whl
x86decomp_test_suite-0.4.0.tar.gz
```

Its wheel and source distribution carry the feature catalog, schemas, self-tests,
documentation, and CLI entry point. The toolkit source distribution also carries
the clean `test-suite/` source tree. Generated run outputs remain outside source.

## Logging contract

Every comprehensive run emits:

- human-readable `run.log`;
- append-only structured `events.jsonl`;
- adapter inventory and resolution provenance;
- exact source inventory and catalog audit;
- JUnit and coverage records;
- all-function/public-API execution reports;
- JSON, Markdown, and HTML summaries;
- isolated stdout/stderr for each subprocess;
- final result counts and exit code.

## Interpretation

The suite is designed to prevent silent regression and silent environmental
omission. It does not claim that finite tests prove arbitrary binaries correct.
Every future toolkit release must update the catalog, tests, adapter contracts,
four architecture maps, skill, docs, changelogs, verification records, package
versions, and both SHA-256 manifests.
