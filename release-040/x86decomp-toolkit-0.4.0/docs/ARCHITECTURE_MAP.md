# x86decomp-toolkit architecture map

**Architecture version:** 0.4.0  
**Release contract:** production-pilot architecture with bounded, evidence-governed claims  
**ASCII companion:** [`docs/ARCHITECTURE_MAP_ASCII.txt`](ARCHITECTURE_MAP_ASCII.txt)  
**Test-suite map:** [`test-suite/docs/ARCHITECTURE_MAP.md`](../test-suite/docs/ARCHITECTURE_MAP.md) and [`test-suite/docs/ARCHITECTURE_MAP_ASCII.txt`](../test-suite/docs/ARCHITECTURE_MAP_ASCII.txt)

This map describes implemented subsystem boundaries. It does not claim universal source recovery or arbitrary-program equivalence.

## Actual v0.4.0 architecture

```mermaid
flowchart TB
    subgraph INPUTS[Authorized target inputs]
        PE[PE32 x86 or PE32+ x86-64\nEXE or DLL]
        SUPPORT[PDB · MAP · OBJ/bigobj · LIB/A\nrebuilt image · source/toolchain records]
        DECISIONS[Explicit target decisions\nmode · authorization · known compiler/linker facts]
    end

    PE --> INGEST
    SUPPORT --> INGEST
    DECISIONS --> TPACK

    subgraph ING[Immutable ingestion]
        INGEST[Safety checks · SHA-256 identity\ncopy/reference policy · bounded parsers\nno implicit target execution]
        TPACK[Verified target pack\nobservations separate from decisions]
        STORE[Content-addressed immutable store]
    end
    INGEST --> TPACK
    INGEST --> STORE

    subgraph STATIC[Static-analysis plane]
        FORMAT[PE · PDB/MSF · COFF/bigobj/archive\nMAP · resources · TLS · relocations]
        CPP[MSVC RTTI · vtables · EH/unwind\nSafeSEH · CRT initializers]
        GHIDRA[Ghidra functions · disassembly · C\ntoken tree · raw/high P-code · references]
        DECODER[Independent Capstone decode\nnormalized operands · CFG · cross-check]
    end
    TPACK --> FORMAT
    TPACK --> CPP
    TPACK --> GHIDRA
    GHIDRA --> DECODER

    subgraph CONTROL[Project control plane]
        PDBASE[Transactional project-state database\nschema migrations · snapshots · leases]
        ADB[Global analysis database\nsymbols · references · ABI/type constraints]
        MEMORY[Hash-chained project memory]
        EVIDENCE[Evidence · claims · contradictions\nthree-independent-source gate]
        WORK[Validator-gated human/AI work queue]
        ORCH[Durable workflow orchestrator\nidempotency · dependencies · retries\nheartbeats · cancellation · recovery]
    end
    STORE --> PDBASE
    FORMAT --> ADB
    CPP --> ADB
    GHIDRA --> ADB
    PDBASE <--> ORCH
    ADB --> EVIDENCE
    EVIDENCE --> WORK
    ORCH --> MEMORY

    subgraph TEMPLATE[Candidate-generation plane]
        TEMPLATE_ENGINE[Grounded target template engine\nmatching · functional · hybrid]
        ASM[Exact-byte assembly fallback]
        CANDIDATE[Ghidra-derived then human/AI-corrected\nC/C++ candidate source]
        LOCAL_PACKETS[Local decomp.me packets\nMCP proposals with approval hashes]
    end
    TPACK --> TEMPLATE_ENGINE
    ADB --> TEMPLATE_ENGINE
    TEMPLATE_ENGINE --> ASM
    TEMPLATE_ENGINE --> CANDIDATE
    CANDIDATE --> LOCAL_PACKETS

    subgraph BUILD[Compiler and linker plane]
        WORKERS[Bounded local workers or isolated containers\nresource limits · no network by default]
        COMPILERS[Hash-pinned user-owned toolchains\ncompiler profiles · flag matrices · cache]
        CORPUS[Built-in and generated ground-truth corpus\nx86/x64 · C/C++ · exact provenance]
        LINKER[COFF/archive/COMDAT resolution\nlayout reconstruction · relink manifests]
        PATCH[Hash-gated PE patch backend]
    end
    ASM --> WORKERS
    CANDIDATE --> WORKERS
    WORKERS --> COMPILERS
    CORPUS --> COMPILERS
    COMPILERS --> LINKER
    LINKER --> PATCH

    subgraph MATCH[Matching-decompilation lane]
        MCOMPILE[candidate compiles]
        MABI[ABI observations pass]
        MDIFF[PE function ↔ COFF symbol\nrelocation normalization · instruction/CFG diff]
        MBYTE[exact scoped byte match]
        MIMAGE[verified patch or relink]
        MWHOLE[target-specific whole-image convergence]
    end
    COMPILERS --> MCOMPILE --> MABI --> MDIFF --> MBYTE --> MIMAGE --> MWHOLE

    subgraph FUNC[Functional-decompilation lane]
        FCOMPILE[candidate compiles]
        FABI[ABI observations pass]
        FDIFF[Unicorn differential harnesses]
        FCOVER[DynamoRIO observed coverage]
        FSYM[bounded Z3/angr symbolic and alias model]
        FINTEG[explicit-consent integration scenarios]
    end
    COMPILERS --> FCOMPILE --> FABI --> FDIFF --> FCOVER --> FSYM --> FINTEG

    subgraph ACCEPT[Acceptance, evidence, and feedback]
        REPORTS[Versioned validator reports with exact scope]
        CLAIMGATE[Evidence record → narrow claim → contradiction check]
        RELEASE[Target release gate\nproject integrity · workflow minima · pipelines\nreproduction · security · convergence]
        REPRO[Reproducibility manifest and clean-machine explanation]
    end
    MWHOLE --> REPORTS
    FINTEG --> REPORTS
    REPORTS --> CLAIMGATE --> RELEASE
    PDBASE --> REPRO --> RELEASE
    RELEASE -->|accepted facts and states| PDBASE
    CLAIMGATE -->|failed or contradictory| ADB

    subgraph OPS[Operations and observation]
        BACKUP[Deterministic backup · restore · repair · GC]
        SERVICE[Read-only FastAPI/API dashboard]
        SECURITY[SBOM · dependency audit · source audit\nmanifest verification]
    end
    PDBASE --> BACKUP
    PDBASE --> SERVICE
    STORE --> SECURITY
    SECURITY --> RELEASE
```

