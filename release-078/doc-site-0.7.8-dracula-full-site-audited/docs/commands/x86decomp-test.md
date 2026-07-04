---
title: x86decomp-test
description: Command reference for the verification executable.
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

| Argument | Details |
| --- | --- |
| `--config` | type: `path` · default: `PosixPath('x86decomp-test.json')`. |
| `--resolve` | nargs: `0` · default: `False`. |
| `--verbose` | nargs: `0` · default: `False`. |

## `x86decomp-test capabilities`

```text
usage: x86decomp-test capabilities [-h] [--config CONFIG]
```

### Arguments

| Argument | Details |
| --- | --- |
| `--config` | type: `path` · default: `PosixPath('x86decomp-test.json')`. |

## `x86decomp-test catalog`

```text
usage: x86decomp-test catalog [-h] [--print]
```

### Arguments

| Argument | Details |
| --- | --- |
| `--print` | nargs: `0` · default: `False`. |

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

| Argument | Details |
| --- | --- |
| `--toolkit-root` | required · type: `path`. |
| `--output-root` | type: `path` · default: `PosixPath('test-results')`. |
| `--config` | type: `path` · default: `PosixPath('x86decomp-test.json')`. |
| `--install-root` | type: `path`. |
| `--non-interactive` | nargs: `0` · default: `False`. |
| `--allow-network` | nargs: `0` · default: `False`. |
| `--allow-install` | nargs: `0` · default: `False`. |
| `--non-strict` | nargs: `0` · default: `False`. |

## `x86decomp-test inventory`

```text
usage: x86decomp-test inventory [-h] [--config CONFIG] [--output OUTPUT]
```

### Arguments

| Argument | Details |
| --- | --- |
| `--config` | type: `path` · default: `PosixPath('x86decomp-test.json')`. |
| `--output` | type: `path`. |

## `x86decomp-test run`

```text
usage: x86decomp-test run [-h] [--config CONFIG] [--verbose]
```

### Arguments

| Argument | Details |
| --- | --- |
| `--config` | type: `path` · default: `PosixPath('x86decomp-test.json')`. |
| `--verbose` | nargs: `0` · default: `False`. |


