---
title: x86decomp release-gate
description: Exact parser-derived reference for x86decomp release-gate in 0.7.5.
---

# `x86decomp release-gate`

## `x86decomp release-gate`

usage: x86decomp release-gate [-h]

### Usage

```text
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

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path`. No help text is declared; parser destination is `project`. |
| `--reproduction-manifest` | type: `_path`. No help text is declared; parser destination is `reproduction_manifest`. |
| `--security-report` | type: `_path`. No help text is declared; parser destination is `security_report`. |
| `--convergence-report` | type: `_path`. No help text is declared; parser destination is `convergence_report`. |
| `--require-workflows` | default: `False` · nargs: `0`. No help text is declared; parser destination is `require_workflows`. |
| `--require-verified-claims` | default: `False` · nargs: `0`. No help text is declared; parser destination is `require_verified_claims`. |
| `--require-succeeded-pipelines` | default: `False` · nargs: `0`. No help text is declared; parser destination is `require_succeeded_pipelines`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
