---
title: x86decomp worker
description: Canonical worker commands implemented by the current capability subsystem.
original_path: commands/worker.html
---

<a id="command-worker-doctor"></a>
<a id="command-worker-list"></a>
<a id="command-worker-register"></a>
<a id="command-worker-select"></a>
<a id="command-worker-status"></a>

Section: Command reference

# `x86decomp worker`

Canonical worker commands implemented by the current capability subsystem.

Metadata: current · canonical group · 5 runnable paths

## Help

```
x86decomp worker --help
```

Metadata: current · governance

## `x86decomp worker doctor`

doctor command

### Usage

```
x86decomp worker doctor [-h] worker_id
```

### Syntax example

```
x86decomp worker doctor worker-local
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `worker_id` required | No argument help text is declared; parser destination is `worker_id`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp worker list`

list command

### Usage

```
x86decomp worker list [-h] [--status STATUS]
```

### Syntax example

```
x86decomp worker list
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--status` | No argument help text is declared; parser destination is `status`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp worker register`

register command

### Usage

```
x86decomp worker register [-h] [--endpoint ENDPOINT]
                                 [--environment-sha256 ENVIRONMENT_SHA256]
                                 name capabilities_json
```

### Syntax example

```
x86decomp worker register example ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `capabilities_json` required | No argument help text is declared; parser destination is `capabilities_json`. |
| `--endpoint` | No argument help text is declared; parser destination is `endpoint`. |
| `--environment-sha256` | No argument help text is declared; parser destination is `environment_sha256`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp worker select`

select command

### Usage

```
x86decomp worker select [-h] required_json
```

### Syntax example

```
x86decomp worker select ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `required_json` required | No argument help text is declared; parser destination is `required_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp worker status`

status command

### Usage

```
x86decomp worker status [-h] worker_id status
```

### Syntax example

```
x86decomp worker status worker-local active
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `worker_id` required | No argument help text is declared; parser destination is `worker_id`. |
| `status` required | No argument help text is declared; parser destination is `status`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
