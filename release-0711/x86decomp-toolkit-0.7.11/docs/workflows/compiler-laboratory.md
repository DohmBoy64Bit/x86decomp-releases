# Compiler Laboratory

**Aegis Protocol** — A fictional real-time strategy game compiled for x86 Windows PE. The original
build environment is lost to history — no build scripts, no compiler version metadata, no PDB.
The decompilation team must identify the exact compiler and flags that produced the shipped binary.

---

## Scenario

> Aegis Protocol shipped in 2004 as a single `aegis.exe`. Community analysis has confirmed it
> is an x86 PE with no debug symbols. The MSVC runtime imports suggest MSVC 6.0 through 2003,
> but none of the entry-point byte patterns match known signatures exactly. The team suspects a
> custom optimization flag combination. They need to register several candidate toolchains, run
> a matrix experiment against a known small function, and verify the winning profile with the
> compiler worker.

## What you will accomplish

1. Register multiple candidate toolchains in the registry with hash verification
2. Snapshot the current tool environment for reproducibility
3. Extract a known function from the target binary
4. Write a candidate C source for that function
5. Create a compiler lab manifest with a matrix of profiles and flags
6. Run the compiler lab and identify the best-scoring experiment
7. Verify the winning profile with a bounded compilation worker
8. Synthesize a COFF object and diff against the original PE function

## Prerequisites

- x86decomp 0.7.11 installed
- Access to MSVC 6.0, MSVC .NET 2003, and MSVC 2005 compilers (or any version subset)
- The target binary `games/aegis/aegis.exe` (x86 PE)
- A candidate C source file for one known function

## Starting file structure

```
games/aegis/
  aegis.exe                  # The target PE (x86, ~3.5 MB)

projects/aegis-decomp/       # Decompilation project (already initialized)
  config/
    compiler-profiles/        # Will hold compiler profiles
  src/
    staging/                  # Will hold candidate C sources
  build/
    compiler/
    candidates/

toolchains.json              # Will be created by toolchain-register
```

---

## Step 1: Register toolchains

```console
$ x86decomp toolchain-register toolchains.json msvc-6.0-x86 msvc 12.00.8168 \
    --executable "compiler=C:\MSVC\VC98\Bin\cl.exe" \
    --executable "linker=C:\MSVC\VC98\Bin\link.exe"

$ x86decomp toolchain-register toolchains.json msvc-2003-x86 msvc 13.10.3077 \
    --executable "compiler=C:\MSVC2003\VC7\Bin\cl.exe" \
    --executable "linker=C:\MSVC2003\VC7\Bin\link.exe"

$ x86decomp toolchain-register toolchains.json msvc-2005-x86 msvc 14.00.50727 \
    --executable "compiler=C:\MSVC2005\VC\Bin\cl.exe" \
    --executable "linker=C:\MSVC2005\VC\Bin\link.exe"
```

**Explanation:** `toolchain-register` records each compiler executable's path and SHA-256 hash in a
JSON registry file. The registry is user-owned — proprietary compiler binaries are never copied,
only referenced by path. `FAMILY` is a string like `msvc`, `clang`, `gcc`. `VERSION` is the
compiler version string. Each `--executable role=path` maps a role name (e.g., `compiler`,
`linker`) to an absolute executable path. At least one `--executable` is required.

**Verify toolchains:**

```console
$ x86decomp toolchain-verify toolchains.json msvc-6.0-x86
$ x86decomp toolchain-verify toolchains.json msvc-2003-x86
$ x86decomp toolchain-verify toolchains.json msvc-2005-x86
```

**Expected output:**

```json
{"toolchain_id": "msvc-6.0-x86", "valid": true, "failures": []}
```

Each toolchain should return `"valid": true` with an empty `failures` list. If a compiler
executable is missing or its hash changed, `valid` is `false` and `failures` lists each problem.

!!! warning "External references"
    Toolchain executables are never copied or bundled. You must maintain the referenced files
    at their recorded paths and re-register after updates.

---

## Step 2: Snapshot the tool environment

```console
$ x86decomp snapshot-tools --output projects/aegis-decomp/tools.json
```

**Explanation:** `snapshot-tools` records detected external tool versions and paths. The output
JSON file is referenced by reproducibility manifests and release gates to ensure the same tool
versions can be assembled for rebuilds.

---

## Step 3: Create compiler profiles

Create `projects/aegis-decomp/config/compiler-profiles/msvc-6.0-x86-default.json`:

```json
{
  "schema_version": 1,
  "id": "msvc-6.0-x86-default",
  "executable": "C:\\MSVC\\VC98\\Bin\\cl.exe",
  "arguments": ["/nologo", "/c", "/MT", "{source}", "/Fo{output}"],
  "timeout_seconds": 60,
  "output_kind": "coff_object"
}
```

