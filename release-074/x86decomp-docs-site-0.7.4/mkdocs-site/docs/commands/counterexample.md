---
title: x86decomp counterexample
description: Canonical counterexample commands implemented by the current capability
  subsystem.
original_path: commands/counterexample.html
---

<a id="command-counterexample-add"></a>
<a id="command-counterexample-list"></a>
<a id="command-counterexample-promote"></a>
<a id="command-counterexample-show"></a>

Section: Command reference

# `x86decomp counterexample`

Canonical counterexample commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp counterexample --help
```

Metadata: current · governance

## `x86decomp counterexample add`

add command

### Usage

```
x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON
                                    [--provenance-json PROVENANCE_JSON]
                                    scope_kind scope_id payload
```

### Syntax example

```
x86decomp counterexample add function pe-rva:00001000 example --predicate-json matches
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `scope_kind` required | No argument help text is declared; parser destination is `scope_kind`. |
| `scope_id` required | No argument help text is declared; parser destination is `scope_id`. |
| `payload` required | No argument help text is declared; parser destination is `payload`. |
| `--predicate-json` required | No argument help text is declared; parser destination is `predicate_json`. |
| `--provenance-json` | No argument help text is declared; parser destination is `provenance_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp counterexample list`

list command

### Usage

```
x86decomp counterexample list [-h]
```

### Syntax example

```
x86decomp counterexample list
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp counterexample promote`

promote command

### Usage

```
x86decomp counterexample promote [-h] counterexample_id destination
```

### Syntax example

```
x86decomp counterexample promote 1 example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `counterexample_id` required | No argument help text is declared; parser destination is `counterexample_id`. |
| `destination` required | No argument help text is declared; parser destination is `destination`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp counterexample show`

show command

### Usage

```
x86decomp counterexample show [-h] counterexample_id
```

### Syntax example

```
x86decomp counterexample show 1
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `counterexample_id` required | No argument help text is declared; parser destination is `counterexample_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
