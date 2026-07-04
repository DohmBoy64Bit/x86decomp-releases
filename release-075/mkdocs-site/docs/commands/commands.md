---
title: x86decomp commands
description: Exact parser-derived reference for x86decomp commands in 0.7.5.
---

# `x86decomp commands`

## `x86decomp commands`

usage: x86decomp commands [-h]

### Usage

```text
x86decomp commands [-h]
                          [--group {abi,asm,boundary,build,campaign,candidate,capsule,changeset,consensus,counterexample,family,graph,headers,hybrid,hypothesis,library,llm,loop,match,module,pe,plugin,project,proof,provenance,reloc,review,runtime,security,source,staging,tests,windows,worker}]
                          [--owner {governance,reconstruction,native,assembly}]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--group` | choices: `abi`, `asm`, `boundary`, `build`, `campaign`, `candidate`, `capsule`, `changeset`, `consensus`, `counterexample`, `family`, `graph`, `headers`, `hybrid`, `hypothesis`, `library`, `llm`, `loop`, `match`, `module`, `pe`, `plugin`, `project`, `proof`, `provenance`, `reloc`, `review`, `runtime`, `security`, `source`, `staging`, `tests`, `windows`, `worker`. No help text is declared; parser destination is `group`. |
| `--owner` | choices: `governance`, `reconstruction`, `native`, `assembly`. No help text is declared; parser destination is `owner`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/canonical.py` · `a525a07fb95f10e5895a43517cdc3ff0a13df421b87195dc687629a02fd1bdd8` |
