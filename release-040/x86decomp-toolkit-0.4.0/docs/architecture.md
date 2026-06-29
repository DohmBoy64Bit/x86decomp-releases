# Architecture — 0.4.0

The maintained visual forms are:

- Mermaid: [`ARCHITECTURE_MAP.md`](ARCHITECTURE_MAP.md)
- plain-text ASCII: [`ARCHITECTURE_MAP_ASCII.txt`](ARCHITECTURE_MAP_ASCII.txt)

Both are release artifacts and must change together.

## Objective

Coordinate immutable binary evidence, static and dynamic analysis, candidate source,
compilers, linkers, matching and functional validators, human/AI work, and durable
project state without allowing any single tool to promote its own output to fact.

## Major planes

### Target and evidence plane

A target pack binds a PE image and optional PDB, MAP, COFF/bigobj objects, libraries,
rebuilt image, compiler information, and explicit operator decisions. Inputs are
hash-sealed. Observations and decisions are stored separately. Missing compiler,
linker, language, authorization, or layout facts remain blockers.

### Analysis plane

Ghidra is the primary decompiler and P-code source. Capstone is the independent decoder.
Native parsers handle bounded PE, PDB/MSF, COFF/bigobj, archive, linker-map, RTTI,
vtable, unwind, TLS, initializer, and exception evidence. All parsers report bounds and
unsupported forms rather than fabricating records.

### Project control plane

Project schema v3 combines immutable content-addressed artifacts, a transactional
SQLite state database, two independent per-function mode states, evidence/claim gates,
work queues, MCP mutation journals, and a hash-chained memory ledger. Migrations create
a backup before changing canonical state.

### Durable orchestration plane

Pipeline manifests define deterministic stages. Job keys derive from stage definition,
input hashes, and tool/environment policy. Successful outputs are materialized outside
ephemeral work directories and sealed in the content store. Missing or altered outputs
invalidate the prior result. Cancellation, retries, heartbeat, stale recovery, and
concurrent leases are persisted transactionally.

### Worker plane

Workers execute declared argument arrays under bounded local-resource or container
policies. Local limits reduce accidental resource exhaustion but are not advertised as
a security sandbox. Container mode records runtime/image/network/filesystem policy.
Compiler workers add toolchain/source/profile/output provenance and cache keys.

### Candidate and linker plane

Generated project templates create real source, assembly, analysis, test, compiler,
linker, report, and orchestration directories. They never emit fake decompiled C/C++.
Matching templates retain exact assembly fallback and require explicit compiler/linker
identity. Linker reconstruction consumes MAP, object, archive, COMDAT, relocation,
section, TLS, initializer, resource, exception, and image-layout evidence.

### Validation plane

Matching and functional lanes remain independent.

Matching validation includes ABI observations, PE-function-to-COFF comparison,
relocation normalization, instruction/CFG comparison, objdiff, exact byte match,
hash-gated image patching, manifest relinking, and target-specific whole-image
convergence.

Functional validation includes ABI observations, declared Unicorn execution, DynamoRIO
coverage, bounded Z3/angr symbolic models, generated harnesses, and explicit integration
scenarios. Every result states its input, observation, path, memory, timeout, and
execution/isolation scope.

### Acceptance and reproducibility plane

Validator reports become evidence, not facts. Claims pass only through the independent
evidence gate. Release acceptance aggregates project integrity, target-pack integrity,
workflow minima, claims, durable pipelines, reproducibility, security, and optional
whole-image convergence. A passing gate means only that those declared contracts passed.

## Dependency direction

```text
CLI / read-only service
  -> target packs / templates / project state / orchestrator
  -> workers / compiler workers / linker reconstruction
  -> PE / COFF / PDB / MAP / Ghidra / decoder adapters
  -> matching / functional / convergence validators
  -> evidence / claims / work queue / project memory

all modules -> util / errors
```

No validator rewrites immutable evidence. No worker owns project truth. No AI proposal
bypasses evidence, compiler, runtime, or acceptance gates.
