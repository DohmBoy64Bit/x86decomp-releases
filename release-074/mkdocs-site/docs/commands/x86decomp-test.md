---
title: x86decomp-test
description: No-silent-skip comprehensive verification harness for x86decomp-toolkit
original_path: commands/x86decomp-test.html
---

<a id="command-adapters"></a>
<a id="command-catalog"></a>
<a id="command-init-config"></a>
<a id="command-inventory"></a>
<a id="command-run"></a>

Section: Verification command reference

# `x86decomp-test`

No-silent-skip comprehensive verification harness for x86decomp-toolkit

Metadata: current · verification executable · 5 runnable paths

## Help

```
x86decomp-test --help
```

Metadata: current · verification harness

## `x86decomp-test adapters`

detect adapters and optionally resolve missing ones

### Usage

```
x86decomp-test adapters [-h] [--config CONFIG] [--resolve] [--verbose]
```

### Syntax example

```
x86decomp-test adapters --config ./x86decomp-test.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--config` default: x86decomp-test.json · type: _path | No argument help text is declared; parser destination is `config`. |
| `--resolve` nargs: 0 · default: False | No argument help text is declared; parser destination is `resolve`. |
| `--verbose` nargs: 0 · default: False | No argument help text is declared; parser destination is `verbose`. |

> **Source basis.** Parser definition: `test-suite/src/x86decomp_testkit/cli.py`; SHA-256 `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · verification harness

## `x86decomp-test catalog`

show the pinned feature catalog path

### Usage

```
x86decomp-test catalog [-h] [--print]
```

### Syntax example

```
x86decomp-test catalog
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--print` nargs: 0 · default: False | No argument help text is declared; parser destination is `print_catalog`. |

> **Source basis.** Parser definition: `test-suite/src/x86decomp_testkit/cli.py`; SHA-256 `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · verification harness

## `x86decomp-test init-config`

create a test configuration

### Usage

```
x86decomp-test init-config [-h] --toolkit-root TOOLKIT_ROOT
                                  [--output-root OUTPUT_ROOT]
                                  [--config CONFIG]
                                  [--install-root INSTALL_ROOT]
                                  [--non-interactive] [--allow-network]
                                  [--allow-install] [--non-strict]
```

### Syntax example

```
x86decomp-test init-config --toolkit-root . --output-root ./test-results --install-root ./.x86decomp-test-tools --config ./x86decomp-test.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--toolkit-root` required · type: _path | No argument help text is declared; parser destination is `toolkit_root`. |
| `--output-root` default: test-results · type: _path | No argument help text is declared; parser destination is `output_root`. |
| `--config` default: x86decomp-test.json · type: _path | No argument help text is declared; parser destination is `config`. |
| `--install-root` type: _path | No argument help text is declared; parser destination is `install_root`. |
| `--non-interactive` nargs: 0 · default: False | No argument help text is declared; parser destination is `non_interactive`. |
| `--allow-network` nargs: 0 · default: False | No argument help text is declared; parser destination is `allow_network`. |
| `--allow-install` nargs: 0 · default: False | No argument help text is declared; parser destination is `allow_install`. |
| `--non-strict` nargs: 0 · default: False | No argument help text is declared; parser destination is `non_strict`. |

> **Source basis.** Parser definition: `test-suite/src/x86decomp_testkit/cli.py`; SHA-256 `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · verification harness

## `x86decomp-test inventory`

print the discovered toolkit surface

### Usage

```
x86decomp-test inventory [-h] [--config CONFIG] [--output OUTPUT]
```

### Syntax example

```
x86decomp-test inventory --config ./x86decomp-test.json --output ./inventory.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--config` default: x86decomp-test.json · type: _path | No argument help text is declared; parser destination is `config`. |
| `--output` type: _path | No argument help text is declared; parser destination is `output`. |

> **Source basis.** Parser definition: `test-suite/src/x86decomp_testkit/cli.py`; SHA-256 `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · verification harness

## `x86decomp-test run`

run the complete suite

### Usage

```
x86decomp-test run [-h] [--config CONFIG] [--verbose]
```

### Syntax example

```
x86decomp-test run --config ./x86decomp-test.json --verbose
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--config` default: x86decomp-test.json · type: _path | No argument help text is declared; parser destination is `config`. |
| `--verbose` nargs: 0 · default: False | No argument help text is declared; parser destination is `verbose`. |

> **Source basis.** Parser definition: `test-suite/src/x86decomp_testkit/cli.py`; SHA-256 `fc69ddd59b29350727a5762fe78f440d3538bee7c83d5342478d18ee3a0dcd67`. Descriptions above use only parser-declared text or an explicit no-help notice.
