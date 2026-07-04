# Toolkit architecture map — 0.7.8

Plain-text companion: `docs/ARCHITECTURE_MAP_ASCII.txt`  
Verification companion: `test-suite/docs/ARCHITECTURE_MAP.md` and `test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`

```mermaid
flowchart LR
  ING[Immutable ingestion] --> STATIC[Static-analysis plane]
  STATIC --> CONTROL[Project control plane]
  CONTROL --> CANDIDATE[Candidate-generation plane]
  STATIC --> LLM[Local LLM proposal plane]
  CONTROL --> LLM
  LLM --> CANDIDATE
  CANDIDATE --> BUILD[Compiler and linker plane]
  BUILD --> RELOC[COFF extraction and relocation resolution]
  RELOC --> MATCH[Matching-decompilation lane]
  BUILD --> FUNCTIONAL[Functional-decompilation lane]
  MATCH --> ACCEPT[Acceptance, evidence, and feedback]
  FUNCTIONAL --> ACCEPT
  ACCEPT -. bounded compiler and byte-difference feedback .-> LLM

  CLI[x86decomp unified CLI] --> CORE[Core command plane]
  CLI --> ROUTER[34 groups / 181 routes]
  ROUTER --> GOV[Governance]
  ROUTER --> RECON[Reconstruction]
  ROUTER --> NATIVE[Native PE]
  ROUTER --> ASM[Assembly]
  RECON --> LLM
  GOV --> CONTROL
  RECON --> CANDIDATE
  NATIVE --> MATCH
  ASM --> BUILD

  PROVIDERS[LM Studio / Ollama / llama.cpp / vLLM / LocalAI / OpenAI-compatible] --> HTTP[Loopback-only bounded HTTP by default]
  HTTP --> LLM
  LLM --> UNTRUSTED[Untrusted JSON and C proposal]
  UNTRUSTED --> BUILD
  RELOC --> RAW{Raw resolved bytes identical?}
  RAW -- yes --> ACCEPTED[byte_matched accepted artifacts]
  RAW -- no --> ACCEPT

  MATCH --> M0[not_started]
  M0 --> M1[instruction_similar]
  M1 --> M2[full_relink_validated]
  FUNCTIONAL --> F0[not_started]
  F0 --> F1[differentially_validated]
  F1 --> F2[symbolically_bounded]
  F2 --> F3[integration_validated]
```

## Boundaries

- Immutable ingestion records artifacts before interpretation.
- Static analysis does not imply runtime behavior.
- Project control preserves evidence, audit, review, and workflow state.
- Candidate generation and local-model output produce proposals, not facts.
- Local-model endpoints are loopback-only by default; remote disclosure requires explicit profile opt-in.
- Compiler and linker evidence is preserved with exact commands and hashes.
- COFF relocations must resolve from explicit evidence before a local-model candidate can match.
- Only raw relocation-resolved byte identity can accept an `llm match` candidate.
- Matching and functional lanes remain separate.
- Acceptance requires the named verifier and durable evidence.
- The active tree contains one current command plane and no release-specific execution plane.

### v0.7.8 acceleration overlay

```mermaid
flowchart LR
  FunctionEvidence[Function packets / byte ranges] --> JobCreate[llm job-create / job-from-range]
  JobCreate --> Batch[llm batch-create / batch-match]
  Batch --> Validator[Compiler + relocation + byte validators]
  Validator --> Promote[candidate promote]
  Promote --> SourceMap[source-map annotate / verify]
  SourceMap --> HumanTree[human-readable source tree]
  HumanTree --> ModFlow[mod branch / regression compare]
```


v0.7.8 universal acceleration overlay: profile-driven function discovery, pattern recipes, text-swap workflow, source-stage/project-health accounting, GhidraMCP operations, runtime/subsystem hints, toolchain/path hygiene, and moddable-source release policy.