Create `projects/aegis-decomp/config/compiler-profiles/msvc-2003-x86-default.json` with the same
structure but pointing to the 2003 compiler path.

Create `projects/aegis-decomp/config/compiler-profiles/msvc-2005-x86-default.json` similarly.

**Explanation:** A compiler profile is a JSON document (schema version 1 or 2) with required
fields: `schema_version`, `id`, `executable`, `arguments`, `timeout_seconds`, `output_kind`.
The `arguments` array must include `{source}` and `{output}` substitution tokens.

---

## Step 4: Extract a known function from the target PE

First, identify a small, well-understood function in the binary. Using Ghidra or prior analysis:

```console
$ x86decomp coff-extract original/aegis-func.bin _UnknownFunc@8 \
    build/reference-func.bin --size 0x80
```

**Explanation:** `coff-extract` parses a COFF object, locates the named symbol, and writes its
raw data bytes to the output file. The optional `--size` flag validates or truncates the extracted
payload to the expected size. Here we extract `_UnknownFunc@8` (a function with 8 bytes of stack
arguments, likely two 4-byte parameters) from a pre-extracted COFF object.

!!! note "Extracting from the PE directly"
    If you don't have a COFF object, you can extract raw bytes directly from the PE using the
    RVA and size from the Ghidra export or from `inspect-pe` section analysis. Write those bytes
    to a binary file for later use as the `diff-function` target.

---

## Step 5: Write a candidate C source

Create `projects/aegis-decomp/src/staging/unknownfunc.c`:

```c
int __stdcall UnknownFunc(int a, int b) {
    if (a > b) {
        return a - b;
    }
    return b - a;
}
```

This matches the hypothesized `stdcall` convention and two-parameter signature of `_UnknownFunc@8`.

---

## Step 6: Create the compiler lab manifest

Create `projects/aegis-decomp/lab-manifest.json`:

```json
{
  "source": "src/staging/unknownfunc.c",
  "output_root": "compiler-lab-output",
  "cache_root": ".compiler-cache",
  "output_name": "candidate.obj",
  "profiles": [
    "config/compiler-profiles/msvc-6.0-x86-default.json",
    "config/compiler-profiles/msvc-2003-x86-default.json",
    "config/compiler-profiles/msvc-2005-x86-default.json"
  ],
  "matrix": {
    "axes": {
      "optimization": ["/O2", "/O1", "/Ox", "/Od"],
      "inline": ["/Ob1", "/Ob2"],
      "intrinsic": ["/Oi", "/Oi-"],
      "favor": ["/Ot", "/Os"]
    }
  },
  "target": {
    "kind": "pe_function",
    "pe": "original/aegis.exe",
    "rva": "0x401000",
    "size": "128",
    "symbol": "_UnknownFunc@8"
  },
  "max_experiments": 128
}
```

**Explanation:** The lab manifest declares:

- `source` — the C file to compile in every experiment
- `profiles` — array of compiler profile paths
- `matrix.axes` — each axis defines a set of values; the lab runs all combinations
- `target` — what to compare against: `pe_function` (extract from PE and diff) or `file` (diff
  two files)
- `max_experiments` — safety cap; the lab refuses to run if the matrix would exceed this count

With 3 profiles × 4 optimizations × 2 inline × 2 intrinsic × 2 favor = 96 experiments, well
under the cap.

!!! danger "Matrix explosion"
    A matrix with 5 axes of 3 values each × 5 profiles = 1,215 experiments. Set
    `max_experiments` to a reasonable value and review the expected count before running.

---

## Step 7: Run the compiler lab

```console
$ x86decomp compiler-lab projects/aegis-decomp/lab-manifest.json \
    --report projects/aegis-decomp/reports/compiler-lab.json
```

**Explanation:** `compiler-lab` runs every profile × matrix combination. Each experiment compiles
the source under the profile with the axis selections as `--extra-arg` values, extracts the COFF
symbol, normalizes relocations, and compares against the target using `compare_pe_function_to_coff_symbol`.
Results are written to per-experiment directories and ranked in the report.

**Expected output structure:**

```
compiler-lab-output/
  p000-v0000/           # Profile 0 (msvc-6.0), variant 0 (/O2 /Ob1 /Oi /Ot)
    candidate.obj
    compile.json
    comparison.json
  p000-v0001/           # Profile 0, variant 1 (/O2 /Ob1 /Oi /Os)
    ...
  ...
reports/
  compiler-lab.json
```

**Lab report (abbreviated):**

