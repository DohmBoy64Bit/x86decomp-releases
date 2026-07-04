---
title: x86decomp build
description: Exact v0.7.8 parser-derived reference for `x86decomp build`.
---


# `x86decomp build`

Canonical build commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp build [-h] [--project PROJECT] [--actor ACTOR]
                       {add-target,add-variant,compare-modes,create,generate,matrix,show,validate} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-target` | `usage: x86decomp build add-target [-h] [--kind KIND] [--output-name OUTPUT_NAME] [--sources-json SOURCES_JSON] [--dependencies-json DEPENDENCIES_JSON] build_id name` | `reconstruction` |
| `add-variant` | `usage: x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER [--compile-flags-json COMPILE_FLAGS_JSON] [--link-flags-json LINK_FLAGS_JSON] [--environment-json ENVIRONMENT_JSON] target_id name` | `reconstruction` |
| `compare-modes` | `usage: x86decomp build compare-modes [-h] historical_build_id portable_build_id` | `reconstruction` |
| `create` | `usage: x86decomp build create [-h] --mode MODE [--generator GENERATOR] [--output-root OUTPUT_ROOT] [--metadata-json METADATA_JSON] name` | `reconstruction` |
| `generate` | `usage: x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id` | `reconstruction` |
| `matrix` | `usage: x86decomp build matrix [-h]` | `reconstruction` |
| `show` | `usage: x86decomp build show [-h] build_id` | `reconstruction` |
| `validate` | `usage: x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id` | `reconstruction` |

### `x86decomp build add-target`

```text
usage: x86decomp build add-target [-h] [--kind KIND]
                                  [--output-name OUTPUT_NAME]
                                  [--sources-json SOURCES_JSON]
                                  [--dependencies-json DEPENDENCIES_JSON]
                                  build_id name
```

| Argument | Exact parser declaration |
| --- | --- |
| `build_id` | required · parser destination: `build_id`. No help text declared. |
| `name` | required · parser destination: `name`. No help text declared. |
| `--kind` | default: `'executable'` · parser destination: `kind`. No help text declared. |
| `--output-name` | parser destination: `output_name`. No help text declared. |
| `--sources-json` | parser destination: `sources_json`. No help text declared. |
| `--dependencies-json` | parser destination: `dependencies_json`. No help text declared. |

### `x86decomp build add-variant`

```text
usage: x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER
                                   [--compile-flags-json COMPILE_FLAGS_JSON]
                                   [--link-flags-json LINK_FLAGS_JSON]
                                   [--environment-json ENVIRONMENT_JSON]
                                   target_id name
```

| Argument | Exact parser declaration |
| --- | --- |
| `target_id` | required · parser destination: `target_id`. No help text declared. |
| `name` | required · parser destination: `name`. No help text declared. |
| `--compiler` | required · parser destination: `compiler`. No help text declared. |
| `--linker` | required · parser destination: `linker`. No help text declared. |
| `--compile-flags-json` | parser destination: `compile_flags_json`. No help text declared. |
| `--link-flags-json` | parser destination: `link_flags_json`. No help text declared. |
| `--environment-json` | parser destination: `environment_json`. No help text declared. |

### `x86decomp build compare-modes`

```text
usage: x86decomp build compare-modes [-h]
                                     historical_build_id portable_build_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `historical_build_id` | required · parser destination: `historical_build_id`. No help text declared. |
| `portable_build_id` | required · parser destination: `portable_build_id`. No help text declared. |

### `x86decomp build create`

```text
usage: x86decomp build create [-h] --mode MODE [--generator GENERATOR]
                              [--output-root OUTPUT_ROOT]
                              [--metadata-json METADATA_JSON]
                              name
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `--mode` | required · parser destination: `mode`. No help text declared. |
| `--generator` | default: `'cmake'` · parser destination: `generator`. No help text declared. |
| `--output-root` | default: `'build'` · parser destination: `output_root`. No help text declared. |
| `--metadata-json` | parser destination: `metadata_json`. No help text declared. |

### `x86decomp build generate`

```text
usage: x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `build_id` | required · parser destination: `build_id`. No help text declared. |
| `--output-root` | parser destination: `output_root`. No help text declared. |

### `x86decomp build matrix`

```text
usage: x86decomp build matrix [-h]
```

### `x86decomp build show`

```text
usage: x86decomp build show [-h] build_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `build_id` | required · parser destination: `build_id`. No help text declared. |

### `x86decomp build validate`

```text
usage: x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `target_id` | required · parser destination: `target_id`. No help text declared. |
| `--variant-id` | parser destination: `variant_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
