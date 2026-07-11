# compiler-lab

Run a compiler experiment matrix from a lab manifest.

### Purpose

Compiles one source file under multiple compiler profiles with variant argument
combinations, scores each output against a target, and ranks results. Answers:
"Which compiler and flags produce the closest match?"

### Syntax

```
x86decomp compiler-lab LAB [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `LAB` | yes | path | JSON lab manifest describing source, profiles, matrix axes, and target |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON lab report to this path |

### Lab manifest schema

The lab manifest is a JSON object with these fields:

| Field | Required | Default | Description |
|---|---|---|---|
| `source` | yes | — | Path to source file to compile |
| `output_root` | yes | — | Directory for per-experiment output subdirectories |
| `profiles` | yes | — | Array of compiler profile JSON paths |
| `matrix` | yes | — | Object with `axes` defining the experiment grid |
| `target` | yes | — | Object with `kind` specifying how to score output |
| `output_name` | no | — | Output filename within each experiment directory |
| `cache_root` | no | — | Content-addressed compiler cache directory |
| `max_experiments` | no | `256` | Maximum allowed experiment count; guards against combinatorial explosion |

### Target kinds

**`pe_function`** — Compare a COFF symbol against a function body in a PE image:

```json
"target": {
    "kind": "pe_function",
    "pe": "original/game.exe",
    "rva": "0x401000",
    "size": "256",
    "symbol": "_ProcessInput@4"
}
```

**`file`** — Compare a reference file against the compiled output:

```json
"target": {
    "kind": "file",
    "path": "reference/output.obj"
}
```

### Matrix axes

Matrix axes values are concatenated as compiler `--extra-arg` values. The lab
computes the Cartesian product of all axis values, then runs each combination
against every profile.

```
total experiments = len(profiles) * len(combinations)
```

The lab raises an error if the total exceeds `max_experiments`.

### Experiment directories

Each experiment creates a subdirectory under `output_root`:

```
output_root/
  p000-v0000/
    candidate.obj       compiled output
    compile.json        compilation provenance
    comparison.json     comparison result and score
  p000-v0001/
    ...
```

### Scoring

| Target kind | Classification | Score |
|---|---|---|
| `pe_function` | `byte_matched` | 4.0 |
| `pe_function` | `relocation_normalized_match` | 3.0 |
| `pe_function` | `instruction_similar` | 2.0 + similarity bonus |
| `pe_function` | `mismatch` | 0.0 |
| `file` | exact match (`equal: true`) | 2.0 |
| `file` | no match | 0.0 – 1.0 (`sequence_similarity`) |
| any | compilation error | -1.0 |

### Files read

- `LAB` — lab manifest JSON
- Each file referenced by `profiles`, `source`, and `target`

### Files written

- Per-experiment output directories under `output_root`
- `--report REPORT` — structured JSON lab report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 with `"compiler lab matrix exceeds max_experiments"` if the experiment count exceeds the cap

### Example

```console
$ x86decomp compiler-lab lab-manifest.json --report lab-report.json
```

With manifest:

```json
{
    "source": "candidate.c",
    "output_root": "lab-output",
    "cache_root": ".compiler-cache",
    "output_name": "candidate.obj",
    "profiles": [
        "profiles/msvc-2019-x86.json",
        "profiles/clang-15-x86-o2.json"
    ],
    "matrix": {
        "axes": {
            "opt": ["/O2", "/O1", "/Od"],
            "arch": ["/arch:IA32", "/arch:SSE2"]
        }
    },
    "target": {
        "kind": "pe_function",
        "pe": "original/game.exe",
        "rva": "0x401000",
        "size": "64",
        "symbol": "_SmallFunc@0"
    },
    "max_experiments": 128
}
```

This runs 2 profiles x 6 axis combinations = 12 experiments.

!!! danger "Matrix explosion"
    A matrix with 5 axes of 3 values each x 5 profiles = 1,215 experiments. Set
    `max_experiments` to a reasonable cap and review the expected count before running.

### Related commands

- [compile / compile-worker](compile.md) — Single compilation under a single profile
- [diff-bytes](../validation/diff-bytes.md) — Byte-for-byte comparison of two files
- [diff-function](../validation/diff-function.md) — Compare PE function to COFF symbol
