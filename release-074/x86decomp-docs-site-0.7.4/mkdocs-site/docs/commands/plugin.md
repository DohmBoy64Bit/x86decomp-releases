---
title: x86decomp plugin
description: Canonical plugin commands implemented by the current capability subsystem.
original_path: commands/plugin.html
---

<a id="command-plugin-doctor"></a>
<a id="command-plugin-install"></a>
<a id="command-plugin-invoke"></a>
<a id="command-plugin-list"></a>
<a id="command-plugin-validate"></a>

Section: Command reference

# `x86decomp plugin`

Canonical plugin commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp plugin --help
```

Metadata: current · governance

## `x86decomp plugin doctor`

doctor command

### Usage

```
x86decomp plugin doctor [-h] plugin_id
```

### Syntax example

```
x86decomp plugin doctor example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `plugin_id` required | No argument help text is declared; parser destination is `plugin_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp plugin install`

install command

### Usage

```
x86decomp plugin install [-h] manifest
```

### Syntax example

```
x86decomp plugin install ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `manifest` required | No argument help text is declared; parser destination is `manifest`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp plugin invoke`

invoke command

### Usage

```
x86decomp plugin invoke [-h] [--timeout TIMEOUT]
                               plugin_id capability request_json
```

### Syntax example

```
x86decomp plugin invoke example-001 example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `plugin_id` required | No argument help text is declared; parser destination is `plugin_id`. |
| `capability` required | No argument help text is declared; parser destination is `capability`. |
| `request_json` required | No argument help text is declared; parser destination is `request_json`. |
| `--timeout` default: 60 · type: int | No argument help text is declared; parser destination is `timeout`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp plugin list`

list command

### Usage

```
x86decomp plugin list [-h]
```

### Syntax example

```
x86decomp plugin list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp plugin validate`

validate command

### Usage

```
x86decomp plugin validate [-h] manifest
```

### Syntax example

```
x86decomp plugin validate ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `manifest` required | No argument help text is declared; parser destination is `manifest`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
