# Changelog

## 0.7.8 — Adapter capability resolution for local inference runtimes

- Added protocol-level adapter capabilities in the comprehensive harness so product adapters and runtime protocols are no longer conflated.
- Added `lm-studio-http`, a loopback-gated OpenAI-compatible HTTP endpoint adapter for LM Studio's local server.
- Added capability reporting for `local-loopback-llm`, `openai-compatible-chat`, `ollama-chat`, and `structured-output-json`.
- Updated adapter detection so LM Studio's OpenAI-compatible endpoint can satisfy OpenAI-compatible local-LLM coverage without pretending to satisfy `ollama`, `llama-server`, `localai`, or `vllm` product adapter identities.
- Added the `x86decomp-test capabilities` command and `capabilities.json` run artifact.
- Added targeted harness tests for LM Studio HTTP probing, loopback-only endpoint policy, and product-versus-protocol separation.
- Preserved the v0.7.7 universal acceleration command surface and evidence boundaries.

Earlier release history is retained in source-control tags and published release archives, not in the active 0.7.8 source tree.
