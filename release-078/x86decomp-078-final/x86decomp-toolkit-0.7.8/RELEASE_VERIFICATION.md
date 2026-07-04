# x86decomp-toolkit 0.7.8 release verification

Adapter capability resolution for local inference runtimes, including LM Studio OpenAI-compatible HTTP endpoint coverage without product-adapter aliasing.

## Surface

- root_commands: 166
- canonical_groups: 59
- canonical_routes: 239
- toolkit_modules: 114
- function_method_symbols: 948
- schemas: 97
- adapters: 37

## New or changed

- Added x86decomp-test capabilities command.
- Added lm-studio-http endpoint adapter.
- Added adapter capability reporting: local-loopback-llm, openai-compatible-chat, ollama-chat, structured-output-json.
- Added loopback-gated OpenAI-compatible /v1/models probe for LM Studio local server.
- Separated protocol capabilities from product adapter identities; LM Studio HTTP does not satisfy ollama, llama-server, localai, or vllm adapter IDs.
- Added targeted test-suite and self-test coverage for capability resolution, LM Studio HTTP probing, loopback policy, and product/protocol separation.

## Verification performed

- targeted_tests: 28/28 passed
- toolkit_manifest: 433/433 verified
- test_suite_manifest: 63/63 verified
- py_compile: passed for toolkit and test-suite sources
- wheel_build: toolkit and test-suite wheels and sdists built
- clean_install: passed
- pip_check: passed
- cli_smoke: x86decomp-test capabilities exposed and produced capability report
- mkdocs_strict_build: passed
- dracula_site_verifier: passed; 392 Markdown pages and 394 built HTML pages

## Not claimed

- Full optional adapter-aware harness pass is not claimed in this environment.
- Live LM Studio/Ollama/llama.cpp/vLLM/LocalAI model-quality benchmarks are not claimed.
- LM Studio HTTP capability coverage does not imply Ollama, vLLM, LocalAI, or llama.cpp server are installed.
