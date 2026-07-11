# x86decomp toolkit 0.7.11

x86decomp is an **evidence-governed toolkit** for authorized analysis, reconstruction, and
validation of native Windows x86 PE32 and x86-64 PE32+ binaries. It unifies 166 root commands
and 239 canonical routes across 59 capability groups behind a single `x86decomp` executable.

Every operation is backed by deterministic validation: byte-identity gates, COFF relocation
checks, compiler round-trip gates, and content-addressed artifact storage. Observations,
derivations, proposals, corroborations, and verified claims remain explicitly separated.

---

## What problems it solves

| Problem | How x86decomp addresses it |
|---|---|
| **Reproducible decompilation** | Exact-byte matching loops, compiler profiles, and relink verification ensure outputs stay byte-identical across rebuilds. |
| **Compiler identification** | The compiler laboratory matrix-compiles ground-truth sources under declared toolchains and compares against the target binary. |
| **Binary matching** | COFF/PE function diffing, whole-image layout comparison, and convergence tracking provide quantitative matching evidence. |
| **Linker reconstruction** | MSVC `.map` parsing, COFF object correlation, and `lld-link` relink plans reconstruct the original link order. |
| **Type recovery** | ABI contracts, MSVC RTTI/vtable metadata scanning, and C++ model recovery produce evidence-linked type claims. |
| **Validation** | Dynamic (Unicorn), symbolic (Z3/angr), and byte-diff validators independently corroborate or contradict claims. |

## Who should use it

- **Reverse engineers** working on authorized Windows binary analysis and reconstruction.
- **Decompilation projects** targeting byte-accurate (matching) or functionally equivalent reconstruction.
- **Security researchers** needing reproducible, evidence-tracked analysis with auditable provenance.
- **Toolchain archaeologists** investigating compiler versions, flags, and linker behavior on shipped PE artifacts.

!!! warning "Authorization required"
    x86decomp requires explicit host-execution authorization before any native code execution.
    Parsing and static analysis paths never execute input binaries.

---

## Major capabilities

### Core analysis

| Group | Capabilities |
|---|---|
| **PE parsing** | `inspect-pe` extracts headers, sections, imports, exports, relocations, resources, and architecture for PE32 and PE32+. |
| **COFF analysis** | `coff-inspect`, `coff-extract`, `coff-synthesize`, `coff-comdat-resolve` parse, extract, and synthesize COFF objects. |
| **PDB inspection** | `pdb-inspect` decodes MSF 7.0 PDB streams and matches them to a companion PE. |
| **Disassembly** | `disassemble` (Capstone) produces deterministic instruction records; `crosscheck-ghidra` compares against Ghidra exports. |

### Validation

| Group | Capabilities |
|---|---|
| **Byte diffing** | `diff-bytes` compares two files with bounded mismatch reporting. |
| **Function diffing** | `diff-function` compares a linked PE function body to an extracted COFF symbol. |
| **Dynamic validation** | `dynamic-validate` executes target and candidate under Unicorn and compares register/memory state. |
| **Symbolic validation** | `symbolic-validate` (Z3) and `angr-validate` (angr) prove functional equivalence for bounded paths. |
| **ABI checking** | `abi-check` validates function behavior against declared ABI contracts. |
| **objdiff integration** | `objdiff-run` executes objdiff-compatible comparison manifests. |

### Reconstruction

| Group | Capabilities |
|---|---|
| **Linker layout** | `map-inspect`, `layout-reconstruct`, and `image-profile` recover section-to-object mappings and layout profiles. |
| **Linker plans** | `linker-plan` builds grounded reconstruction plans with relink manifest generation. |
| **Relinking** | `relink` executes full-image relinks from declared reconstruction manifests. |
| **Image patching** | `patch-image` writes a replacement function body into a PE at a specified RVA. |
| **C++ recovery** | `metadata-scan` and `cpp-recover` extract RTTI, vtables, inheritance, and class relationships. |
| **Harness generation** | `harness-generate` creates execution harnesses from ABI contracts for validator input. |

### Ghidra integration

| Group | Capabilities |
|---|---|
| **Export** | `ghidra-export` runs the bundled Ghidra headless export workflow (function artifacts, disassembly, decompiler output). |
| **MCP gateway** | `mcp-tools`, `mcp-read`, `mcp-propose`, `mcp-commit` provide a gated MCP (Model Context Protocol) channel to Ghidra. All mutations require evidence-linked proposals and explicit approval. |

### Local LLM

| Group | Capabilities |
|---|---|
| **Provider management** | `llm providers`, `llm profile-create` support LM Studio, Ollama, llama.cpp, vLLM, LocalAI, and OpenAI-compatible backends. |
| **Proposal pipeline** | `llm prompt`, `llm match`, `llm verify` run the proposal → compile → byte-match → accept cycle. |
| **Safety** | Endpoints are loopback-only by default, secrets use environment variables, accepted reports require zero unresolved relocations. |

!!! tip "LLM output is a proposal"
    Model-generated C is treated as an untrusted proposal until the deterministic compiler,
    COFF, relocation, and raw byte-identity gates pass. Only exact-byte matches are accepted.

### Compiler laboratory

| Group | Capabilities |
|---|---|
| **Single compile** | `compile` compiles one source under a declared compiler profile. |
| **Matrix experiments** | `compiler-lab` runs multi-axis compiler/flag/version matrices from a lab manifest. |
| **Worker compile** | `compile-worker` provides bounded local or containerized compilation. |
| **Toolchain registry** | `toolchain-register` and `toolchain-verify` manage versioned compiler toolchains with hash verification. |

