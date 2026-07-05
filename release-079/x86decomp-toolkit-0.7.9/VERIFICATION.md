# Verification contract — 0.7.9

A release is complete only when the exact packaged source passes the same current-only contract used during development.

## Required evidence

- Python compilation and package import success
- Recursive JSON Schema meta-validation and example validation
- Java syntax validation for all Ghidra scripts
- Exact recursive inventory reconciliation for modules, functions and methods, root commands, canonical routes, schemas, scripts, adapters, and workflow states
- Zero historical release references or versioned release artifacts
- Exactly one toolkit and one test-suite entry point
- One exact reconciled inventory containing toolkit, supplemental public-surface, and standalone verifier tests, with zero failures, errors, and skips
- Current function and method body execution audit
- Root command and canonical route process audit
- Coverage floors
- Package build, clean install, entry-point launch, and `pip check`
- Source-distribution and deterministic source-ZIP extraction tests
- Exact root and standalone test-suite `MANIFEST.sha256` verification
- SHA-256 verification for every release artifact and the final bundle

Unavailable external integrations are listed explicitly as BLOCKED. They are never converted into passing or skipped results.


## 0.7.9 adapter-capability note

The test harness now records protocol capabilities separately from product adapter identities. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
