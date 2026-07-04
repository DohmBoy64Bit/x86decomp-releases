---
title: x86decomp commands
description: Exact v0.7.8 parser-derived reference for `x86decomp commands`.
---


# `x86decomp commands`

## Usage

```text
usage: x86decomp commands [-h]
                          [--group {abi,asm,asset,boundary,build,campaign,candidate,capsule,changeset,class,compiler-rules,consensus,counterexample,decompiler,diff,family,function,game-pattern,ghidra-mcp,graph,headers,hybrid,hypothesis,image-text,library,llm,loop,match,mod,module,pattern,pe,playability,plugin,progress,project,proof,provenance,regression,release-policy,reloc,review,runtime,runtime-analysis,script-port,security,source,source-map,source-stage,staging,subsystem,tests,text-swap,toolchain,triage,type,vtable,windows,worker}]
                          [--owner {governance,reconstruction,native,assembly}]
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--group` | choices: `abi`, `asm`, `asset`, `boundary`, `build`, `campaign`, `candidate`, `capsule`, `changeset`, `class`, `compiler-rules`, `consensus`, `counterexample`, `decompiler`, `diff`, `family`, `function`, `game-pattern`, `ghidra-mcp`, `graph`, `headers`, `hybrid`, `hypothesis`, `image-text`, `library`, `llm`, `loop`, `match`, `mod`, `module`, `pattern`, `pe`, `playability`, `plugin`, `progress`, `project`, `proof`, `provenance`, `regression`, `release-policy`, `reloc`, `review`, `runtime`, `runtime-analysis`, `script-port`, `security`, `source`, `source-map`, `source-stage`, `staging`, `subsystem`, `tests`, `text-swap`, `toolchain`, `triage`, `type`, `vtable`, `windows`, `worker` · parser destination: `group`. No help text declared. |
| `--owner` | choices: `governance`, `reconstruction`, `native`, `assembly` · parser destination: `owner`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
