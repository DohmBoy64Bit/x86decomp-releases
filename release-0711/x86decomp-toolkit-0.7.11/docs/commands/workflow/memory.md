# Project Memory Commands

Evidence-linked project-memory ledger with hash-chained integrity and Markdown rendering.

## `memory-add`

Append an evidence-linked project-memory entry.

```bash
x86decomp memory-add PROJECT \
  --actor ACTOR --category CAT --summary TEXT \
  --details-json "{}" --evidence ID...
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `--actor` | yes | Actor name (e.g. `analyst-sean`, `compiler-lab`) |
| `--category` | yes | Entry category (e.g. `compiler-hypothesis`, `type-decision`, `blocker`) |
| `--summary` | yes | Concise summary of the event or decision |
| `--details-json` | no | Structured details as a JSON object (default: `"{}"`) |
| `--evidence` | no | Evidence IDs to link; repeatable |

The memory ledger is stored in `memory/events.jsonl`. Each entry contains a monotonically increasing sequence, UTC timestamp, actor, category, summary, structured details, evidence IDs, and hash-chain links to the previous entry.

### Examples

```bash
# Record a compiler hypothesis
x86decomp memory-add ./myproject \
  --actor "compiler-lab" \
  --category "compiler-hypothesis" \
  --summary "MSVC 2019 16.11.5 /O2 /Gy confirmed for .text section" \
  --details-json "{\"compiler\": \"msvc-2019\", \"version\": \"16.11.5\", \"flags\": [\"/O2\", \"/Gy\"]}" \
  --evidence compiler-lab-001

# Record a type layout decision
x86decomp memory-add ./myproject \
  --actor "analyst-sean" \
  --category "type-decision" \
  --summary "Accepted struct layout for Entity at 0x401200: 3 fields, 16 bytes" \
  --details-json "{\"struct\": \"Entity\", \"rva\": \"0x401200\", \"size\": 16, \"fields\": 3}"

# Record a blocker
x86decomp memory-add ./myproject \
  --actor "workflow-update" \
  --category "blocker" \
  --summary "pe-rva:00401000 blocked: unresolved indirect call through vtable" \
  --evidence ghidra-401000-indirect
```

---

## `memory-verify`

Verify the integrity of project-memory records.

```bash
x86decomp memory-verify PROJECT
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |

Verifies the hash chain across all memory entries. Reports any broken links, missing hashes, or tampered entries.

### Example

```bash
x86decomp memory-verify ./myproject
```

---

## `memory-render`

Render project memory as Markdown.

```bash
x86decomp memory-render PROJECT
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |

Generates `memory/PROJECT_MEMORY.md` from the events ledger. The rendered file is regenerated on each call; manual edits to the Markdown file are overwritten.

### Example

```bash
x86decomp memory-render ./myproject
```
