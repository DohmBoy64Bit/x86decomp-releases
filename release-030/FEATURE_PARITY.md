# Feature-parity matrix — 0.3.0

This matrix maps the agreed architecture and v0.3 production-hardening milestones to
concrete source, commands, contracts, and tests. “Implemented” means a real bounded
code path exists and fails explicitly when prerequisites are absent. It does not mean
arbitrary-binary correctness, original-source recovery, or universal equivalence.

## Regression compatibility

| Requirement | Implementation | Verification |
|---|---|---|
| Preserve 0.2.0 commands | v0.3 only adds subcommands; existing handlers remain | complete v0.2 regression suite included in full run |
| Preserve two mode schemas | `workflow.py` and existing workflow schema unchanged | `test_modes_and_db.py` |
| Preserve prior report fields | v0.3 additions are additive; e.g. `tls` remains linked-image TLS and `coff_tls` is separate | old tests plus v0.3 metadata tests |
| Preserve project/evidence memory | no migration required for 0.2 projects | project, evidence and memory tests |
| Explicit regression override | monotonic workflow with audited `--allow-regression` | workflow tests |

## Two independent modes

| Requirement | Implementation | Command/contract | Verification |
|---|---|---|---|
| Matching mode per function | independent matching state machine | `workflow-init`, `workflow-update`; `function-workflow.schema.json` | `test_modes_and_db.py` |
| Functional mode per function | independent functional state machine | same record, separate fields | `test_modes_and_db.py` |
| Independent progression | separate status, report and blocker maps | monotonic transitions | positive and invalid-transition tests |
| Source maturation | original bytes through accepted candidate | workflow source-stage field | workflow tests |
| Report-gated transitions | compiler/ABI/diff/dynamic/symbolic/integration reports are attached by kind | workflow and work queue | workflow/work-queue tests |

## PE ingestion and immutable evidence

| Requirement | Implementation | Verification |
|---|---|---|
| PE32/i386 | bounded parser in `pe32.py`/`pe.py` | valid/malformed fixtures |
| PE32+/AMD64 | bounded parser in `pe.py` | PE64 tests and real `lld-link` images |
| Sections, alignments and image layout | PE section model | parser and image tests |
| Imports, delay imports and exports | bounded directory parsers | parser contracts/tests |
| Resources | bounded recursive resource leaves | parser contracts |
| Base relocations | typed relocation records | parser, patch and image rebasing tests |
| Debug/CodeView/PDB references | debug directory, RSDS/NB records, bounded MSF 7.0, PDB GUID/age, TPI/IPI headers and DBI modules/sources/contributions | `pdb-inspect`; real Clang/LLD PDB identity test |
| TLS | template/index/callback directory for x86/x64 | parser/metadata tests |
| Load configuration and SafeSEH fields | architecture-aware load config | parser/metadata code paths |
| x64 runtime functions | exception-directory `.pdata` entries | real x64 RTTI/unwind test |
| Immutable original | project hash manifest and verification | tamper tests |
| Copied evidence | content-addressed evidence storage | evidence integrity tests |

## COFF, relocations and COMDAT

| Requirement | Implementation | Command/test |
|---|---|---|
| Classic COFF | `coff.py` 18-byte symbols | `coff-inspect`; synthetic and real Clang tests |
| Bigobj | ANON_OBJECT_HEADER_BIGOBJ and 20-byte symbols | minimal bigobj fixture |
| i386 relocations | ABSOLUTE, DIR16/32, REL16/32, DIR32NB, SECTION, SECREL, TOKEN, SECREL7 | parser/diff reports |
| AMD64 relocations | ADDR64/32/32NB, REL32 variants, SECTION, SECREL, SECREL7, TOKEN, PAIR, SSPAN32 | parser/diff reports |
| Relocation addends and widths | section-byte extraction with explicit width | COFF records and tests |
| Relocation overflow | `IMAGE_SCN_LNK_NRELOC_OVFL` first-record count | bounded parser path |
| Long names/string table | section and symbol string-table resolution | COFF parser tests |
| Auxiliary records | section/function definitions, weak externals, file and raw records | synthetic and real Clang weak test |
| Weak external aliases | storage class 105 and fallback characteristics | real i686 Windows-GNU Clang object test |
| COMDAT selection | all seven PE/COFF selection policies | `coff-comdat-resolve`; synthetic policy tests |
| Associative COMDAT | parent section retained in candidate/resolution | resolver contract |
| COMDAT conflicts | exact/same-size/noduplicate violations stay explicit | conflict tests |
| Multi-section synthetic objects | section/symbol/relocation writer | COFF/relink tests |
| COFF archives/static and import libraries | ar container, long names, both linker indexes, embedded objects and import records | `lib-inspect`; real `llvm-ar` and `lld-link` tests |

