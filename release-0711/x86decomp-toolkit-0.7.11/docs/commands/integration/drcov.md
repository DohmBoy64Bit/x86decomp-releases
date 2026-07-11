# DynamoRIO drcov Commands

DynamoRIO drcov coverage log parsing and target tracing. The module executes a user-authorized program under `drrun -t drcov` and parses the text basic-block table.

---

## `x86decomp drcov-parse`

Parse a DynamoRIO drcov text coverage log.

### Purpose

Normalizes a drcov `-dump_text` log file into stable, structured JSON records of modules and basic blocks. Retains the original log path, DRCOV version and flavor, module table entries (base, end, entry, checksum, timestamp, path), and basic-block table entries (module index, start address, size).

### Syntax

```
x86decomp drcov-parse LOG
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `LOG` | yes | path | DynamoRIO drcov text log file (`-dump_text` output) |

### Files read

- `LOG` — drcov text coverage log

### Output

JSON object with `source`, `version`, `flavor`, `module_version`, `modules` array, and `blocks` array.

### Example

```console
$ x86decomp drcov-parse traces/drcov.target.exe.0000.proc.log
```

---

## `x86decomp drcov-run`

Run a target executable under DynamoRIO drcov tracing.

### Purpose

Invokes `drrun -t drcov` with the target executable and declared program arguments, capturing the text coverage log to a temporary directory then copying it to the declared output directory. Supports configurable timeout and the drrun executable path.

### Syntax

```
x86decomp drcov-run EXECUTABLE OUTPUT_DIR [--drrun PATH] [--program-arg ARG]... [--timeout SECONDS] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `EXECUTABLE` | yes | path | Target executable to trace under DynamoRIO |
| `OUTPUT_DIR` | yes | path | Directory for the captured drcov output log |

### Options

| Option | Default | Description |
|---|---|---|
| `--drrun PATH` | `drrun` (PATH lookup) | Path to the DynamoRIO `drrun.exe` executable |
| `--program-arg ARG` | `[]` | Argument passed to the target executable; repeatable |
| `--timeout SECONDS` | `300` | Maximum time in seconds before the trace is terminated |
| `--report REPORT` | none | Write structured JSON trace report to this path |

!!! warning "Execution authorization"
    `drcov-run` executes the target program under DynamoRIO. Only run executables
    you own or are authorized to analyze. DynamoRIO instrumentation provides code
    coverage, not a security sandbox.

### Files read

- `EXECUTABLE` — target program to trace

### Files written

- `OUTPUT_DIR` — captured drcov log file
- `--report REPORT` — JSON trace report with metadata and coverage summary

### Example

```console
$ x86decomp drcov-run target.exe traces/coverage/ \
    --drrun "C:\DynamoRIO\bin64\drrun.exe" \
    --program-arg --level --program-arg map1 \
    --timeout 120 \
    --report reports/drcov-run.json
```

### Related commands

- [drcov-parse](#x86decomp-drcov-parse) — Parse a drcov coverage log
- [integration-run](integration-run.md) — Integration scenario execution
- [dynamic-validate](../validation/dynamic.md) — Differential binary validation
