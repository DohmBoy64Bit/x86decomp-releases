# Reverse-engineering practice audit

## Strong practices — Verified or strongly supported

- Acquisition/evidence, parsing, analysis, interpretation, candidate generation, validation, and reporting are separated into distinct modules and claim levels.
- Input and artifact SHA-256 values, deterministic manifests, compiler commands, and evidence records support provenance and reproducibility.
- PE/COFF/PDB parsing uses bounded readers and explicit size/member/path limits. A deterministic malformed-input smoke run rejected 7,000 generated invalid samples through expected typed errors with no unexpected exception.
- Local-model output is explicitly untrusted and cannot be accepted by the byte-match lane without compiler, relocation, and raw-byte identity evidence.
- Unknown, blocked, unavailable, and partial states are modeled rather than converted to silent success.
- Matching-decompilation and functional-decompilation claims remain separate.
- Project backups reject traversal, links, devices, excessive members, per-member sizes, and total expansion limits.
- Reports, JSON schemas, JUnit, Markdown/HTML, and machine-readable command output support analyst and automation workflows.

## Limits and concerns

- COR-001 affects backup restoration on the earliest declared Python 3.11 patch releases.
- Complete parser correctness cannot be proven by static review and bounded malformed-input smoke testing; adversarial format fuzzing at scale remains desirable.
- Optional Ghidra, DynamoRIO, angr, compiler, native-execution, and model-server integrations were not fully exercised in this environment.
- Non-loopback service/model use is explicit but shifts authentication, TLS, network isolation, and data-disclosure controls to the operator; this is documented as an operational trust boundary rather than asserted as an exploitable defect.
- Command/reference documentation does not yet explain every analyst workflow, expected output, false-positive boundary, and safety implication (DOC-002).

## Suitability verdict

The project demonstrates sound evidence-governed reverse-engineering principles for an alpha-stage toolkit: provenance, claim separation, deterministic validation, bounded parsing, and explicit blocked states are stronger than typical ad-hoc tooling. Suitability for production or hostile-input use remains conditional on remediation of the verified findings, broader integration/fuzz testing, and operator-controlled sandboxing for external tools and native execution.
