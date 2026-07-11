# abi-check

Validate observed behavior against an ABI contract.

### Purpose

Disassembles a binary code blob and statically checks whether the observed
instruction patterns conform to a declared ABI contract. Verifies calling
convention compliance: prologue/epilogue structure, register usage, stack
frame management, parameter access patterns, and return value handling.

### Syntax

```
x86decomp abi-check CODE CONTRACT [--base BASE] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `CODE` | yes | path | Binary code blob to analyze |
| `CONTRACT` | yes | path | JSON ABI contract specifying expected calling convention and behavior |

### Options

| Option | Default | Description |
|---|---|---|
| `--base ADDR` | `0` | Base address for disassembly (integer, supports `0x` prefix) |
| `--report REPORT` | none | Write structured JSON validation report to this path |

### ABI contract format

The ABI contract is a JSON document declaring expected behavior:

```json
{
    "architecture": "x86",
    "convention": "stdcall",
    "stack_argument_bytes": 4,
    "callee_stack_cleanup": 4,
    "variadic": false,
    "this_register": null,
    "register_arguments": [],
    "return_registers": ["eax"],
    "structure_return": false,
    "floating_point": "none"
}
```

### Accepted values

| Field | Accepted values |
|---|---|
| `architecture` | `x86`, `x86_64` |
| `convention` | `cdecl`, `stdcall`, `thiscall`, `fastcall`, `vectorcall`, `unknown` |
| `floating_point` | `x87`, `sse`, `mixed`, `none`, `unknown` |
| `stack_argument_bytes` | integer or `null` |
| `callee_stack_cleanup` | integer or `null` |
| `variadic` | boolean |
| `this_register` | register name string or `null` |
| `register_arguments` | array of register name strings |
| `return_registers` | array of register name strings |
| `structure_return` | boolean |

### Validation checks

The validator examines the disassembled instruction stream for:

- Prologue pattern (push ebp / mov ebp, esp, frame allocation)
- Epilogue pattern (mov esp, ebp / pop ebp, ret with stack cleanup)
- Parameter access relative to the expected frame layout
- Caller vs callee stack cleanup matching the declared convention
- Register usage consistent with the declared convention
- Return register usage matching declared return type
- Floating-point instruction presence matching the declared float mode

### Files read

- `CODE` — binary code blob
- `CONTRACT` — JSON ABI contract

### Files written

- `--report REPORT` — structured JSON validation report

### Exit behavior

- Exit 0 on success with JSON result on stdout (pass or fail — both are valid results)
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp abi-check original/func.bin contracts/func-abi.json \
    --base 0x401000 \
    --report build/abi-check-report.json
```

With contract file:

```json
{
    "architecture": "x86",
    "convention": "stdcall",
    "stack_argument_bytes": 8,
    "callee_stack_cleanup": 8,
    "variadic": false,
    "this_register": null,
    "register_arguments": [],
    "return_registers": ["eax"],
    "structure_return": false,
    "floating_point": "none"
}
```

!!! tip "ABI contracts and matching work"
    When you have a correct byte match from [`diff-function`](diff-function.md),
    the matching compiler profile gives you the calling convention. Use
    `abi-check` to validate that your reconstructed C source follows the same
    convention before attempting a byte match — mismatched conventions are a common
    cause of relocation mismatches.

### Related commands

- [diff-function](diff-function.md) — PE function to COFF symbol comparison
- [dynamic-validate](dynamic.md) — Differential execution via Unicorn
- [symbolic-validate](symbolic.md) — Symbolic equivalence via Z3
