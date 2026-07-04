---
title: x86decomp test-bundle-create
description: Exact v0.7.8 parser-derived reference for `x86decomp test-bundle-create`.
---


# `x86decomp test-bundle-create`

## Usage

```text
usage: x86decomp test-bundle-create [-h] --artifact ARTIFACT
                                    --authorization AUTHORIZATION
                                    [--name NAME] [--description DESCRIPTION]
                                    [--expected-architecture {x86,x86_64}]
                                    output
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · type: `_path` · parser destination: `output`. No help text declared. |
| `--artifact` | required · parser destination: `artifact`. role=path |
| `--authorization` | required · parser destination: `authorization`. No help text declared. |
| `--name` | parser destination: `name`. No help text declared. |
| `--description` | parser destination: `description`. No help text declared. |
| `--expected-architecture` | choices: `x86`, `x86_64` · parser destination: `expected_architecture`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