## Linker layout reconstruction

| Requirement | Implementation | Command/test |
|---|---|---|
| MSVC/LLD map parser | module, timestamp, preferred base, segments, publics, entry, contributions | `map-inspect`; map tests |
| Public object ownership | `Lib:Object` parsing and normalized object keys | map/layout tests |
| Map-to-PE section mapping | subsection base-name mapping with ordinal fallback provenance | layout report |
| Object correlation | supplied object hash, sections and COMDAT inventory | `layout-reconstruct` |
| Public-derived object order | first mapped public address per object | layout tests |
| Contribution confidence | object-order and byte-accurate-contribution flags are separate | layout schema/report tests |
| COMDAT-aware layout | resolver report embedded in layout report | layout tests |
| Non-claim | complete original layout remains false unless all evidence is supplied | report contract |

## Ghidra analysis and MCP

| Requirement | Implementation | Artifact/verification |
|---|---|---|
| Project manifest | `ExportProjectManifest.java` | program, sections, functions, symbols, types, metrics |
| Per-function packets | `ExportFunctionArtifacts.java` | exact ranges, bytes, instructions, references |
| Decompiled C and token tree | decompiler C plus recursive `ClangNode` JSONL | artifact export |
| Raw/high P-code | instruction P-code and high-function operations | JSONL/text artifacts |
| Discontiguous bodies | all Ghidra `AddressRange` records retained | range manifests |
| Queries | `QueryAnalysis.java` | refs, disassembly, function lookup |
| Independent decode | Capstone x86/x64, operands, branches and CFG | decoder tests |
| Ghidra cross-check | normalized instruction disagreement report | cross-check tests |
| MCP stdio and HTTP | JSON-RPC clients | mock protocol tests |
| Read-only default | mutation-like reads rejected | MCP policy tests |
| Transactional mutation | evidence/rationale proposal hash then exact commit | MCP mutation tests |

Live Ghidra execution remains installation dependent; the scripts are Java syntax
validated and an executable headless verification script is included.

## Microsoft C++ metadata, exceptions, TLS and initialization

| Requirement | Implementation | Verification |
|---|---|---|
| RTTI TypeDescriptor | x86/x64 pointer-sized descriptor and mangled name scans | real Clang/LLD C++ image |
| CompleteObjectLocator | x86 absolute and x64 image-relative layouts with self check | real C++ image |
| Class hierarchy/base descriptors | counts, arrays, PMD fields, attributes and nested hierarchy links | real multiple-class image |
| Vftable address points | validated locator pointer followed by executable function slots | real C++ image |
| Linker-map symbol enrichment | vtable slots, functions and handlers receive matching public names | metadata report |
| x64 runtime/unwind | UNWIND_INFO versions, flags, codes, stack sizes, handlers and chained records | real x64 image test |
| x86 SafeSEH | validated sorted handler RVA table | metadata parser path |
| x86 EH FuncInfo | conservative structurally plausible candidates | explicit candidate classification |
| Linked TLS | template bytes/hash, index RVA, zero fill and callbacks | `metadata-scan` |
| COFF TLS | `.tls$*` and `.CRT$XL*` sections, hashes and relocation symbols | real Clang TLS object test |
| Static initializers | `.CRT$X*` order, bytes/hash, relocations and target symbols | real C++ object test |
| Non-claim | no source-level EH/class/constructor completeness assertion | metadata report flag |

## Compiler/version ground-truth corpus

| Requirement | Implementation | Verification |
|---|---|---|
| Reproducible compiler identity | executable hash and complete version output | corpus records |
| Full command/environment provenance | argv, base/case/matrix flags and environment policy | corpus records |
| x86 and x64 | Windows MSVC-compatible target profiles | built-in manifest |
| C and C++ | separate compiler profiles with RTTI/EH options | built-in manifest |
| Optimization matrix | O0/O1/O2/Os | manifest schema and tests |
| Frame-pointer matrix | default and keep-frame-pointer | built-in manifest test |
| 24 source cases | scalar, CFG, switches, layout, aliasing, ABI, TLS, varargs, calls, vectorization and C++ metadata/EH cases | all sources compile for x86/x64 in release verification |
| User-owned historical compilers | arbitrary registered executable/profile; no redistribution | toolchain registry |
| Corpus hash verification | source and output hash checks | `corpus-verify` tests |
| Cross-version comparison | aligned case/variant object bytes, sections and symbols | `corpus-compare` test |
| Non-claim | no compiler identity or semantic equivalence inferred from bytes | comparison report flag |

## Matching decompilation and whole-image reconstruction

