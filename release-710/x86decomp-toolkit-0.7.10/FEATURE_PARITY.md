# Current feature-parity contract — 0.7.10

The active repository contains one current implementation. Parity means every supported capability maps to current code, a current command or API, current schemas where applicable, current tests, and current documentation.

| Capability plane | Current package or module | Primary command groups | Verification focus |
|---|---|---|---|
| Evidence governance | `x86decomp.governance` | campaign, hypothesis, proof, review, consensus, graph, worker | audit chain, evidence gates, locks, deterministic bundles |
| Project reconstruction | `x86decomp.reconstruction` | module, source, headers, build, library, capsule, security, changeset | project layout, provenance, ABI, build models, security, merge safety |
| Native PE reconstruction | `x86decomp.native` | boundary, match, hybrid, staging, loop, runtime, windows, pe | slot safety, exact comparison, PE preservation, bounded execution |
| Assembly materialization | `x86decomp.assembly` | asm, reloc, hybrid | byte default, annotations, relocation resolution, exact round trips |
| Local LLM proposals | `x86decomp.local_llm` | llm | local provider profiles, deterministic prompts, compiler loop, relocation resolution, exact byte identity |
| Core analysis | `x86decomp` root modules | init, inspect-pe, compile, diff, symbolic, dynamic, pipeline, release-gate | parsing, reproducibility, orchestration, validation, security |
| Verification harness | `x86decomp_testkit` | x86decomp-test | recursive inventory, no skips, adapters, coverage, packaging |

## Exact current interface

- One toolkit executable: `x86decomp`
- One test-suite executable: `x86decomp-test`
- 59 canonical capability groups
- 239 canonical routes
- Byte assembly remains the default
- Matching and functional workflows remain distinct
- Optional adapters remain explicit and cannot silently disappear

## Removal rule

Release-numbered structure has been removed, but capability behavior has not been discarded. Any future removal requires a complete successor, explicit contract update, and passing regression evidence.


## 0.7.10 adapter-capability note

The test harness now records protocol capabilities separately from product adapter identities. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
