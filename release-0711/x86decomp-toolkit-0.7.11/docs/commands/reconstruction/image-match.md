# Image Matching

Commands for whole-image layout profiling and PE image comparison.

## `x86decomp image-profile`

Derive a target-specific whole-image layout profile from a reference PE.

```console
x86decomp image-profile REFERENCE OUTPUT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REFERENCE` | yes | path | Reference PE image |
| `OUTPUT` | yes | path | Write the derived profile as JSON |

### Output

A deterministic JSON profile describing the reference image layout: section headers,
alignment, entry point, and structural properties used by `image-match` and
`relink` comparisons.

### Example

```console
$ x86decomp image-profile original/game.exe profile.json
```

### Related Commands

- [`image-match`](#x86decomp-image-match) — compare images using this profile

---

## `x86decomp image-match`

Compare a candidate PE image against a reference under an explicit layout profile.

```console
x86decomp image-match REFERENCE CANDIDATE --profile PROFILE --report REPORT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REFERENCE` | yes | path | Reference PE image |
| `CANDIDATE` | yes | path | Candidate (reconstructed) PE image |
| `--profile` | no | path | Layout profile from `image-profile` |
| `--report` | no | path | Write comparison report as JSON |

### Output

A JSON comparison report with byte-level mismatch counts, section-level
comparisons, and summary match status.

!!! tip "Relink integration"
    When used from `x86decomp relink`, the profile is read from the relink
    manifest's `layout_profile` field. The match report is embedded in the
    relink output for convergence tracking.

### Example

```console
$ x86decomp image-match original/game.exe build/reconstructed.exe \
    --profile profile.json \
    --report match-report.json
```

### Related Commands

- [`image-profile`](#x86decomp-image-profile) — derive the layout profile
- [`relink`](relink.md) — relink and compare automatically
- [`convergence-analyze`](../convergence/convergence.md) — track convergence over time
