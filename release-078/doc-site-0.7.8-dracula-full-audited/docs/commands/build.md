---
title: x86decomp build
---

# `x86decomp build`

Canonical build commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp build [-h] [--project PROJECT] [--actor ACTOR]
                       {add-target,add-variant,compare-modes,create,generate,matrix,show,validate} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add-target` | `usage: x86decomp build add-target [-h] [--kind KIND] [--output-name OUTPUT_NAME] [--sources-json SOURCES_JSON] [--dependencies-json DEPENDENCIES_JSON] build_id name` |
| `add-variant` | `usage: x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER [--compile-flags-json COMPILE_FLAGS_JSON] [--link-flags-json LINK_FLAGS_JSON] [--environment-json ENVIRONMENT_JSON] target_id name` |
| `compare-modes` | `usage: x86decomp build compare-modes [-h] historical_build_id portable_build_id` |
| `create` | `usage: x86decomp build create [-h] --mode MODE [--generator GENERATOR] [--output-root OUTPUT_ROOT] [--metadata-json METADATA_JSON] name` |
| `generate` | `usage: x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id` |
| `matrix` | `usage: x86decomp build matrix [-h]` |
| `show` | `usage: x86decomp build show [-h] build_id` |
| `validate` | `usage: x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp build add-target` | `reconstruction` |
| `x86decomp build add-variant` | `reconstruction` |
| `x86decomp build compare-modes` | `reconstruction` |
| `x86decomp build create` | `reconstruction` |
| `x86decomp build generate` | `reconstruction` |
| `x86decomp build matrix` | `reconstruction` |
| `x86decomp build show` | `reconstruction` |
| `x86decomp build validate` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