```json
{
  "schema_version": 1,
  "source": "src/staging/unknownfunc.c",
  "experiment_count": 96,
  "best_experiment": "p000-v0000",
  "experiments": [
    {
      "id": "p000-v0000",
      "profile": "config/compiler-profiles/msvc-6.0-x86-default.json",
      "selections": {
        "optimization": "/O2",
        "inline": "/Ob1",
        "intrinsic": "/Oi",
        "favor": "/Ot"
      },
      "score": 4.0,
      "comparison": {"classification": "byte_matched"}
    },
    {
      "id": "p000-v0008",
      "profile": "config/compiler-profiles/msvc-6.0-x86-default.json",
      "selections": {
        "optimization": "/O1",
        "inline": "/Ob2",
        "intrinsic": "/Oi",
        "favor": "/Os"
      },
      "score": 2.15,
      "comparison": {"classification": "instruction_similar"}
    },
    {
      "id": "p001-v0000",
      "profile": "config/compiler-profiles/msvc-2003-x86-default.json",
      "selections": {
        "optimization": "/O2",
        "inline": "/Ob1",
        "intrinsic": "/Oi",
        "favor": "/Ot"
      },
      "score": 0.0,
      "comparison": {"classification": "mismatch"}
    }
  ]
}
```

**Scoring classifications:**

| Classification | Score | Meaning |
|---|---|---|
| `byte_matched` | 4.0 | Relocation-normalized bytes are identical |
| `relocation_normalized_match` | 3.0 | Same codegen, only relocation fixups differ |
| `instruction_similar` | 2.0 | Structurally similar instructions |
| `mismatch` | 0.0 | Different codegen |
| Compilation error | -1.0 | Experiment failed to compile |

---

## Step 8: Analyze the best experiment

From the report, `p000-v0000` scored 4.0 with `byte_matched` — MSVC 6.0 with `/O2 /Ob1 /Oi /Ot`.
This is the likely original compiler and flag combination.

Examine the comparison details:

```json
{
  "id": "p000-v0000",
  "comparison": {
    "classification": "byte_matched",
    "byte_comparison": {
      "match": true,
      "similarity": 1.0
    },
    "instruction_comparison": {
      "instruction_count": 18,
      "matching_instructions": 18
    }
  }
}
```

---

## Step 9: Create the optimal compiler profile

Create `projects/aegis-decomp/config/compiler-profiles/aegis-matched.json` using the winning
combination:

```json
{
  "schema_version": 1,
  "id": "aegis-matched",
  "executable": "C:\\MSVC\\VC98\\Bin\\cl.exe",
  "arguments": [
    "/nologo", "/c", "/MT",
    "/O2", "/Ob1", "/Oi", "/Ot",
    "{source}", "/Fo{output}"
  ],
  "timeout_seconds": 60,
  "output_kind": "coff_object"
}
```

---

## Step 10: Verify the winning profile with a single compile

```console
$ x86decomp compile projects/aegis-decomp/config/compiler-profiles/aegis-matched.json \
    projects/aegis-decomp/src/staging/unknownfunc.c \
    projects/aegis-decomp/build/candidates/unknownfunc.obj \
    --report projects/aegis-decomp/reports/compile-aegis.json \
    --extra-arg /Gd
```

**Explanation:** `compile` runs the compiler profile against one source file. The `--extra-arg`
flag appends additional compiler arguments beyond those in the profile. `--report` writes a
structured compilation report with the output hash, tool version, environment, and timing.
`--cache` (not used here) would enable content-addressed caching to skip redundant builds.

---

## Step 11: Verify with the compiler worker (containerized)

```console
$ x86decomp compile-worker projects/aegis-decomp/config/compiler-profiles/aegis-matched.json \
    projects/aegis-decomp/src/staging/unknownfunc.c \
    projects/aegis-decomp/build/candidates/unknownfunc-worker.obj \
    --isolation local_bounded \
    --report projects/aegis-decomp/reports/compile-worker.json
```

**Explanation:** `compile-worker` copies inputs into an ephemeral workspace and invokes the
compiler profile through a bounded worker. `--isolation local_bounded` runs in a temporary
directory on the host (not a security boundary). For production isolation, use
`--isolation container` with `--container-image`.

!!! warning "Local mode is not a security boundary"
    `--isolation local_bounded` executes the compiler directly on the host. Use
    `--isolation container` when compiling untrusted source or profiles.

---

## Step 12: Synthesize a COFF object and diff against the PE

Extract the compiled symbol and create a synthetic COFF:

