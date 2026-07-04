# Adapter detection, installation, and live-test contract

## Detection order

Every adapter is resolved before any prompt:

1. saved custom path or endpoint;
2. adapter-specific environment variable;
3. system `PATH`, Python importability, or loopback HTTP endpoint probe;
4. known platform locations;
5. interactive resolution only when still missing.

Detected tools produce no question. Only a missing adapter triggers:

```text
Is it already installed at a custom path? [y/N]
```

A custom executable, interpreter, virtual-environment root, installation directory, or HTTP endpoint is validated before persistence.

## Adapter identity versus protocol capability

v0.7.8 separates **adapter identity** from **protocol capability**.

Adapter identity answers which product or tool is available:

```text
lm-studio
lm-studio-http
ollama
llama-server
localai
vllm
```

Protocol capability answers what a resolved adapter can exercise:

```text
local-loopback-llm
openai-compatible-chat
ollama-chat
structured-output-json
```

This prevents false coverage. LM Studio's local server may satisfy `openai-compatible-chat`, but it does not satisfy the `ollama`, `vllm`, `localai`, or `llama-server` adapter identities.

## LM Studio HTTP endpoint

`lm-studio-http` probes an OpenAI-compatible `/v1/models` endpoint. By default, only loopback endpoints are allowed. Set one of:

```text
LM_STUDIO_BASE_URL=http://127.0.0.1:1234/v1
X86DECOMP_LM_STUDIO_URL=http://127.0.0.1:1234/v1
```

Remote endpoints require `allow_network=true` in the test-suite configuration. This keeps the default harness local-only while still allowing explicit remote validation when the operator chooses it.

## Installation consent

Automatic installation requires `allow_install=true`. Network-backed installation also requires `allow_network=true`. Commands and downloads are logged before execution. Historical/proprietary MSVC is user-owned custom-path only. Live HTTP endpoints are not installed automatically.

## Adapter families

- Python/testing: Python, pytest, coverage, jsonschema, javalang, PyYAML, build.
- Analysis/validation: Capstone, Unicorn, Z3, angr, LIEF, FastAPI, Uvicorn.
- Native tools: Java, Ghidra, DynamoRIO, objdiff, Clang/Clang++, GCC/G++, LLD, LLVM librarian/readobj/objdump, CMake, Ninja.
- Production hardening: pip-audit and Docker/Podman container runtime.
- Local inference runtimes: LM Studio CLI, LM Studio HTTP endpoint, Ollama, llama.cpp server, vLLM, and LocalAI.
- Proprietary toolchain: operator-owned MSVC.

## Live probes

Existence is insufficient. Resolved adapters perform a real bounded operation:

- Python packages import and report versions.
- C/C++ compilers build fixtures; Clang emits Windows COFF.
- `lld-link` produces a minimal Windows PE.
- LLVM tools inspect or archive real objects.
- Ghidra imports a generated PE and runs maintained exporters.
- DynamoRIO runs `drcov` over a harmless suite-owned host fixture.
- objdiff executes the declared CLI path.
- pip-audit scans the selected environment and preserves its report.
- Docker/Podman executes a bounded capability/version probe; target workers still require an explicitly declared image and policy.
- Local inference executable adapters execute bounded version/help probes only.
- `lm-studio-http` executes a bounded loopback `/v1/models` probe.

Unresolved tools become `BLOCKED`, never passed or silently skipped.

## Download safety

Downloaded archives are bounded by bytes/member count, hashed, and extracted through a path-confined routine rejecting absolute paths, traversal, symlinks, hard links, and special files. A logged hash establishes byte identity, not publisher authenticity; release policy should pin vendor checksums/signatures where available.
