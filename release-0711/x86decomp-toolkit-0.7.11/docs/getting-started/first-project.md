# First project

This guide walks through initializing an x86decomp project against a native Windows PE binary,
inspecting the binary and its debug information, verifying project integrity, and exporting
Ghidra function artifacts.

---

## Initialize a project

### From a PE binary

```console
$ x86decomp init target.exe my-project/
```

This command:

1. Parses the PE binary and extracts its architecture (x86 or x86-64), SHA-256 hash, and metadata.
2. Copies the binary into `my-project/original/` (unless `--reference-binary` is passed).
3. Creates the project directory tree with all required subdirectories:
   ```
   my-project/
   ├── project.json
   ├── analysis/
   │   ├── program.json
   │   ├── host.json
   │   ├── database/          (SQLite analysis database)
   │   ├── exports/
   │   ├── mcp-transactions/
   │   └── ghidra/
   ├── artifacts/             (content-addressed artifact store)
   ├── build/
   │   ├── compiler/
   │   ├── candidates/
   │   ├── cache/
   │   ├── patches/
   │   └── relink/
   ├── config/
   │   ├── compiler-profiles/
   │   ├── toolchains/
   │   └── harnesses/
   ├── evidence/
   │   ├── items/
   │   ├── claims/
   │   └── files/
   ├── functions/
   ├── memory/                (project memory ledger)
   ├── orchestration/
   │   ├── pipelines/
   │   ├── logs/
   │   └── work/
   ├── original/
   │   └── target.exe
   ├── reports/
   │   ├── matching/
   │   ├── functional/
   │   ├── benchmarks/
   │   ├── convergence/
   │   ├── reproducibility/
   │   └── security/
   ├── src/
   │   ├── asm/
   │   ├── staging/
   │   ├── matched/
   │   └── functional/
   ├── state/                 (project state database)
   ├── target-pack/
   ├── templates/
   ├── tests/
   │   └── harnesses/
   └── work/                  (work-queue database)
   ```
4. Initializes SQLite databases for analysis, project state, and the work queue.
5. Initializes the content-addressed artifact store.
6. Writes `project.json` with the project ID, architecture, default modes, and binary metadata.
7. Records an initial project-memory event.

Output:

```json
{
  "schema_version": 3,
  "project_id": "x86d-a1b2c3d4e5f67890-deadbeef",
  "created_at": "2026-07-11T14:22:31.123456Z",
  "supported_scope": "native Windows PE32 x86",
  "architecture": "x86",
  "default_modes": ["matching", "functional"],
  "binary": {
    "name": "target.exe",
    "source_kind": "copied",
    "path": "original/target.exe",
    "sha256": "a1b2c3d4e5f67890...",
    "size": 172032
  },
  "program_manifest": "analysis/program.json",
  "analysis_database": "analysis/database/analysis.sqlite3",
  "work_queue": "work/tasks.sqlite3",
  "memory_ledger": "memory/events.jsonl",
  "function_root": "functions",
  "evidence_root": "evidence",
  "project_state_database": "state/project-state.sqlite3",
  "content_store": "artifacts",
  "target_pack": "target-pack/target.toml",
  "orchestration_root": "orchestration",
  "toolkit_release": "0.7.11",
  "status": "initialized"
}
```

!!! tip "Reference binary mode"
    Pass `--reference-binary` to avoid copying the binary into the project directory. The
    project references the binary at its original path. Use this for large binaries or when
    you prefer external storage.

### From a target pack

A target pack captures observed facts about a binary (PE metadata, PDB contents, linker map,
object files, libraries) in a portable directory. Create one from a binary:

```console
$ x86decomp target-pack-infer target.exe target-pack/ --name "My Target" \
    --pdb target.pdb --map target.map
```

Then initialize a project from the verified target pack:

```console
$ x86decomp project-from-target target-pack/ my-project/
```

!!! note
    `target-pack-infer` records observed facts and user-supplied decisions separately. It never
    invents compiler versions, linker flags, function names, or source layout. Missing
    information is recorded as unknown.

---

## Inspect the PE binary

```console
$ x86decomp inspect-pe target.exe
```

Output (abbreviated):

```json
{
  "file_sha256": "a1b2c3d4e5f678901122334455667788990011...",
  "architecture": "x86",
  "machine": 332,
  "number_of_sections": 4,
  "sections": [
    {
      "name": ".text",
      "virtual_address": 4096,
      "virtual_size": 94208,
      "raw_size": 94208,
      "characteristics": 1610612768
    },
    {
      "name": ".rdata",
      "virtual_address": 98304,
      "virtual_size": 16384,
      "raw_size": 16384,
      "characteristics": 1073741888
    },
    {
      "name": ".data",
      "virtual_address": 114688,
      "virtual_size": 8192,
      "raw_size": 8192,
      "characteristics": 3221225536
    },
    {
      "name": ".rsrc",
      "virtual_address": 122880,
      "virtual_size": 4096,
      "raw_size": 4096,
      "characteristics": 1073741888
    }
  ],
  "image_base": 4194304,
  "entry_rva": 4096,
  "size_of_image": 131072,
  "size_of_headers": 1024,
  "subsystem": 2,
  "imports": [
    {
      "dll": "KERNEL32.dll",
      "symbols": [
        {"name": "GetModuleHandleA", "hint": null, "ordinal": null},
        {"name": "ExitProcess", "hint": null, "ordinal": null}
      ]
    },
    {
      "dll": "USER32.dll",
      "symbols": [
        {"name": "MessageBoxA", "hint": null, "ordinal": null}
      ]
    }
  ],
  "exports": [],
  "resources": [
    {
      "type": 16,
      "name": 1,
      "language": 1033,
      "size": 520,
      "offset": 102400
    }
  ],
  "relocations": [],
  "tls": null
}
```

