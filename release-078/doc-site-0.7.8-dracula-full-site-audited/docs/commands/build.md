---
title: x86decomp build
description: Command reference for `x86decomp build`.
---


# `x86decomp build`

Canonical build commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp build [-h] [--project PROJECT] [--actor ACTOR]
                       {add-target,add-variant,compare-modes,create,generate,matrix,show,validate} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

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

| Argument | Details |
| --- | --- |
| `build_id` | required. |
| `name` | required. |
| `--kind` | default: `'executable'`. |
| `--output-name` | — |
| `--sources-json` | — |
| `--dependencies-json` | — |

### `x86decomp build add-variant`

```text
usage: x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER
                                   [--compile-flags-json COMPILE_FLAGS_JSON]
                                   [--link-flags-json LINK_FLAGS_JSON]
                                   [--environment-json ENVIRONMENT_JSON]
                                   target_id name
```

| Argument | Details |
| --- | --- |
| `target_id` | required. |
| `name` | required. |
| `--compiler` | required. |
| `--linker` | required. |
| `--compile-flags-json` | — |
| `--link-flags-json` | — |
| `--environment-json` | — |

### `x86decomp build compare-modes`

```text
usage: x86decomp build compare-modes [-h]
                                     historical_build_id portable_build_id
```

| Argument | Details |
| --- | --- |
| `historical_build_id` | required. |
| `portable_build_id` | required. |

### `x86decomp build create`

```text
usage: x86decomp build create [-h] --mode MODE [--generator GENERATOR]
                              [--output-root OUTPUT_ROOT]
                              [--metadata-json METADATA_JSON]
                              name
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `--mode` | required. |
| `--generator` | default: `'cmake'`. |
| `--output-root` | default: `'build'`. |
| `--metadata-json` | — |

### `x86decomp build generate`

```text
usage: x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id
```

| Argument | Details |
| --- | --- |
| `build_id` | required. |
| `--output-root` | — |

### `x86decomp build matrix`

```text
usage: x86decomp build matrix [-h]
```

### `x86decomp build show`

```text
usage: x86decomp build show [-h] build_id
```

| Argument | Details |
| --- | --- |
| `build_id` | required. |

### `x86decomp build validate`

```text
usage: x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id
```

| Argument | Details |
| --- | --- |
| `target_id` | required. |
| `--variant-id` | — |


