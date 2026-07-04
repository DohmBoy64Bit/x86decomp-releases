---
title: x86decomp-test
description: Exact v0.7.8 parser-derived reference for the verification executable.
---


# `x86decomp-test`

The independent verification executable.

## Usage

```text
usage: x86decomp-test [-h]
                      {init-config,adapters,capabilities,inventory,run,catalog} ...
```

## Commands

| Command | Usage |
| --- | --- |
| `adapters` | `usage: x86decomp-test adapters [-h] [--config CONFIG] [--resolve] [--verbose]` |
| `capabilities` | `usage: x86decomp-test capabilities [-h] [--config CONFIG]` |
| `catalog` | `usage: x86decomp-test catalog [-h] [--print]` |
| `init-config` | `usage: x86decomp-test init-config [-h] --toolkit-root TOOLKIT_ROOT [--output-root OUTPUT_ROOT] [--config CONFIG] [--install-root INSTALL_ROOT] [--non-interactive] [--allow-network] [--allow-install] [--non-strict]` |
| `inventory` | `usage: x86decomp-test inventory [-h] [--config CONFIG] [--output OUTPUT]` |
| `run` | `usage: x86decomp-test run [-h] [--config CONFIG] [--verbose]` |

## `x86decomp-test adapters`

```text
usage: x86decomp-test adapters [-h] [--config CONFIG] [--resolve] [--verbose]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | type: `_path` · default: `PosixPath('x86decomp-test.json')` · parser destination: `config`. No help text declared. |
| `--resolve` | nargs: `0` · default: `False` · parser destination: `resolve`. No help text declared. |
| `--verbose` | nargs: `0` · default: `False` · parser destination: `verbose`. No help text declared. |

## `x86decomp-test capabilities`

```text
usage: x86decomp-test capabilities [-h] [--config CONFIG]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | type: `_path` · default: `PosixPath('x86decomp-test.json')` · parser destination: `config`. No help text declared. |

## `x86decomp-test catalog`

```text
usage: x86decomp-test catalog [-h] [--print]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--print` | nargs: `0` · default: `False` · parser destination: `print_catalog`. No help text declared. |

## `x86decomp-test init-config`

```text
usage: x86decomp-test init-config [-h] --toolkit-root TOOLKIT_ROOT
                                  [--output-root OUTPUT_ROOT]
                                  [--config CONFIG]
                                  [--install-root INSTALL_ROOT]
                                  [--non-interactive] [--allow-network]
                                  [--allow-install] [--non-strict]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--toolkit-root` | required · type: `_path` · parser destination: `toolkit_root`. No help text declared. |
| `--output-root` | type: `_path` · default: `PosixPath('test-results')` · parser destination: `output_root`. No help text declared. |
| `--config` | type: `_path` · default: `PosixPath('x86decomp-test.json')` · parser destination: `config`. No help text declared. |
| `--install-root` | type: `_path` · parser destination: `install_root`. No help text declared. |
| `--non-interactive` | nargs: `0` · default: `False` · parser destination: `non_interactive`. No help text declared. |
| `--allow-network` | nargs: `0` · default: `False` · parser destination: `allow_network`. No help text declared. |
| `--allow-install` | nargs: `0` · default: `False` · parser destination: `allow_install`. No help text declared. |
| `--non-strict` | nargs: `0` · default: `False` · parser destination: `non_strict`. No help text declared. |

## `x86decomp-test inventory`

```text
usage: x86decomp-test inventory [-h] [--config CONFIG] [--output OUTPUT]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | type: `_path` · default: `PosixPath('x86decomp-test.json')` · parser destination: `config`. No help text declared. |
| `--output` | type: `_path` · parser destination: `output`. No help text declared. |

## `x86decomp-test run`

```text
usage: x86decomp-test run [-h] [--config CONFIG] [--verbose]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | type: `_path` · default: `PosixPath('x86decomp-test.json')` · parser destination: `config`. No help text declared. |
| `--verbose` | nargs: `0` · default: `False` · parser destination: `verbose`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| verification harness cli | `test-suite/src/x86decomp_testkit/cli.py` | `c4be8f226c0b7067846b385618b2392017fbbb113082016b4d72855098b07c44` |

## Verification boundary

This page is regenerated from the v0.7.8 `x86decomp-test` parser surface. It documents parser-declared syntax; it does not claim that optional adapters or live local-model endpoints are installed.
