# Benchmark Validation Corpus

**Solar Knights** — A fictional space combat game compiled for x86-64 Windows PE. The
decompilation team needs a repeatable benchmark corpus to validate toolchain accuracy, measure
decompilation progress, and guard against regressions across the full relink pipeline.

---

## Scenario

> Solar Knights is a large x86-64 title with over 8,000 functions. The team has identified
> the target compiler as MSVC 2019 but needs to build a ground-truth corpus that exercises
> every language feature used in the game: integer arithmetic, floating-point (SSE/x87),
> struct layout, calling conventions, control flow, and template instantiations. The corpus
> must be deterministic and reproducible so that every benchmark run produces identical
> results on any machine with the same toolchain.

## What you will accomplish

1. Create a compiler ground-truth manifest from a toolchain repository
2. Build the corpus — compile every source under every declared compiler/flag combination
3. Verify the corpus against recorded source and output hashes
4. Generate a deterministic synthetic C/C++ source corpus for additional coverage
5. Verify the generated corpus integrity
6. Run the benchmark corpus against the ground-truth reference
7. Record benchmark results as evidence

## Prerequisites

- x86decomp 0.7.11 installed
- A compiler repository directory containing at least one toolchain
- The target binary `games/solarknights/solarknights.exe` (x86-64 PE)
- At least 2 GB of free disk space for corpus outputs

## Starting file structure

```
games/solarknights/
  solarknights.exe            # The target PE (x86-64, ~12 MB)

projects/solarknights-decomp/  # Decompilation project (already initialized)

compiler-repo/
  # Directory containing compiler executable metadata for corpus manifest generation
```

---

## Step 1: Create the compiler ground-truth manifest

```console
$ x86decomp corpus-create-manifest compiler-repo/ corpus-manifest.json
```

**Explanation:** `corpus-create-manifest` scans a compiler repository directory for available
toolchain executables and emits a reproducible JSON manifest that declares every compiler/version/flag
combination to build. The manifest serves as the input contract for `corpus-build`. The repository
must contain compiler executables and version metadata.

**Expected output — manifest fragment:**

```json
{
  "schema_version": 1,
  "repository": "compiler-repo",
  "toolchains": [
    {
      "id": "msvc-2019-x64",
      "family": "msvc",
      "version": "19.29.30137",
      "executables": {
        "compiler": { "path": "...", "sha256": "..." }
      }
    }
  ],
  "source_families": [...],
  "matrix": {
    "optimization": ["/O2", "/O1", "/Od", "/Ox"],
    "floating_point": ["/fp:precise", "/fp:fast"]
  }
}
```

---

## Step 2: Build the ground-truth corpus

```console
$ x86decomp corpus-build corpus-manifest.json build/corpus/ \
    --report reports/corpus-build.json
```

**Explanation:** `corpus-build` reads the manifest and executes every declared compiler/version/flag
combination. Each build records: source file SHA-256, compiler executable SHA-256, version string,
full command line, environment state, COFF object metadata (sections, symbols, relocations,
COMDAT info), and output object SHA-256. All results are written to the structured JSON report.
Output objects are stored in `build/corpus/`.

**Expected directory structure:**

```
build/corpus/
  msvc-2019-x64/
    O2_fp_precise/
      case_001.obj
      case_002.obj
      ...
    O1_fp_precise/
      case_001.obj
      ...
reports/
  corpus-build.json      # Full structured corpus report
```

---

## Step 3: Verify the corpus

```console
$ x86decomp corpus-verify reports/corpus-build.json
```

**Explanation:** `corpus-verify` re-checks every source and output SHA-256 recorded in the corpus
build report against the current filesystem. Reports mismatches with the exact file path and
expected-vs-observed hash values. This is the integrity gate — a passing verification means every
file in the corpus is bit-identical to when it was built.

**Expected output:**

```json
{
  "schema_version": 1,
  "report": "reports/corpus-build.json",
  "valid": true,
  "total_entries": 384,
  "mismatches": [],
  "missing": []
}
```

!!! warning "Hash mismatches"
    If `valid` is `false`, the `mismatches` array lists each file with its expected and observed
    hashes. Common causes: compiler executable was updated, source file was edited, or output
    directory was cleaned. Rebuild the corpus with `corpus-build` if toolchains changed.

---

## Step 4: Generate a deterministic synthetic source corpus

```console
$ x86decomp corpus-generate generated-corpus/ \
    --cases-per-family 16 \
    --seed 0xCAFE \
    --report reports/corpus-generate.json
```

