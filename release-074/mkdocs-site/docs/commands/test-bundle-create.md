---
title: x86decomp test-bundle-create
description: create a hash-sealed authorized static test bundle
original_path: commands/test-bundle-create.html
---

<a id="command-test-bundle-create"></a>

Section: Command reference

# `x86decomp test-bundle-create`

create a hash-sealed authorized static test bundle

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp test-bundle-create --help
```

Metadata: current · core

## `x86decomp test-bundle-create`

create a hash-sealed authorized static test bundle

### Usage

```
x86decomp test-bundle-create [-h] --artifact ARTIFACT
                                    --authorization AUTHORIZATION
                                    [--name NAME] [--description DESCRIPTION]
                                    [--expected-architecture {x86,x86_64}]
                                    output
```

### Syntax example

```
x86decomp test-bundle-create ./output.json --artifact example --authorization example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--artifact` required | role=path |
| `--authorization` required | No argument help text is declared; parser destination is `authorization`. |
| `--name` | No argument help text is declared; parser destination is `name`. |
| `--description` | No argument help text is declared; parser destination is `description`. |
| `--expected-architecture` choices: x86, x86_64 | No argument help text is declared; parser destination is `expected_architecture`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
