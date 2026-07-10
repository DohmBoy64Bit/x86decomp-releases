---
title: 'Example: full-relink and whole-image convergence project'
description: Correlate PE, MAP, COFF, and library evidence into an explicit linker
  plan, execute a manifest-driven relink, compare whole images, and iterate with durable
  convergence history.
original_path: project-examples/full-relink-convergence.html
---

<a id="model"></a>
<a id="full-relink-convergence-flow-title"></a>
<a id="full-relink-convergence-flow-desc"></a>
<a id="arrow-full-relink-convergence"></a>
<a id="full-relink-convergence-flow-caption"></a>
<a id="inventory"></a>
<a id="layout"></a>
<a id="plan"></a>
<a id="relink"></a>
<a id="compare"></a>
<a id="iterate"></a>
<a id="state"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: full-relink and whole-image convergence project

Correlate PE, MAP, COFF, and library evidence into an explicit linker plan, execute a manifest-driven relink, compare whole images, and iterate with durable convergence history.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.11 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is a supporting linker-reconstruction workflow. It can advance a matching project but remains evidence-limited.

**On this page**

1. [Convergence model](#model)
2. [Inventory inputs](#inventory)
3. [Reconstruct layout](#layout)
4. [Build a linker plan](#plan)
5. [Execute relink](#relink)
6. [Compare images](#compare)
7. [Iterate](#iterate)
8. [Advance workflow](#state)
9. [Truth boundary](#limits)
10. [Source basis](#source-basis)

## Convergence model

Each iteration preserves unresolved facts and measured image differences instead of guessing erased linker state.PE + MAP → COFF + libraries → Layout report → Linker plan → Relink manifest → Image match → Convergence history

PE + MAPCOFF + librariesLayout reportLinker planRelink manifestImage matchConvergence history

Each iteration preserves unresolved facts and measured image differences instead of guessing erased linker state.

```ascii-fallback
PE + MAP → COFF + libraries → Layout report → Linker plan → Relink manifest → Image match → Convergence history
```

1

## Verify all layout evidence

```
x86decomp inspect-pe target.exe
x86decomp map-inspect target.map
x86decomp coff-inspect build/entry.obj
x86decomp lib-inspect runtime.lib
x86decomp coff-comdat-resolve build/entry.obj build/sub_00401230.obj --report reports/comdat.json
```

Object order, contributions, COMDAT selection, libraries, machine type, and section properties all affect relinking. Use the real artifacts; a MAP alone cannot substantiate object contents.

2

## Correlate PE sections, MAP contributions, and objects

```
x86decomp layout-reconstruct target.exe target.map build/entry.obj build/sub_00401230.obj --report reports/layout.json
```

The layout report correlates the supplied evidence and exposes gaps. It does not manufacture missing objects or claim exact historical ordering where the inputs do not support it.

3

## Build an evidence-limited linker plan

```
x86decomp linker-plan target.exe target.map build/entry.obj build/sub_00401230.obj --library runtime.lib --linker lld-link --output-image build/reconstructed.exe --report reports/linker-plan.json --write-relink-manifest config/relink.json
```

Inspect `unresolved` and `ready_for_relink` in the plan. The generated manifest is an executable proposal built from known inputs, not a recovered original command line.

4

## Execute the explicit manifest

The bundled x64 manifest illustrates the relink schema:

```
{
  "schema_version": 1,
  "linker": "lld-link",
  "objects": ["entry.obj"],
  "output": "linked.exe",
  "arguments": [
    "/nologo",
    "/machine:x64",
    "/entry:entry",
    "/subsystem:console",
    "/nodefaultlib",
    "/out:{output}",
    "{objects}"
  ],
  "environment": {},
  "inherit_environment": true,
  "timeout_seconds": 60
}
```

```
x86decomp relink config/relink.json --report reports/relink.json
```

The report captures the linker identity, command array, object identities, stdout/stderr, return code, and output hash. Success requires a zero return code and an output file; it does not imply image equality.

5

## Derive a target-specific profile and compare

```
x86decomp image-profile target.exe config/image-profile.json
x86decomp image-match target.exe build/reconstructed.exe --profile config/image-profile.json --report reports/image-match.json
```

The image matcher reports raw exact identity separately from profile-normalized identity. Normalization is explicit and target-specific; it must not be described as byte-identical.

6

## Analyze differences and append history

```
x86decomp convergence-analyze target.exe build/reconstructed.exe --profile config/image-profile.json --report reports/convergence-001.json --history reports/convergence-history.json
x86decomp convergence-analyze target.exe build/reconstructed-002.exe --profile config/image-profile.json --previous reports/convergence-001.json --report reports/convergence-002.json --history reports/convergence-history.json
```

The analyzer groups section differences, compares with a previous report, emits next-step recommendations, and appends history. Its `complete` condition is raw exact match; recommendations are diagnostic, not proof of root cause.

7

## Advance matching status only when policy passes

```
x86decomp workflow-update project pe-rva:00401230 --matching-status image_integrated --report-kind image-match --report-path reports/image-match.json
x86decomp workflow-update project pe-rva:00401230 --matching-status full_relink_validated --report-kind convergence --report-path reports/convergence-002.json
```

> **State recording is separate.** Validators emit reports, but they do not automatically promote a function workflow. Inspect a passing report first, then use `workflow-update` to attach that report and record the justified status.

## Truth boundary

- A successful linker invocation is not a matching image.
- A normalized match is not raw identity.
- A linker plan preserves unresolved fields and cannot recover erased flags without evidence.
- Whole-image equality does not authenticate original source or prove behavior for every runtime input.

## v0.7.11 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/linker_reconstruction.py` | `f67bc3077e7d54a9a32e542113cc28eadf00fa581c8e3d3c26e5c1b45a4e0900` |
| `src/x86decomp/relink.py` | `d401db042d4cc8300ccd4babd28cea400dca824d187a7caf0a1f3ead407fb296` |
| `src/x86decomp/image_match.py` | `a9c72f376532369da77440496a1ea07564da5071ef8e6108e29c58e33e96fcf4` |
| `src/x86decomp/convergence.py` | `2b943e9c8c2399089e1b8c2815c0de4cb1bcf0468c09e64a647fef3508922f74` |
| `tests/test_relink.py` | `580ca742c9d4f1d53de889f6f6bc5800e04147a31d86f0424a6d7a7252cefbb1` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
