# Compiler Laboratory

The compiler laboratory runs matrix experiments: compile one source file under many compiler
profiles with variant arguments, score each output against a target, and rank the results.
This answers the question: "Which compiler and flags produce the closest match?"

## Lab Manifest Structure

A lab manifest is a JSON document specifying the source, compiler profiles, matrix axes,
and target:

```json
{
  "source": "candidate.c",
  "output_root": "compiler-lab-output",
  "cache_root": ".compiler-cache",
  "output_name": "candidate.obj",
  "profiles": [
    "config/compiler-profiles/msvc-2019-x86-release.json",
    "config/compiler-profiles/msvc-2019-x86-debug.json",
    "config/compiler-profiles/clang-15-x86-o2.json"
  ],
  "matrix": {
    "axes": {
      "optimization": ["O0", "O1", "O2", "Ox"],
      "favor": ["blend", "size", "speed"],
      "whole_program": ["false", "true"]
    }
  },
  "target": {
    "kind": "pe_function",
    "pe": "original/game.exe",
    "rva": "0x401000",
    "size": "256",
    "symbol": "?ProcessInput@@YAHH@Z"
  },
  "max_experiments": 128
}
```

## Target Kinds

### pe_function Target

Compares a COFF symbol against a function body in the original PE:

```json
"target": {
  "kind": "pe_function",
  "pe": "original/game.exe",
  "rva": "0x401000",
  "size": "256",
  "symbol": "_ProcessInput@4"
}
```

Scoring uses `compare_pe_function_to_coff_symbol`:

| Classification | Base Score |
|---|---|
| `byte_matched` | 4.0 |
| `relocation_normalized_match` | 3.0 |
| `instruction_similar` | 2.0 |
| `mismatch` | 0.0 |

Plus fractional bonus from `normalized_similarity` of the instruction comparison.

### file Target

Compares a reference file against the compiled output:

```json
"target": {
  "kind": "file",
  "path": "reference/output.obj"
}
```

Scoring:

| Result | Score |
|---|---|
| `equal: true` | 2.0 |
| Not equal | `sequence_similarity` (0.0–1.0) |

## Running the Lab

```bash
x86decomp compiler-lab --lab lab-manifest.json --report lab-report.json
```

The lab creates one output directory per experiment:

```
compiler-lab-output/
├── p000-v0000/        # Profile 0, variant 0
│   ├── candidate.obj
│   ├── compile.json
│   └── comparison.json
├── p000-v0001/
│   ...
```

## Matrix Expansion

The matrix axes expand to all combinations. With the example above:

- 3 profiles × 4 optimization levels × 3 favor modes × 2 whole_program flags = 72 experiments

The `max_experiments` field (default 256) guards against accidental combinatorial explosion:

!!! danger "Matrix explosion"
    A matrix with 5 axes of 3 values each × 5 profiles = 1,215 experiments. Set
    `max_experiments` to a reasonable cap and review the expected count before running.

## Compiler Caching

`cache_root` specifies a directory for compiler output caching. Subsequent lab runs skip
redundant compilations if the source, profile, and arguments are unchanged:

```json
{
  "cache_root": ".compiler-cache"
}
```

The cache is content-addressed — identical inputs produce cache hits regardless of
experiment order.

## Interpreting Results

The lab report ranks experiments by score (highest first):

```json
{
  "schema_version": 1,
  "created_at": "2026-07-11T10:00:00Z",
  "source": "/project/candidate.c",
  "experiment_count": 72,
  "best_experiment": "p001-v0008",
  "experiments": [
    {
      "id": "p001-v0008",
      "profile": "config/compiler-profiles/msvc-2019-x86-release.json",
      "selections": {"optimization": "O2", "favor": "speed", "whole_program": "true"},
      "score": 4.0,
      "comparison": {"classification": "byte_matched"}
    },
    {
      "id": "p000-v0005",
      "profile": "config/compiler-profiles/msvc-2019-x86-debug.json",
      "selections": {"optimization": "O0", "favor": "blend", "whole_program": "false"},
      "score": 2.15,
      "comparison": {"classification": "instruction_similar"}
    },
    {
      "id": "p002-v0011",
      "profile": "config/compiler-profiles/clang-15-x86-o2.json",
      "selections": {"optimization": "O2", "favor": "speed", "whole_program": "true"},
      "score": 0.0,
      "comparison": {"classification": "mismatch"}
    }
  ]
}
```

!!! tip "Finding the right compiler profile"
    Run the compiler lab early in a matching decompilation project. The best-scoring
    profile tells you which compiler and flags the original binary was built with.
    Use this profile for all subsequent matching work.

## With Extra Arguments

Matrix axes values are passed as compiler arguments. The `compile` command receives them as
`--extra-arg` values:

```json
"matrix": {
  "axes": {
    "opt": ["/O2", "/O1", "/Od"],
    "arch": ["/arch:IA32", "/arch:SSE2"]
  }
}
```

Each combination: `/O2 /arch:IA32`, `/O1 /arch:IA32`, `/Od /arch:IA32`, `/O2 /arch:SSE2`, etc.

## Practical Example: Identifying Original Compiler

1. Extract a known small function from the PE:

```bash
x86decomp coff-extract --input original.obj --symbol _SmallFunc@0 \
  --output reference.bin
```

2. Write a candidate C source for that function in `candidate.c`.

3. Create `lab.json` with all plausible MSVC versions and optimization flags:

```json
{
  "source": "candidate.c",
  "profiles": [
    "profiles/msvc-2015-x86.json",
    "profiles/msvc-2017-x86.json",
    "profiles/msvc-2019-x86.json",
    "profiles/msvc-2022-x86.json"
  ],
  "matrix": {
    "axes": {
      "opt": ["/O2", "/Ox", "/O1", "/Od"],
      "whole_program": ["/GL", "/GL-"],
      "intrinsic": ["/Oi", "/Oi-"]
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

4. Run and inspect best:

```bash
x86decomp compiler-lab --lab lab.json --report lab-report.json
```

5. The top result tells you: "MSVC 2019, /O2, no whole-program optimization, intrinsics
   enabled" produced a byte match. That's your target compiler profile.

## Fallback on Compilation Error

When a profile/argument combination fails to compile, the experiment records the error and
a score of -1.0. These are ranked last in the report.

## Integration with Evidence

Lab results can be recorded as `compiler_output` evidence:

```bash
x86decomp evidence-add --project . \
  --kind compiler_output \
  --source "Compiler lab experiment p001-v0008" \
  --locator "lab:lab-manifest.json:experiment:p001-v0008" \
  --assertion "MSVC 2019 /O2 /Oi produces byte-matched output for _SmallFunc@0" \
  --independent-group "compiler-lab" \
  --file "./compiler-lab-output/p001-v0008/candidate.obj"
```
