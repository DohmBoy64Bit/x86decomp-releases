# Supported scope and non-goals

## Implemented formats

- Native Windows PE32 i386.
- Native Windows PE32+ AMD64.
- Classic COFF and Microsoft bigobj i386/AMD64 relocatable objects.
- COFF archives (`.lib`/`.a`), linker symbol members, long-name tables, import-object
  records and embedded COFF members.
- MSF 7.0 PDB container inventory, PDB identity, TPI/IPI headers, DBI modules,
  section contributions and source-file mappings.
- MSVC/LLD map files with bounded public-symbol and section-contribution parsing.
- Function artifacts with one or more discontiguous address ranges.
- C, C++, assembly, binary, relocatable-object and executable compiler outputs.
- Authorized, non-executing ZIP test bundles containing declared binary evidence.

## Matching mode support

Implemented:

- compiler profile execution, output caching and flag matrices;
- user-owned historical toolchain registry with executable/version hashing;
- PE-function to COFF-symbol extraction;
- classic/bigobj symbols, auxiliary records, weak externals, relocation overflow and
  broader i386/AMD64 relocation classifications;
- COMDAT selection, association and conflict inventories;
- raw, relocation-normalized and normalized instruction/CFG comparison;
- static ABI observations;
- exact-byte assembly fallback;
- synthetic single- and multi-section COFF construction with declared relocations and
  COMDAT metadata;
- COFF archive and import-library inventory;
- map-derived object ordering and section-contribution evidence;
- target-specific whole-image profiles, optional rebasing and declared nondeterministic
  field normalization;
- PE patching with checksum update;
- manifest-driven full linker invocation and optional whole-image comparison;
- manifest-driven objdiff CLI execution with pinned inputs and captured output.

The toolkit does not generically infer every consumed relocation, original object
boundary, archive-resolution decision, ICF/LTCG transformation, linker script, section
padding choice or proprietary compiler behavior. Those remain target-specific
reconstruction work and must be supported by evidence.

## Windows C++ metadata support

Implemented bounded inventory and correlation for:

- x86/x64 MSVC RTTI type descriptors, complete-object locators, class hierarchies,
  base descriptors and PMD layouts;
- candidate vtables and RTTI relationships;
- x64 runtime-function and unwind records, chained unwind and handler references;
- x86 SafeSEH and conservative exception FuncInfo candidates;
- linked-image and COFF TLS templates/callback evidence;
- `.CRT$X*` static-initializer contributions;
- PDB GUID/age correlation with PE RSDS data;
- PDB DBI modules, section contributions and source-file mappings.

Full CodeView type/symbol decoding, arbitrary compiler-family RTTI, complete exception
semantics and original C++ source organization are not claimed.

## Functional mode support

Implemented:

- concrete Unicorn function harnesses;
- deterministic external-call summaries;
- observed register/memory comparisons;
- built-in bounded Capstone/Z3 symbolic comparison;
- optional angr bounded comparison with declared symbolic memory regions and finite
  alias relations;
- DynamoRIO drcov coverage capture/parsing;
- explicit integration scenario execution comparing exit code, streams and declared
  files;
- validator-gated integration status.

Finite tests and bounded symbolic models are not universal semantic proof. Windows API,
heap, threading, exceptions, callbacks, devices, timing and complete process state
require a target-specific integration environment supplied by the project.

## Explicitly unsupported as automatic guarantees

- Recovery of original comments, local names, macros, formatting or translation units.
- Guaranteed original class, template, inline or source-file organization.
- Correct static analysis of arbitrary packed, virtualized or self-modifying code.
- Automatic bypass of DRM, anti-debugging or access controls.
- Safe host execution of unknown targets.
- Resolution of every indirect branch, exception edge or dynamic code target.
- Universal all-input program equivalence.
- Generic byte-identical whole-image reconstruction without target-specific evidence.
- Complete PDB/CodeView semantic reconstruction from every producer/version.

Unsupported behavior must fail or be labeled unknown; it must never be represented by
a success-shaped placeholder.

## Version 0.4 operational scope

Implemented production-control capabilities:

- evidence-driven target packs and grounded project-template generation;
- schema-v3 transactional project state with migration, integrity checks, deterministic
  backup/restore, repair, snapshots, leases, and content-store garbage collection;
- durable idempotent pipelines with retries, cancellation, heartbeat/stale recovery,
  hash-keyed inputs, materialized outputs, and output-tamper invalidation;
- resource-bounded local workers and declared Docker/Podman container workers;
- compiler-worker provenance and target-specific linker-reconstruction plans;
- generated differential harness contracts from explicit ABI/pointer declarations;
- whole-image convergence reports and release-gate aggregation;
- reproducibility manifests, source-tree audits, SBOM generation, and pip-audit adapter;
- deterministic generated source corpora with exact generator/seed/source hashes;
- read-only operational service snapshots;
- explicit compatibility contracts for 0.2 and 0.3.1 release surfaces.

A local resource-bounded worker is not a malware sandbox. Container isolation depends on
the selected runtime, daemon, image, mount, user, and network policies. Production
acceptance remains target- and environment-specific and requires live adapter evidence.
