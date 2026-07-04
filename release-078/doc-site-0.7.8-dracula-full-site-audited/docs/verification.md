---
title: Verification
description: 0.7.8 verification summary.
---

# Verification

The 0.7.8 update was checked with targeted source, parser, documentation, and packaging verification in this environment. Optional native-analysis dependencies such as Capstone/angr were not installed here, so the complete optional adapter/runtime harness was not rerun in this environment.

Confirmed checks:

- source manifests regenerated and verified: 429/429 root files, 60/60 test-suite files;
- parser-derived canonical surface: 151 root commands, 44 groups, 201 routes;
- targeted acceleration tests: 3/3 pass;
- release-contract, reconstruction CLI, and local-LLM targeted tests: 17/17 pass;
- MkDocs strict build: pass;
- end-user site verifier: pass.


## v0.7.8 verification boundary

The v0.7.8 update was validated with targeted acceleration tests, source-manifest regeneration, parser-derived command coverage, a strict MkDocs build, and the end-user site verifier. Optional native-analysis dependencies may still be unavailable on a given host; unavailable runtime adapters must be reported as BLOCKED rather than passed.


## 0.7.8 adapter capabilities

The harness now reports protocol capabilities separately from product adapters. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
