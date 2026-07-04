---
title: x86decomp security
description: Command reference for `x86decomp security`.
---


# `x86decomp security`

Canonical security commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp security [-h] [--project PROJECT] [--actor ACTOR]
                          {finding,policy,report,scan} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `finding` | `usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON rule_id severity subject_id summary` | `reconstruction` |
| `policy` | `usage: x86decomp security policy [-h] name policy_json` | `reconstruction` |
| `report` | `usage: x86decomp security report [-h]` | `reconstruction` |
| `scan` | `usage: x86decomp security scan [-h] observations_json` | `reconstruction` |

### `x86decomp security finding`

```text
usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON
                                  rule_id severity subject_id summary
```

| Argument | Details |
| --- | --- |
| `rule_id` | required. |
| `severity` | required. |
| `subject_id` | required. |
| `summary` | required. |
| `--evidence-json` | required. |

### `x86decomp security policy`

```text
usage: x86decomp security policy [-h] name policy_json
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `policy_json` | required. |

### `x86decomp security report`

```text
usage: x86decomp security report [-h]
```

### `x86decomp security scan`

```text
usage: x86decomp security scan [-h] observations_json
```

| Argument | Details |
| --- | --- |
| `observations_json` | required. |


