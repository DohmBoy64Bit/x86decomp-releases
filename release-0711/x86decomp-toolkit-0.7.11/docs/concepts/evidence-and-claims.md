# Evidence and Claims

The evidence system is the governance backbone of x86decomp. Every assertion about a binary,
function, type, or compilation result must be backed by verifiable evidence that satisfies
a strict three-source independence gate.

## Evidence Kinds

Seven evidence types are available. Each records a specific category of observation.

| Kind | Value | Typical Source |
|---|---|---|
| `binary_bytes` | Raw bytes from the analyzed binary | `inspect-pe`, `coff-extract`, `pe` module |
| `static_analysis` | Facts from static analysis without execution | `disassemble`, `crosscheck-ghidra`, `metadata-scan` |
| `dynamic_trace` | Observations from execution or emulation | `dynamic-validate`, `drcov-parse`, Unicorn harness |
| `compiler_output` | Artifacts from compiling reconstructed source | `compile`, `compiler-lab` |
| `debug_symbol` | Information from debug symbols | `pdb-inspect`, PDB-based type recovery |
| `external_document` | Facts from external documentation or references | Ghidra export, MSVC documentation, manual analysis |
| `human_review` | Assertions by a human reviewer | Manual annotation, expert verification |

## Adding Evidence

```bash
x86decomp evidence-add --project ./myproject \
  --kind static_analysis \
  --source "Capstone disassembly at rva 0x401000" \
  --locator "pe:mybinary.exe:rva:0x401000:offset:64" \
  --assertion "Function 0x401000 is __stdcall with 12 bytes of stack arguments" \
  --independent-group "disassembly-analysis" \
  --file "./reports/disasm-401000.json"
```

Every evidence record requires:

- **kind**: One of the seven `EvidenceKind` values.
- **source**: A human-readable description of where the evidence came from.
- **locator**: A precise machine-readable locator (e.g., `pe:filename:rva:0x...:offset:N`).
- **assertion**: The specific claim this evidence supports.
- **independent_group**: A label identifying the analytical method or toolchain. Three
  **different** groups are required for verification.

!!! tip "Group naming"
    Use meaningful group names like `capstone-disasm`, `ghidra-decomp`, `msvc-pdb`,
    `dynamic-unicorn`. Avoid generic labels like `group1` or `analysis` — they make it
    harder to reason about independence.

### Optional File Attachment

The `--file` argument attaches a content-addressed copy to the evidence record:

```bash
x86decomp evidence-add --project . \
  --kind compiler_output \
  --source "Compiled with MSVC 2019 x86 Release" \
  --locator "compile:profile:msvc-2019-x86-rel:rva:0x401000" \
  --assertion "Compiled candidate.obj matches instruction stream" \
  --independent-group "msvc-2019-compilation" \
  --file "./build/candidates/candidate.obj"
```

The file is copied into `evidence/files/` with a content hash in the evidence record.

## Claims

A claim links a subject, predicate, and object, backed by one or more evidence records.

### Creating a Claim

```bash
x86decomp claim-create --project . \
  --subject "pe-rva:00401000" \
  --predicate "has_calling_convention" \
  --object "__stdcall" \
  --evidence ev-abc123def4567890 \
  --note "Observed ret 0Ch in epilogue"
```

### Attaching Evidence

```bash
x86decomp claim-attach --project . \
  --claim cl-0011223344556677 \
  --evidence ev-aaa111bbb222ccc3
```

## Verification Gate

A claim reaches `verified` only when ALL of the following hold:

1. **At least three evidence records** are attached.
2. **At least three independent groups** are represented among those records.
3. **At least two evidence kinds** are represented.
4. **No contradiction records** are attached.
5. **Every file-backed evidence hash** still matches.

### Running Verification

```bash
x86decomp claim-verify --project . --claim cl-0011223344556677
```

```json
{
  "claim_id": "cl-0011223344556677",
  "verification_status": "passed",
  "state": "verified",
  "evidence_count": 3,
  "independent_group_count": 3,
  "evidence_kind_count": 2,
  "failures": []
}
```

### Verification Failure

```json
{
  "claim_id": "cl-0011223344556677",
  "verification_status": "failed",
  "state": "corroborated",
  "evidence_count": 3,
  "independent_group_count": 2,
  "evidence_kind_count": 1,
  "failures": [
    "fewer than three independent evidence groups",
    "fewer than two evidence kinds"
  ]
}
```

!!! warning "Corroborated is not verified"
    A claim with 2+ evidence records but fewer than the full gate requirement enters
    `corroborated` state. This means "supported but not independently verified." Do not
    treat `corroborated` claims as established facts.

## Evidence Integrity Audits

Individual evidence records can be audited for file tampering:

```bash
# Evidence integrity is checked automatically during claim-verify.
# For standalone audit, use the EvidenceStore API:
```

The audit checks:
- That file-backed evidence still points to an existing file within the project root.
- That the file's SHA-256 matches the recorded digest.
- That the file path does not escape the project root.

## Contradictions

When evidence conflicts with a claim, add it as a contradiction:

```bash
x86decomp claim-contradict --project . \
  --claim cl-0011223344556677 \
  --evidence ev-contradicting-record
```

A claim with ANY contradiction records cannot be verified, regardless of supporting evidence
count. The contradiction must be resolved (the evidence record removed or the claim updated).

!!! danger "Do not delete contradiction evidence"
    Contradictions are evidence, not errors. If evidence genuinely contradicts a claim,
    the claim should be revised, not the evidence deleted. Deleting contradictory evidence
    undermines the governance model.

## Claim Lifecycle

```
                ┌─────────┐
                │PROPOSED │ ◄── Initial state, no evidence attached
                └────┬────┘
                     │ evidence attached (>= 2 records)
                     ▼
              ┌──────────────┐
              │CORROBORATED  │ ◄── Some evidence, insufficient for verification
              └──────┬───────┘
                     │
        ┌────────────┼────────────┐
        │ 3+ records │            │ contradiction added
        │ 3+ groups  │            │
        │ 2+ kinds   │            │
        │ no contra- │            │
        │ dictions   │            ▼
        ▼            │     ┌──────────┐
   ┌──────────┐      │     │ REJECTED │
   │ VERIFIED │      │     └──────────┘
   └──────────┘      │
                     │ evidence added to existing claim
                     ▼
              ┌──────────────┐
              │  (back to    │
              │  PROPOSED)   │
              └──────────────┘
```

Attaching evidence to an already-verified claim resets it to `proposed`, requiring
re-verification.

## Typical Evidence Strategy per Claim Type

| Claim Type | Evidence Kind 1 | Evidence Kind 2 | Evidence Kind 3 |
|---|---|---|---|
| Calling convention | `static_analysis` (disassembly) | `debug_symbol` (PDB) | `human_review` |
| Function boundaries | `binary_bytes` (PE) | `static_analysis` (Ghidra) | `external_document` (MAP) |
| Byte match | `compiler_output` (compile) | `binary_bytes` (COFF extract) | `static_analysis` (instruction compare) |
| Type layout | `debug_symbol` (PDB) | `static_analysis` (RTTI scan) | `human_review` |
| Behavior equivalence | `dynamic_trace` (validate) | `compiler_output` (compile) | `static_analysis` (symbolic) |

!!! tip "Don't over-evidence"
    Three independent sources are the minimum for verification, not a target. If you have
    one strong source and two weak ones, the claim verifies — but the verification gate
    does not assess evidence *quality*, only *count and diversity*.
