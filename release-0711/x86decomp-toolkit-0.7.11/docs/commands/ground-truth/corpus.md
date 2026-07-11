# Corpus Commands

Ground-truth corpus creation, building, verification, and comparison. The corpus records source hashes, compiler hashes and versions, complete command lines, environment policy, COFF structure, symbols, COMDAT metadata, and output hashes.

---

## `x86decomp corpus-create-manifest`

Create the bundled compiler ground-truth manifest from a repository directory.

### Purpose

Scans a compiler repository for available toolchain executables and emits a reproducible manifest that declares every compiler/version/flag combination to build. The manifest is the input contract for `corpus-build`.

### Syntax

```
x86decomp corpus-create-manifest REPOSITORY OUTPUT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REPOSITORY` | yes | path | Directory containing compiler executables and version metadata |
| `OUTPUT` | yes | path | Output path for the generated JSON manifest |

### Files read

- `REPOSITORY` — compiler repository directory tree

### Files written

- `OUTPUT` — JSON ground-truth corpus manifest

### Example

```console
$ x86decomp corpus-create-manifest ./compiler-repo corpus-manifest.json
```

---

## `x86decomp corpus-build`

Build a reproducible compiler/version ground-truth corpus from a manifest.

### Purpose

Reads a corpus manifest and executes every declared compiler/version/flag combination. Each build records source hash, compiler executable hash, version string, full command line, environment, COFF object metadata, and output hash. Results are written as a structured report.

### Syntax

```
x86decomp corpus-build MANIFEST OUTPUT_DIR [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `MANIFEST` | yes | path | JSON corpus manifest (from `corpus-create-manifest`) |
| `OUTPUT_DIR` | yes | path | Directory for compiled outputs and intermediate artifacts |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON corpus report to this path |

### Files read

- `MANIFEST` — JSON corpus manifest

### Files written

- `OUTPUT_DIR` — compiled object files and artifacts
- `--report REPORT` — structured JSON corpus build report

### Example

```console
$ x86decomp corpus-build corpus-manifest.json build/corpus/ --report reports/corpus-build.json
```

---

## `x86decomp corpus-verify`

Verify source and output hashes in a ground-truth corpus report.

### Purpose

Re-checks every source and output hash recorded in a corpus build report against the current filesystem. Reports mismatches with exact path and expected-vs-observed hash values.

### Syntax

```
x86decomp corpus-verify REPORT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REPORT` | yes | path | JSON corpus build report to verify |

### Files read

- `REPORT` — JSON corpus build report

### Example

```console
$ x86decomp corpus-verify reports/corpus-build.json
```

---

## `x86decomp corpus-compare`

Compare compiler/version ground-truth corpus reports.

### Purpose

Accepts two or more corpus build reports and compares them by compiler version, flag matrix, and per-case output hashes. Reports which cases are byte-identical across corpora and which differ.

### Syntax

```
x86decomp corpus-compare REPORTS... [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REPORTS` | yes | path (1+) | Two or more corpus build report paths to compare |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON comparison report to this path |

### Files read

- `REPORTS` — two or more JSON corpus build reports

### Files written

- `--report REPORT` — JSON comparison report

### Example

```console
$ x86decomp corpus-compare reports/msvc-2019.json reports/msvc-2022.json \
    --report reports/corpus-compare.json
```

---

## `x86decomp corpus-generate`

Generate a deterministic parameterized C/C++ source corpus.

### Purpose

Produces a deterministic set of C and C++ source files using a seeded random number generator. Each file exercises specific language features (control flow, integer sizes, struct layouts, calling conventions) to serve as compiler test inputs. The source files and a manifest recording per-file identities are written to the output directory.

### Syntax

```
x86decomp corpus-generate OUTPUT_DIR [--cases-per-family N] [--seed SEED] [--c-only] [--cpp-only] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `OUTPUT_DIR` | yes | path | Directory for generated source files and manifest |

### Options

| Option | Default | Description |
|---|---|---|
| `--cases-per-family N` | `8` | Number of cases to generate per source family |
| `--seed SEED` | `0x86DEC0DE` | Deterministic random seed (decimal or hex with `0x` prefix) |
| `--c-only` | false | Generate only C sources (mutually exclusive with `--cpp-only`) |
| `--cpp-only` | false | Generate only C++ sources (mutually exclusive with `--c-only`) |
| `--report REPORT` | none | Write structured JSON generation report to this path |

!!! warning "Mutual exclusion"
    `--c-only` and `--cpp-only` are mutually exclusive. If neither is specified, both C and C++ sources are generated.

### Files written

- `OUTPUT_DIR` — generated `.c` and/or `.cpp` source files plus manifest
- `--report REPORT` — JSON generation report

### Example

```console
$ x86decomp corpus-generate generated-corpus/ --cases-per-family 16 --seed 0xCAFE \
    --report reports/corpus-generate.json

$ x86decomp corpus-generate generated-corpus/ --c-only --cases-per-family 8
```

---

## `x86decomp corpus-generated-verify`

Verify generated corpus source identities.

### Purpose

Re-checks every source file identity recorded in a corpus generation report against the current filesystem. Verifies that no file has been modified, added, or removed since generation.

### Syntax

```
x86decomp corpus-generated-verify REPORT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REPORT` | yes | path | JSON corpus generation report (from `corpus-generate`) |

### Files read

- `REPORT` — JSON generation report

### Example

```console
$ x86decomp corpus-generated-verify reports/corpus-generate.json
```

### Related commands

- [benchmark-run](benchmarks.md) — Run benchmarks against a corpus
- [corpus-create-manifest](#x86decomp-corpus-create-manifest) — Create the compiler manifest
- [corpus-build](#x86decomp-corpus-build) — Build the corpus from a manifest
