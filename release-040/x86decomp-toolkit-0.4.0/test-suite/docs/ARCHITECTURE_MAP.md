# x86decomp comprehensive test-suite architecture map

**Architecture version:** 0.4.0  
**Release contract:** no-silent-skip verification for x86decomp-toolkit 0.4.0  
**ASCII companion:** [`test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`](ARCHITECTURE_MAP_ASCII.txt)  
**Toolkit map:** [`docs/ARCHITECTURE_MAP.md`](../../docs/ARCHITECTURE_MAP.md)

## Actual v0.4.0 test-suite architecture

```mermaid
flowchart TB
    CONFIG[Test configuration\ntoolkit root · output root · strict mode\ninstall/network/host-execution consent]

    subgraph RESOLVE[Adapter resolution]
        CATALOG[Version-pinned adapter catalog]
        CONFIGURED[Configured path]
        ENV[Environment variable]
        PATH[System PATH]
        KNOWN[Known platform locations]
        CUSTOM[Prompt for custom path\nonly when still missing]
        INSTALL[Consent-gated installer\nonly when custom path did not resolve]
        BLOCKED[Explicit BLOCKED result]
    end

    CONFIG --> CATALOG
    CATALOG --> CONFIGURED --> ENV --> PATH --> KNOWN
    KNOWN -->|found| READY[Resolved adapter with version/path]
    KNOWN -->|missing and interactive| CUSTOM
    CUSTOM -->|valid| READY
    CUSTOM -->|not installed| INSTALL
    INSTALL -->|installed and validated| READY
    INSTALL -->|declined/unsupported/failed| BLOCKED
    KNOWN -->|missing and noninteractive| BLOCKED

    subgraph INVENTORY[Pinned surface and catalog drift]
        DISCOVER[Discover toolkit modules · all functions/methods\nCLI commands · schemas · Ghidra scripts]
        PINNED[Pinned surface catalog for 0.4.0]
        DRIFT[Exact catalog drift audit]
    end
    CONFIG --> DISCOVER
    DISCOVER --> DRIFT
    PINNED --> DRIFT

    subgraph BUILTIN[Built-in verification]
        STRUCTURE[Manifest hashes · schema meta-validation\nJava syntax · skill/frontmatter/contracts]
        CLI[Every CLI subcommand parse-tested]
        TESTS[Native + supplemental pytest tests]
        COVERAGE[All function-body execution audit\nline and branch floors · zero pytest skips]
        MAPS[Toolkit/test-suite Mermaid+ASCII synchronization]
        MIGRATION[Legacy schema/command/project migration tests]
        SECURITY[Archive/input safety · release manifest · SBOM/audit contracts]
    end
    DRIFT --> STRUCTURE
    STRUCTURE --> CLI --> TESTS --> COVERAGE
    STRUCTURE --> MAPS
    STRUCTURE --> MIGRATION
    STRUCTURE --> SECURITY

    subgraph PROCESS[Safe process execution]
        ARGUMENTS[Argument-array execution\nno shell interpolation]
        LIMITS[Timeout · stdout/stderr capture\nseparate per-test logs]
        ISOLATION[Clean environments\nPYTEST plugin autoload disabled]
    end
    READY --> ARGUMENTS --> LIMITS --> ISOLATION

    subgraph LIVE[Live adapter and production probes]
        ADAPTER_TESTS[Real adapter operation when resolved]
        GHIDRA[Ghidra import/export]
        TOOLCHAINS[Compilers/linkers/objdiff]
        RUNTIME[DynamoRIO/Unicorn/Z3/angr]
        WORKERS[Container and bounded-worker capabilities]
    end
    ISOLATION --> ADAPTER_TESTS
    ADAPTER_TESTS --> GHIDRA
    ADAPTER_TESTS --> TOOLCHAINS
    ADAPTER_TESTS --> RUNTIME
    ADAPTER_TESTS --> WORKERS

    subgraph PACKAGE[Packaging and clean-install verification]
        BUILD[Build wheel and source distribution]
        CLEAN[Install wheel into clean virtual environment]
        PROBE[Installed CLI and packaged data probes]
    end
    COVERAGE --> BUILD --> CLEAN --> PROBE

    subgraph RESULTS[Unified result and detailed logging]
        EVENTS[JSONL event stream]
        LOGS[Run log plus per-test stdout/stderr]
        REPORTS[JSON · Markdown · HTML · JUnit · coverage]
        STATUS[PASS · FAIL · ERROR · BLOCKED]
        STRICT[Strict release gate]
    end
    STRUCTURE --> STATUS
    CLI --> STATUS
    TESTS --> STATUS
    COVERAGE --> STATUS
    ADAPTER_TESTS --> STATUS
    BLOCKED --> STATUS
    PROBE --> STATUS
    STATUS --> EVENTS
    STATUS --> LOGS
    STATUS --> REPORTS
    STATUS --> STRICT
    STRICT -->|FAIL/ERROR| EXIT1[exit 1]
    STRICT -->|BLOCKED in strict mode| EXIT2[exit 2]
    STRICT -->|all required checks pass| EXIT0[exit 0]
```

## Result semantics

```mermaid
stateDiagram-v2
    [*] --> PASS: required check completed successfully
    [*] --> FAIL: assertion or acceptance contract failed
    [*] --> ERROR: test infrastructure or execution failed
    [*] --> BLOCKED: required adapter/capability unavailable

    BLOCKED --> PASS: adapter resolved and live probe passes on a later run
    BLOCKED --> FAIL: adapter resolves but its live probe fails
```

`BLOCKED` is never rewritten as `PASS`, never omitted, and causes exit code 2 in strict mode.

## Adapter prompt contract

```mermaid
flowchart LR
    D[Detect adapter] --> F{Found?}
    F -->|yes| R[Record path/version; do not prompt]
    F -->|no| I{Interactive?}
    I -->|no| B[BLOCKED]
    I -->|yes| Q[Ask whether installed at custom path]
    Q -->|valid path| R
    Q -->|not installed/invalid| C{Install consent and supported installer?}
    C -->|yes| X[Install, hash/log, re-detect]
    C -->|no| B
    X --> F
```

## Maintenance contract

Update this map and `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt` whenever:

- toolkit modules, functions, commands, schemas, adapters or workflow states change;
- test result semantics or strict exit codes change;
- adapter detection, custom-path prompts, installer policy or live probes change;
- test execution, coverage, packaging, migration, security or report stages change;
- the toolkit architecture maps or release version change.
