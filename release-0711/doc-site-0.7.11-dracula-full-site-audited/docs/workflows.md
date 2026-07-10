---
title: Practical paths through the toolkit
description: Example x86decomp workflows for inspection, reconstruction, assembly,
  evidence, and verification.
original_path: workflows.html
---

<a id="workflow-1"></a>
<a id="workflow-2"></a>
<a id="workflow-3"></a>
<a id="workflow-4"></a>
<a id="workflow-5"></a>
<a id="workflow-6"></a>
<a id="workflow-7"></a>
<a id="workflow-8"></a>

Section: Example workflows

# Practical paths through the toolkit

Each workflow is intentionally small. Open the linked command reference when you need every available option.

Metadata: Workflow 1

## Inspect a PE image { .doc-workflow-step }

Understand the target before making reconstruction claims.

```
x86decomp inspect-pe ./target.exe
x86decomp image-profile ./reference.exe ./output.json
x86decomp metadata-scan ./target.exe
```

Metadata: Workflow 2

## Create and verify a project { .doc-workflow-step }

Create durable project state and confirm that required files and contracts are intact.

```
x86decomp init ./target.exe ./work
x86decomp verify-project ./work
x86decomp project check
```

Metadata: Workflow 3

## Disassemble and compare a function { .doc-workflow-step }

Decode a bounded range and compare linked output with a candidate object.

```
x86decomp disassemble ./function.bin
x86decomp diff-function ./target.exe 0x1000 1 ./candidate.obj example
x86decomp diff-bytes ./target.exe ./candidate.bin
```

Metadata: Workflow 4

## Materialize conservative assembly { .doc-workflow-step }

Keep exact byte-form output as the default, then opt into annotations when useful.

```
x86decomp asm materialize ./input.json ./generated.asm ./generated.obj ./resolved.bin --symbol example --rva 0x1000 --symbol-map ./target.map
x86decomp asm annotate ./candidate.c ./output.json --symbol example --rva 0x1000
x86decomp asm verify-roundtrip ./candidate.c ./original.bin ./generated.obj ./resolved.bin --symbol example --rva 0x1000 --symbol-map ./target.map
```

Metadata: Workflow 5

## Run an evidence-led hypothesis { .doc-workflow-step }

Record a proposed explanation, attach evidence, and gate its transition.

```
x86decomp hypothesis create recovered-parser-loop function pe-rva:00001000 --origin analyst
x86decomp hypothesis evidence hypothesis-001 example-001 --stance support --weight 1.0 --kind analysis --group independent-source
x86decomp hypothesis gate hypothesis-001
```

Metadata: Workflow 6

## Build and evaluate a candidate { .doc-workflow-step }

Create a candidate, add source, compile it, and compare the result.

```
x86decomp candidate create candidate-main
x86decomp candidate add-file ./candidate.bin ./candidate.c src/candidate.c
x86decomp candidate evaluate ./candidate.bin exact-bytes active
```

Metadata: Workflow 7

## Run the exact source verification { .doc-workflow-step }

Reconcile the entire current test inventory and source manifests.

```
make verify-hashes
make verify
make test-suite
```

Metadata: Workflow 8

## Run the adapter-aware harness { .doc-workflow-step }

Detect optional tools, run available checks, and record unavailable tools as blocked.

```
x86decomp-test init-config --toolkit-root . --output-root ./test-results --install-root ./.x86decomp-test-tools --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

> **Source-verified project examples.** See [Project examples](project-examples.md) for matching, functional, both-mode hybrid, and major supporting workflows grounded in the 0.7.11 source.

> **Audit status.** Every x86decomp and x86decomp-test command on this page parses with the real 0.7.11 parser. Runtime success still depends on the declared input files, tools, and authorization boundary.
