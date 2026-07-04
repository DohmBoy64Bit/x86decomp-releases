---
title: x86decomp consensus
description: Command reference for `x86decomp consensus`.
---


# `x86decomp consensus`

Canonical consensus commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp consensus [-h] [--project PROJECT] [--actor ACTOR]
                           {conflicts,explain,record,resolve,scan} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `conflicts` | `usage: x86decomp consensus conflicts [-h]` | `governance` |
| `explain` | `usage: x86decomp consensus explain [-h] subject_kind subject_id property_name` | `governance` |
| `record` | `usage: x86decomp consensus record [-h] --adapter ADAPTER --adapter-version ADAPTER_VERSION --evidence-id EVIDENCE_ID --group GROUP [--confidence CONFIDENCE] subject_kind subject_id property_name value_json` | `governance` |
| `resolve` | `usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE [--lock] subject_kind subject_id property_name selected_value_json` | `governance` |
| `scan` | `usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND] [--subject-id SUBJECT_ID]` | `governance` |

### `x86decomp consensus conflicts`

```text
usage: x86decomp consensus conflicts [-h]
```

### `x86decomp consensus explain`

```text
usage: x86decomp consensus explain [-h] subject_kind subject_id property_name
```

| Argument | Details |
| --- | --- |
| `subject_kind` | required. |
| `subject_id` | required. |
| `property_name` | required. |

### `x86decomp consensus record`

```text
usage: x86decomp consensus record [-h] --adapter ADAPTER
                                  --adapter-version ADAPTER_VERSION
                                  --evidence-id EVIDENCE_ID --group GROUP
                                  [--confidence CONFIDENCE]
                                  subject_kind subject_id property_name
                                  value_json
```

| Argument | Details |
| --- | --- |
| `subject_kind` | required. |
| `subject_id` | required. |
| `property_name` | required. |
| `value_json` | required. |
| `--adapter` | required. |
| `--adapter-version` | required. |
| `--evidence-id` | required. |
| `--group` | required · default: `'consensus'`. |
| `--confidence` | type: `float` · default: `1.0`. |

### `x86decomp consensus resolve`

```text
usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE
                                   [--lock]
                                   subject_kind subject_id property_name
                                   selected_value_json
```

| Argument | Details |
| --- | --- |
| `subject_kind` | required. |
| `subject_id` | required. |
| `property_name` | required. |
| `selected_value_json` | required. |
| `--method` | required. |
| `--rationale` | required. |
| `--lock` | nargs: `0` · default: `False`. |

### `x86decomp consensus scan`

```text
usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND]
                                [--subject-id SUBJECT_ID]
```

| Argument | Details |
| --- | --- |
| `--subject-kind` | — |
| `--subject-id` | — |


