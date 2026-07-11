# dynamic-validate

Differentially execute and compare two binaries using the Unicorn emulator.

### Purpose

Runs both a target binary blob and a candidate binary blob through the Unicorn
CPU emulator under identical initial register/memory state, then compares
observable side effects (register values, memory writes, flags). Designed for
bounded leaf-function comparison where external calls are represented by
user-supplied deterministic stubs in the harness.

### Syntax

```
x86decomp dynamic-validate TARGET CANDIDATE HARNESS [--target-base BASE] [--candidate-base BASE] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET` | yes | path | Reference binary function blob (ground truth bytes) |
| `CANDIDATE` | yes | path | Recompiled binary function blob to validate |
| `HARNESS` | yes | path | JSON harness specifying initial register state, memory layout, and stub hooks |

### Options

| Option | Default | Description |
|---|---|---|
| `--target-base ADDR` | none | Base address at which to load the target blob (integer, supports `0x` prefix) |
| `--candidate-base ADDR` | none | Base address at which to load the candidate blob (integer, supports `0x` prefix) |
| `--report REPORT` | none | Write structured JSON validation report to this path |

### Dependencies

Requires the Unicorn CPU emulator engine. Install with:

```console
$ pip install x86decomp-toolkit[dynamic]
```

!!! danger "Not a security boundary"
    This validator emulates bounded leaf routines. It intentionally does not model
    a complete Windows process, the filesystem, or the network. External calls are
    only modeled when the harness provides deterministic stubs.

### Harness format

The harness is a JSON document that describes:

- Initial register values (eax, ecx, edx, ebx, esp, ebp, esi, edi, eflags, and x86_64 extended registers)
- Memory pages with their contents and permissions
- Hook functions for external calls with deterministic return behavior
- Expected output: register values, memory regions to compare, flag masks

### Files read

- `TARGET` — reference binary blob
- `CANDIDATE` — candidate binary blob
- `HARNESS` — JSON execution harness

### Files written

- `--report REPORT` — structured JSON validation report

### Exit behavior

- Exit 0 on success with JSON result on stdout (match or mismatch — both are valid results)
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 with `ExternalToolError` if Unicorn is not installed

### Example

```console
$ x86decomp dynamic-validate original/func.bin build/candidate.bin harnesses/func-harness.json \
    --target-base 0x401000 \
    --candidate-base 0x500000 \
    --report build/dynamic-report.json
```

!!! tip "Harness generation"
    Use `x86decomp harness-generate` to produce initial harness templates from an
    ABI contract and binary functions. Edit the generated harness to add stubs for
    any functions the target calls.

### Related commands

- [symbolic-validate / angr-validate](symbolic.md) — Symbolic equivalence via Z3 or angr
- [diff-bytes](diff-bytes.md) — Byte-for-byte comparison
- [diff-function](diff-function.md) — PE function to COFF symbol comparison
- [abi-check](abi.md) — Static ABI contract validation