### Evidence, workflow, and project management

| Group | Capabilities |
|---|---|
| **Evidence store** | `evidence-add`, `claim-create`, `claim-attach`, `claim-verify`, `claim-contradict` track provenance-bearing evidence and claims. |
| **Workflow** | `workflow-init`, `workflow-show`, `workflow-update` manage per-function decompilation state across stages. |
| **Work queue** | `work-create`, `work-next`, `work-claim`, `work-propose`, `work-validate` implement a task queue for multi-analyst collaboration. |
| **Project memory** | `memory-add`, `memory-verify`, `memory-render` maintain an append-only, evidence-linked project ledger. |
| **Pipelines** | `pipeline-create`, `pipeline-run`, `pipeline-status` orchestrate durable multi-stage analysis pipelines. |
| **Project operations** | `project-migrate`, `project-backup`, `project-restore`, `project-repair`, `project-gc` manage project lifecycle. |

### Ground truth and benchmarks

| Group | Capabilities |
|---|---|
| **Corpus** | `corpus-create-manifest`, `corpus-build`, `corpus-verify`, `corpus-compare` build and validate compiler ground-truth corpora. |
| **Synthetic corpus** | `corpus-generate`, `corpus-generated-verify` produce deterministic parameterized C/C++ source corpora. |
| **Benchmarks** | `benchmark-run` executes declared benchmark corpora with measured results. |

### Security and release

| Group | Capabilities |
|---|---|
| **Audit** | `security-audit` audits source trees for declared security checks; `dependency-audit` runs pip-audit. |
| **SBOM** | `sbom-generate` produces software bills of materials. |
| **Release** | `release-manifest-verify` verifies hash manifests; `release-gate` evaluates target-release acceptance contracts. |

### Integration and service

| Group | Capabilities |
|---|---|
| **DynamoRIO** | `drcov-run` and `drcov-parse` trace execution and parse coverage logs. |
| **Integration** | `integration-run` executes declared integration scenarios. |
| **Service** | `serve` exposes a read-only project API (loopback-only by default). |

---

## Supported project types

x86decomp recognizes three decompilation project approaches:

| Mode | Goal |
|---|---|
| **Matching** | Byte-identical reconstruction of every function. Every candidate must pass exact-byte diffing, COFF symbol comparison, and full-image relink verification. |
| **Functional** | Semantically equivalent reconstruction verified through dynamic, symbolic, and harness-based validation. Functions may differ in register allocation or instruction selection. |
| **Hybrid** | A mix of matching functions (where exact parity is achievable) and functional equivalents (where compiler or floating-point differences block matching). Tracked per-function via workflow state. |

Projects default to both `matching` and `functional` modes. Individual functions are tracked separately through the workflow system (`workflow-init`, `workflow-update`).

---

## Typical process

```console
# 1. Initialize a PE analysis project
$ x86decomp init target.exe my-project/

# 2. Inspect the binary
$ x86decomp inspect-pe target.exe

# 3. Snapshot available tools
$ x86decomp snapshot-tools --output tools.json --ghidra-home /opt/ghidra

# 4. Export Ghidra function artifacts
$ x86decomp ghidra-export target.exe ghidra-project/ target functions-out/

# 5. Import artifacts into the project
$ x86decomp artifact-import my-project/ functions-out/

# 6. Initialize per-function workflow states
$ x86decomp workflow-init my-project/ sub_401000 --mode matching --mode functional

# 7. Create decompilation candidates, compile, validate
#    (driven through the pipeline or manual work-queue loop)

# 8. Verify project integrity
$ x86decomp verify-project my-project/

# 9. Track convergence
$ x86decomp convergence-analyze target.exe candidate.exe --report convergence.json
```

---

## Where to start

| If you want to... | Go here |
|---|---|
| Install the toolkit | [Installation guide](getting-started/installation.md) |
| Set up your first project | [First project](getting-started/first-project.md) |
| Understand verification | [Verification](getting-started/verification.md) |
| Learn the conceptual model | [Concepts overview](concepts/overview.md) |
| Browse all commands | [Command reference index](commands/index.md) |
| Understand the architecture | [Architecture](reference/architecture.md) |

---

## Evidence vocabulary

The toolkit uses a precise vocabulary to avoid conflating confidence levels:

| Term | Meaning |
|---|---|
| **Observed** | A fact directly measured from the binary, file, or tool output. |
| **Derived** | An inference produced mechanically from observations (e.g., compiler version inferred from entry-point byte patterns). |
| **Proposed** | A human or LLM-supplied hypothesis not yet independently verified. |
| **Corroborated** | A claim independently supported by at least one piece of evidence from a different source. |
| **Accepted** | A claim that has passed its declared evidence gate (e.g., two independent validators, or exact-byte match). |
| **Verified** | A claim whose supporting evidence has itself been verified (content hashes, tool versions, reproducibility). |
| **Rejected** | A claim contradicted by independent evidence. |
| **Blocked** | A claim that cannot be evaluated due to missing tools, unsupported instructions, or incomplete integration. |
| **Unknown** | Explicitly recorded absence of evidence; not a silent skip. |

!!! note "Explicit unknowns"
    Unsupported instructions, missing adapters, timeouts, and blocked integrations are reported
    explicitly. The toolkit never silently skips validation or fabricates success.
