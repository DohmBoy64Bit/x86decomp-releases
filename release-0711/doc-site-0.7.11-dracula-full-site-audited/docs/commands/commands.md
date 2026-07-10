---
title: x86decomp commands
description: Parser-derived command reference page for `commands`.
---

# `x86decomp commands`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp commands [-h]
                          [--group {abi,asm,asset,boundary,build,campaign,candidate,capsule,changeset,class,compiler-rules,consensus,counterexample,decompiler,diff,family,function,game-pattern,ghidra-mcp,graph,headers,hybrid,hypothesis,image-text,library,llm,loop,match,mod,module,pattern,pe,playability,plugin,progress,project,proof,provenance,regression,release-policy,reloc,review,runtime,runtime-analysis,script-port,security,source,source-map,source-stage,staging,subsystem,tests,text-swap,toolchain,triage,type,vtable,windows,worker}]
                          [--owner {governance,reconstruction,native,assembly}]

options:
  -h, --help            show this help message and exit
  --group {abi,asm,asset,boundary,build,campaign,candidate,capsule,changeset,class,compiler-rules,consensus,counterexample,decompiler,diff,family,function,game-pattern,ghidra-mcp,graph,headers,hybrid,hypothesis,image-text,library,llm,loop,match,mod,module,pattern,pe,playability,plugin,progress,project,proof,provenance,regression,release-policy,reloc,review,runtime,runtime-analysis,script-port,security,source,source-map,source-stage,staging,subsystem,tests,text-swap,toolchain,triage,type,vtable,windows,worker}
  --owner {governance,reconstruction,native,assembly}
```
