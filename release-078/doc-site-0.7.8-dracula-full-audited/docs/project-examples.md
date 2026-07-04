---
title: Project Examples
description: Source-verified example workflows for official project modes and supporting
  tasks.
---

# Project Examples

Pick the example closest to your project goal. The examples preserve the original bounded claims: they do not assume a compiler, linker, ABI, function size, tool availability, passing result, or execution safety for your target.

> **Mode model.** The 0.7.8 project schema permits only `matching` and `functional` in `selected_modes`. A target decision of `preferred_mode: both` enables both; “hybrid” describes their build/workflow composition, not a third enum.

## Example Catalog

<div class="doc-card-grid">
<a class="doc-card" href="matching-project/">
<strong>End-to-end matching project</strong>
<span>Compile, ABI-check, function-diff, image-match, and converge toward relink validation.</span>
</a>
<a class="doc-card" href="functional-project/">
<strong>End-to-end functional project</strong>
<span>Use bounded concrete, symbolic, and integration validation without requiring byte identity.</span>
</a>
<a class="doc-card" href="hybrid-project/">
<strong>End-to-end hybrid composition</strong>
<span>Keep assembly fallbacks while matching and functional lanes progress independently.</span>
</a>
<a class="doc-card" href="static-analysis-evidence/">
<strong>Static analysis and evidence</strong>
<span>Inventory formats, import analysis artifacts, cross-check instructions, and govern claims.</span>
</a>
<a class="doc-card" href="compiler-laboratory/">
<strong>Compiler identification and lab</strong>
<span>Register toolchains, run bounded matrices, preserve provenance, and rank evidence.</span>
</a>
<a class="doc-card" href="patch-image-integration/">
<strong>Patch-image integration</strong>
<span>Create a fixed-length derived patch image after independently establishing the allowed target range.</span>
</a>
<a class="doc-card" href="full-relink-convergence/">
<strong>Full relink and convergence</strong>
<span>Build evidence-limited linker plans, relink, compare images, and track convergence.</span>
</a>
<a class="doc-card" href="abi-type-recovery/">
<strong>ABI and type recovery</strong>
<span>Recover interface candidates, manage constraint conflicts, and generate harnesses.</span>
</a>
<a class="doc-card" href="target-release-reproducibility/">
<strong>Target release and reproducibility</strong>
<span>Verify manifests, audits, workflows, claims, pipelines, and release contracts.</span>
</a>
<a class="doc-card" href="benchmark-validation-corpus/">
<strong>Benchmark and validation corpus</strong>
<span>Run controlled byte, dynamic, symbolic, integration, and corpus experiments.</span>
</a>
<a class="doc-card" href="project-operations-recovery/">
<strong>Project operations and recovery</strong>
<span>Back up, migrate, repair, collect, orchestrate, recover, and restore safely.</span>
</a>
<a class="doc-card" href="text-swap-project/">
<strong>End-to-end text-swap project</strong>
<span>Compose replacement text bytes, inject them into the original PE container, verify the bounded section replacement, and keep full-relink claims separate.</span>
</a>
</div>

## Command-line Notation

Examples use one command per line so they paste cleanly in PowerShell and POSIX shells. Replace uppercase placeholder values such as digests, pipeline IDs, and stage IDs with values measured or returned by your project.
