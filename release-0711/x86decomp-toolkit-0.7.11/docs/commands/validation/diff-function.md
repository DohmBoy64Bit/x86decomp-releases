# diff-function

Compare a linked PE function body to a COFF object symbol.

### Purpose

Extracts a function body from a PE image at a given RVA and size, extracts the
matching symbol from a COFF object (with relocation normalization), then
compares them byte-for-byte. Also performs instruction-stream comparison. This
is the primary matching-mode validation: "Does my compiled COFF symbol match
the original PE function?"

### Syntax

```
x86decomp diff-function PE RVA SIZE COFF SYMBOL [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PE` | yes | path | PE32 or PE32+ image file |
| `RVA` | yes | int | Relative virtual address of the function in the PE (supports `0x` prefix) |
| `SIZE` | yes | int | Size in bytes of the function body (supports `0x` prefix) |
| `COFF` | yes | path | COFF object file containing the symbol |
| `SYMBOL` | yes | string | Symbol name to extract from the COFF object |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON comparison report to this path |

### How it works

1. Parses the PE image and resolves the RVA to a file offset
2. Extracts `SIZE` bytes from the PE as the target function body
3. Parses the COFF object and extracts the named symbol payload
4. Selects the matching COFF section with non-zero relocation entries
5. Normalizes COFF relocations by zeroing relocation target bytes
6. Performs byte comparison with `max_mismatches=64`
7. Performs instruction-stream comparison using the toolkit disassembler
8. Reports a classification: `byte_matched`, `relocation_normalized_match`, `instruction_similar`, or `mismatch`

### Output structure

| Field | Description |
|---|---|
| `classification` | One of `byte_matched`, `relocation_normalized_match`, `instruction_similar`, `mismatch` |
| `byte_comparison` | Byte-level diff result (prefix, suffix, mismatches, similarity) |
| `instruction_comparison` | Instruction-stream comparison result |
| `normalized_similarity` | Similarity ratio after relocation normalization (0.0 – 1.0) |

### Files read

- `PE` — PE image file
- `COFF` — COFF object file

### Files written

- `--report REPORT` — structured JSON comparison report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 if the RVA is not mapped by any PE section

### Example

```console
$ x86decomp diff-function original/game.exe 0x401000 256 build/candidate.obj _ProcessInput@4 \
    --report build/diff-function-report.json
```

!!! note "RVA and SIZE support hex"
    Both `RVA` and `SIZE` accept decimal or hex values. Prefix hex with `0x`:
    `0x401000`, `0x100`. Values are parsed with `int(value, 0)`.

!!! warning "Relocation normalization is not always sufficient"
    Some compiler/linker combinations produce differences beyond relocation fixups
    (e.g. merged jump tables, padding bytes, function alignment). A
    `relocation_normalized_match` classification confirms the same codegen with
    only relocation differences. Use `instruction_similar` as a strong indicator
    that the compiler and flags are correct.

### Related commands

- [diff-bytes](diff-bytes.md) — Byte-for-byte comparison of two arbitrary files
- [compiler-lab](../compilation/compiler-lab.md) — Automated scoring across compiler profiles using this comparison
- [compile](../compilation/compile.md) — Compile source using a compiler profile
