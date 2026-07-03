---
title: Integrations
description: Exact adapter and local-inference provider declarations.
---

# Integrations

The verification harness declares **36 adapters**. Unresolved adapters are `BLOCKED`; they are never passed or silently skipped.

## Adapter catalog

| ID | Display name | Kind | Required for | Discovery declarations | Optional |
| --- | --- | --- | --- | --- | --- |
| `angr` | angr | `python` | `angr`, `symbolic-memory` | modules: `angr` | no |
| `build` | Python build | `python` | `packaging` | modules: `build` | no |
| `capstone` | Capstone Python bindings | `python` | `disassembly`, `matching`, `symbolic` | modules: `capstone` | no |
| `clang` | Clang C compiler | `executable` | `compiler`, `corpus`, `coff` | commands: `clang`, `clang.exe`; environment: `CLANG` | no |
| `clangxx` | Clang C++ compiler | `executable` | `compiler`, `corpus`, `cpp` | commands: `clang++`, `clang++.exe`; environment: `CLANGXX` | no |
| `cmake` | CMake | `executable` | `native-build` | commands: `cmake`, `cmake.exe` | no |
| `container-runtime` | Docker or Podman container runtime | `executable` | `isolated-workers`, `compiler-worker` | commands: `docker`, `podman`, `docker.exe`, `podman.exe` | no |
| `coverage` | coverage.py | `python` | `coverage`, `public-api` | modules: `coverage` | no |
| `dynamorio` | DynamoRIO | `directory` | `drcov-live`, `runtime-tracing` | commands: `drrun`, `drrun.exe`; environment: `DYNAMORIO_HOME` | no |
| `fastapi` | FastAPI | `python` | `service` | modules: `fastapi` | no |
| `gcc` | GCC C compiler | `executable` | `compiler-regression` | commands: `gcc`, `gcc.exe` | no |
| `ghidra` | Ghidra | `directory` | `ghidra-live`, `pcode`, `decompiler` | commands: `analyzeHeadless`, `analyzeHeadless.bat`; environment: `GHIDRA_HOME` | no |
| `gxx` | GCC C++ compiler | `executable` | `compiler-regression` | commands: `g++`, `g++.exe` | no |
| `java` | Java runtime | `executable` | `ghidra` | commands: `java`; environment: `JAVA_HOME` | no |
| `javalang` | javalang | `python` | `ghidra-static` | modules: `javalang` | no |
| `jsonschema` | jsonschema | `python` | `contracts` | modules: `jsonschema` | no |
| `lief` | LIEF | `python` | `independent-pe` | modules: `lief` | no |
| `llama-server` | llama.cpp server | `executable` | `local-llm`, `llama.cpp` | commands: `llama-server`, `llama-server.exe` | yes |
| `lld-link` | LLD COFF linker | `executable` | `relink`, `whole-image` | commands: `lld-link`, `lld-link.exe`; environment: `LLD_LINK` | no |
| `llvm-lib` | LLVM librarian | `executable` | `coff-archive` | commands: `llvm-lib`, `llvm-lib.exe`, `llvm-ar` | no |
| `llvm-objdump` | LLVM objdump | `executable` | `independent-disassembly` | commands: `llvm-objdump`, `llvm-objdump.exe` | no |
| `llvm-readobj` | LLVM object inspector | `executable` | `independent-coff` | commands: `llvm-readobj`, `llvm-readobj.exe` | no |
| `lm-studio` | LM Studio CLI | `executable` | `local-llm`, `lm-studio` | commands: `lms`, `lms.exe` | yes |
| `localai` | LocalAI server | `executable` | `local-llm`, `localai` | commands: `local-ai`, `local-ai.exe`, `localai`, `localai.exe` | yes |
| `msvc` | User-owned Microsoft C/C++ toolchain | `toolchain` | `historical-msvc`, `matching` | commands: `cl.exe`, `link.exe`; environment: `VCINSTALLDIR`, `VSINSTALLDIR` | yes |
| `ninja` | Ninja | `executable` | `native-build` | commands: `ninja`, `ninja.exe` | no |
| `objdiff` | objdiff CLI | `executable` | `objdiff`, `matching` | commands: `objdiff-cli`, `objdiff`; environment: `OBJDIFF` | no |
| `ollama` | Ollama | `executable` | `local-llm`, `ollama` | commands: `ollama`, `ollama.exe` | yes |
| `pip-audit` | pip-audit | `python` | `dependency-security`, `release` | modules: `pip_audit` | no |
| `pytest` | pytest | `python` | `unit`, `integration` | modules: `pytest` | no |
| `python` | Python 3.11+ | `executable` | `all` | commands: `python3`, `python` | no |
| `pyyaml` | PyYAML | `python` | `skill-frontmatter` | modules: `yaml` | no |
| `unicorn` | Unicorn Python bindings | `python` | `dynamic`, `functional` | modules: `unicorn` | no |
| `uvicorn` | Uvicorn | `python` | `service` | modules: `uvicorn` | no |
| `vllm` | vLLM server | `executable` | `local-llm`, `vllm` | commands: `vllm`, `vllm.exe` | yes |
| `z3` | Z3 Python bindings | `python` | `symbolic`, `functional` | modules: `z3` | no |

**Source:** `test-suite/src/x86decomp_testkit/adapters/catalog.py`  
**SHA-256:** `48d74c2b917d045b5cc0fe50956d32e1f9717f245a77eb735bae0d9c5b4ca1b9`

## Local-model provider profiles

The `llm` capability implements **6 provider presets**. Provider support means the declared HTTP contract is implemented; it is not a claim that every served model can produce matching C.

| Provider | Protocol | Default base URL | Models path | Chat path | Structured output |
| --- | --- | --- | --- | --- | --- |
| `llama.cpp` | `openai-chat` | `http://127.0.0.1:8080/v1` | `/models` | `/chat/completions` | `openai-json-schema` |
| `lm-studio` | `openai-chat` | `http://127.0.0.1:1234/v1` | `/models` | `/chat/completions` | `openai-json-schema` |
| `localai` | `openai-chat` | `http://127.0.0.1:8080/v1` | `/models` | `/chat/completions` | `openai-json-schema` |
| `ollama` | `ollama-chat` | `http://127.0.0.1:11434` | `/api/tags` | `/api/chat` | `ollama-json-schema` |
| `openai-compatible` | `openai-chat` | `http://127.0.0.1:8000/v1` | `/models` | `/chat/completions` | `openai-json-schema` |
| `vllm` | `openai-chat` | `http://127.0.0.1:8000/v1` | `/models` | `/chat/completions` | `openai-json-schema` |

**Source:** `src/x86decomp/local_llm/profiles.py`  
**SHA-256:** `5bce6554b8d5dbccd0a18c965bae92e82cc8517f7c86997621d662f3bcff1ca2`

Profiles are loopback-only by default. Remote endpoints require explicit opt-in, and secrets are referenced by environment-variable name rather than stored in profile JSON.
