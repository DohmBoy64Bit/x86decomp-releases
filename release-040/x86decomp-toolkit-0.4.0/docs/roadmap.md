# Roadmap

## Version 0.4 production-pilot milestone

Version 0.4 converts the 0.3 analysis baseline into a durable target-production
platform while preserving every retained 0.3.1 command, schema, module, adapter,
workflow state, and Ghidra script.

Implemented milestones:

- evidence-driven target packs and automatic/semi-automatic matching, functional, or
  hybrid project templates that preserve unknown compiler/linker/language facts;
- a transactional schema-v3 project database with migration, integrity checking,
  deterministic backup/restore, repair, snapshots, leases, and content-store garbage
  collection;
- a durable idempotent workflow orchestrator with job identities, retries,
  cancellation, heartbeat/stale-job recovery, content-hashed inputs, materialized
  outputs, and output-tamper invalidation;
- bounded local and container worker contracts with timeout, CPU, memory, output-size,
  environment, network-policy, and provenance records;
- compiler-worker and target-specific linker-reconstruction plans;
- automatic dynamic-harness generation from explicit ABI and pointer-region contracts;
- deeper C++ relationship recovery over bounded RTTI/vtable metadata;
- flag-accurate bounded symbolic additions for carry/borrow and selected condition
  operations;
- target-specific whole-image convergence history and release-gate aggregation;
- reproducibility manifests, source-tree security audits, CycloneDX SBOM output, and a
  real pip-audit adapter;
- a configurable deterministic C/C++ source-corpus generator whose outputs are hashed
  and explicitly separated from compiler-execution or equivalence claims;
- a read-only operational service snapshot covering project, workflow, worker, and
  verification health;
- an integrated test-suite catalog and compatibility gates that prevent silent surface
  loss.

## Evidence still required per deployment

The architecture is implemented, but a target is production-accepted only after its
own evidence and live environment satisfy the release gate. In particular:

1. exercise the exact Ghidra, DynamoRIO, objdiff, compiler, linker, and container
   versions selected for the target;
2. migrate or create the target project and verify backup/restore on a second clean
   environment;
3. run target-specific matching and/or functional acceptance scenarios;
4. reproduce accepted artifacts from immutable inputs and pinned tools;
5. resolve or explicitly block unsupported PDB, exception, linker, alias, or ISA cases;
6. retain authorization and threat-model decisions for every native execution boundary.

## Candidates for 0.5

- complete selected CodeView type/global/public symbol streams for named compiler
  families while preserving record offsets and provenance;
- richer MSVC exception-state and language-handler models tied to verified compiler
  versions;
- linker-family plugins for selected MSVC/LLD generations, including ICF/LTCG and
  incremental-link evidence where observable;
- distributed signed worker attestations and remote content-store replication;
- analyst UI mutation workflows backed by the existing evidence and transaction gates;
- broader symbolic summaries for floating point, Windows APIs, callbacks, threads, and
  heap object lifetimes;
- multiple authorized real-world pilot targets with published bounded metrics.

No roadmap item changes the non-goals: the toolkit does not promise original-source
recovery, universal C++ reconstruction, or proof of arbitrary-program equivalence.
