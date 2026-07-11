# Command structure

The `x86decomp` CLI organizes **166 root commands** and **239 canonical routes** across **59 capability groups** behind a single executable. Every command emits deterministic JSON on standard output and reports errors on standard error with exit code `2`.

---

## Root commands

Root commands are registered directly under `x86decomp` by `_build_parser` in `src/x86decomp/cli.py`. They are flat, positional-action-oriented names with no grouping layer:

```bash
x86decomp init binary.exe project/
x86decomp disassemble code.bin --base 0x401000 --architecture x86
x86decomp coff-inspect object.obj
x86decomp verify-project project/
```

Root commands fall into three safety classifications based on parser metadata alone:

| Classification | Meaning |
|---|---|
| **apparently-read-only-by-name** | Name and arguments suggest no mutation (`inspect-pe`, `disassemble`, `coff-inspect`, `map-inspect`, `verify-project`, etc.). |
| **potentially-mutating** | Creates or writes files, records state, or invokes external processes (`init`, `compile`, `patch-image`, `project-backup`, etc.). |
| **review-required** | Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs. |

These classifications are advisory. The toolkit does not block a mutating command based on its label.

---

## Canonical commands (group/action pattern)

Canonical commands use a two-level `group action` pattern dispatched through four capability owners:

| Owner | Description |
|---|---|
| `governance` | Evidence-driven convergence control plane (campaigns, hypotheses, consensus, proofs, reviews, workers, plugins). |
| `reconstruction` | Project-scale reconstruction (modules, headers, builds, provenance, ABI, tests, capsules, LLM, candidates, patterns, text-swap, Ghidra MCP, toolchains). |
| `native` | Native PE reconstruction and closed-loop matching (boundary audit, match, hybrid, PE ops, staging, loop, runtime, windows tools). |
| `assembly` | Relocation-aware mnemonic assembly (asm annotation/materialize/verify-roundtrip/batch, reloc, hybrid generate). |

Each canonical group is invoked as:

```bash
x86decomp <group> <action> [--project .] [--actor analyst] [action args...]
```

Every canonical group accepts two shared arguments before its action:

| Argument | Default | Description |
|---|---|---|
| `--project` | `.` | Project root used by the capability implementation (default: current directory). |
| `--actor` | `analyst` | Identity recorded in provenance records, mutations, and audit trails. |

### Ambiguous routes and merged groups

When multiple owners expose the same `(group, action)` pair, the canonical router resolves one owner via declared precedence in `_MERGED_GROUPS` or `_LATEST_SHARED_OWNER`. Ambiguous routes with no declared resolution raise a `ContractError`.

Merged groups include:

| Group | Actions with non-default owner |
|---|---|
| `project` | `init` → assembly, `check` → assembly, `synthesize-layout` → reconstruction, `explain-boundaries` → reconstruction, `export` → reconstruction |
| `changeset` | `export/inspect/apply` → governance, `create/add-operation/merge/conflicts/rebase/verify/show` → reconstruction |
| `hybrid` | `compose/verify` → native, `generate` → assembly |

### Listing canonical routes

```bash
x86decomp commands                           # full catalog
x86decomp commands --group project           # one group only
x86decomp commands --owner reconstruction    # one owner only
```

The catalog output includes group count, route count, merged-group declarations, and a per-route listing of `{group, action, owner}`.

---

## JSON output format

Every command serializes its result as **deterministic indented JSON** on standard output. The emitter uses `sort_keys=True`, `indent=2`, `ensure_ascii=False`, and a `default=str` fallback for non-JSON-native values.

Dataclass-like objects are converted through their `__dict__` before serialization.

The assembly CLI uses a custom emitter that strips bulky `resolved_bytes` payloads before printing.

### Example

```json
{
  "architecture": "x86",
  "file_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "machine": 332,
  "number_of_sections": 4,
  "size_of_image": 655360
}
```

---

## Error behavior

Expected user-facing errors are caught and reported as a structured JSON diagnostic on **standard error** with **exit code 2**:

```json
{"error": "ContractError", "message": "project directory is not empty: /path/to/project"}
```

The following exception types are treated as expected errors:

- `X86DecompError` and its subclasses (`ContractError`, `VerificationError`)
- `KeyError`, `OSError`, `TypeError`, `ValueError`
- `subprocess.SubprocessError` (when invoked through a capability CLI that declares it)

Argument parsing errors (from `argparse`) also exit with status `2` and print usage diagnostics to standard error. Unexpected exceptions (like `RuntimeError`) propagate as unhandled Python tracebacks.

---

## `--help`

Every root command, canonical group, and canonical action prints its usage when given `--help` or `-h`:

```bash
x86decomp --help                         # top-level help
x86decomp init --help                    # root command help
x86decomp project --help                 # canonical group help
x86decomp project check --help           # canonical action help
x86decomp asm materialize --help         # assembly action help
```

The `--help` flag exits with status `0` and is non-destructive. It is the recommended way to explore the current live argument surface without consulting external documentation.

---

## Related pages

| Page | Content |
|---|---|
| [Project: init / verify-project](project/init-verify.md) | `init`, `verify-project`, `inspect-pe`, `pdb-inspect` |
| [Project: Target Pack](project/target-pack.md) | `target-pack-infer`, `target-pack-verify`, `project-from-target`, `template-derive`, `template-materialize` |
| [Project: Operations](project/operations.md) | `project-check`, `project-migrate`, `project-backup`, `project-restore`, `project-repair`, `project-gc` |
| [Analysis: PE and PDB](analysis/pe-pdb.md) | `inspect-pe`, `pdb-inspect` |
| [Analysis: Disassembly](analysis/disassembly.md) | `disassemble`, `crosscheck-ghidra` |
| [Analysis: COFF](analysis/coff.md) | `coff-inspect`, `lib-inspect`, `coff-extract`, `coff-synthesize`, `coff-comdat-resolve` |
| [Analysis: Metadata](analysis/metadata.md) | `metadata-scan` |
