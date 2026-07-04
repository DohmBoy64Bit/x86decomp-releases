---
title: x86decomp image-text
description: Exact v0.7.8 parser-derived reference for `x86decomp image-text`.
---


# `x86decomp image-text`

Canonical image-text commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp image-text [-h] [--project PROJECT] [--actor ACTOR]
                            {compose} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compose` | `usage: x86decomp image-text compose [-h] [--function-list FUNCTION_LIST] [--fallback-byte FALLBACK_BYTE] output` | `reconstruction` |

### `x86decomp image-text compose`

```text
usage: x86decomp image-text compose [-h] [--function-list FUNCTION_LIST]
                                    [--fallback-byte FALLBACK_BYTE]
                                    output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |
| `--function-list` | parser destination: `function_list`. No help text declared. |
| `--fallback-byte` | type: `<lambda>` · default: `204` · parser destination: `fallback_byte`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
