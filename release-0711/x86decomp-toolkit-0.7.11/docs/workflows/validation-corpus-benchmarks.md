# Validation Corpus Benchmarks

**Technical objective:** Systematic benchmark corpus construction and execution — ground-truth corpus building, synthetic corpus generation, multi-compiler benchmarking, cache-accelerated compilation, and comparative analysis.

**Game:** Thunder Rally (fictional arcade racer, x86 PE32, MSVC 2010, 2.8 MB executable, diverse function sizes from 16 to 4,096 bytes).

---

## Overview

Thunder Rally has 1,200+ functions spanning arithmetic helpers (16 bytes) to full physics solvers (4,096 bytes). The team needs to establish which compiler/optimization combinations produce byte-identical output for which function categories, then build a reusable benchmark corpus that validates match rates across toolchains. A synthetic corpus fills gaps for edge cases not found in the original binary.

You will learn:

1. How to build a ground-truth corpus from the project's functions.
2. How to generate a synthetic corpus for edge-case coverage.
3. How to run benchmarks with compiler-lab matrix experiments.
4. How to use compilation caching for repeated runs.
5. How to compare benchmark results across compiler/version combinations.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/thunder-rally/thunder_rally.exe` — PE32 x86 |
| **Project** | `games/thunder-rally/project/` |
| **Toolchains** | MSVC 2010, MSVC 2015, MSVC 2019, GCC 9.3 (MinGW), Clang 14 |
| **Compiler profiles** | 15 profiles (5 compilers x 3 optimization levels each) |
| **Disk space** | ~3 GB for corpus build artifacts |

---

## Starting directory structure

```
games/thunder-rally/
├── thunder_rally.exe
└── project/
    ├── project.json
    ├── config/
    │   ├── compiler-profiles/
    │   │   ├── msvc2010-o2.json
    │   │   ├── msvc2015-o2.json
    │   │   ├── msvc2019-o2.json
    │   │   ├── gcc-9.3-o2.json
    │   │   └── clang-14-o2.json
    │   ├── benchmarks/
    │   │   ├── function-corpus-manifest.json
    │   │   └── synthetic-corpus-manifest.json
    │   └── labs/
    │       └── compiler-matrix.json
    ├── src/
    │   └── matched/
    ├── build/
    │   ├── cache/
    │   └── candidates/
    ├── reports/
    │   └── benchmarks/
    └── corpus/
        ├── ground-truth/
        └── synthetic/
```

---

## Step 1: Build a ground-truth compiler corpus

First, create a manifest for the bundled ground-truth source repository:

```console
$ x86decomp corpus-create-manifest games/thunder-rally/project/src/matched/ \
    games/thunder-rally/project/config/benchmarks/function-corpus-manifest.json
```

**What happens:** `corpus-create-manifest` scans the source directory and produces a manifest listing every source file with its SHA-256, the expected compiler profiles, and the output-naming scheme. The manifest is the input to `corpus-build`.

Build the corpus:
```console
$ x86decomp corpus-build games/thunder-rally/project/config/benchmarks/function-corpus-manifest.json \
    games/thunder-rally/corpus/ground-truth/ \
    --report games/thunder-rally/project/reports/benchmarks/ground-truth-corpus.json
```

**What happens:** `corpus-build` compiles every source in the manifest under every declared compiler profile, produces COFF objects, extracts function symbols, and records:
- Source SHA-256
- Compiler profile (family, version, flags)
- Output COFF SHA-256
- Symbol table with sizes and section assignments
- Compilation time and exit code

This produces a directory tree:
```
corpus/ground-truth/
├── msvc2010-o2/
│   ├── func_401000.obj
│   ├── func_401200.obj
│   └── ...
├── msvc2015-o2/
│   └── ...
└── gcc-9.3-o2/
    └── ...
```

Verify the corpus:
```console
$ x86decomp corpus-verify games/thunder-rally/project/reports/benchmarks/ground-truth-corpus.json
```

**What happens:** `corpus-verify` re-checks every SHA-256 in the corpus report against the actual files. Any mismatch (file changed after report generation) is flagged.

---

## Step 2: Generate a synthetic corpus for edge cases

The original binary's functions don't cover every compiler idiom. Generate a parameterized synthetic corpus:

```console
$ x86decomp corpus-generate games/thunder-rally/corpus/synthetic/ \
    --cases-per-family 16 \
    --seed 0x86DEC0DE \
    --c-only \
    --report games/thunder-rally/project/reports/benchmarks/synthetic-corpus-gen.json
