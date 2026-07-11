# Reproducibility

Reproducibility manifests capture every input that matters for rebuilding a project's state:
project files, the binary, external tools, and the host environment. `reproduce-create` builds
the manifest; `reproduce-verify` checks whether current state matches it.

## Creating a Manifest

```bash
x86decomp reproduce-create --project ./myproject --output ./reproduce.json
```

This captures:

### Project Files

Every file in the project's critical path is recorded with SHA-256 and size:

- `project.json` — the project definition file.
- `analysis/program.json` — the program manifest (configurable via `program_manifest` in project.json).
- `memory/events.jsonl` — the project memory ledger.
- All files under the `target_pack` directory (if configured).

### Binary

The original binary's path and SHA-256 hash:

```json
"binary": {
  "path": "C:\\projects\\myproject\\original\\game.exe",
  "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "expected_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```

### Tools

Versions and hashes of external tools. Default toolset:

```json
"tools": {
  "python": {"available": true, "path": "/usr/bin/python3", "sha256": "..."},
  "java": {"available": true, "path": "/usr/bin/java", "sha256": "..."},
  "gcc": {"available": true, "path": "/usr/bin/gcc", "sha256": "..."},
  "clang": {"available": false, "requested": "clang"},
  "lld-link": {"available": true, "path": "/usr/bin/lld-link", "sha256": "..."},
  "objdiff-cli": {"available": false, "requested": "objdiff-cli"},
  "analyzeHeadless": {"available": true, "path": "/opt/ghidra/support/analyzeHeadless", "sha256": "..."}
}
```

Missing tools are recorded as `available: false` — they do not block manifest creation.

### Custom Tool List

```bash
x86decomp reproduce-create --project . \
  --output reproduce.json \
  --tools python,clang,lld-link,cmake
```

### Host Environment

```json
"host": {
  "python": "3.11.9 (main, Apr  2 2024, 08:25:04) [Clang 15.0.0]",
  "platform": "Linux-6.5.0-28-generic-x86_64-with-glibc2.38",
  "implementation": "CPython"
}
```

### Content Store

The manifest includes the content store index (SHA-256 catalog of all stored artifacts) if the
content store directory exists.

### Project and Target Pack Checks

The manifest records the result of `verify-project` (or `check_project_state` for schema v3
projects) and `target-pack-verify` if a target pack is present.

## Verifying a Manifest

```bash
x86decomp reproduce-verify --project ./myproject --manifest ./reproduce.json
```

The verifier checks:

1. **Every critical file**: Exists, hash unchanged, path within project root.
2. **Primary binary**: Exists, hash matches the expected value from `project.json`.
3. **Every tool**: Still available, executable hash unchanged.

```json
{
  "reproducible": true,
  "failures": [],
  "warnings": [
    "tool was unavailable when manifest was created: clang"
  ],
  "checked_at": "2026-07-11T10:30:00Z",
  "manifest": "C:\\projects\\myproject\\reproduce.json"
}
```

### Verification Failures

| Failure | Cause | Fix |
|---|---|---|
| `critical file missing: project.json` | Project deleted or moved | Restore from backup |
| `critical file changed: src/matched/...` | Source was edited | Commit changes and re-create manifest, or revert |
| `primary binary is unavailable or changed` | Binary moved or corrupted | Restore original binary |
| `required tool is now unavailable: clang` | Tool uninstalled | Reinstall the tool |
| `tool executable changed: gcc` | Compiler was updated | Install exact previous version or re-create manifest |
| `critical path escapes project` | Manifest contains absolute paths outside root | Re-create manifest with correct project root |

## What Is NOT Captured

The manifest intentionally excludes:

- **OS-level state**: Environment variables (except as reported by tools), kernel version,
  system libraries.
- **Compiler intermediate files**: `.o`, `.obj` files in `build/` directory (unless in
  content store).
- **Evidence files**: Individual evidence records are not bundled; they live in the project
  and are covered by `verify-project`.
- **Secrets**: No API keys, passwords, or tokens are ever recorded.

!!! warning "A matching hash proves byte identity, not semantic correctness"
    Two different tool versions can produce byte-identical outputs. The manifest records
    tool identities so you can reproduce the *process*, but the `sha256` of the output is
    the ultimate proof.

## Typical Workflow

### Initial Snapshot

```bash
# After project initialization and initial analysis
x86decomp reproduce-create --project ./myproject --output ./reproduce-v1.json
```

### After Toolchain Change

```bash
# After upgrading MSVC
x86decomp reproduce-create --project ./myproject --output ./reproduce-v2.json
x86decomp reproduce-verify --project ./myproject --manifest ./reproduce-v1.json
# Expect: tool executable changed: cl.exe
```

### Before Sharing with Collaborator

```bash
# Create a manifest for the collaborator
x86decomp reproduce-create --project . --output reproduce-share.json

# Collaborator verifies on their machine
x86decomp reproduce-verify --project . --manifest reproduce-share.json
# Fix any tool discrepancies before starting work
```

### CI Pipeline Check

```bash
# In CI: verify that the checked-out project matches the bundled manifest
x86decomp reproduce-verify --project . --manifest reproduce-baseline.json
# Exit code non-zero on failure → CI fails the build
```

## Limitations

The manifest records what *can* be recorded deterministically. Known limitations:

- **Tool availability is host-specific**: Missing tools remain unresolved. The manifest
  documents them but cannot install them.
- **External tool version output is preserved verbatim**: It is not interpreted as
  provenance by itself. Two tools with identical version strings may still produce
  different output.
- **Matching hash proves byte identity, not semantic correctness**: A reproduced binary
  with the right SHA-256 is byte-identical. That does not guarantee the source is correct
  or complete.
