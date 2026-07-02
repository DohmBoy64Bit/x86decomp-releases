---
title: x86decomp security
description: Canonical security commands implemented by the current capability subsystem.
original_path: commands/security.html
---

<a id="command-security-finding"></a>
<a id="command-security-policy"></a>
<a id="command-security-report"></a>
<a id="command-security-scan"></a>

Section: Command reference

# `x86decomp security`

Canonical security commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp security --help
```

Metadata: current · reconstruction

## `x86decomp security finding`

finding command

### Usage

```
x86decomp security finding [-h] --evidence-json EVIDENCE_JSON
                                  rule_id severity subject_id summary
```

### Syntax example

```
x86decomp security finding example-001 example example-001 example --evidence-json ./evidence.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `rule_id` required | No argument help text is declared; parser destination is `rule_id`. |
| `severity` required | No argument help text is declared; parser destination is `severity`. |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `summary` required | No argument help text is declared; parser destination is `summary`. |
| `--evidence-json` required | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp security policy`

policy command

### Usage

```
x86decomp security policy [-h] name policy_json
```

### Syntax example

```
x86decomp security policy example conservative
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `name` required | No argument help text is declared; parser destination is `name`. |
| `policy_json` required | No argument help text is declared; parser destination is `policy_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp security report`

report command

### Usage

```
x86decomp security report [-h]
```

### Syntax example

```
x86decomp security report
```

### Arguments

No route-specific arguments are declared.

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp security scan`

scan command

### Usage

```
x86decomp security scan [-h] observations_json
```

### Syntax example

```
x86decomp security scan ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `observations_json` required | No argument help text is declared; parser destination is `observations_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.