```

**What happens:** `corpus-generate` produces a deterministic C source corpus from parameterized templates:

| Flag | Effect |
|---|---|
| `--cases-per-family 16` | Each family (prologue, arithmetic, control-flow, calling-convention, data-access, floating-point, etc.) gets 16 variants |
| `--seed 0x86DEC0DE` | Deterministic seed — same seed always produces the same corpus |
| `--c-only` | Only C sources; `--cpp-only` would restrict to C++; omit both for mixed |
| `--report` | Records every generated source's identity and template parameters |

The output directory contains:
```
corpus/synthetic/
├── report.json
├── prologue/
│   ├── case_000.c
│   ├── case_001.c
│   └── ... (16 files)
├── arithmetic/
│   └── ... (16 files)
├── control-flow/
│   └── ...
└── ... (8+ families)
```

Verify the generated corpus:
```console
$ x86decomp corpus-generated-verify games/thunder-rally/project/reports/benchmarks/synthetic-corpus-gen.json
```

**What happens:** `corpus-generated-verify` confirms every generated source matches its declared identity (template, seed, case index). This ensures the corpus is authentic and has not been hand-edited.

Now build the synthetic corpus into COFF objects:
```console
$ x86decomp corpus-build games/thunder-rally/project/config/benchmarks/synthetic-corpus-manifest.json \
    games/thunder-rally/corpus/synthetic-compiled/ \
    --report games/thunder-rally/project/reports/benchmarks/synthetic-corpus-compiled.json
```

---

## Step 3: Run a compiler-lab matrix experiment

Create a `compiler-lab` manifest (`games/thunder-rally/project/config/labs/compiler-matrix.json`):

```json
{
  "lab_id": "thunder-rally-compiler-matrix-v1",
  "axes": [
    {"name": "compiler", "values": ["msvc2010", "msvc2015", "msvc2019", "gcc-9.3", "clang-14"]},
    {"name": "optimization", "values": ["Od", "O1", "O2"]}
  ],
  "source_corpus": "../corpus/synthetic/",
  "compare_against": "../corpus/ground-truth/"
}
```

Run the lab:
```console
$ x86decomp compiler-lab games/thunder-rally/project/config/labs/compiler-matrix.json \
    --report games/thunder-rally/project/reports/benchmarks/compiler-matrix-report.json
```

**What happens:** `compiler-lab` executes the full matrix (5 compilers x 3 optimization levels = 15 combinations), compiles every source in the corpus under each combination, collects compilation statistics, and reports match rates against the ground truth.

---

## Step 4: Run benchmarks with cache acceleration

Individual function benchmarks with cache:
```console
$ x86decomp compile games/thunder-rally/project/config/compiler-profiles/msvc2010-o2.json \
    games/thunder-rally/project/src/matched/func_401000.c \
    games/thunder-rally/project/build/candidates/func_401000.obj \
    --cache games/thunder-rally/project/build/cache/ \
    --report games/thunder-rally/project/reports/benchmarks/compile-401000.json
```

**What happens:** `compile --cache` stores compilation results by content hash. On subsequent runs with the same source and profile, the cached COFF is returned without re-invoking the compiler. This dramatically speeds up repeated benchmark runs.

Run the full benchmark corpus:
```console
$ x86decomp benchmark-run games/thunder-rally/project/config/benchmarks/function-corpus-manifest.json \
    --report games/thunder-rally/project/reports/benchmarks/benchmark-run-2026-07-11.json
```

**What happens:** `benchmark-run` executes all benchmarks declared in the manifest and emits measured results:
- Per-function compilation time (ms)
- Per-function match status (exact, mismatch, compile-failed)
- Per-compiler match rate (percentage of functions matching)
- Total elapsed time
- Cache hit rate

---

## Step 5: Compare benchmark results across corpora

Compare the ground-truth corpus against the synthetic corpus results:
```console
$ x86decomp corpus-compare \
    games/thunder-rally/project/reports/benchmarks/ground-truth-corpus.json \
    games/thunder-rally/project/reports/benchmarks/synthetic-corpus-compiled.json \
    --report games/thunder-rally/project/reports/benchmarks/corpus-comparison.json
```

**What happens:** `corpus-compare` diffs two corpus reports side-by-side:
- **Matched in both:** Functions that produce byte-identical output in both corpora
- **Matched in ground-truth only:** Functions whose synthetic version differs (possible template gap)
- **Matched in synthetic only:** Functions whose ground-truth source is not yet byte-accurate
- **Size deltas:** Per-function size differences between corpora
- **Compiler-specific patterns:** Which compilers match more functions in which corpus

Example comparison output:
```json
{
  "corpus_a": "ground-truth-corpus",
  "corpus_b": "synthetic-corpus-compiled",
  "common_functions": 895,
  "a_only_matched": 341,
  "b_only_matched": 67,
  "both_matched": 554,
  "per_compiler": {
    "msvc2010-o2": {"match_rate_a": 0.92, "match_rate_b": 0.88, "delta": -0.04},
    "msvc2019-o2": {"match_rate_a": 0.94, "match_rate_b": 0.91, "delta": -0.03}
  }
}
```

Compare the compiler-lab matrix results against the benchmark run:
```console
$ x86decomp corpus-compare \
    games/thunder-rally/project/reports/benchmarks/compiler-matrix-report.json \
    games/thunder-rally/project/reports/benchmarks/benchmark-run-2026-07-11.json \
    --report games/thunder-rally/project/reports/benchmarks/lab-vs-benchmark.json
