---
title: x86decomp release-gate
description: evaluate explicit target release acceptance contracts
original_path: commands/release-gate.html
---

<a id="command-release-gate"></a>

Section: Command reference

# `x86decomp release-gate`

evaluate explicit target release acceptance contracts

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp release-gate --help
```

Metadata: current · core

## `x86decomp release-gate`

evaluate explicit target release acceptance contracts

### Usage

```
x86decomp release-gate [-h]
                              [--reproduction-manifest REPRODUCTION_MANIFEST]
                              [--security-report SECURITY_REPORT]
                              [--convergence-report CONVERGENCE_REPORT]
                              [--require-workflows]
                              [--require-verified-claims]
                              [--require-succeeded-pipelines]
                              [--report REPORT]
                              project
```

### Syntax example

```
x86decomp release-gate ./work
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--reproduction-manifest` type: _path | No argument help text is declared; parser destination is `reproduction_manifest`. |
| `--security-report` type: _path | No argument help text is declared; parser destination is `security_report`. |
| `--convergence-report` type: _path | No argument help text is declared; parser destination is `convergence_report`. |
| `--require-workflows` nargs: 0 · default: False | No argument help text is declared; parser destination is `require_workflows`. |
| `--require-verified-claims` nargs: 0 · default: False | No argument help text is declared; parser destination is `require_verified_claims`. |
| `--require-succeeded-pipelines` nargs: 0 · default: False | No argument help text is declared; parser destination is `require_succeeded_pipelines`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