Key fields:

| Field | Description |
|---|---|
| `architecture` | `x86` for PE32 (32-bit), `x86_64` for PE32+ (64-bit). |
| `machine` | Machine type constant (0x014C = x86, 0x8664 = x86-64). |
| `entry_rva` | Relative virtual address of the program entry point. |
| `image_base` | Preferred load address of the image. |
| `subsystem` | 2 = Windows GUI, 3 = Windows console. |
| `sections` | Section name, RVA, size, and characteristics. |
| `imports` | DLLs and imported symbols. |
| `exports` | Exported symbols (empty for most executables). |

---

## Inspect a PDB (if available)

```console
$ x86decomp pdb-inspect target.pdb --pe target.exe
```

Output (abbreviated):

```json
{
  "signature": "A1B2C3D4-E5F6-7890-1122-334455667788-1",
  "age": 1,
  "dbi": {
    "module_name": "target.exe",
    "sources": [
      "src/main.c",
      "src/utils.c",
      "src/helpers.c"
    ],
    "sections": [
      {"name": ".text", "stream": ...},
      {"name": ".rdata", "stream": ...},
      {"name": ".data", "stream": ...}
    ]
  },
  "public_symbols": [
    {"name": "_main", "section": 1, "offset": 0},
    {"name": "_helper_func", "section": 1, "offset": 320},
    {"name": "_globals", "section": 3, "offset": 0}
  ],
  "type_info": {
    "types_found": 47,
    "udts_found": 8
  },
  "pe_match": {
    "matched": true,
    "pe_signature": "A1B2C3D4-E5F6-7890-1122-334455667788-1",
    "pe_age": 1
  }
}
```

!!! tip "PDB-to-PE matching"
    The `--pe` flag causes `pdb-inspect` to compare the PDB's embedded GUID and age against the
    PE's debug directory. A `pe_match.matched: true` result confirms the PDB was built for this
    exact binary.

---

## Verify the project

```console
$ x86decomp verify-project my-project/
```

Output:

```json
{
  "project_id": "x86d-a1b2c3d4e5f67890-deadbeef",
  "architecture": "x86",
  "valid": true,
  "failures": [],
  "binary_path": "/home/user/my-project/original/target.exe",
  "memory_event_count": 1
}
```

`valid: true` with an empty `failures` list means the project structure, binary SHA-256,
program manifest, databases, content store, and project memory ledger are all intact.

!!! warning "Verification failures"
    If `valid` is `false`, the `failures` list explains each issue: missing files, SHA-256
    mismatches, schema version problems, or broken project memory entries. See
    [Verification](verification.md) for diagnosing and repairing failures.

---

## Snapshot the tool environment

Record the current tool versions for reproducibility:

```console
$ x86decomp snapshot-tools --output tools.json --ghidra-home /opt/ghidra
```

This file is referenced by reproducibility manifests and release gates to ensure the same tool
versions can be assembled for rebuilds.

---

## Export Ghidra function artifacts

If Ghidra is available, export function-level artifacts (disassembly, decompiler output,
control flow) for import into the project:

```console
$ x86decomp ghidra-export target.exe ghidra-project/ target \
    functions-out/ --ghidra-home /opt/ghidra
```

Or print the command for manual execution:

```console
$ x86decomp ghidra-export target.exe ghidra-project/ target \
    functions-out/ --ghidra-home /opt/ghidra --print-command
```

Output structure in `functions-out/`:

```
functions-out/
├── export.json              (export manifest with function list and hashes)
├── sub_401000/
│   ├── function.json        (metadata: address, size, name)
│   ├── decompiled.c         (Ghidra decompiler output)
│   ├── disassembly.jsonl    (instruction records)
│   └── cfg.json             (control-flow graph)
├── sub_401200/
│   └── ...
└── sub_401a00/
    └── ...
```

Import artifacts into the project:

```console
$ x86decomp artifact-import my-project/ functions-out/
```

Output:

```json
{
  "artifact_dir": "/home/user/my-project/functions/sub_401000",
  "verification": {
    "valid": true,
    "failures": []
  }
}
```

!!! note
    Artifacts are verified on import. Each artifact directory must contain a `function.json`
    manifest with content hashes. The import stores artifacts in the project's `functions/`
    directory tree.

---

## Next steps

- [Run verification checks](verification.md) to understand project integrity.
- [Understand decompilation modes](../concepts/decompilation-modes.md) and workflow state.
- [Browse all commands](../commands/index.md) for the full reference.
- [Follow a workflow](../workflows/index.md) for matching or functional decompilation.
