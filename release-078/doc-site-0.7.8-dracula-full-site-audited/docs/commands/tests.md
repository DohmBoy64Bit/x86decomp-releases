---
title: x86decomp tests
description: Command reference for `x86decomp tests`.
---


# `x86decomp tests`

Canonical tests commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp tests [-h] [--project PROJECT] [--actor ACTOR]
                       {add,explain,list,promote-counterexample,synthesize} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add` | `usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON --evidence-json EVIDENCE_JSON name scope_kind scope_id test_kind relative_path content_file` | `reconstruction` |
| `explain` | `usage: x86decomp tests explain [-h] test_id` | `reconstruction` |
| `list` | `usage: x86decomp tests list [-h]` | `reconstruction` |
| `promote-counterexample` | `usage: x86decomp tests promote-counterexample [-h] [--name NAME] counterexample_id` | `reconstruction` |
| `synthesize` | `usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id` | `reconstruction` |

### `x86decomp tests add`

```text
usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON
                           --evidence-json EVIDENCE_JSON
                           name scope_kind scope_id test_kind relative_path
                           content_file
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `scope_kind` | required. |
| `scope_id` | required. |
| `test_kind` | required. |
| `relative_path` | required. |
| `content_file` | required. |
| `--applicability-json` | required. |
| `--evidence-json` | required. |

### `x86decomp tests explain`

```text
usage: x86decomp tests explain [-h] test_id
```

| Argument | Details |
| --- | --- |
| `test_id` | required. |

### `x86decomp tests list`

```text
usage: x86decomp tests list [-h]
```

### `x86decomp tests promote-counterexample`

```text
usage: x86decomp tests promote-counterexample [-h] [--name NAME]
                                              counterexample_id
```

| Argument | Details |
| --- | --- |
| `counterexample_id` | required. |
| `--name` | — |

### `x86decomp tests synthesize`

```text
usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id
```

| Argument | Details |
| --- | --- |
| `scope_kind` | required. |
| `scope_id` | required. |
| `--name` | — |