```

---

## Step 6: Drill into individual function differences

For any function that mismatches, compare directly:
```console
$ x86decomp diff-function games/thunder-rally/thunder_rally.exe \
    0x1000 48 \
    games/thunder-rally/corpus/synthetic-compiled/msvc2010-o2/prologue_case_000.obj \
    _prologue_case_000 \
    --report games/thunder-rally/project/reports/benchmarks/func-diff-401000.json
```

**What happens:** `diff-function` gives byte-level detail on exactly which offsets differ, helping diagnose whether the mismatch is in compiler padding, register selection, instruction encoding, or relocation resolution.

---

## Expected state after each stage

| Stage | Key deliverable |
|---|---|
| **corpus-create-manifest** | Manifest JSON for the ground-truth corpus |
| **corpus-build** | Compiled COFF objects for every source-compiler pair; corpus report |
| **corpus-verify** | Verification confirming all hashes in the report are correct |
| **corpus-generate** | Synthetic C source corpus with deterministic identities |
| **corpus-generated-verify** | Verification of synthetic source identities |
| **compiler-lab** | Matrix experiment report — match rates across 15 combinations |
| **benchmark-run** | Timing and match-rate measurements |
| **corpus-compare** | Comparative analysis between corpora and compiler profiles |

---

## Verification checklist

- [ ] `corpus-verify` passes — all ground-truth COFF hashes match their recorded values
- [ ] `corpus-generated-verify` passes — all synthetic sources have valid identities
- [ ] `compiler-lab` completes all 15 matrix cells without failures
- [ ] `benchmark-run` reports non-zero cache hit rate for repeated compilations
- [ ] No function regresses in match rate between corpus builds
- [ ] `corpus-compare` identifies specific functions and compilers that differ

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `corpus-build` fails for specific compiler | Toolchain not registered for that compiler | Run `toolchain-register` for the missing compiler |
| `corpus-build` produces zero-byte COFF | Source compile error under that profile | Check the source against the compiler's C standard version; use `--extra-arg` to add compatibility flags |
| `corpus-generate` seed changes between runs | Someone modified the seed parameter | Use the exact seed in the report; regenerate with the same seed |
| `benchmark-run` cache misses on repeated runs | Source file modified between runs | Lock source files with `source lock` canonical command before benchmarking |
| `corpus-compare` shows unexpected regressions | Compiler profile flags changed | Verify profiles with `toolchain-verify`; diff profile JSONs with `diff-bytes` |
| `compiler-lab` times out for large matrix | Matrix too large for available resources | Split into smaller lab manifests; run sequentially |

---

## Related reference pages

- [Corpus Commands](../commands/ground-truth/corpus.md)
- [benchmark-run](../commands/ground-truth/benchmarks.md)
- [compiler-lab](../commands/compilation/compiler-lab.md)
- [compile](../commands/compilation/compile.md)
- [Toolchains](../commands/compilation/toolchains.md)
- [diff-function](../commands/validation/diff-function.md)
- [Benchmark Corpus Configuration](../config/benchmark-corpus.md)
- [Compiler Profile](../config/compiler-profile.md)

---

## Optional extensions

1. **Cross-architecture corpus:** Generate the same synthetic corpus with `--seed 0x86DEC0DE` and build it for both `x86` and `x86_64`. Compare with `corpus-compare` to identify architecture-specific compiler behaviors.

2. **Coverage-guided corpus expansion:** Run `drcov-run` on the original binary, parse with `drcov-parse`, and identify functions with zero coverage. Generate additional synthetic sources that exercise those uncovered paths.

3. **Nightly benchmark pipeline:** Create a `pipeline-create` manifest that chains `corpus-build` → `corpus-verify` → `benchmark-run` → `corpus-compare` → `evidence-add`. Run nightly via `pipeline-run` to catch regressions early.

4. **objdiff integration:** For functions that are close but not byte-identical, run `objdiff-run` with a comparison manifest to get visual diff output:
   ```console
   $ x86decomp objdiff-run games/thunder-rally/project/config/benchmarks/objdiff-manifest.json \
       --report objdiff-report.json
   ```

5. **Toolchain matrix expansion:** Register additional toolchains (GCC 11, Clang 16, MSVC 2022) with `toolchain-register` and add them to the compiler-lab matrix to measure match rates across modern toolchains.
