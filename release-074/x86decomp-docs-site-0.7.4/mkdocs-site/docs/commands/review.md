---
title: x86decomp review
description: Canonical review commands implemented by the current capability subsystem.
original_path: commands/review.html
---

<a id="command-review-assign"></a>
<a id="command-review-create"></a>
<a id="command-review-decide"></a>
<a id="command-review-list"></a>
<a id="command-review-lock"></a>
<a id="command-review-show"></a>

Section: Command reference

# `x86decomp review`

Canonical review commands implemented by the current capability subsystem.

Metadata: current · canonical group · 6 runnable paths

## Help

```
x86decomp review --help
```

Metadata: current · governance

## `x86decomp review assign`

assign command

### Usage

```
x86decomp review assign [-h] review_id assignee
```

### Syntax example

```
x86decomp review assign review-001 example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `review_id` required | No argument help text is declared; parser destination is `review_id`. |
| `assignee` required | No argument help text is declared; parser destination is `assignee`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp review create`

create command

### Usage

```
x86decomp review create [-h] [--priority PRIORITY]
                               [--details-json DETAILS_JSON]
                               kind subject_id summary
```

### Syntax example

```
x86decomp review create analysis example-001 example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `kind` required | No argument help text is declared; parser destination is `kind`. |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `summary` required | No argument help text is declared; parser destination is `summary`. |
| `--priority` default: 50 · type: int | No argument help text is declared; parser destination is `priority`. |
| `--details-json` | No argument help text is declared; parser destination is `details_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp review decide`

decide command

### Usage

```
x86decomp review decide [-h] --rationale RATIONALE [--lock]
                               review_id decision
```

### Syntax example

```
x86decomp review decide review-001 example --rationale reviewed-change
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `review_id` required | No argument help text is declared; parser destination is `review_id`. |
| `decision` required | No argument help text is declared; parser destination is `decision`. |
| `--rationale` required | No argument help text is declared; parser destination is `rationale`. |
| `--lock` nargs: 0 · default: False | No argument help text is declared; parser destination is `lock`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp review list`

list command

### Usage

```
x86decomp review list [-h] [--status STATUS] [--limit LIMIT]
```

### Syntax example

```
x86decomp review list
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--status` | No argument help text is declared; parser destination is `status`. |
| `--limit` default: 100 · type: int | No argument help text is declared; parser destination is `limit`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp review lock`

lock command

### Usage

```
x86decomp review lock [-h] review_id
```

### Syntax example

```
x86decomp review lock review-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `review_id` required | No argument help text is declared; parser destination is `review_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp review show`

show command

### Usage

```
x86decomp review show [-h] review_id
```

### Syntax example

```
x86decomp review show review-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `review_id` required | No argument help text is declared; parser destination is `review_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
