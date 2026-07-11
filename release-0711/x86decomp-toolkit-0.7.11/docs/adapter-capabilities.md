# Adapter capabilities — 0.7.11

The test harness records **protocol capabilities** separately from **installed product adapters**.
A loopback OpenAI-compatible `/v1/models` response can establish that the `lm-studio-http`
protocol path is available. It does not establish that `ollama`, `llama-server`, `localai`, or
`vllm` is installed, so those adapter identities remain unavailable unless their own detectors
succeed.

Local-model output is always treated as an untrusted C proposal. Acceptance requires the normal
deterministic gates: contract validation, compilation under the selected profile, relocation-aware
comparison, and exact byte evidence where matching mode requires it. A protocol probe never counts
as proof of a successful decompilation or reconstruction.

The recursive feature catalog, toolkit and test-suite architecture maps, and this MkDocs site are
release-controlled artifacts. Changes to adapter detection or protocol behavior must update those
artifacts and their tests in the same change.