| Requirement | Implementation | Command/test |
|---|---|---|
| Compiler profiles/cache/labs | isolated argv execution, hashes, cache and flag matrix | compiler tests |
| PE function ↔ COFF symbol | symbol extent, relocations, instruction and CFG comparison | `diff-function`; tests |
| Raw vs normalized distinction | separate byte and relocation-normalized classifications | diff report |
| ABI observations | x86 calling conventions and x64 register/stack model | `abi-check`; tests |
| Hybrid build | exact-byte assembly fallback and candidate trees | real make/assembler test |
| PE patch | input/function hash gates and checksum regeneration | patch tests |
| Manifest relink | exact linker invocation with tool/object/output provenance | real `lld-link` test |
| Layout profile | exact reference hash, architecture, base, entry, alignment, section order/layout | `image-profile` |
| Whole-image raw match | every file byte | `image-match` tests |
| Explicit normalization | checksum, optional timestamp/certificate/debug ranges and extra named ranges | checksum and real CodeView debug tests |
| Candidate rebasing | supported base relocation types only | image matcher path |
| Per-section reports | layout and byte differences | image matcher tests |
| Non-claim | profile-normalized match is not raw identity or semantic proof | report classification |
| objdiff/decomp.me adapters | local explicit manifests/packets; no hidden upload | adapter tests |

## Functional and symbolic validation

| Requirement | Implementation | Verification |
|---|---|---|
| Concrete function harness | Unicorn register/stack/memory state | equal/different tests |
| Deterministic external calls | explicit summaries | dynamic contract/tests |
| Built-in symbolic engine | Capstone/Z3 bounded paths and counterexamples | symbolic tests |
| Secondary angr backend | comparative path execution | real angr tests |
| Symbolic memory regions | named, sized, aligned, byte-addressable symbolic objects | alias test |
| Symbolic region bases | finite alias slots and stride | alias test |
| Alias relationships | equal, distinct, disjoint and may-alias | harness schema and counterexample test |
| Memory observations | selected region/offset/size plus registers | alias report |
| Completion accounting | final/active/deadended/errored/truncated counts | alias report |
| Runtime coverage | DynamoRIO drcov runner/parser | parser tests; live tool external |
| Integration runner | explicit consent/wrapper, streams, exit and file observations | integration tests |
| Non-claim | finite model/scenario scopes and universal-equivalence=false | all validator reports |

## Authorized regression test bundles

| Requirement | Implementation | Verification |
|---|---|---|
| Deterministic bundle creation | `create_test_bundle` with generated hashes | round-trip test |
| Authorization declaration | mandatory non-empty affirmative statement | rejection test |
| Safe ZIP extraction | rejects absolute/parent/backslash/drive paths, duplicates and symlinks | traversal tests |
| Expansion controls | member, total and compression-ratio limits | implementation bounds |
| Artifact integrity | optional manifest hashes become mandatory checks when present | mismatch test |
| Static PE/PDB/metadata inspection | primary/reference/candidate images and GUID/age-correlated PDB | real PDB bundle test |
| Static COFF/COMDAT/archive/map/layout | supplied objects, `.lib`/`.a` archives and map | bundle analysis pipeline and real archive test |
| Whole-image pair | reference/candidate plus optional profile | bundle analysis pipeline |
| No execution | report records `supplied_code_executed=false` | round-trip/inspection tests |
| Contracts and template | test-bundle input/report schemas and example | contract validation |

## Evidence, work queue, memory and service

| Requirement | Implementation | Verification |
|---|---|---|
| Three-source claim gate | count, independent groups, kind diversity, hashes and contradictions | evidence tests |
| Append-only memory | hash-chained JSONL and rendered Markdown | tamper tests |
| Global analysis database | SQLite entities, references, ABI/type constraints and conflicts | DB tests |
| Validator-gated work queue | proposals accepted only after required validators | queue tests |
| AI not evidence | skill, AGENTS and workflow contracts | policy tests/review |
| Benchmarks | decomposed discovery/matching/functional/intervention metrics | benchmark tests |
| Read-only service | FastAPI project/function/report/work views | optional service module |
| Detailed skill | `skills/x86decomp/SKILL.md` version 3.0.0 | frontmatter/contract validation |

## External validation boundaries

The release includes executable adapters and procedures but cannot locally prove every
operator-specific installation. Live Ghidra, DynamoRIO target execution, a real
operator-selected `objdiff` version, historical proprietary MSVC versions, and real
commercial target layouts require those exact external tools/artifacts. The release
record distinguishes unavailable integrations from executed tests.

## Deliberate non-claims

Version 0.3 is a production-oriented bounded framework, not an omniscient decompiler.
It does not claim generic recovery of erased source facts, complete CodeView record semantics,
every original object boundary or linker-generated byte, arbitrary indirect control
flow, safe execution of unknown native code, complete compiler-specific C++ EH
semantics, or all-input equivalence. Those remain target-specific evidence and
engineering problems rather than hidden placeholders.
