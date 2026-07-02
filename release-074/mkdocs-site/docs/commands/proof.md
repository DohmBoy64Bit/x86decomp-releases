---
title: x86decomp proof
description: Canonical proof commands implemented by the current capability subsystem.
original_path: commands/proof.html
---

<a id="command-proof-evaluate"></a>
<a id="command-proof-export"></a>
<a id="command-proof-inspect"></a>
<a id="command-proof-obligation"></a>
<a id="command-proof-result"></a>
<a id="command-proof-verify"></a>

Section: Command reference

# `x86decomp proof`

Canonical proof commands implemented by the current capability subsystem.

Metadata: current · canonical group · 6 runnable paths

## Help

```
x86decomp proof --help
```

Metadata: current · governance

## `x86decomp proof evaluate`

evaluate command

### Usage

```
x86decomp proof evaluate [-h] obligation_id
```

### Syntax example

```
x86decomp proof evaluate example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `obligation_id` required | No argument help text is declared; parser destination is `obligation_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp proof export`

export command

### Usage

```
x86decomp proof export [-h] [--include INCLUDE] output
```

### Syntax example

```
x86decomp proof export ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `output` required | No argument help text is declared; parser destination is `output`. |
| `--include` default: [] | No argument help text is declared; parser destination is `include`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp proof inspect`

inspect command

### Usage

```
x86decomp proof inspect [-h] path
```

### Syntax example

```
x86decomp proof inspect ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp proof obligation`

obligation command

### Usage

```
x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON]
                                  scope_kind scope_id property_name
                                  required_status
```

### Syntax example

```
x86decomp proof obligation function pe-rva:00001000 ./target.exe active
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `scope_kind` required | No argument help text is declared; parser destination is `scope_kind`. |
| `scope_id` required | No argument help text is declared; parser destination is `scope_id`. |
| `property_name` required | No argument help text is declared; parser destination is `property_name`. |
| `required_status` required | No argument help text is declared; parser destination is `required_status`. |
| `--assumptions-json` | No argument help text is declared; parser destination is `assumptions_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp proof result`

result command

### Usage

```
x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256]
                              obligation_id status validator report_json
```

### Syntax example

```
x86decomp proof result example-001 active example-001 ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `obligation_id` required | No argument help text is declared; parser destination is `obligation_id`. |
| `status` required | No argument help text is declared; parser destination is `status`. |
| `validator` required | No argument help text is declared; parser destination is `validator`. |
| `report_json` required | No argument help text is declared; parser destination is `report_json`. |
| `--artifact-sha256` | No argument help text is declared; parser destination is `artifact_sha256`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp proof verify`

verify command

### Usage

```
x86decomp proof verify [-h] path
```

### Syntax example

```
x86decomp proof verify ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
