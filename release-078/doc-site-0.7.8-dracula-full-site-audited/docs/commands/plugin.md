---
title: x86decomp plugin
description: Exact v0.7.8 parser-derived reference for `x86decomp plugin`.
---


# `x86decomp plugin`

Canonical plugin commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp plugin [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,install,invoke,list,validate} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `doctor` | `usage: x86decomp plugin doctor [-h] plugin_id` | `governance` |
| `install` | `usage: x86decomp plugin install [-h] manifest` | `governance` |
| `invoke` | `usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT] plugin_id capability request_json` | `governance` |
| `list` | `usage: x86decomp plugin list [-h]` | `governance` |
| `validate` | `usage: x86decomp plugin validate [-h] manifest` | `governance` |

### `x86decomp plugin doctor`

```text
usage: x86decomp plugin doctor [-h] plugin_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `plugin_id` | required · parser destination: `plugin_id`. No help text declared. |

### `x86decomp plugin install`

```text
usage: x86decomp plugin install [-h] manifest
```

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required · parser destination: `manifest`. No help text declared. |

### `x86decomp plugin invoke`

```text
usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT]
                               plugin_id capability request_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `plugin_id` | required · parser destination: `plugin_id`. No help text declared. |
| `capability` | required · parser destination: `capability`. No help text declared. |
| `request_json` | required · parser destination: `request_json`. No help text declared. |
| `--timeout` | type: `int` · default: `60` · parser destination: `timeout`. No help text declared. |

### `x86decomp plugin list`

```text
usage: x86decomp plugin list [-h]
```

### `x86decomp plugin validate`

```text
usage: x86decomp plugin validate [-h] manifest
```

| Argument | Exact parser declaration |
| --- | --- |
| `manifest` | required · parser destination: `manifest`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
