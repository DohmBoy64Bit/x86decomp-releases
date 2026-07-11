# Patch Image

Patch a function body into a PE image at a given RVA, replacing the original bytes
in-place.

## `x86decomp patch-image`

```console
x86decomp patch-image ORIGINAL CANDIDATE OUTPUT \
    --rva RVA \
    --expected-original-sha256 HASH \
    --expected-function-sha256 HASH \
    --report REPORT
```

### Purpose

Replace a function body in a PE image with a candidate byte sequence. The command
rewrites the file at the target RVA, zeroes and recalculates the PE checksum, and
writes a new output file — the original is never modified.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `ORIGINAL` | yes | path | Original PE image to read from |
| `CANDIDATE` | yes | path | File containing replacement function bytes |
| `OUTPUT` | yes | path | Patched output PE image |
| `--rva` | yes | integer | RVA of the function to patch |
| `--expected-original-sha256` | no | string | Reject if original PE hash does not match |
| `--expected-function-sha256` | no | string | Reject if original function bytes do not match |
| `--report` | no | path | Write patching report as JSON |

### Hash Gates

Both `--expected-original-sha256` and `--expected-function-sha256` are optional
safety gates. When provided, the command aborts with a `ContractError` if the
respective hash does not match.

- `expected-original-sha256` — guards against using the wrong original PE
- `expected-function-sha256` — guards against patching a function that was already
  modified or incorrectly located

### Limitations

The in-place patching backend:

- Cannot grow a function beyond its original byte footprint
- Requires control-flow, unwind, relocation, and data references to already be valid
  for the patch location

!!! warning "Size constraint"
    The candidate byte sequence must not exceed the original function size.
    If the candidate is shorter, remaining original bytes are left untouched.
    Consider rebuilding the object and relinking for resized functions.

### Output Report

```json
{
  "kind": "patch_image",
  "original": "...",
  "original_sha256": "...",
  "candidate": "...",
  "candidate_sha256": "...",
  "output": "...",
  "output_sha256": "...",
  "function_rva": 4096,
  "file_offset": 1024,
  "patch_size": 256,
  "original_function_sha256": "...",
  "pe_checksum": 0
}
```

### Example

```console
$ x86decomp patch-image original/game.exe candidate.bin build/patched.exe \
    --rva 0x1000 \
    --expected-original-sha256 abc123def456... \
    --expected-function-sha256 789abc012def... \
    --report patch-report.json
```

### Related Commands

- [`relink`](relink.md) — full-image relink for multi-function changes
- [`diff-function`](../validation/diff-function.md) — compare PE function to COFF symbol
- [`compile`](../compilation/compile.md) — produce the candidate bytes from source
