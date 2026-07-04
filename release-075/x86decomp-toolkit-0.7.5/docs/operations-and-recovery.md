# Operations, resumability, and recovery

## Durable pipeline model

A pipeline is a JSON manifest with a stable `pipeline_id` and ordered stages. A stage is either:

- a bounded command with declared inputs, outputs, environment, isolation, and limits; or
- an evidence gate requiring named verified claims.

The orchestrator stores jobs and events in SQLite. A stage’s idempotency key includes its normalized contract and input hashes. Successful outputs are materialized under `orchestration/results`, copied into the immutable content store, and recorded in project state.

A previous success is reused only when its output files and hashes still validate. Missing or altered outputs force a rerun.

## Job states

```text
pending · running · succeeded · failed · blocked · cancelled
```

`blocked` means required evidence or a required adapter/capability was unavailable. It is not success.

## Cancellation and stale runners

Running jobs update a heartbeat. Cancellation is polled by the worker and terminates the child process group. If a process or host dies, `pipeline-recover` can reset jobs whose heartbeat is older than a declared bound.

```bash
x86decomp pipeline-cancel project/ pipeline-id --stage-id compile
x86decomp pipeline-recover project/ --pipeline-id pipeline-id --stale-seconds 600
```

Recovery is explicit and logged. It does not infer that partially written outputs are valid.

## Transactional state

Project schema v3 adds:

- `state/project-state.sqlite3`;
- migration history;
- snapshots and leases;
- immutable artifact references;
- target-pack and orchestration paths.

Migrations are monotonic. A non-dry-run migration creates or records a backup as configured and writes migration provenance.

## Check, backup, restore, repair, and GC

```bash
x86decomp project-check project/
x86decomp project-migrate project/ --dry-run
x86decomp project-backup project/ backup.tar.gz
x86decomp project-restore backup.tar.gz restored-project/
x86decomp project-repair project/             # dry run
x86decomp project-repair project/ --apply
x86decomp project-gc project/                  # dry run
x86decomp project-gc project/ --apply
```

Backups are deterministic gzip/tar archives with normalized metadata. Backup creation rejects symlinks. Restore rejects traversal, absolute paths, links, devices, oversized members, and excessive expansion, and extracts through a staging directory.

Repair only reconstructs indexes and missing empty infrastructure that can be derived safely. It does not rewrite target bytes, evidence, claims, or candidate source.

Garbage collection deletes only unreferenced content-store objects and defaults to dry-run.

## Worker boundaries

### Local bounded worker

Applies timeout, CPU/memory/process limits where the host supports them, captures bounded logs, and terminates the process group. This is operational containment, not a security sandbox.

### Container worker

Uses Docker or Podman with:

- `--network=none`;
- `--read-only`;
- `--cap-drop=ALL`;
- `no-new-privileges`;
- explicit memory and PID limits;
- one work bind mount;
- ephemeral no-exec `/tmp`.

The container image remains an operator-controlled dependency and must be pinned by digest for a reproducible production deployment.

## Reproducibility

`reproduce-create` records project files, artifact identities, selected tools, configuration, and known limits. `reproduce-verify` checks the manifest against the current machine and explains exact mismatches.

```bash
x86decomp reproduce-create project/ project/reports/reproducibility/manifest.json \
  --required-tool ghidra --required-tool clang
x86decomp reproduce-verify project/ project/reports/reproducibility/manifest.json
```

## Release gate

The release gate can require:

- valid project and target pack;
- per-function workflow minima;
- verified claims;
- succeeded durable pipelines;
- a valid reproduction manifest;
- a passing security report;
- a convergence report satisfying target acceptance.

The output includes a truth statement. A pass means only that the declared gate passed.
