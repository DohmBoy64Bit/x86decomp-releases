---
title: x86decomp build
description: Canonical build commands implemented by the current capability subsystem.
original_path: commands/build.html
---

<a id="command-build-add-target"></a>
<a id="command-build-add-variant"></a>
<a id="command-build-compare-modes"></a>
<a id="command-build-create"></a>
<a id="command-build-generate"></a>
<a id="command-build-matrix"></a>
<a id="command-build-show"></a>
<a id="command-build-validate"></a>

Section: Command reference

# `x86decomp build`

Canonical build commands implemented by the current capability subsystem.

Metadata: current · canonical group · 8 runnable paths

## Help

```
x86decomp build --help
```

Metadata: current · reconstruction

## `x86decomp build add-target`

add-target command

### Usage

```
x86decomp build add-target [-h] [--kind KIND]
                                  [--output-name OUTPUT_NAME]
                                  [--sources-json SOURCES_JSON]
                                  [--dependencies-json DEPENDENCIES_JSON]
                                  build_id name
```

### Syntax example

```
x86decomp build add-target example-001 example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `build_id` required | No argument help text is declared; parser destination is `build_id`. |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `--kind` default: 'executable' | No argument help text is declared; parser destination is `kind`. |
| `--output-name` | No argument help text is declared; parser destination is `output_name`. |
| `--sources-json` | No argument help text is declared; parser destination is `sources_json`. |
| `--dependencies-json` | No argument help text is declared; parser destination is `dependencies_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build add-variant`

add-variant command

### Usage

```
x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER
                                   [--compile-flags-json COMPILE_FLAGS_JSON]
                                   [--link-flags-json LINK_FLAGS_JSON]
                                   [--environment-json ENVIRONMENT_JSON]
                                   target_id name
```

### Syntax example

```
x86decomp build add-variant ./target.exe example --compiler clang --linker lld-link
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target_id` required | No argument help text is declared; parser destination is `target_id`. |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `--compiler` required | No argument help text is declared; parser destination is `compiler`. |
| `--linker` required | No argument help text is declared; parser destination is `linker`. |
| `--compile-flags-json` | No argument help text is declared; parser destination is `compile_flags_json`. |
| `--link-flags-json` | No argument help text is declared; parser destination is `link_flags_json`. |
| `--environment-json` | No argument help text is declared; parser destination is `environment_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build compare-modes`

compare-modes command

### Usage

```
x86decomp build compare-modes [-h]
                                     historical_build_id portable_build_id
```

### Syntax example

```
x86decomp build compare-modes example-001 8080
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `historical_build_id` required | No argument help text is declared; parser destination is `historical_build_id`. |
| `portable_build_id` required | No argument help text is declared; parser destination is `portable_build_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build create`

create command

### Usage

```
x86decomp build create [-h] --mode MODE [--generator GENERATOR]
                              [--output-root OUTPUT_ROOT]
                              [--metadata-json METADATA_JSON]
                              name
```

### Syntax example

```
x86decomp build create example --mode release
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `--mode` required | No argument help text is declared; parser destination is `mode`. |
| `--generator` default: 'cmake' | No argument help text is declared; parser destination is `generator`. |
| `--output-root` default: 'build' | No argument help text is declared; parser destination is `output_root`. |
| `--metadata-json` | No argument help text is declared; parser destination is `metadata_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build generate`

generate command

### Usage

```
x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id
```

### Syntax example

```
x86decomp build generate example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `build_id` required | No argument help text is declared; parser destination is `build_id`. |
| `--output-root` | No argument help text is declared; parser destination is `output_root`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build matrix`

matrix command

### Usage

```
x86decomp build matrix [-h]
```

### Syntax example

```
x86decomp build matrix
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build show`

show command

### Usage

```
x86decomp build show [-h] build_id
```

### Syntax example

```
x86decomp build show example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `build_id` required | No argument help text is declared; parser destination is `build_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp build validate`

validate command

### Usage

```
x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id
```

### Syntax example

```
x86decomp build validate ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target_id` required | No argument help text is declared; parser destination is `target_id`. |
| `--variant-id` | No argument help text is declared; parser destination is `variant_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.
