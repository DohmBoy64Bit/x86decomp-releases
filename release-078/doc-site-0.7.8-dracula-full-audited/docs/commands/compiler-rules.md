---
title: x86decomp compiler-rules
---

# `x86decomp compiler-rules`

Canonical compiler-rules commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp compiler-rules [-h] [--project PROJECT] [--actor ACTOR]
                                {compare-flags,learn-rule,rule-report} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `compare-flags` | `usage: x86decomp compiler-rules compare-flags [-h] [--output OUTPUT] reports [reports ...]` |
| `learn-rule` | `usage: x86decomp compiler-rules learn-rule [-h] rule_id observations output` |
| `rule-report` | `usage: x86decomp compiler-rules rule-report [-h] [--output OUTPUT] rules [rules ...]` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp compiler-rules compare-flags` | `reconstruction` |
| `x86decomp compiler-rules learn-rule` | `reconstruction` |
| `x86decomp compiler-rules rule-report` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