```console
$ x86decomp coff-extract projects/aegis-decomp/build/candidates/unknownfunc.obj \
    _UnknownFunc@8 projects/aegis-decomp/build/candidates/unknownfunc-extracted.bin

$ x86decomp coff-synthesize projects/aegis-decomp/build/candidates/unknownfunc-extracted.bin \
    _UnknownFunc@8 projects/aegis-decomp/build/candidates/unknownfunc-synth.obj \
    --architecture x86
```

**Explanation:** `coff-extract` pulls the symbol's raw bytes from the COFF. `coff-synthesize`
wraps raw machine-code bytes into a new COFF object with the given symbol name. The
`--architecture` flag determines the machine type (`0x014C` for x86). Optionally, use
`--relocations` with a JSON relocation file to apply relocation entries.

Now diff the synthesized COFF against the original PE function:

```console
$ x86decomp diff-function projects/aegis-decomp/original/aegis.exe \
    0x401000 128 \
    projects/aegis-decomp/build/candidates/unknownfunc-synth.obj \
    _UnknownFunc@8 \
    --report projects/aegis-decomp/reports/diff-function-aegis.json
```

**Explanation:** `diff-function` extracts the function body from the PE at the given RVA and size,
extracts the matching symbol from the COFF object (with relocation normalization), and performs
both byte-level and instruction-stream comparison. Returns a classification:
`byte_matched`, `relocation_normalized_match`, `instruction_similar`, or `mismatch`.

**Expected output:**

```json
{
  "classification": "byte_matched",
  "byte_comparison": {"match": true, "similarity": 1.0},
  "instruction_comparison": {
    "instruction_count": 18,
    "matching_instructions": 18
  },
  "normalized_similarity": 1.0
}
```

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `toolchain-register` rejects the executable | File does not exist or is not a regular file | Verify the absolute path and that the file is not a symlink |
| `compiler-lab` returns all scores as -1.0 | Compiler profile arguments are incorrect | Test with `compile` first using the same profile and source |
| `diff-function` returns `mismatch` despite `byte_matched` in lab | RVA or size is wrong | Verify the RVA against the Ghidra export's `function.json` |
| Lab exceeds `max_experiments` | Matrix is too large | Reduce axes, reduce profiles, or increase the cap |
| `coff-extract` cannot find symbol | Symbol name does not match (name mangling) | Use `coff-inspect` to list all symbols in the COFF object |
| `compile-worker` fails with container image | Docker/Podman not running or image not pulled | Use `--isolation local_bounded` or pull the container image first |

---

## Related reference pages

- [Compiler Laboratory concept](../concepts/compiler-laboratory.md) — Lab manifest structure and scoring
- [compile / compile-worker commands](../commands/compilation/compile.md) — Compile profiles and worker isolation
- [compiler-lab command](../commands/compilation/compiler-lab.md) — Lab manifest schema and matrix expansion
- [toolchain-register / toolchain-verify commands](../commands/compilation/toolchains.md) — Toolchain registry and verification
- [COFF Commands](../commands/analysis/coff.md) — `coff-inspect`, `coff-extract`, `coff-synthesize`
- [diff-function command](../commands/validation/diff-function.md) — PE function to COFF symbol comparison
- [Compiler Profile schema](../config/compiler-profile.md) — Profile JSON format

---

## Optional extensions

1. **Cross-compiler scoring** — Add `clang` and `gcc` toolchains to the lab manifest to see if
   any open-source compiler produces the same codegen. Some games were built with Intel's compiler
   (`icl`), which shares MSVC compatibility.

2. **Per-function lab** — Run the compiler lab for 3–5 functions across different source files
   (`.c` and `.cpp`). Consistent winning profiles across functions increase confidence in the
   compiler identification.

3. **Cache-accelerated reruns** — Add `"cache_root": ".compiler-cache"` to the lab manifest.
   Subsequent lab runs skip redundant compilations when the source, profile, and arguments are
   unchanged. The cache is content-addressed — identical inputs produce cache hits regardless of
   experiment order.

4. **Evidence recording** — Record the winning experiment as `compiler_output` evidence:

   ```console
   $ x86decomp evidence-add projects/aegis-decomp/ \
       --kind compiler_output \
       --source "Compiler lab experiment p000-v0000" \
       --locator "lab:lab-manifest.json:experiment:p000-v0000" \
       --assertion "MSVC 6.0 /O2 /Ob1 /Oi /Ot produces byte-matched output for _UnknownFunc@8" \
       --independent-group "compiler-lab" \
       --file compiler-lab-output/p000-v0000/comparison.json
   ```

5. **objdiff integration** — After identifying the compiler profile, create an objdiff manifest
   and run:

   ```console
   $ x86decomp objdiff-run objdiff-manifest.json --report reports/objdiff.json
   ```
