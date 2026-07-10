---
title: x86decomp release-gate
description: Parser-derived command reference page for `release-gate`.
---

# `x86decomp release-gate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

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

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --reproduction-manifest REPRODUCTION_MANIFEST
  --security-report SECURITY_REPORT
  --convergence-report CONVERGENCE_REPORT
  --require-workflows
  --require-verified-claims
  --require-succeeded-pipelines
  --report REPORT
```
