---
title: x86decomp changeset
description: Canonical changeset commands implemented by the current capability subsystem.
original_path: commands/changeset.html
---

<a id="command-changeset-add-operation"></a>
<a id="command-changeset-apply"></a>
<a id="command-changeset-conflicts"></a>
<a id="command-changeset-create"></a>
<a id="command-changeset-export"></a>
<a id="command-changeset-inspect"></a>
<a id="command-changeset-merge"></a>
<a id="command-changeset-rebase"></a>
<a id="command-changeset-show"></a>
<a id="command-changeset-verify"></a>

Section: Command reference

# `x86decomp changeset`

Canonical changeset commands implemented by the current capability subsystem.

Metadata: current · canonical group · 10 runnable paths

## Help

```
x86decomp changeset --help
```

Metadata: current · reconstruction

## `x86decomp changeset add-operation`

add-operation command

### Usage

```
x86decomp changeset add-operation [-h] changeset_id operation_json
```

### Syntax example

```
x86decomp changeset add-operation example-001 ./target.exe
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `changeset_id` required | No argument help text is declared; parser destination is `changeset_id`. |
| `operation_json` required | No argument help text is declared; parser destination is `operation_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp changeset apply`

apply command

### Usage

```
x86decomp changeset apply [-h] path
```

### Syntax example

```
x86decomp changeset apply ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp changeset conflicts`

conflicts command

### Usage

```
x86decomp changeset conflicts [-h] changeset_id
```

### Syntax example

```
x86decomp changeset conflicts example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `changeset_id` required | No argument help text is declared; parser destination is `changeset_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp changeset create`

create command

### Usage

```
x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH]
                                  name
```

### Syntax example

```
x86decomp changeset create example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `--base-audit-hash` | No argument help text is declared; parser destination is `base_audit_hash`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp changeset export`

export command

### Usage

```
x86decomp changeset export [-h] [--after-hash AFTER_HASH] output
```

### Syntax example

```
x86decomp changeset export ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--after-hash` | No argument help text is declared; parser destination is `after_hash`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp changeset inspect`

inspect command

### Usage

```
x86decomp changeset inspect [-h] path
```

### Syntax example

```
x86decomp changeset inspect ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp changeset merge`

merge command

### Usage

```
x86decomp changeset merge [-h] left_id right_id name
```

### Syntax example

```
x86decomp changeset merge example-001 example-001 example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `left_id` required | No argument help text is declared; parser destination is `left_id`. |
| `right_id` required | No argument help text is declared; parser destination is `right_id`. |
| `name` required | No argument help text is declared; parser destination is `name`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp changeset rebase`

rebase command

### Usage

```
x86decomp changeset rebase [-h] changeset_id new_base_hash
```

### Syntax example

```
x86decomp changeset rebase example-001 0x400000
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `changeset_id` required | No argument help text is declared; parser destination is `changeset_id`. |
| `new_base_hash` required | No argument help text is declared; parser destination is `new_base_hash`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp changeset show`

show command

### Usage

```
x86decomp changeset show [-h] changeset_id
```

### Syntax example

```
x86decomp changeset show example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `changeset_id` required | No argument help text is declared; parser destination is `changeset_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp changeset verify`

verify command

### Usage

```
x86decomp changeset verify [-h] changeset_id
```

### Syntax example

```
x86decomp changeset verify example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `changeset_id` required | No argument help text is declared; parser destination is `changeset_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.
