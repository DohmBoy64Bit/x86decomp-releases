---
title: x86decomp text-swap
description: Exact v0.7.8 parser-derived reference for `x86decomp text-swap`.
---


# `x86decomp text-swap`

Canonical text-swap commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp text-swap [-h] [--project PROJECT] [--actor ACTOR]
                           {build,inject,plan,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `build` | `usage: x86decomp text-swap build [-h] --original ORIGINAL [--section-name SECTION_NAME] replacement output` | `reconstruction` |
| `inject` | `usage: x86decomp text-swap inject [-h] [--output OUTPUT] plan` | `reconstruction` |
| `plan` | `usage: x86decomp text-swap plan [-h] [--section-name SECTION_NAME] original replacement output` | `reconstruction` |
| `verify` | `usage: x86decomp text-swap verify [-h] [--output OUTPUT] plan image` | `reconstruction` |

### `x86decomp text-swap build`

```text
usage: x86decomp text-swap build [-h] --original ORIGINAL
                                 [--section-name SECTION_NAME]
                                 replacement output
```

| Argument | Exact parser declaration |
| --- | --- |
| `replacement` | required · parser destination: `replacement`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--original` | required · parser destination: `original`. No help text declared. |
| `--section-name` | default: `'.text'` · parser destination: `section_name`. No help text declared. |

### `x86decomp text-swap inject`

```text
usage: x86decomp text-swap inject [-h] [--output OUTPUT] plan
```

| Argument | Exact parser declaration |
| --- | --- |
| `plan` | required · parser destination: `plan`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp text-swap plan`

```text
usage: x86decomp text-swap plan [-h] [--section-name SECTION_NAME]
                                original replacement output
```

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · parser destination: `original`. No help text declared. |
| `replacement` | required · parser destination: `replacement`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--section-name` | default: `'.text'` · parser destination: `section_name`. No help text declared. |

### `x86decomp text-swap verify`

```text
usage: x86decomp text-swap verify [-h] [--output OUTPUT] plan image
```

| Argument | Exact parser declaration |
| --- | --- |
| `plan` | required · parser destination: `plan`. No help text declared. |
| `image` | required · parser destination: `image`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
