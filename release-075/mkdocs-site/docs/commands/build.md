---
title: x86decomp build
description: Exact parser-derived reference for x86decomp build in 0.7.5.
---

# `x86decomp build`

Canonical capability group with 8 routes. Shared group options are shown in every exact usage string.

## `x86decomp build add-target`

usage: x86decomp build add-target [-h] [--kind KIND]

### Usage

```text
x86decomp build add-target [-h] [--kind KIND]
                                  [--output-name OUTPUT_NAME]
                                  [--sources-json SOURCES_JSON]
                                  [--dependencies-json DEPENDENCIES_JSON]
                                  build_id name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `build_id` | required. No help text is declared; parser destination is `build_id`. |
| `name` | required. No help text is declared; parser destination is `name`. |
| `--kind` | default: `'executable'`. No help text is declared; parser destination is `kind`. |
| `--output-name` | declared. No help text is declared; parser destination is `output_name`. |
| `--sources-json` | declared. No help text is declared; parser destination is `sources_json`. |
| `--dependencies-json` | declared. No help text is declared; parser destination is `dependencies_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build add-variant`

usage: x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER

### Usage

```text
x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER
                                   [--compile-flags-json COMPILE_FLAGS_JSON]
                                   [--link-flags-json LINK_FLAGS_JSON]
                                   [--environment-json ENVIRONMENT_JSON]
                                   target_id name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target_id` | required. No help text is declared; parser destination is `target_id`. |
| `name` | required. No help text is declared; parser destination is `name`. |
| `--compiler` | required. No help text is declared; parser destination is `compiler`. |
| `--linker` | required. No help text is declared; parser destination is `linker`. |
| `--compile-flags-json` | declared. No help text is declared; parser destination is `compile_flags_json`. |
| `--link-flags-json` | declared. No help text is declared; parser destination is `link_flags_json`. |
| `--environment-json` | declared. No help text is declared; parser destination is `environment_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build compare-modes`

usage: x86decomp build compare-modes [-h]

### Usage

```text
x86decomp build compare-modes [-h]
                                     historical_build_id portable_build_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `historical_build_id` | required. No help text is declared; parser destination is `historical_build_id`. |
| `portable_build_id` | required. No help text is declared; parser destination is `portable_build_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build create`

usage: x86decomp build create [-h] --mode MODE [--generator GENERATOR]

### Usage

```text
x86decomp build create [-h] --mode MODE [--generator GENERATOR]
                              [--output-root OUTPUT_ROOT]
                              [--metadata-json METADATA_JSON]
                              name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `--mode` | required. No help text is declared; parser destination is `mode`. |
| `--generator` | default: `'cmake'`. No help text is declared; parser destination is `generator`. |
| `--output-root` | default: `'build'`. No help text is declared; parser destination is `output_root`. |
| `--metadata-json` | declared. No help text is declared; parser destination is `metadata_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build generate`

usage: x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id

### Usage

```text
x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `build_id` | required. No help text is declared; parser destination is `build_id`. |
| `--output-root` | declared. No help text is declared; parser destination is `output_root`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build matrix`

usage: x86decomp build matrix [-h]

### Usage

```text
x86decomp build matrix [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build show`

usage: x86decomp build show [-h] build_id

### Usage

```text
x86decomp build show [-h] build_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `build_id` | required. No help text is declared; parser destination is `build_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp build validate`

usage: x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id

### Usage

```text
x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target_id` | required. No help text is declared; parser destination is `target_id`. |
| `--variant-id` | declared. No help text is declared; parser destination is `variant_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
