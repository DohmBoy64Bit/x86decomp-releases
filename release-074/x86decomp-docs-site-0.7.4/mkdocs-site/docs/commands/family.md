---
title: x86decomp family
description: Canonical family commands implemented by the current capability subsystem.
original_path: commands/family.html
---

<a id="command-family-add"></a>
<a id="command-family-correlate"></a>
<a id="command-family-create"></a>
<a id="command-family-report"></a>

Section: Command reference

# `x86decomp family`

Canonical family commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp family --help
```

Metadata: current · governance

## `x86decomp family add`

add command

### Usage

```
x86decomp family add [-h] [--metadata-json METADATA_JSON]
                            family_id label path
```

### Syntax example

```
x86decomp family add example-001 example ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `family_id` required | No argument help text is declared; parser destination is `family_id`. |
| `label` required | No argument help text is declared; parser destination is `label`. |
| `path` required | No argument help text is declared; parser destination is `path`. |
| `--metadata-json` | No argument help text is declared; parser destination is `metadata_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp family correlate`

correlate command

### Usage

```
x86decomp family correlate [-h] [--block-size BLOCK_SIZE]
                                  left_member_id right_member_id
```

### Syntax example

```
x86decomp family correlate example-001 example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `left_member_id` required | No argument help text is declared; parser destination is `left_member_id`. |
| `right_member_id` required | No argument help text is declared; parser destination is `right_member_id`. |
| `--block-size` default: 64 · type: int | No argument help text is declared; parser destination is `block_size`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp family create`

create command

### Usage

```
x86decomp family create [-h] name
```

### Syntax example

```
x86decomp family create example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp family report`

report command

### Usage

```
x86decomp family report [-h] family_id
```

### Syntax example

```
x86decomp family report example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `family_id` required | No argument help text is declared; parser destination is `family_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
