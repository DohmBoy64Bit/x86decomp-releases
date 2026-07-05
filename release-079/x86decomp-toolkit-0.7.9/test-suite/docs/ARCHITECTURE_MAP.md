# Test-suite architecture map — 0.7.9

Toolkit map: `docs/ARCHITECTURE_MAP.md`  
Plain-text companion: `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`

```mermaid
flowchart LR
  CONFIG[Configuration] --> RESOLVE[Adapter resolution]
  RESOLVE --> INSTALLED[installed adapter]
  RESOLVE --> CUSTOM[custom path]
  RESOLVE --> CONSENT[consent-gated installation]
  RESOLVE --> BLOCKED[BLOCKED]

  RESOLVE --> LOCAL[Local-model runtime adapters]
  LOCAL --> LMS[LM Studio CLI]
  LOCAL --> OLLAMA[Ollama]
  LOCAL --> LLAMA[llama.cpp server]
  LOCAL --> VLLM[vLLM]
  LOCAL --> LOCALAI[LocalAI]

  CATALOG[Pinned surface] --> INVENTORY[Recursive current inventory]
  INVENTORY --> DRIFT[catalog drift]
  INVENTORY --> BUILTIN[Built-in verification]
  BUILTIN --> LLMTEST[Local-LLM mock transport and real Clang/COFF gate tests]
  LLMTEST --> PROCESS[Safe process execution]
  PROCESS --> RESULT[Unified result]
  RESULT --> PASS[PASS]
  RESULT --> FAIL[FAIL]
  RESULT --> ERROR[ERROR]
  RESULT --> BLOCKED
  PASS --> GATE[Strict release gate]
  FAIL --> GATE
  ERROR --> GATE
  BLOCKED --> GATE
```

The harness inventories the complete current source tree, schemas, commands, canonical routes, adapters, and function/method bodies. Local-model protocol behavior is tested with bounded loopback mock servers, while live LM Studio, Ollama, llama.cpp, vLLM, and LocalAI runtimes are detected as adapters and become explicit `BLOCKED` results when unavailable. Tests cannot be silently skipped.

### v0.7.9 acceleration verification overlay

```mermaid
flowchart LR
  Parser[parser contracts] --> AccelTests[acceleration helper tests]
  AccelTests --> Docs[docs/site sync checks]
  AccelTests --> Manifest[source manifest verification]
```
