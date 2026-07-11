# Evidence and Claims Commands

Provenance-bearing evidence records and evidence-linked claims with a deterministic verification gate.

## `evidence-add`

Add a provenance-bearing evidence record to a project.

```bash
x86decomp evidence-add PROJECT \
  --kind KIND --source SRC --locator LOC \
  --assertion ASSERT --independent-group GROUP \
  --file PATH --id ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `--kind` | yes | Evidence category from `EvidenceKind` enum |
| `--source` | yes | Source identifier (tool, author, document) |
| `--locator` | yes | Location string (RVA, file offset, section offset) |
| `--assertion` | yes | Assertion text describing what was observed |
| `--independent-group` | yes | Independent evidence group name (claims require >=3 distinct groups) |
| `--file` | no | Optional backing file path, hashed for integrity |
| `--id` | no | Explicit evidence ID; auto-generated if omitted |

### Evidence kinds

| Value | Description |
|---|---|
| `binary_bytes` | Raw bytes read directly from the analyzed binary |
| `static_analysis` | Facts derived from static analysis without execution |
| `dynamic_trace` | Observations captured while executing or emulating the target |
| `compiler_output` | Artifacts produced by compiling reconstructed source |
| `debug_symbol` | Information recovered from debug symbols (e.g. PDB data) |
| `external_document` | Facts sourced from external documentation or references |
| `human_review` | Assertions contributed by a human reviewer |

### Examples

```bash
# Binary bytes evidence
x86decomp evidence-add ./myproject \
  --kind binary_bytes \
  --source "PE section .text" \
  --locator "RVA 0x401000-0x401050" \
  --assertion "Function prologue: push ebp; mov ebp, esp; sub esp, 0x10" \
  --independent-group "text-section" \
  --file original.exe

# Static analysis evidence
x86decomp evidence-add ./myproject \
  --kind static_analysis \
  --source "Ghidra 11.0" \
  --locator "function FUN_00401000" \
  --assertion "Function takes three arguments: (int*, size_t, uint32_t)" \
  --independent-group "ghidra-analysis" \
  --id ghidra-401000-params

# Compiler output evidence
x86decomp evidence-add ./myproject \
  --kind compiler_output \
  --source "msvc-2019-x86-release" \
  --locator "compile 00401000" \
  --assertion "Candidate compiles to COFF with symbol _Func@12" \
  --independent-group "compiler-testing" \
  --file reports/compilation/401000.json
```

---

## `claim-create`

Create an evidence-linked project claim.

```bash
x86decomp claim-create PROJECT \
  --subject SUBJ --predicate PRED --object OBJ \
  --evidence ID... --id ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `--subject` | yes | Subject entity (e.g. function ID) |
| `--predicate` | yes | Predicate relation (e.g. `has_calling_convention`) |
| `--object` | yes | Object value (e.g. `cdecl`) |
| `--evidence` | no | Evidence IDs to link; repeatable |
| `--id` | no | Explicit claim ID; auto-generated if omitted |

### Verification gate

A claim reaches `verified` only when all conditions pass:

1. At least 3 evidence records
2. At least 3 independent groups
3. At least 2 distinct evidence kinds
4. All file-backed evidence hashes still match
5. No unresolved contradiction evidence

A claim with 2 records may become `corroborated`; 1 or zero remains `proposed`.

### Examples

```bash
# Create a calling convention claim
x86decomp claim-create ./myproject \
  --subject "pe-rva:00401000" \
  --predicate "has_calling_convention" \
  --object "cdecl" \
  --evidence ghidra-401000-params compiler-401000-cdecl analyst-401000-review

# Create without evidence (proposed state)
x86decomp claim-create ./myproject \
  --subject "pe-rva:00401000" \
  --predicate "has_original_name" \
  --object "ProcessInput" \
  --id claim-401000-name
```

---

## `claim-attach`

Attach an evidence record to an existing claim.

```bash
x86decomp claim-attach PROJECT CLAIM_ID EVIDENCE_ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `CLAIM_ID` | yes | Claim identifier |
| `EVIDENCE_ID` | yes | Evidence record identifier |

### Example

```bash
x86decomp claim-attach ./myproject claim-401000-name pdb-401000-symbol
```

---

## `claim-verify`

Evaluate whether a claim has sufficient independent evidence.

```bash
x86decomp claim-verify PROJECT CLAIM_ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `CLAIM_ID` | yes | Claim identifier |

The command returns the claim's current state (`proposed`, `corroborated`, `verified`, or `rejected`) and a breakdown of evidence counts, groups, kinds, and any contradictions.

### Example

```bash
x86decomp claim-verify ./myproject claim-401000-cconv
```

---

## `claim-contradict`

Attach contradictory evidence to a claim.

```bash
x86decomp claim-contradict PROJECT CLAIM_ID EVIDENCE_ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `CLAIM_ID` | yes | Claim identifier |
| `EVIDENCE_ID` | yes | Evidence record that contradicts the claim |

A claim with unresolved contradictions cannot reach `verified` state.

### Example

```bash
x86decomp claim-contradict ./myproject claim-401000-cconv dynamic-trace-401000-stdcall
```
