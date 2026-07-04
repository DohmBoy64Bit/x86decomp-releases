---
title: 'Example: project operations and recovery workflow'
description: Maintain a long-lived project with checks, deterministic backups, safe
  restore, dry-run migration and repair, content-addressed garbage collection, durable
  pipelines, retries, cancellation, and stale-run recovery.
---

<a id="model"></a>
<a id="project-operations-recovery-flow-title"></a>
<a id="project-operations-recovery-flow-desc"></a>
<a id="arrow-project-operations-recovery"></a>
<a id="project-operations-recovery-flow-caption"></a>
<a id="check"></a>
<a id="migrate"></a>
<a id="gc"></a>
<a id="pipeline"></a>
<a id="control"></a>
<a id="recover"></a>
<a id="restore"></a>
<a id="limits"></a>
<a id="source-basis"></a>

# Example: project operations and recovery workflow

Maintain a long-lived project with checks, deterministic backups, safe restore, dry-run migration and repair, content-addressed garbage collection, durable pipelines, retries, cancellation, and stale-run recovery.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.8 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is an operational lifecycle workflow shared by matching, functional, and both-mode projects.

**On this page**

1. [Operations model](#model)
2. [Check and back up](#check)
3. [Migrate and repair](#migrate)
4. [Verify and collect content](#gc)
5. [Create and run pipeline](#pipeline)
6. [Inspect/retry/cancel](#control)
7. [Recover stale jobs](#recover)
8. [Restore safely](#restore)
9. [Truth boundary](#limits)
10. [Source basis](#source-basis)

## Operations model

Destructive or state-changing operations are separated from inspection and use explicit apply or destination choices.Project check → Deterministic backup → Dry-run change → Apply repair → Durable pipeline → Recovery → Verified restore

Project checkDeterministic backupDry-run changeApply repairDurable pipelineRecoveryVerified restore

Destructive or state-changing operations are separated from inspection and use explicit apply or destination choices.

```ascii-fallback
Project check → Deterministic backup → Dry-run change → Apply repair → Durable pipeline → Recovery → Verified restore
```

1

## Check state and create a backup first

```
x86decomp project-check project
x86decomp project-backup project backups/project-before-change.tar.gz
```

The backup is a deterministic gzip/tar archive for the same project content and rejects symlinks. Keep it outside the project root that may be repaired or migrated.

2

## Preview migrations and repairs

```
x86decomp project-migrate project --dry-run
x86decomp project-repair project
```

Both commands are inspection-first. `project-repair` is dry-run unless `--apply` is supplied and repairs only derivable infrastructure; it does not invent missing source, toolchains, evidence, or validation results.

```
x86decomp project-migrate project --backup backups/project-migration.tar.gz
x86decomp project-repair project --apply
```

3

## Verify the content store before garbage collection

```
x86decomp content-verify project/artifacts
x86decomp project-gc project
x86decomp project-gc project --apply
```

GC is dry-run by default and removes only unreferenced content-store objects when applied. It is not a generic deletion command for project reports or source files.

4

## Create and run a durable pipeline

```
x86decomp pipeline-create project project/orchestration/pipelines/default.json
x86decomp pipeline-run project project/orchestration/pipelines/default.json
```

Use `--without-ghidra` when the default pipeline must omit that stage. The orchestrator persists jobs in SQLite, computes idempotency keys from normalized contracts and input hashes, materializes outputs into the content store, and revalidates successful outputs before reuse.

5

## Inspect, retry, or cancel explicit jobs

```
x86decomp pipeline-status project PIPELINE_ID
x86decomp pipeline-retry project PIPELINE_ID STAGE_ID --cascade
x86decomp pipeline-cancel project PIPELINE_ID --stage-id STAGE_ID
```

Retry and cancellation operate on durable identifiers returned by the pipeline. `--cascade` deliberately invalidates dependent stages; it is not implied by a normal retry.

6

## Recover only stale runner heartbeats

```
x86decomp pipeline-recover project --pipeline-id PIPELINE_ID --stale-seconds 600
```

Recovery resets jobs whose durable runner heartbeat is stale under the supplied threshold. It does not declare failed validators successful or reconstruct lost outputs.

7

## Restore into a deliberate destination

```
x86decomp project-restore backups/project-before-change.tar.gz restored-project
x86decomp project-check restored-project
x86decomp content-verify restored-project/artifacts
```

Restore uses staging and archive safety bounds before committing the destination. Verify the restored project before replacing any active workspace.

## Operational guarantees and limits

- Backups protect recorded project state, not external toolchains or referenced artifacts that were never copied.
- Repair restores derivable infrastructure only.
- Pipeline reuse depends on validated identities and materialized outputs.
- Stale-job recovery changes runner state, not scientific or validation conclusions.
- Always retain a verified backup before applying migrations, repair, or GC.

## v0.7.8 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file |
| --- |
| `src/x86decomp/cli.py` |
| `src/x86decomp/project_state.py` |
| `src/x86decomp/orchestrator.py` |
| `src/x86decomp/content_store.py` |
| `src/x86decomp/security_audit.py` |
| `tests/test_project.py` |


## Related examples

- [Matching project](matching-project.md)
- [Functional project](functional-project.md)
- [Hybrid composition](hybrid-project.md)
