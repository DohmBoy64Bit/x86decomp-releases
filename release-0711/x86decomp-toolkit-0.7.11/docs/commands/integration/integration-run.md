# integration-run

## `x86decomp integration-run`

Execute declared integration scenarios with explicit host execution authorization.

### Purpose

Reads an integration manifest that declares target and candidate executables, input/output observations, and expected exit codes or output hashes. Each scenario runs both the target and candidate processes in temporary working directories and compares only the declared observations. Finite scenarios are never treated as universal equivalence proof.

### Syntax

```
x86decomp integration-run MANIFEST [--allow-host-execution] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `MANIFEST` | yes | path | JSON integration manifest declaring scenarios and observations |

### Options

| Option | Default | Description |
|---|---|---|
| `--allow-host-execution` | false | Explicitly authorize native execution of target and candidate processes on the host |
| `--report REPORT` | none | Write structured JSON integration report to this path |

!!! danger "Host execution requires explicit authorization"
    Integration scenarios execute real Windows binaries. The toolkit never runs them without
    `--allow-host-execution`. Without this flag the command fails with a contract error.
    Only enable this flag when you have verified the executables and trust the manifest.

### Manifest structure

Each scenario declares:

- `name` — human-readable scenario label
- `target` — path to the reference executable
- `candidate` — path to the candidate executable
- `observations` — declared outputs to compare (exit code, stdout hash, file outputs)

Path templates `{artifact}` and `{workdir}` are resolved against the manifest directory and per-scenario temporary directories.

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 if `--allow-host-execution` is not provided and the manifest requires native execution

### Example

```console
$ x86decomp integration-run integration/scenarios.json \
    --allow-host-execution \
    --report reports/integration-results.json
```

### Related commands

- [benchmark-run](../ground-truth/benchmarks.md) — Run benchmarks including integration scenarios
- [dynamic-validate](../validation/dynamic.md) — Differential binary validation
- [drcov-run](drcov.md#x86decomp-drcov-run) — Run target under DynamoRIO tracing
