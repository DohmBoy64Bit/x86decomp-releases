---
title: 'Example: static analysis and evidence project'
description: Inventory a native PE, supporting symbols, objects, libraries, and function
  artifacts without executing the target or claiming reconstructed source.
original_path: project-examples/static-analysis-evidence.html
---

<a id="model"></a>
<a id="static-analysis-evidence-flow-title"></a>
<a id="static-analysis-evidence-flow-desc"></a>
<a id="arrow-static-analysis-evidence"></a>
<a id="static-analysis-evidence-flow-caption"></a>
<a id="pack"></a>
<a id="inspect"></a>
<a id="ghidra"></a>
<a id="crosscheck"></a>
<a id="claims"></a>
<a id="database"></a>
<a id="deliverables"></a>
<a id="limits"></a>
<a id="source-basis"></a>

Section: Project examples

# Example: static analysis and evidence project

Inventory a native PE, supporting symbols, objects, libraries, and function artifacts without executing the target or claiming reconstructed source.

> **Example notation.** Paths and function identifiers are representative local names. Commands and options are exact v0.7.5 parser forms; target-specific hashes, addresses, profiles, reports, and passing outcomes must come from the actual project.

> **Classification.** This is a supporting analysis workflow, not an additional project mode. It can feed either matching or functional work.

**On this page**

