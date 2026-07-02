---
title: x86decomp campaign
description: Canonical campaign commands implemented by the current capability subsystem.
original_path: commands/campaign.html
---

<a id="command-campaign-branch"></a>
<a id="command-campaign-create"></a>
<a id="command-campaign-list"></a>
<a id="command-campaign-pause"></a>
<a id="command-campaign-plan"></a>
<a id="command-campaign-resume"></a>
<a id="command-campaign-snapshot"></a>
<a id="command-campaign-start"></a>
<a id="command-campaign-status"></a>
<a id="command-campaign-stop"></a>

Section: Command reference

# `x86decomp campaign`

Canonical campaign commands implemented by the current capability subsystem.

Metadata: current · canonical group · 10 runnable paths

## Help

```
x86decomp campaign --help
```

Metadata: current · governance

## `x86decomp campaign branch`

branch command

### Usage

```
x86decomp campaign branch [-h] [--parent PARENT] campaign_id name
```

### Syntax example

```
x86decomp campaign branch campaign-main example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `--parent` | No argument help text is declared; parser destination is `parent`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign create`

create command

### Usage

```
x86decomp campaign create [-h] [--budget-json BUDGET_JSON]
                                 [--policy-json POLICY_JSON]
                                 goal
```

### Syntax example

```
x86decomp campaign create example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `goal` required | No argument help text is declared; parser destination is `goal`. |
| `--budget-json` | No argument help text is declared; parser destination is `budget_json`. |
| `--policy-json` | No argument help text is declared; parser destination is `policy_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign list`

list command

### Usage

```
x86decomp campaign list [-h]
```

### Syntax example

```
x86decomp campaign list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign pause`

pause command

### Usage

```
x86decomp campaign pause [-h] campaign_id
```

### Syntax example

```
x86decomp campaign pause campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign plan`

plan command

### Usage

```
x86decomp campaign plan [-h] campaign_id
```

### Syntax example

```
x86decomp campaign plan campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign resume`

resume command

### Usage

```
x86decomp campaign resume [-h] campaign_id
```

### Syntax example

```
x86decomp campaign resume campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign snapshot`

snapshot command

### Usage

```
x86decomp campaign snapshot [-h] campaign_id
```

### Syntax example

```
x86decomp campaign snapshot campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign start`

start command

### Usage

```
x86decomp campaign start [-h] campaign_id
```

### Syntax example

```
x86decomp campaign start campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign status`

status command

### Usage

```
x86decomp campaign status [-h] campaign_id
```

### Syntax example

```
x86decomp campaign status campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp campaign stop`

stop command

### Usage

```
x86decomp campaign stop [-h] campaign_id
```

### Syntax example

```
x86decomp campaign stop campaign-main
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `campaign_id` required | No argument help text is declared; parser destination is `campaign_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
