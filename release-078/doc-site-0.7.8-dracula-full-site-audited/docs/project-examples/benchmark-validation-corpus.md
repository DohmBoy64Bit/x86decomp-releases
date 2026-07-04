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

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.8 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

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

## v0.7.8 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/benchmarks.py` | `b9b28fbcb2f38723b274e4150b1c3914ddcbceab1b49461fc5797a84f9e13fb3` |
| `src/x86decomp/ground_truth.py` | `9684fbcda0fd5060b3c1f2d0efb83892900c69190d33e24fd7e49f91885181e2` |
| `src/x86decomp/dynamic.py` | `a09cbba16f498158cf30191397884f0a70051c767b778cd520ac229b6e85e451` |
| `src/x86decomp/symbolic.py` | `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3` |
| `src/x86decomp/integration.py` | `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845` |
| `tests/test_linker_metadata_corpus.py` | `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
