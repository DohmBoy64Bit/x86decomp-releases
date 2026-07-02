---
title: 'Example: benchmark and validation-corpus project'
description: Generate or build controlled corpora, run byte, dynamic, symbolic, integration,
  and analysis cases, preserve human-intervention counts, and compare reproducible
  reports.
original_path: project-examples/benchmark-validation-corpus.html
---

<a id="model"></a>
<a id="benchmark-validation-corpus-flow-title"></a>
<a id="benchmark-validation-corpus-flow-desc"></a>
<a id="arrow-benchmark-validation-corpus"></a>
<a id="benchmark-validation-corpus-flow-caption"></a>
<a id="synthetic"></a>
<a id="ground"></a>
<a id="manifest"></a>
<a id="run"></a>
<a id="compare"></a>
<a id="bundle"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: benchmark and validation-corpus project

Generate or build controlled corpora, run byte, dynamic, symbolic, integration, and analysis cases, preserve human-intervention counts, and compare reproducible reports.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.4 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is an evaluation workflow for the toolkit, validators, compilers, or methods—not an additional decompilation mode.

**On this page**

1. [Benchmark model](#model)
2. [Generate source corpus](#synthetic)
3. [Build ground truth](#ground)
4. [Define cases](#manifest)
5. [Run benchmark](#run)
6. [Compare reports](#compare)
7. [Create authorized bundle](#bundle)
8. [Truth boundary](#limits)
9. [Source basis](#source-basis)

## Benchmark model

Each result remains tied to its case kind, bounds, inputs, and recorded human interventions.Known cases → Hash identities → Byte cases → Dynamic cases → Symbolic cases → Integration cases → Aggregate report

Known casesHash identitiesByte casesDynamic casesSymbolic casesIntegration casesAggregate report

Each result remains tied to its case kind, bounds, inputs, and recorded human interventions.

```ascii-fallback
Known cases → Hash identities → Byte cases → Dynamic cases → Symbolic cases → Integration cases → Aggregate report
```

1

## Generate and verify deterministic C/C++ sources

```
x86decomp corpus-generate build/generated-corpus --cases-per-family 8 --seed 0x86DEC0DE --report reports/generated-corpus.json
x86decomp corpus-generated-verify reports/generated-corpus.json
```

Generation is deterministic for the declared options and records source identities. It does not claim that any compiler built those files or that the generated sources correspond to an original program.

2

## Build compiler/version ground truth

```
x86decomp corpus-create-manifest . build/ground-truth-manifest.json
x86decomp corpus-build build/ground-truth-manifest.json build/ground-truth --report reports/ground-truth.json
x86decomp corpus-verify reports/ground-truth.json
```

A ground-truth report binds known sources, profiles, tool identities, and output hashes. Use it to compare controlled compiler behavior, not to infer unknown historical provenance without independent evidence.

3

## Define heterogeneous benchmark cases

The bundled benchmark manifest demonstrates exact bytes, one concrete Unicorn harness, one bounded symbolic case, and one process integration scenario:

```
{
  "schema_version": 1,
  "name": "bounded-add-demo",
  "cases": [
    {
      "id": "exact-byte-pair",
      "kind": "byte_pair",
      "target": "../validators/add_stack_target.bin",
      "candidate": "../validators/add_stack_candidate.bin",
      "human_interventions": 0
    },
    {
      "id": "unicorn-one-input",
      "kind": "dynamic",
      "target": "../validators/add_stack_target.bin",
      "candidate": "../validators/add_stack_candidate.bin",
      "harness": "../validators/add_stack_harness.json",
      "human_interventions": 1
    },
    {
      "id": "z3-bounded-all-inputs",
      "kind": "symbolic",
      "target": "../validators/add_stack_target.bin",
      "candidate": "../validators/add_stack_candidate.bin",
      "architecture": "x86",
      "stack_argument_words": 2,
      "output_registers": [
        "eax"
      ],
      "max_steps": 100,
      "max_paths": 8,
      "human_interventions": 1
    },
    {
      "id": "process-integration-one-scenario",
      "kind": "integration",
      "manifest": "../integration/bounded-demo.json",
      "allow_host_execution": true,
      "human_interventions": 1
    }
  ]
}
```

Every case can record `human_interventions`. Do not erase manual effort when comparing methods.

4

## Run and preserve the aggregate report

```
x86decomp benchmark-run examples/benchmarks/bounded-demo.json --report reports/benchmark-bounded-demo.json
```

The runner dispatches by case kind and aggregates outcomes. The bundled demo’s integration case sets `allow_host_execution` to true and its manifest uses `host_explicit`; it is a controlled Python demo, not a safe template for unknown native code. Use an `external_wrapper` boundary and leave host execution disabled for untrusted targets. Interpret each case using its underlying validator’s truth boundary; aggregate pass counts do not broaden those claims.

5

## Compare corpus outputs across known builds

```
x86decomp corpus-compare reports/gcc-12-ground-truth.json reports/gcc-13-ground-truth.json --report reports/ground-truth-comparison.json
```

Cross-report comparison shows measured identity and output differences between the supplied known reports. It does not establish semantic equivalence.

6

## Create a hash-sealed authorized static test bundle

```
x86decomp test-bundle-create build/authorized-test-bundle.zip --artifact primary_image=authorized/target.exe --artifact pdb=authorized/target.pdb --authorization "I own these artifacts or have permission to analyze them." --name regression-target --description "Static regression corpus" --expected-architecture x86
x86decomp test-bundle-inspect build/authorized-test-bundle.zip --report reports/test-bundle-inspection.json
```

Creation records authorization and hashes. Inspection uses safe extraction, verifies hashes, and performs static inspection. A successful inspection is not malware clearance or semantic equivalence.

## Benchmark truth boundary

- Do not merge byte, dynamic, symbolic, and integration passes into a stronger universal claim.
- Report case counts, completed and failed counts, per-case errors, validator bounds, tool identities from the underlying reports, and human interventions. The benchmark aggregate does not define separate skip or blocked counters.
- Generated-source reproducibility is not compiler-output reproducibility until a build report exists.
- Static bundle inspection is not permission to execute the contained target.

## v0.7.4 source basis

> **Triple-check model.** Each example was checked against the CLI parser, implementation behavior, and an independent test, schema, or contract document. Full hashes and search anchors are in [the source audit](source-audit.md).

| Evidence class | File | Lines | SHA-256 |
| --- | --- | --- | --- |
| parser | `src/x86decomp/cli.py` | L138–L141 | `21e0654ced2f` |
| parser | `src/x86decomp/cli.py` | L183–L186 | `21e0654ced2f` |
| implementation | `src/x86decomp/benchmarks.py` | L40–L43 | `b9b28fbcb2f3` |
| implementation | `src/x86decomp/benchmarks.py` | L51–L54 | `b9b28fbcb2f3` |
| implementation | `src/x86decomp/ground_truth.py` | L72–L75 | `9684fbcda0fd` |
| implementation | `src/x86decomp/synthetic_corpus.py` | L243–L246 | `a0475235f700` |
| example | `examples/benchmarks/bounded-demo.json` | L37–L40 | `980ad9dc8352` |
| example | `examples/integration/bounded-demo.json` | L5–L8 | `e1b589e23a5f` |
| test | `tests/test_linker_metadata_corpus.py` | L162–L165 | `aa88771eecf6` |
| test | `tests/test_production.py` | L507–L510 | `da0d4bd57f7f` |

## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