**Explanation:** `corpus-generate` produces a deterministic set of C and C++ source files using a
seeded PRNG (default seed `0x86DEC0DE`). Each file exercises specific language features: control
flow (if/else, switch, loops), integer sizes (int8_t through int64_t), struct layouts (packed,
aligned, bitfields), calling conventions, and pointer arithmetic. `--cases-per-family` controls
how many cases are generated per source family; `--seed` ensures deterministic output across runs.

!!! tip "C-only or C++-only"
    Use `--c-only` to generate only C source files, or `--cpp-only` for only C++ sources.
    These flags are mutually exclusive. If neither is specified, both C and C++ are generated.

**Expected output structure:**

```
generated-corpus/
  manifest.json                # Per-file identities and hashes
  case_0001.c
  case_0001.cpp
  case_0002.c
  case_0002.cpp
  ... (up to case_0016 per language)
```

---

## Step 5: Verify the generated corpus

```console
$ x86decomp corpus-generated-verify reports/corpus-generate.json
```

**Explanation:** `corpus-generated-verify` re-checks every source file identity recorded in the
generation report against the current filesystem. Verifies that no file has been modified, added,
or removed since generation. This ensures the synthetic corpus is pristine before it enters the
benchmark pipeline.

**Expected output:**

```json
{
  "report": "reports/corpus-generate.json",
  "valid": true,
  "total_files": 32,
  "modified": [],
  "missing": [],
  "added": []
}
```

---

## Step 6: Create the benchmark manifest

Create `benchmarks/solarknights-validation.json`:

```json
{
  "cases": [
    {
      "kind": "byte_pair",
      "label": "corpus_bytematch_msvc2019_O2_case001",
      "target": "build/corpus/msvc-2019-x64/O2_fp_precise/case_001.obj",
      "candidate": "build/corpus/msvc-2019-x64/O2_fp_precise/case_001.obj",
      "expect": { "matched": true }
    },
    {
      "kind": "pe_coff",
      "label": "function_spawn_enemy_byte_match",
      "target": "original/solarknights.exe",
      "target_rva": "0x140001000",
      "target_size": "128",
      "candidate": "build/candidates/spawn_enemy.obj",
      "symbol": "?SpawnEnemy@@YAXH@Z",
      "expect": { "classification": "byte_matched" }
    },
    {
      "kind": "dynamic",
      "label": "physics_tick_dynamic_validate",
      "target": "bin/target_physics_tick.bin",
      "candidate": "bin/candidate_physics_tick.bin",
      "harness": "harnesses/physics_tick_harness.json",
      "expect": { "differentially_validated": true }
    },
    {
      "kind": "symbolic",
      "label": "damage_calc_symbolic_validate",
      "target": "bin/target_damage_calc.bin",
      "candidate": "bin/candidate_damage_calc.bin",
      "architecture": "x86_64",
      "input_registers": ["rcx", "rdx", "r8"],
      "stack_argument_words": 0,
      "output_registers": ["rax"],
      "max_steps": 1000,
      "max_paths": 64,
      "expect": { "result": "equivalent" }
    },
    {
      "kind": "discovery_metrics",
      "label": "function_discovery_recall",
      "expected_function_count": 8427,
      "discovered_functions": 8203,
      "expect": { "recall": 0.95, "precision": 0.90, "minimum_f1": 0.92 }
    }
  ]
}
```

**Benchmark kinds summary:**

| Kind | What it validates |
|---|---|
| `byte_pair` | Exact byte-for-byte identity between two files |
| `pe_coff` | PE function body matches an extracted COFF symbol |
| `dynamic` | Differential Unicorn execution with a harness |
| `symbolic` | Bounded symbolic equivalence via Z3 |
| `integration` | Declared integration scenario observations |
| `discovery_metrics` | True-positive rate for function/type discovery |

---

## Step 7: Run the benchmark corpus

```console
$ x86decomp benchmark-run benchmarks/solarknights-validation.json \
    --report reports/benchmark-results.json
```

**Explanation:** `benchmark-run` executes every case declared in the manifest. Each case is run
independently: byte pairs are diffed, PE functions are compared against COFF symbols, dynamic
and symbolic validation is performed, and discovery metrics are computed. Results are compared
against declared expectations. The report records per-case pass/fail, timing, and detailed
comparison output.

**Expected output (abbreviated):**

