---
title: x86decomp library
description: Canonical library commands implemented by the current capability subsystem.
original_path: commands/library.html
---

<a id="command-library-accept"></a>
<a id="command-library-candidates"></a>
<a id="command-library-externalize"></a>
<a id="command-library-identify"></a>
<a id="command-library-reconstruct"></a>
<a id="command-library-reject"></a>

Section: Command reference

# `x86decomp library`

Canonical library commands implemented by the current capability subsystem.

Metadata: current · canonical group · 6 runnable paths

## Help

```
x86decomp library --help
```

Metadata: current · reconstruction

## `x86decomp library accept`

accept command

### Usage

```
x86decomp library accept [-h] match_id
```

### Syntax example

```
x86decomp library accept example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `match_id` required | No argument help text is declared; parser destination is `match_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp library candidates`

candidates command

### Usage

```
x86decomp library candidates [-h] subject_id
```

### Syntax example

```
x86decomp library candidates example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp library externalize`

externalize command

### Usage

```
x86decomp library externalize [-h] match_id
```

### Syntax example

```
x86decomp library externalize example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `match_id` required | No argument help text is declared; parser destination is `match_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp library identify`

identify command

### Usage

```
x86decomp library identify [-h] [--version-range VERSION_RANGE]
                                  --confidence CONFIDENCE
                                  --evidence-json EVIDENCE_JSON
                                  subject_id library_name
```

### Syntax example

```
x86decomp library identify example-001 ./library.lib --confidence 1.0 --evidence-json ./evidence.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `subject_id` required | No argument help text is declared; parser destination is `subject_id`. |
| `library_name` required | No argument help text is declared; parser destination is `library_name`. |
| `--version-range` | No argument help text is declared; parser destination is `version_range`. |
| `--confidence` required · type: float | No argument help text is declared; parser destination is `confidence`. |
| `--evidence-json` required | No argument help text is declared; parser destination is `evidence_json`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp library reconstruct`

reconstruct command

### Usage

```
x86decomp library reconstruct [-h] match_id
```

### Syntax example

```
x86decomp library reconstruct example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `match_id` required | No argument help text is declared; parser destination is `match_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp library reject`

reject command

### Usage

```
x86decomp library reject [-h] match_id
```

### Syntax example

```
x86decomp library reject example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `match_id` required | No argument help text is declared; parser destination is `match_id`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.