## Actual matching-state path

```mermaid
stateDiagram-v2
    [*] --> not_started
    not_started --> decompiled: function artifact and candidate representation exist
    decompiled --> compiles: declared compiler emitted the expected artifact
    compiles --> abi_compatible: declared ABI checks passed
    abi_compatible --> instruction_similar: normalized instruction/CFG comparison passed
    instruction_similar --> byte_matched: scoped original and candidate bytes are exact
    byte_matched --> image_integrated: hash-gated patch or relink integration passed
    image_integrated --> full_relink_validated: target-specific relink/image gate passed

    not_started --> blocked
    decompiled --> blocked
    compiles --> blocked
    abi_compatible --> blocked
    instruction_similar --> blocked
    byte_matched --> blocked
    image_integrated --> blocked
    blocked --> not_started: blocker resolved with audit trail
```

## Actual functional-state path

```mermaid
stateDiagram-v2
    [*] --> not_started
    not_started --> decompiled: function artifact and candidate representation exist
    decompiled --> compiles: declared compiler emitted the expected artifact
    compiles --> abi_compatible: declared ABI checks passed
    abi_compatible --> differentially_validated: all declared concrete harnesses passed
    differentially_validated --> symbolically_bounded: bounded symbolic obligations passed
    symbolically_bounded --> integration_validated: declared integration scenarios passed

    not_started --> blocked
    decompiled --> blocked
    compiles --> blocked
    abi_compatible --> blocked
    differentially_validated --> blocked
    symbolically_bounded --> blocked
    blocked --> not_started: blocker resolved with audit trail
```

## Independent function state

```mermaid
flowchart LR
    F[Function pe-rva:XXXXXXXX] --> M[Matching state]
    F --> U[Functional state]
    M --> MR[Matching reports]
    U --> UR[Functional reports]
    MR --> E[Shared evidence and claim gate]
    UR --> E
```

A function can be `instruction_similar` in matching mode while already `integration_validated` in functional mode. Neither lane promotes the other.

## Trust and execution boundaries

```mermaid
flowchart LR
    U[Untrusted target artifacts] -->|bounded parse only| S[Static ingestion]
    S --> P[Project evidence]
    P --> L[Local bounded worker\nnot a security boundary]
    P --> C[Container worker\nread-only root · no network · dropped capabilities]
    P --> V[Disposable VM/external wrapper\nfor unknown native execution]
    L --> R[Reports]
    C --> R
    V --> R
```

## Maintenance contract

Update this document and `docs/ARCHITECTURE_MAP_ASCII.txt` together whenever any of the following changes:

- project schemas, migrations, databases, or durable job states;
- supported target inputs or parser boundaries;
- matching or functional states;
- worker isolation, adapter, or execution policy;
- target-pack/template behavior;
- compiler/linker, validation, convergence, release, or evidence gates;
- service/API ownership or trust boundaries.

The integrated test suite checks the presence, release version, required planes, workflow states, and cross-links of all four architecture artifacts.
