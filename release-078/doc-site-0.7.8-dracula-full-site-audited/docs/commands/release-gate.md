---
title: x86decomp release-gate
description: Command reference for `x86decomp release-gate`.
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

| Argument | Details |
| --- | --- |
| `project` | required · type: `path`. |
| `--reproduction-manifest` | type: `path`. |
| `--security-report` | type: `path`. |
| `--convergence-report` | type: `path`. |
| `--require-workflows` | nargs: `0` · default: `False`. |
| `--require-verified-claims` | nargs: `0` · default: `False`. |
| `--require-succeeded-pipelines` | nargs: `0` · default: `False`. |
| `--report` | type: `path`. |


