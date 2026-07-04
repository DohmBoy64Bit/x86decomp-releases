---
title: x86decomp test-bundle-create
description: Exact parser-derived reference for x86decomp test-bundle-create in 0.7.5.
---

# `x86decomp test-bundle-create`

## `x86decomp test-bundle-create`

usage: x86decomp test-bundle-create [-h] --artifact ARTIFACT

### Usage

```text
x86decomp test-bundle-create [-h] --artifact ARTIFACT
                                    --authorization AUTHORIZATION
                                    [--name NAME] [--description DESCRIPTION]
                                    [--expected-architecture {x86,x86_64}]
                                    output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · type: `_path`. No help text is declared; parser destination is `output`. |
| `--artifact` | required. role=path |
| `--authorization` | required. No help text is declared; parser destination is `authorization`. |
| `--name` | declared. No help text is declared; parser destination is `name`. |
| `--description` | declared. No help text is declared; parser destination is `description`. |
| `--expected-architecture` | choices: `x86`, `x86_64`. No help text is declared; parser destination is `expected_architecture`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
