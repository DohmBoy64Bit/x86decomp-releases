---
title: x86decomp release-gate
description: Exact v0.7.8 parser-derived reference for `x86decomp release-gate`.
---


# `x86decomp release-gate`

## Usage

```text
usage: x86decomp release-gate [-h]
                              [--reproduction-manifest REPRODUCTION_MANIFEST]
                              [--security-report SECURITY_REPORT]
                              [--convergence-report CONVERGENCE_REPORT]
                              [--require-workflows]
                              [--require-verified-claims]
                              [--require-succeeded-pipelines]
                              [--report REPORT]
                              project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--reproduction-manifest` | type: `_path` · parser destination: `reproduction_manifest`. No help text declared. |
| `--security-report` | type: `_path` · parser destination: `security_report`. No help text declared. |
| `--convergence-report` | type: `_path` · parser destination: `convergence_report`. No help text declared. |
| `--require-workflows` | nargs: `0` · default: `False` · parser destination: `require_workflows`. No help text declared. |
| `--require-verified-claims` | nargs: `0` · default: `False` · parser destination: `require_verified_claims`. No help text declared. |
| `--require-succeeded-pipelines` | nargs: `0` · default: `False` · parser destination: `require_succeeded_pipelines`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
