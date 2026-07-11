# benchmark-run

## `x86decomp benchmark-run`

Run a declared benchmark corpus and emit measured results.

### Purpose

Executes every benchmark case declared in a JSON manifest. Each case specifies a *kind* and compares declared expectations against computed metrics. Benchmark kinds cover byte-level comparison, PE/COFF structural comparison, dynamic differential execution, symbolic bounded comparison, integration scenarios, and classification discovery metrics.

### Syntax

```
x86decomp benchmark-run MANIFEST [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `MANIFEST` | yes | path | JSON benchmark manifest declaring cases and expected results |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON benchmark report to this path |

### Benchmark kinds

| Kind | Description |
|---|---|
| `byte_pair` | Byte-for-byte comparison of two files with bounded mismatch reporting |
| `pe_coff` | Compare a linked PE function to its corresponding COFF symbol |
| `dynamic` | Differential execution and comparison of two binaries under a harness |
| `symbolic` | Symbolic bounded comparison of binary functions |
| `integration` | Execute declared integration scenarios with declared observations |
| `discovery_metrics` | Calculate precision, recall, and F1 for function/type discovery against known ground truth |

### Manifest structure

The benchmark manifest is a JSON object with a `cases` array. Each case declares:

- `kind` — one of the six benchmark kinds
- `label` — human-readable case identifier
- `target` / `candidate` — paths to files compared (relative to manifest directory)
- `expect` — expected outcome assertions (e.g., `matched`, `instruction_similar`, `differentially_validated`)

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp benchmark-run benchmarks/validation-corpus.json \
    --report reports/benchmark-results.json
```

Example manifest fragment:

```json
{
  "cases": [
    {
      "kind": "byte_pair",
      "label": "function_001_byte_match",
      "target": "obj/msvc2019/function_001.obj",
      "candidate": "obj/gcc11/function_001.obj",
      "expect": { "matched": false }
    },
    {
      "kind": "dynamic",
      "label": "function_042_dynamic_validate",
      "target": "bin/target_function_042.asm.bin",
      "candidate": "bin/candidate_function_042.asm.bin",
      "harness": "harnesses/harness_042.json",
      "expect": { "differentially_validated": true }
    }
  ]
}
```

### Related commands

- [corpus-build](corpus.md#x86decomp-corpus-build) — Build the compiler ground-truth corpus
- [corpus-generate](corpus.md#x86decomp-corpus-generate) — Generate a deterministic source corpus
- [dynamic-validate](../validation/dynamic.md) — Differential binary validation
- [symbolic-validate](../validation/symbolic.md) — Symbolic bounded comparison
