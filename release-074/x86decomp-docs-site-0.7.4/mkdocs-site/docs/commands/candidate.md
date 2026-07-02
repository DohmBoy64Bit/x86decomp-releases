---
title: x86decomp candidate
description: Canonical candidate commands implemented by the current capability subsystem.
original_path: commands/candidate.html
---

<a id="command-candidate-add-file"></a>
<a id="command-candidate-compare"></a>
<a id="command-candidate-create"></a>
<a id="command-candidate-evaluate"></a>
<a id="command-candidate-list"></a>
<a id="command-candidate-show"></a>
<a id="command-candidate-transition"></a>

Section: Command reference

# `x86decomp candidate`

Canonical candidate commands implemented by the current capability subsystem.

Metadata: current · canonical group · 7 runnable paths

## Help

```
x86decomp candidate --help
```

Metadata: current · governance

## `x86decomp candidate add-file`

add-file command

### Usage

```
x86decomp candidate add-file [-h] candidate_id source relative_path
```

### Syntax example

```
x86decomp candidate add-file ./candidate.bin ./candidate.c src/candidate.c
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `candidate_id` required | No argument help text is declared; parser destination is `candidate_id`. |
| `source` required | No argument help text is declared; parser destination is `source`. |
| `relative_path` required | No argument help text is declared; parser destination is `relative_path`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp candidate compare`

compare command

### Usage

```
x86decomp candidate compare [-h] left_id right_id
```

### Syntax example

```
x86decomp candidate compare example-001 example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `left_id` required | No argument help text is declared; parser destination is `left_id`. |
| `right_id` required | No argument help text is declared; parser destination is `right_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp candidate create`

create command

### Usage

```
x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID]
                                  [--parent PARENT]
                                  [--objective-json OBJECTIVE_JSON]
                                  branch_name
```

### Syntax example

```
x86decomp candidate create candidate-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `branch_name` required | No argument help text is declared; parser destination is `branch_name`. |
| `--campaign-id` | No argument help text is declared; parser destination is `campaign_id`. |
| `--parent` | No argument help text is declared; parser destination is `parent`. |
| `--objective-json` | No argument help text is declared; parser destination is `objective_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp candidate evaluate`

evaluate command

### Usage

```
x86decomp candidate evaluate [-h] [--value VALUE]
                                    [--details-json DETAILS_JSON]
                                    candidate_id metric status
```

### Syntax example

```
x86decomp candidate evaluate ./candidate.bin exact-bytes active
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `candidate_id` required | No argument help text is declared; parser destination is `candidate_id`. |
| `metric` required | No argument help text is declared; parser destination is `metric`. |
| `status` required | No argument help text is declared; parser destination is `status`. |
| `--value` type: float | No argument help text is declared; parser destination is `value`. |
| `--details-json` | No argument help text is declared; parser destination is `details_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp candidate list`

list command

### Usage

```
x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]
```

### Syntax example

```
x86decomp candidate list
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--campaign-id` | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp candidate show`

show command

### Usage

```
x86decomp candidate show [-h] candidate_id
```

### Syntax example

```
x86decomp candidate show ./candidate.bin
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `candidate_id` required | No argument help text is declared; parser destination is `candidate_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp candidate transition`

transition command

### Usage

```
x86decomp candidate transition [-h] --reason REASON candidate_id state
```

### Syntax example

```
x86decomp candidate transition ./candidate.bin active --reason reviewed-change
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `candidate_id` required | No argument help text is declared; parser destination is `candidate_id`. |
| `state` required | No argument help text is declared; parser destination is `state`. |
| `--reason` required | No argument help text is declared; parser destination is `reason`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
