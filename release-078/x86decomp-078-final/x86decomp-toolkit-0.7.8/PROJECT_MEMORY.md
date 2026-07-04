# Project memory — x86decomp-toolkit 0.7.8

## Durable architecture decision

The toolkit is a unified current-release product. All retained behavior lives in capability-oriented current modules. Release-numbered implementations, executables, bridges, installers, overlays, reports, and test baselines are not part of the active repository.

## Stable product decisions

- `x86decomp` is the only toolkit executable.
- `x86decomp-test` is the only verification executable.
- The canonical interface contains 34 groups and 181 routes.
- Governance, reconstruction, native PE work, and assembly materialization are current capability packages.
- Byte-form assembly is the default exact-preservation path.
- Matching and functional validation are separate state machines.
- Project schemas are additive and namespaced by capability.
- External tools are optional adapters whose absence is reported as BLOCKED, never skipped silently.
- Native execution requires consent and bounded isolation.
- Local-model output is always an untrusted C proposal; only deterministic compilation and exact relocation-resolved byte comparison can accept it.
- Every release must update the recursive catalog, four synchronized architecture artifacts, and the Material for MkDocs documentation site.

## Release discipline

The source tree is distributed as a complete release. Package managers or replacement source archives handle installation. The toolkit does not mutate an older source tree through embedded release installers.


## 0.7.8 adapter-capability note

The test harness now records protocol capabilities separately from product adapter identities. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
