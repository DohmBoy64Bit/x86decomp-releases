# Release Commands

Software bill of materials generation and release hash manifest verification.

---

## `x86decomp sbom-generate`

Generate a software bill of materials.

### Purpose

Inventories the installed toolkit distribution: Python package metadata, declared dependencies with versions, installed files, and any bundled tool executables. The output is a self-contained JSON document suitable for supply-chain audit and release attestation.

### Syntax

```
x86decomp sbom-generate OUTPUT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `OUTPUT` | yes | path | Output path for the JSON SBOM document |

### Files written

- `OUTPUT` — JSON software bill of materials

### SBOM contents

| Section | Description |
|---|---|
| `metadata` | Release version and generation timestamp |
| `packages` | Installed Python packages with versions and dependencies |
| `files` | Installed file inventory with paths and hashes |
| `executables` | Bundled or referenced tool executables |

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr

### Example

```console
$ x86decomp sbom-generate release/sbom-0.7.11.json
```

---

## `x86decomp release-manifest-verify`

Verify every entry in a release hash manifest.

### Purpose

Checks each file listed in a release hash manifest against the current filesystem root. Verifies that every declared file exists and matches its expected SHA-256 hash. Reports missing files, unexpected files, and hash mismatches individually.

### Syntax

```
x86decomp release-manifest-verify ROOT [--manifest PATH]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `ROOT` | yes | path | Root directory to verify against the manifest |

### Options

| Option | Default | Description |
|---|---|---|
| `--manifest PATH` | none | Path to the JSON release hash manifest |

### Files read

- `ROOT` — filesystem tree to verify
- `--manifest PATH` — JSON hash manifest declaring expected file paths and SHA-256 hashes

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error or any hash mismatch
- Reports individual mismatches with path, expected hash, and observed hash

### Example

```console
$ x86decomp release-manifest-verify ./dist --manifest release/manifest-0.7.11.json
```

### Related commands

- [sbom-generate](#x86decomp-sbom-generate) — Generate SBOM
- [security-audit](audit.md#x86decomp-security-audit) — Source tree security audit
- [dependency-audit](audit.md#x86decomp-dependency-audit) — Dependency vulnerability scan
