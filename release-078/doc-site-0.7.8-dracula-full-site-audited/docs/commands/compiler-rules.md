---
title: x86decomp compiler-rules
description: Command reference for `x86decomp compiler-rules`.
---


# `x86decomp compiler-rules`

Canonical compiler-rules commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp compiler-rules [-h] [--project PROJECT] [--actor ACTOR]
                                {compare-flags,learn-rule,rule-report} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compare-flags` | `usage: x86decomp compiler-rules compare-flags [-h] [--output OUTPUT] reports [reports ...]` | `reconstruction` |
| `learn-rule` | `usage: x86decomp compiler-rules learn-rule [-h] rule_id observations output` | `reconstruction` |
| `rule-report` | `usage: x86decomp compiler-rules rule-report [-h] [--output OUTPUT] rules [rules ...]` | `reconstruction` |

### `x86decomp compiler-rules compare-flags`

```text
usage: x86decomp compiler-rules compare-flags [-h] [--output OUTPUT]
                                              reports [reports ...]
```

| Argument | Details |
| --- | --- |
| `reports` | required · nargs: `+`. |
| `--output` | — |

### `x86decomp compiler-rules learn-rule`

```text
usage: x86decomp compiler-rules learn-rule [-h] rule_id observations output
```

| Argument | Details |
| --- | --- |
| `rule_id` | required. |
| `observations` | required. |
| `output` | required. |

### `x86decomp compiler-rules rule-report`

```text
usage: x86decomp compiler-rules rule-report [-h] [--output OUTPUT]
                                            rules [rules ...]
```

| Argument | Details |
| --- | --- |
| `rules` | required · nargs: `+`. |
| `--output` | — |


