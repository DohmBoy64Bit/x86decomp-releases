# Feature parity and current surface — 0.7.11

This file records the shipped 0.7.11 surface. It is a release inventory, not a claim that every
optional external integration is available on every machine.

## Verified command surface

Runtime parser introspection registers 166 root commands. The canonical capability layer exposes
59 groups and 239 group/action routes. The generated command reference in
`docs/COMMAND_REFERENCE_0.7.11.md` and its JSON companion are checked against those live parsers by
the regression suite.

## Binary and reconstruction scope

The toolkit parses native Windows PE32 x86 and PE32+ x86-64 images without executing them. The
shipped parsers cover headers, sections, imports, exports, relocations, resources, debug records,
TLS, delay imports, load configuration, and architecture-specific metadata described in
`docs/supported-scope.md`. COFF objects and archives, MSF 7.0 PDB inventory, linker maps, bounded MSVC
metadata recovery, artifact import, evidence records, workflows, durable pipelines, and
reproducibility manifests are part of the same source release.

## Contracts and packaged assets

The repository contains 97 JSON schemas and three Ghidra scripts. The 24 compiler ground-truth
sources under `corpus/ground_truth_sources` are duplicated inside the Python package only so wheels
can use them at runtime; an exact byte-for-byte synchronization test prevents drift.

## Optional integrations

Capstone, Unicorn, Z3, angr, FastAPI/Uvicorn, LIEF, compilers, Ghidra, DynamoRIO, and MCP endpoints
remain optional. Unavailable tools are reported as unavailable or BLOCKED rather than silently
passing. Protocol capability is not the same as installed product identity; the authoritative
0.7.11 rule is in `docs/adapter-capabilities.md`.

## Acceptance boundaries

Local-model output is untrusted proposal text. Static parsing does not imply semantic equivalence,
and a successful compile does not imply a byte match. Claims advance only through the evidence,
ABI, differential, symbolic, integration, relocation-aware, or exact-byte gates appropriate to the
selected workflow mode.
