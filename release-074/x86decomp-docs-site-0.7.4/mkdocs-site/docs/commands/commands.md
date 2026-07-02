---
title: x86decomp commands
description: list canonical capability routes and implementation owners
original_path: commands/commands.html
---

<a id="command-commands"></a>

Section: Command reference

# `x86decomp commands`

list canonical capability routes and implementation owners

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp commands --help
```

Metadata: current · canonical interface

## `x86decomp commands`

list canonical capability routes and implementation owners

### Usage

```
x86decomp commands [-h]
                          [--group {abi,asm,boundary,build,campaign,candidate,capsule,changeset,consensus,counterexample,family,graph,headers,hybrid,hypothesis,library,loop,match,module,pe,plugin,project,proof,provenance,reloc,review,runtime,security,source,staging,tests,windows,worker}]
                          [--owner {governance,reconstruction,native,assembly}]
```

### Syntax example

```
x86decomp commands
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `--group` choices: abi, asm, boundary, build, campaign, candidate, capsule, changeset, consensus, counterexample, family, graph, headers, hybrid, hypothesis, library, loop, match, module, pe, plugin, project, proof, provenance, reloc, review, runtime, security, source, staging, tests, windows, worker | No argument help text is declared; parser destination is `group`. |
| `--owner` choices: governance, reconstruction, native, assembly | No argument help text is declared; parser destination is `owner`. |

> **Source basis.** Parser definition: `src/x86decomp/canonical.py`; SHA-256 `4424ac7f4214c0af367791e1cba7268b5bc1d9ff0d7fa4f56d4c94fff6eae782`. Descriptions above use only parser-declared text or an explicit no-help notice.