```json
{
  "manifest": "benchmarks/solarknights-validation.json",
  "total_cases": 5,
  "passed": 4,
  "failed": 1,
  "cases": [
    {
      "label": "corpus_bytematch_msvc2019_O2_case001",
      "kind": "byte_pair",
      "passed": true,
      "result": { "match": true },
      "elapsed_ms": 12.3
    },
    {
      "label": "function_spawn_enemy_byte_match",
      "kind": "pe_coff",
      "passed": true,
      "result": { "classification": "byte_matched" },
      "elapsed_ms": 45.7
    }
  ],
  "summary": {
    "total_elapsed_ms": 2834.1,
    "pass_rate": 0.8
  }
}
```

---

## Step 8: Record benchmark results as evidence

```console
$ x86decomp evidence-add projects/solarknights-decomp/ \
    --kind compiler_output \
    --source "Benchmark corpus: solarknights-validation" \
    --locator "benchmarks/solarknights-validation.json" \
    --assertion "4/5 benchmark cases passed; MSVC 2019 /O2 produces byte-identical output for ground-truth corpus" \
    --independent-group "benchmark-validation" \
    --file reports/benchmark-results.json \
    --id ev-benchmark-20260711

$ x86decomp evidence-add projects/solarknights-decomp/ \
    --kind compiler_output \
    --source "Synthetic corpus generation" \
    --locator "reports/corpus-generate.json" \
    --assertion "32 deterministic source files generated with seed 0xCAFE, all identities verified" \
    --independent-group "corpus-generation" \
    --file reports/corpus-generate.json \
    --id ev-corpus-generated
```

**Explanation:** Each benchmark run becomes `compiler_output` evidence in the project. This evidence
can later be attached to claims about compiler identity, function correctness, or toolchain accuracy
through the `claim-create` and `claim-attach` commands.

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `corpus-build` reports missing compiler | Toolchain not registered in the corpus manifest | Run `corpus-create-manifest` with the correct repository directory |
| `corpus-verify` reports hash mismatches | Output objects were rebuilt or modified | Rebuild with `corpus-build` or restore from backup |
| `corpus-generate` produces different files on different machines | Different Python version or platform | The generator uses `random` with a fixed seed — verify Python 3.11+ and identical platform |
| `benchmark-run` times out on symbolic cases | Path explosion or large max-steps | Reduce `max_paths` or `max_steps` in benchmark manifest |
| `benchmark-run` fails with `ExternalToolError` | Missing optional dependencies | Install with `pip install x86decomp-toolkit[dynamic,symbolic]` |
| `corpus-generated-verify` reports added files | Manual edits or temp files in the corpus directory | Clean the directory and re-generate |

---

## Related reference pages

- [Corpus Commands](../commands/ground-truth/corpus.md) — `corpus-create-manifest`, `corpus-build`, `corpus-verify`, `corpus-generate`, `corpus-generated-verify`, `corpus-compare`
- [benchmark-run command](../commands/ground-truth/benchmarks.md) — Benchmark manifest structure and kinds
- [Evidence and Claims Commands](../commands/workflow/evidence-claims.md) — `evidence-add`, `claim-create`
- [Compiler Laboratory concept](../concepts/compiler-laboratory.md) — Matrix experiments and scoring
- [Compiler Laboratory workflow](compiler-laboratory.md) — Identifying the original compiler
- [Reproducibility concept](../concepts/reproducibility.md) — Reproducible builds and verification

---

## Optional extensions

1. **Cross-compiler comparison** — Run `corpus-compare` with two corpus build reports to identify
   which optimizations produce identical output across MSVC versions:

   ```console
   $ x86decomp corpus-compare reports/corpus-msvc2019.json reports/corpus-msvc2022.json \
       --report reports/corpus-cross-compare.json
   ```

2. **Incremental benchmark** — Add new cases to the benchmark manifest as functions are decompiled.
   Run `benchmark-run` after each batch to track the growing pass rate.

3. **CI integration** — Automate `corpus-build && corpus-verify && benchmark-run` in CI with a
   reproducibility manifest (`x86decomp reproduce-create`) to lock toolchain versions.

4. **Coverage-guided corpus** — After running `drcov-run` on the target game, use the coverage log
   to identify which language features are exercised at runtime. Feed those feature families into
   `corpus-generate` for targeted coverage.

5. **Release-gate integration** — Feed the benchmark report into `x86decomp release-gate` with
   `--require-workflows` to enforce that all benchmark cases pass before a release is accepted.
