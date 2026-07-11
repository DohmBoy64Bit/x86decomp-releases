# Content store

The content store is a **content-addressable storage (CAS)** system. Each file is stored
under its SHA-256 digest. Metadata is tracked in the project state database.

## Location

The content store lives at the path specified by `content_store` in `project.json`
(default: `artifacts/`). It is created automatically during `x86decomp init`.

## `x86decomp content-put`

Store content by cryptographic digest.

```bash
x86decomp content-put STORE FILE \
  --media-type application/octet-stream \
  --reference REF \
  --kind artifact \
  --owner user
```

| Argument | Description |
|---|---|
| `STORE` | Path to the content store directory |
| `FILE` | File to store |
| `--media-type` | MIME type (default: `application/octet-stream`) |
| `--reference` | Human-readable reference string |
| `--kind` | Classification tag (default: `artifact`) |
| `--owner` | Identity recorded in metadata |

The file is copied into the store under a path derived from its SHA-256 digest. The
metadata record is written to the project state database.

!!! tip "Immutability"
    Once stored, content is immutable. The same digest always resolves to the same bytes.
    The store rejects attempts to overwrite existing digests with different content.

## `x86decomp content-verify`

Verify content-addressed storage integrity.

```bash
x86decomp content-verify STORE
```

| Argument | Description |
|---|---|
| `STORE` | Path to the content store directory |

This command reads every object in the store, recomputes its SHA-256 digest, and compares
it to the path-derived digest. Mismatches, missing files, and unexpected files are
reported.

## Integration with pipelines

The orchestrator copies successful stage outputs into the content store and records
references in project state. A previous success is reused only when its output files and
hashes still validate.

## Garbage collection

Unreferenced content-store objects can be cleaned with `project-gc`:

```bash
x86decomp project-gc project/           # dry run: lists what would be deleted
x86decomp project-gc project/ --apply   # deletes unreferenced objects
```

!!! warning "Dry-run first"
    Always run without `--apply` first to verify which objects will be removed.

## Recovery

If content verification fails, restore from backup:

```bash
x86decomp project-restore --project . --backup state/backups/latest.tar.gz
```

Or regenerate specific files and re-store them:

```bash
x86decomp compile --profile config/compiler-profiles/msvc-2019-x86.json \
  --source src/matched/00401000.c --output build/candidates/00401000.obj
x86decomp content-put --store artifacts --file build/candidates/00401000.obj
```
