---
title: x86decomp-test
description: Exact parser-derived reference for the 0.7.8 verification executable.
---

# `x86decomp-test`

The independent verification executable.

## `x86decomp-test adapters`

usage: x86decomp-test adapters [-h] [--config CONFIG] [--resolve] [--verbose]

### Usage

```text
x86decomp-test adapters [-h] [--config CONFIG] [--resolve] [--verbose]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | default: `PosixPath('x86decomp-test.json')` · type: `_path`. No help text is declared; parser destination is `config`. |
| `--resolve` | default: `False` · nargs: `0`. No help text is declared; parser destination is `resolve`. |
| `--verbose` | default: `False` · nargs: `0`. No help text is declared; parser destination is `verbose`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `verification harness` | `test-suite/src/x86decomp_testkit/cli.py` · `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67` |
## `x86decomp-test catalog`

usage: x86decomp-test catalog [-h] [--print]

### Usage

```text
x86decomp-test catalog [-h] [--print]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--print` | default: `False` · nargs: `0`. No help text is declared; parser destination is `print_catalog`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `verification harness` | `test-suite/src/x86decomp_testkit/cli.py` · `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67` |
## `x86decomp-test init-config`

usage: x86decomp-test init-config [-h] --toolkit-root TOOLKIT_ROOT

### Usage

```text
x86decomp-test init-config [-h] --toolkit-root TOOLKIT_ROOT
                                  [--output-root OUTPUT_ROOT]
                                  [--config CONFIG]
                                  [--install-root INSTALL_ROOT]
                                  [--non-interactive] [--allow-network]
                                  [--allow-install] [--non-strict]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--toolkit-root` | required · type: `_path`. No help text is declared; parser destination is `toolkit_root`. |
| `--output-root` | default: `PosixPath('test-results')` · type: `_path`. No help text is declared; parser destination is `output_root`. |
| `--config` | default: `PosixPath('x86decomp-test.json')` · type: `_path`. No help text is declared; parser destination is `config`. |
| `--install-root` | type: `_path`. No help text is declared; parser destination is `install_root`. |
| `--non-interactive` | default: `False` · nargs: `0`. No help text is declared; parser destination is `non_interactive`. |
| `--allow-network` | default: `False` · nargs: `0`. No help text is declared; parser destination is `allow_network`. |
| `--allow-install` | default: `False` · nargs: `0`. No help text is declared; parser destination is `allow_install`. |
| `--non-strict` | default: `False` · nargs: `0`. No help text is declared; parser destination is `non_strict`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `verification harness` | `test-suite/src/x86decomp_testkit/cli.py` · `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67` |
## `x86decomp-test inventory`

usage: x86decomp-test inventory [-h] [--config CONFIG] [--output OUTPUT]

### Usage

```text
x86decomp-test inventory [-h] [--config CONFIG] [--output OUTPUT]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | default: `PosixPath('x86decomp-test.json')` · type: `_path`. No help text is declared; parser destination is `config`. |
| `--output` | type: `_path`. No help text is declared; parser destination is `output`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `verification harness` | `test-suite/src/x86decomp_testkit/cli.py` · `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67` |
## `x86decomp-test run`

usage: x86decomp-test run [-h] [--config CONFIG] [--verbose]

### Usage

```text
x86decomp-test run [-h] [--config CONFIG] [--verbose]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--config` | default: `PosixPath('x86decomp-test.json')` · type: `_path`. No help text is declared; parser destination is `config`. |
| `--verbose` | default: `False` · nargs: `0`. No help text is declared; parser destination is `verbose`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `verification harness` | `test-suite/src/x86decomp_testkit/cli.py` · `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67` |
