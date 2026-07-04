---
title: x86decomp 0.7.8 Documentation
description: Evidence-governed x86/x86-64 decompilation toolkit documentation.
---

# x86decomp 0.7.8 Documentation

Use this MkDocs site to install the toolkit, create projects, run matching and functional workflows, and use bounded local-model C generation.

<div class="doc-stat-grid">
<div><strong>166</strong><span>toolkit root commands</span></div>
<div><strong>239</strong><span>canonical routes</span></div>
<div><strong>145</strong><span>Python modules</span></div>
<div><strong>100</strong><span>JSON Schemas</span></div>
<div><strong>59</strong><span>test source files</span></div>
<div><strong>36</strong><span>adapter declarations</span></div>
</div>

## Start here

- [Getting started](getting-started.md)
- [Workflows](workflows.md)
- [Local LLM C generation](local-llm.md)
- [Project Examples](project-examples.md)
- [Complete command reference](commands/index.md)

## Scope

The model is a proposal engine only. Exact byte acceptance comes from deterministic compilation, COFF extraction, complete relocation resolution, and raw byte identity. Analyze and execute only authorized targets in appropriately isolated environments.


## Universal decompilation acceleration

Version 0.7.8 adds function discovery, pattern recipes, text-section swap workflows, project health/progress reconciliation, source-stage classification, GhidraMCP operations, compiler-rule ledgers, runtime/subsystem detection, toolchain/path hygiene, decompiler cleanup, and moddable-source policy checks. See [Decompilation Acceleration](decompilation-acceleration.md).


## 0.7.8 adapter capabilities

The harness now reports protocol capabilities separately from product adapters. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
