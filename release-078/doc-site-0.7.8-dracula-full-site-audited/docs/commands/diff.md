---
title: x86decomp diff
description: Exact v0.7.8 parser-derived reference for `x86decomp diff`.
---


# `x86decomp diff`

Canonical diff commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp diff [-h] [--project PROJECT] [--actor ACTOR] {explain} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `explain` | `usage: x86decomp diff explain [-h] [--source SOURCE] [--output OUTPUT] diff_report` | `reconstruction` |

### `x86decomp diff explain`

```text
usage: x86decomp diff explain [-h] [--source SOURCE] [--output OUTPUT]
                              diff_report
```

| Argument | Exact parser declaration |
| --- | --- |
| `diff_report` | required · parser destination: `diff_report`. No help text declared. |
| `--source` | parser destination: `source`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