1. [Evidence flow](#model)
2. [Seal inputs](#pack)
3. [Inspect formats](#inspect)
4. [Export Ghidra artifacts](#ghidra)
5. [Cross-check instructions](#crosscheck)
6. [Record evidence and claims](#claims)
7. [Ingest/query analysis](#database)
8. [Deliverables](#deliverables)
9. [Truth boundary](#limits)
10. [Source basis](#source-basis)

## Evidence flow

Static observations remain provenance-bearing and separate from operator decisions or reconstructed-source claims.Authorized files → Target pack → PE/PDB/MAP/COFF → Ghidra export → Disassembly check → Evidence claims → Analysis report

Authorized filesTarget packPE/PDB/MAP/COFFGhidra exportDisassembly checkEvidence claimsAnalysis report

Static observations remain provenance-bearing and separate from operator decisions or reconstructed-source claims.

```ascii-fallback
Authorized files → Target pack → PE/PDB/MAP/COFF → Ghidra export → Disassembly check → Evidence claims → Analysis report
```

1

## Create and verify the target pack

```
x86decomp target-pack-infer target.exe target-pack --pdb target.pdb --map target.map --object original/foo.obj --library original/runtime.lib --decisions decisions.json
x86decomp target-pack-verify target-pack
```

By default the pack copies regular-file artifacts and records their identities. `--reference-artifacts` stores references instead; use it only when that storage policy is deliberate.

2

## Inspect every available binary format

```
x86decomp inspect-pe target.exe
x86decomp pdb-inspect target.pdb --pe target.exe
x86decomp map-inspect target.map
x86decomp coff-inspect original/foo.obj
x86decomp lib-inspect original/runtime.lib
x86decomp metadata-scan target.exe --object original/foo.obj --map target.map --report reports/metadata.json
```

These parsers expose format metadata and bounded recoveries. Unsupported, malformed, packed, virtualized, encrypted, self-modifying, CLR, kernel-mode, or anti-analysis targets must not be silently treated as ordinary supported inputs.

3

## Export and import Ghidra function artifacts

```
x86decomp ghidra-export target.exe ghidra-projects TargetProject exports/ghidra --selector all --report reports/ghidra-export.json
x86decomp artifact-import project exports/ghidra/functions/pe-rva_00401230
x86decomp artifact-verify project/functions/pe-rva_00401230
```

The exporter records function body ranges, instructions, references, decompiler output, and p-code where available. Imported hashes protect the packet from unnoticed mutation; they do not authenticate Ghidra’s semantic interpretation.

4

## Independently disassemble and cross-check

```
$functionDir = "project/functions/pe-rva_00401230"
$rangeFile = (Get-Content "$functionDir/function.json" | ConvertFrom-Json).body_ranges[0].file
$rangePath = Join-Path $functionDir $rangeFile
x86decomp disassemble $rangePath --base 0x401230 --architecture x86 --report reports/disassembly/sub_00401230.json
x86decomp crosscheck-ghidra "$functionDir/instructions.jsonl" $rangePath --base 0x401230 --architecture x86 --report reports/crosscheck/sub_00401230.json
```

The cross-check compares an independent decoder’s view with the exported instruction stream. Agreement strengthens a bounded observation; disagreement is evidence to investigate, not something to normalize away.

5

## Store evidence before making claims

```
x86decomp evidence-add project --kind static_analysis --source ghidra --locator pe-rva:00401230 --assertion "Ghidra exported a function beginning at RVA 0x401230" --independent-group ghidra-export --file project/functions/pe-rva_00401230/function.json --id ev-ghidra-00401230
x86decomp evidence-add project --kind static_analysis --source independent-disassembler --locator pe-rva:00401230 --assertion "Independent disassembly starts at RVA 0x401230" --independent-group independent-disassembly --file reports/crosscheck/sub_00401230.json --id ev-crosscheck-00401230
x86decomp evidence-add project --kind human_review --source analyst --locator pe-rva:00401230 --assertion "Analyst reviewed the exported manifest and independent cross-check" --independent-group analyst-review --id ev-review-00401230
x86decomp claim-create project --subject pe-rva:00401230 --predicate has-entry-rva --object 0x401230 --evidence ev-ghidra-00401230 --evidence ev-crosscheck-00401230 --evidence ev-review-00401230 --id claim-entry-00401230
x86decomp claim-verify project claim-entry-00401230
```

The strict governance gate requires at least three evidence records, three independent groups, two evidence kinds, no unresolved contradiction records, and intact hashes for file-backed evidence. It does not parse the referenced report files to decide whether their substantive conclusions support the assertion, so only add each evidence record after review. Passing the gate records a governed `verified` state; it is not a mathematical guarantee that the proposition is true. Contradictory evidence can be attached with `claim-contradict`.

6

## Ingest artifacts and inspect type constraints

```
x86decomp db-ingest project/analysis.sqlite project/functions/pe-rva_00401230 --image-base 0x400000
x86decomp db-query project/analysis.sqlite "SELECT id, address_rva, name FROM entities WHERE kind = 'function' ORDER BY address_rva"
x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 calling_convention stdcall analyst-note --evidence-id ev-abi-1 --confidence 0.8
x86decomp db-constraint-conflicts project/analysis.sqlite pe-rva:00401230 calling_convention
```

Constraints retain provenance and confidence. A contradictory constraint cannot be accepted until conflicts are resolved; the database is not a truth oracle.

## Typical deliverables

- Verified target pack and artifact inventory.
- PE/PDB/MAP/COFF/library parser reports.
- Hash-verified per-function analysis packets.
- Independent disassembly cross-check reports.
- Provenance-bearing evidence, claims, and unresolved contradictions.
- An analysis database ready for ABI, matching, functional, or linker work.

## Truth boundary

Static analysis can establish observed bytes, metadata, references, and tool-derived hypotheses. It does not recover authenticated original source, prove decompiler types, or establish runtime equivalence without later validation.

## v0.7.5 source basis

> **Verification model.** Command syntax is checked against the live parser. The source files below are hashed from the current release; implementation and test rows are retained as independent truth boundaries.

| Evidence file | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/pe.py` | `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0` |
| `src/x86decomp/ghidra.py` | `98657d48a9d3ebb79eaf951aa8676ffd7ca696c2ba2f07fe8a5c4f0ad622c2b3` |
| `src/x86decomp/disassembly.py` | `cc86a46f8c8674a6e14304158bd1d2467fb09ccbb00778c116204b0a639638b3` |
| `src/x86decomp/evidence.py` | `de8befd97c8e7f0529f7c3c2750836f8f38fab52e26987cf390d725faad3ee1e` |
| `src/x86decomp/analysis_db.py` | `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad` |
| `tests/test_ghidra.py` | `1c9a934bad943761f8d9b6bc22509a054a8ead82747d2091d5f7e84c5682b88b` |


## Related examples

[Matching project

Open the source-verified workflow.](matching-project.md)[Functional project

Open the source-verified workflow.](functional-project.md)[Hybrid composition

Open the source-verified workflow.](hybrid-project.md)
