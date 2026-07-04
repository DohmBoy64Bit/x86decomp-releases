---
title: x86decomp candidate
description: Command reference for `x86decomp candidate`.
---


# `x86decomp candidate`

Canonical candidate commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp candidate [-h] [--project PROJECT] [--actor ACTOR]
                           {add-file,compare,create,evaluate,list,promote,search,show,transition} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-file` | `usage: x86decomp candidate add-file [-h] candidate_id source relative_path` | `governance` |
| `compare` | `usage: x86decomp candidate compare [-h] left_id right_id` | `governance` |
| `create` | `usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID] [--parent PARENT] [--objective-json OBJECTIVE_JSON] branch_name` | `governance` |
| `evaluate` | `usage: x86decomp candidate evaluate [-h] [--value VALUE] [--details-json DETAILS_JSON] candidate_id metric status` | `governance` |
| `list` | `usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]` | `governance` |
| `promote` | `usage: x86decomp candidate promote [-h] --candidate CANDIDATE --report REPORT [--stage STAGE] [--update-workflow] [--update-build] [--overwrite] function_id` | `reconstruction` |
| `search` | `usage: x86decomp candidate search [-h] [--phase PHASE] [--output OUTPUT]` | `reconstruction` |
| `show` | `usage: x86decomp candidate show [-h] candidate_id` | `governance` |
| `transition` | `usage: x86decomp candidate transition [-h] --reason REASON candidate_id state` | `governance` |

### `x86decomp candidate add-file`

```text
usage: x86decomp candidate add-file [-h] candidate_id source relative_path
```

| Argument | Details |
| --- | --- |
| `candidate_id` | required. |
| `source` | required. |
| `relative_path` | required. |

### `x86decomp candidate compare`

```text
usage: x86decomp candidate compare [-h] left_id right_id
```

| Argument | Details |
| --- | --- |
| `left_id` | required. |
| `right_id` | required. |

### `x86decomp candidate create`

```text
usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID]
                                  [--parent PARENT]
                                  [--objective-json OBJECTIVE_JSON]
                                  branch_name
```

| Argument | Details |
| --- | --- |
| `branch_name` | required. |
| `--campaign-id` | — |
| `--parent` | — |
| `--objective-json` | — |

### `x86decomp candidate evaluate`

```text
usage: x86decomp candidate evaluate [-h] [--value VALUE]
                                    [--details-json DETAILS_JSON]
                                    candidate_id metric status
```

| Argument | Details |
| --- | --- |
| `candidate_id` | required. |
| `metric` | required. |
| `status` | required. |
| `--value` | type: `float`. |
| `--details-json` | — |

### `x86decomp candidate list`

```text
usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]
```

| Argument | Details |
| --- | --- |
| `--campaign-id` | — |

### `x86decomp candidate promote`

```text
usage: x86decomp candidate promote [-h] --candidate CANDIDATE --report REPORT
                                   [--stage STAGE] [--update-workflow]
                                   [--update-build] [--overwrite]
                                   function_id
```

| Argument | Details |
| --- | --- |
| `function_id` | required. |
| `--candidate` | required. |
| `--report` | required. |
| `--stage` | default: `'matched'`. |
| `--update-workflow` | nargs: `0` · default: `False`. |
| `--update-build` | nargs: `0` · default: `False`. |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp candidate search`

```text
usage: x86decomp candidate search [-h] [--phase PHASE] [--output OUTPUT]
```

| Argument | Details |
| --- | --- |
| `--phase` | — |
| `--output` | — |

### `x86decomp candidate show`

```text
usage: x86decomp candidate show [-h] candidate_id
```

| Argument | Details |
| --- | --- |
| `candidate_id` | required. |

### `x86decomp candidate transition`

```text
usage: x86decomp candidate transition [-h] --reason REASON candidate_id state
```

| Argument | Details |
| --- | --- |
| `candidate_id` | required. |
| `state` | required. |
| `--reason` | required. |


