# Test Bundle Commands

Hash-sealed authorized static test bundles for safe artifact exchange.

---

## `x86decomp test-bundle-create`

Create a hash-sealed authorized static test bundle.

### Purpose

Creates a ZIP archive containing a `x86decomp-test-bundle.json` manifest and hash-listed artifact files. The bundle is the preferred way to provide a real regression target without asking the toolkit to execute an uploaded Windows program. All hashes are calculated at creation time and the manifest includes an affirmative authorization statement.

### Syntax

```
x86decomp test-bundle-create OUTPUT --artifact role=path... --authorization TEXT [--name NAME] [--description DESC] [--expected-architecture {x86,x86_64}]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `OUTPUT` | yes | path | Output path for the `.zip` test bundle |

### Options

| Option | Default | Description |
|---|---|---|
| `--artifact role=path` | **required** (repeatable) | Artifact declaration using `role=path` format; must be specified at least once |
| `--authorization TEXT` | **required** | Affirmative authorization statement (e.g., "I own these artifacts or have permission to analyze them.") |
| `--name NAME` | none | Human-readable bundle name |
| `--description DESC` | none | Bundle description |
| `--expected-architecture {x86,x86_64}` | none | Expected target architecture for validation |

### Supported artifact roles

| Role | Description |
|---|---|
| `primary_image` | Primary PE image (EXE or DLL) to analyze |
| `reference_image` | Reference PE image for comparison |
| `candidate_image` | Candidate (rebuilt) PE image for comparison |
| `pdb` | Matching PDB debug database |
| `linker_map` | MSVC-compatible linker map file |
| `coff_object` | COFF object file from the original build |
| `static_library` | COFF static or import library |
| `source` | Source file |
| `compiler_profile` | JSON compiler profile |
| `image_profile` | JSON image layout profile |
| `documentation` | Supporting documentation |

### Files written

- `OUTPUT` — ZIP bundle containing manifest and artifact files

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr

!!! warning "Authorization required"
    `--authorization` is a required argument. The manifest records an affirmative statement
    that you own or are authorized to analyze the artifacts. The inspector rejects bundles
    without this statement.

### Example

```console
$ x86decomp test-bundle-create authorized-target.zip \
    --name "Authorized game build 1.0" \
    --expected-architecture x86 \
    --authorization "I own these artifacts or have permission to analyze them." \
    --artifact primary_image=target.exe \
    --artifact linker_map=target.map \
    --artifact pdb=target.pdb \
    --artifact coff_object=obj/main.obj
```

For whole-image comparison:

```console
$ x86decomp test-bundle-create image-pair.zip \
    --authorization "Authorized private regression artifacts." \
    --artifact reference_image=original.exe \
    --artifact candidate_image=rebuilt.exe \
    --artifact image_profile=original-image-profile.json
```

---

## `x86decomp test-bundle-inspect`

Safely extract, verify, and statically inspect an authorized test bundle.

### Purpose

Performs static-only operations on a test bundle: verifies archive and artifact hashes, parses PE images, scans bounded MSVC metadata, parses COFF objects and libraries, inspects PDB identity, resolves COMDAT groups, parses linker maps, and compares reference/candidate images when both are supplied. The inspector never executes any binary, object, library, source file, or script from the bundle.

### Syntax

```
x86decomp test-bundle-inspect BUNDLE [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `BUNDLE` | yes | path | Test bundle ZIP archive to inspect |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON inspection report to this path |

### Inspection operations

| Operation | Description |
|---|---|
| Archive verification | Validates archive structure and artifact hashes |
| PE parsing | Extracts section, import, export, resource, TLS, debug, and relocation metadata |
| MSVC metadata | Scans RTTI, vtables, unwind/EH, TLS, and initializer evidence |
| COFF parsing | Parses classic COFF and bigobj objects plus bounded static/import archives |
| PDB identity | Parses PDB identity, TPI/IPI headers, DBI modules, and contributions |
| COMDAT resolution | Resolves COMDAT groups across supplied objects |
| Linker layout | Parses MSVC-compatible maps and reconstructs evidenced layout relationships |
| Image comparison | Compares reference and candidate images when both are supplied |

!!! danger "Static only"
    The inspector performs **only** static operations. It never executes any EXE, DLL,
    object, library, source file, or script from the bundle. Parser success is not a
    malware-safety determination and is not proof of semantic equivalence.

### Guardrails

The inspector rejects:
- Absolute paths, `..` components, backslash or drive-qualified paths
- Duplicate members, symbolic links
- Oversized files or excessive compression ratios
- Undeclared or missing artifact files
- Artifact hash mismatches
- Manifests without an affirmative authorization statement

### Example

```console
$ x86decomp test-bundle-inspect authorized-target.zip \
    --report reports/test-bundle.json
```

### Related commands

- [artifact-import](artifact.md#x86decomp-artifact-import) — Import function artifact into project
- [artifact-verify](artifact.md#x86decomp-artifact-verify) — Verify function artifact integrity
- [inspect-pe](../analysis/pe-pdb.md) — Parse PE metadata
- [pdb-inspect](../analysis/pe-pdb.md) — Inspect PDB database
