---
title: x86decomp reloc
---

# `x86decomp reloc`

Canonical reloc commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp reloc [-h] [--project PROJECT] [--actor ACTOR]
                       {inspect,resolve,supported} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `inspect` | `usage: x86decomp reloc inspect [-h] [--symbol SYMBOL] object` |
| `resolve` | `usage: x86decomp reloc resolve [-h] [--image-base IMAGE_BASE] object symbol base_rva symbol_map output` |
| `supported` | `usage: x86decomp reloc supported [-h]` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp reloc inspect` | `assembly` |
| `x86decomp reloc resolve` | `assembly` |
| `x86decomp reloc supported` | `assembly` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
