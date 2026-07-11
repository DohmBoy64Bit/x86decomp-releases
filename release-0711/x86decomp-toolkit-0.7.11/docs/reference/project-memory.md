# Project-memory protocol

Every project maintains an append-only evidence-linked ledger.

## Ledger format

`memory/events.jsonl` is authoritative. Each event contains:

| Field | Description |
|---|---|
| `sequence` | Monotonically increasing integer |
| `timestamp` | UTC timestamp |
| `actor` | Who recorded the event |
| `category` | Classification tag |
| `summary` | Concise human-readable description |
| `details` | Structured data |
| `evidence_ids` | Linked evidence records |
| `previous_hash` | Hash of the preceding event |
| `current_hash` | Hash of this event |

Changing any prior event breaks the chain. The chain detects accidental or casual
mutation; it is not a substitute for a cryptographic signature or trusted timestamp.

## What belongs in memory

* Compiler family/version hypotheses and the experiments that changed them
* Function status transitions
* Accepted and rejected type layouts
* Target-specific linker behavior
* Unresolved indirect jumps
* Legal or security constraints
* Tool-version changes that alter analysis
* Decisions that future contributors would otherwise repeat

## What does NOT belong in memory

!!! danger "Excluded content"
    * Unsupported guesses presented as facts
    * Raw binary blobs
    * Secrets, credentials, or private user data
    * Transient console noise
    * Huge decompiler dumps already stored as artifacts

## Rendering

`memory/PROJECT_MEMORY.md` is generated from the ledger. Editing it does not alter the
ledger and the next render overwrites changes.

## Commands

```bash
# Add an event
x86decomp memory-add --project . \
  --actor analyst \
  --category compiler-hypothesis \
  --summary "MSVC 2019 19.29.30133 confirmed via entry-point fingerprint" \
  --evidence ev-abc123

# Verify chain integrity
x86decomp memory-verify --project .

# Generate PROJECT_MEMORY.md
x86decomp memory-render --project .
```
