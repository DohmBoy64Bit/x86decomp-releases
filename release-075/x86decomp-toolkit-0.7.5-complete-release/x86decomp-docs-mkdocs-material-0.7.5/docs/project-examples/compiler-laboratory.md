---
title: 'Example: compiler identification and compiler laboratory'
description: Register real toolchains, compile a controlled matrix, preserve executable
  provenance, and rank candidate outputs without claiming the historical compiler
  from similarity alone.
original_path: project-examples/compiler-laboratory.html
---

<a id="model"></a>
<a id="compiler-laboratory-flow-title"></a>
<a id="compiler-laboratory-flow-desc"></a>
<a id="arrow-compiler-laboratory"></a>
<a id="compiler-laboratory-flow-caption"></a>
<a id="register"></a>
<a id="profile"></a>
<a id="matrix"></a>
<a id="score"></a>
<a id="corpus"></a>
<a id="worker"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: compiler identification and compiler laboratory

Register real toolchains, compile a controlled matrix, preserve executable provenance, and rank candidate outputs without claiming the historical compiler from similarity alone.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.5 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is a supporting experiment workflow. It can inform matching, but ranking is evidence—not historical attribution.

**On this page**

1. [Laboratory model](#model)
2. [Register toolchains](#register)
3. [Verify profiles](#profile)
4. [Run the matrix](#matrix)
5. [Interpret ranking](#score)
6. [Use ground truth](#corpus)
7. [Bound execution](#worker)
8. [Truth boundary](#limits)
9. [Source basis](#source-basis)

## Laboratory model

Every experiment preserves the executable and input identities used to produce a candidate output.Known source → Toolchain registry → Profile matrix → Bounded compile → Object comparison → Ranked evidence → Independent corroboration

Known sourceToolchain registryProfile matrixBounded compileObject comparisonRanked evidenceIndependent corroboration

Every experiment preserves the executable and input identities used to produce a candidate output.

```ascii-fallback
Known source → Toolchain registry → Profile matrix → Bounded compile → Object comparison → Ranked evidence → Independent corroboration
```

1

## Register and verify the actual toolchain

```
x86decomp toolchain-register config/toolchains.json gcc-13-x86 gcc 13.2 --executable cc=C:\Toolchains\gcc\bin\gcc.exe
x86decomp toolchain-verify config/toolchains.json gcc-13-x86
```

Registration hashes referenced executables and records their roles. Proprietary or external toolchain binaries are not copied into the project. Verification detects identity drift.

2

## Use a complete compiler profile

The bundled `examples/compiler-profiles/gcc-i686-object.json` demonstrates the schema with source/output placeholders, timeout, environment policy, family, version label, and version probe. It intentionally produces a 32-bit ELF relocatable object, so do not use it as a COFF matching profile without changing the actual compiler contract.

```
{
  "schema_version": 2,
  "id": "gcc-i686-c-object-o2",
  "description": "Compile freestanding C into a 32-bit i386 ELF relocatable object without linking.",
  "executable": "gcc",
  "language": "c",
  "output_kind": "relocatable_object",
  "timeout_seconds": 60,
  "arguments": [
    "-m32",
    "-std=c11",
    "-O2",
    "-fno-pic",
    "-fno-pie",
    "-fno-asynchronous-unwind-tables",
    "-fno-stack-protector",
    "-c",
    "{source}",
    "-o",
    "{output}"
  ],
  "environment": {},
  "family": "gcc",
  "version": "user-installed",
  "command_prefix": [],
  "inherit_environment": true,
  "version_arguments": [
    "--version"
  ]
}
```

For PE matching, provide a separately evidenced profile that emits the required COFF object and records the exact installed executable.

3

## Run a bounded optimization matrix

The bundled lab example varies `-O0` and `-O2`, caps experiments at four, and uses dedicated output/cache roots:

```
{
  "source": "../sample_source/add.c",
  "profiles": [
    "../compiler-profiles/gcc-i686-object.json"
  ],
  "output_root": "../../build/example-lab/output",
  "cache_root": "../../build/example-lab/cache",
  "output_name": "add.o",
  "max_experiments": 4,
  "matrix": {
    "axes": {
      "optimization": [
        "-O0",
        "-O2"
      ]
    }
  },
  "target": {}
}
```

```
x86decomp compiler-lab examples/labs/gcc-optimization-matrix.json --report reports/compiler-lab.json
```

The lab expands declared axes only, runs profiles through the compiler contract, uses cache identities, and records each experiment. A cap prevents accidental unbounded matrices.

4

## Configure comparison and inspect the exact ranking

The bundled lab has an empty `target` object, so it compiles experiments but does not compare them. For matching work, use an evidenced COFF-producing profile and declare one of the implemented target kinds, for example:

```
{
  "target": {
    "kind": "pe_function",
    "pe": "../../target.exe",
    "rva": 4198960,
    "size": 32,
    "symbol": "sub_00401230"
  }
}
```

```
x86decomp compiler-lab config/coff-matching-lab.json --report reports/compiler-lab-coff.json
$lab = Get-Content reports/compiler-lab-coff.json | ConvertFrom-Json
$lab.best_experiment
$lab.experiments | Select-Object id, score, selections, error
```

Experiment directories use the exact v0.7.5 IDs `p000-v0000`, `p000-v0001`, and so on. For a `pe_function` target the implementation calls the PE-versus-COFF comparator and scores its classification plus normalized instruction similarity. “Best” means best under that target and scoring policy; it is not proof that the compiler family, exact version, flags, or source were the originals.

5

## Build and compare controlled ground truth

```
x86decomp corpus-create-manifest . build/ground-truth-manifest.json
x86decomp corpus-build build/ground-truth-manifest.json build/ground-truth --report reports/ground-truth.json
x86decomp corpus-verify reports/ground-truth.json
x86decomp corpus-compare reports/gcc-12.json reports/gcc-13.json --report reports/compiler-comparison.json
```

Ground-truth corpora bind known source, compiler/version profiles, and output hashes. Cross-report comparisons identify measured differences between known runs; they do not infer semantic equivalence or identify an unknown historical compiler by themselves.

6

## Use the bounded compiler worker when isolation policy requires it

```
x86decomp compile-worker profiles/target.json src/candidate.c build/candidate.obj --isolation local_bounded --cache build/compiler-cache --report reports/compiler-worker.json
```

The worker runs a real subprocess contract with bounded execution and output hashing. Container mode requires an explicit image and available container runtime; the command does not create an isolation platform by itself.

## Required interpretation

- A successful compiler invocation proves that the declared command produced the recorded output in that environment.
- A cache hit is valid only for the profile, executable, source, and argument identity encoded by the implementation.
- A highest score is a ranking under the configured comparison, not compiler attribution.
- Unknown historical flags remain unknown unless separate evidence resolves them.

## v0.7.5 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/compiler.py` | `f21f38f6ed0804a959188e31f5c9fa498d7d0740536fbb82594a375b12353944` |
| `src/x86decomp/compiler_lab.py` | `05a54baba63c926190c0e2fb45bff09c6eb338ed6a479e6e47be210a6b1de859` |
| `src/x86decomp/toolchains.py` | `9dde5962b67d30fec64266313f5488a4e5501de9db26605d4719cbe276cde03f` |
| `tests/test_compiler.py` | `9645daed68779957cd14addad7626d32d99056f551c27d873e3f475cfe862f64` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
