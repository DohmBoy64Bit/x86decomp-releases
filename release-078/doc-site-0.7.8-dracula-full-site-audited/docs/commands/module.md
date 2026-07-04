---
title: x86decomp module
description: Command reference for `x86decomp module`.
---


# `x86decomp module`

Canonical module commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp module [-h] [--project PROJECT] [--actor ACTOR]
                        {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-member` | `usage: x86decomp module add-member [-h] [--ordinal ORDINAL] [--evidence-json EVIDENCE_JSON] module_id member_kind member_id` | `reconstruction` |
| `add-unit-member` | `usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE] [--ordinal ORDINAL] unit_id member_kind member_id` | `reconstruction` |
| `assign` | `usage: x86decomp module assign [-h] --module MODULE [--class-name CLASS_NAME] [--header HEADER] [--source SOURCE] [--report REPORT] function_id` | `reconstruction` |
| `create` | `usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] name` | `reconstruction` |
| `create-unit` | `usage: x86decomp module create-unit [-h] [--module-id MODULE_ID] [--language LANGUAGE] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] source_path` | `reconstruction` |
| `list` | `usage: x86decomp module list [-h]` | `reconstruction` |
| `show` | `usage: x86decomp module show [-h] module_id` | `reconstruction` |
| `show-unit` | `usage: x86decomp module show-unit [-h] unit_id` | `reconstruction` |
| `suggest` | `usage: x86decomp module suggest [-h] [--output OUTPUT]` | `reconstruction` |

### `x86decomp module add-member`

```text
usage: x86decomp module add-member [-h] [--ordinal ORDINAL]
                                   [--evidence-json EVIDENCE_JSON]
                                   module_id member_kind member_id
```

| Argument | Details |
| --- | --- |
| `module_id` | required. |
| `member_kind` | required. |
| `member_id` | required. |
| `--ordinal` | type: `int` · default: `0`. |
| `--evidence-json` | — |

### `x86decomp module add-unit-member`

```text
usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE]
                                        [--ordinal ORDINAL]
                                        unit_id member_kind member_id
```

| Argument | Details |
| --- | --- |
| `unit_id` | required. |
| `member_kind` | required. |
| `member_id` | required. |
| `--linkage` | default: `'external'`. |
| `--ordinal` | type: `int` · default: `0`. |

### `x86decomp module assign`

```text
usage: x86decomp module assign [-h] --module MODULE [--class-name CLASS_NAME]
                               [--header HEADER] [--source SOURCE]
                               [--report REPORT]
                               function_id
```

| Argument | Details |
| --- | --- |
| `function_id` | required. |
| `--module` | required. |
| `--class-name` | — |
| `--header` | — |
| `--source` | — |
| `--report` | — |

### `x86decomp module create`

```text
usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH]
                               [--confidence CONFIDENCE]
                               [--evidence-json EVIDENCE_JSON]
                               name
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `--kind` | default: `'static-library'`. |
| `--source-path` | — |
| `--confidence` | type: `float` · default: `1.0`. |
| `--evidence-json` | — |

### `x86decomp module create-unit`

```text
usage: x86decomp module create-unit [-h] [--module-id MODULE_ID]
                                    [--language LANGUAGE]
                                    [--confidence CONFIDENCE]
                                    [--evidence-json EVIDENCE_JSON]
                                    source_path
```

| Argument | Details |
| --- | --- |
| `source_path` | required. |
| `--module-id` | — |
| `--language` | default: `'cpp'`. |
| `--confidence` | type: `float` · default: `1.0`. |
| `--evidence-json` | — |

### `x86decomp module list`

```text
usage: x86decomp module list [-h]
```

### `x86decomp module show`

```text
usage: x86decomp module show [-h] module_id
```

| Argument | Details |
| --- | --- |
| `module_id` | required. |

### `x86decomp module show-unit`

```text
usage: x86decomp module show-unit [-h] unit_id
```

| Argument | Details |
| --- | --- |
| `unit_id` | required. |

### `x86decomp module suggest`

```text
usage: x86decomp module suggest [-h] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--output` | — |


