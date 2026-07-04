---
title: x86decomp pe
description: Exact v0.7.8 parser-derived reference for `x86decomp pe`.
---


# `x86decomp pe`

Canonical pe commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp pe [-h] [--project PROJECT] [--actor ACTOR]
                    {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `export-coff` | `usage: x86decomp pe export-coff [-h] [--section SECTION] image output` | `native` |
| `export-sections` | `usage: x86decomp pe export-sections [-h] [--section SECTION] image output` | `native` |
| `inventory` | `usage: x86decomp pe inventory [-h] image` | `native` |
| `patch-apply` | `usage: x86decomp pe patch-apply [-h] plan_id` | `native` |
| `patch-plan` | `usage: x86decomp pe patch-plan [-h] original output operations_json` | `native` |
| `text-swap` | `usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME] original replacement output` | `native` |

### `x86decomp pe export-coff`

```text
usage: x86decomp pe export-coff [-h] [--section SECTION] image output
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--section` | parser destination: `section`. No help text declared. |

### `x86decomp pe export-sections`

```text
usage: x86decomp pe export-sections [-h] [--section SECTION] image output
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--section` | parser destination: `section`. No help text declared. |

### `x86decomp pe inventory`

```text
usage: x86decomp pe inventory [-h] image
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |

### `x86decomp pe patch-apply`

```text
usage: x86decomp pe patch-apply [-h] plan_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `plan_id` | required · parser destination: `plan_id`. No help text declared. |

### `x86decomp pe patch-plan`

```text
usage: x86decomp pe patch-plan [-h] original output operations_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · parser destination: `original`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `operations_json` | required · parser destination: `operations_json`. No help text declared. |

### `x86decomp pe text-swap`

```text
usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME]
                              original replacement output
```

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · parser destination: `original`. No help text declared. |
| `replacement` | required · parser destination: `replacement`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--section-name` | default: `'.text'` · parser destination: `section_name`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
