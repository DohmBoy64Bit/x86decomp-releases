# Project-memory protocol

## Ledger

`memory/events.jsonl` is authoritative. Each event contains:

- monotonically increasing `sequence`;
- UTC timestamp;
- actor;
- category;
- concise summary;
- structured details;
- evidence IDs;
- previous event hash;
- current event hash.

Changing any prior event breaks the chain. The chain detects accidental or casual
mutation; it is not a substitute for a cryptographic signature or trusted timestamp.

## What belongs in memory

- compiler family/version hypotheses and the experiments that changed them;
- function status transitions;
- accepted and rejected type layouts;
- target-specific linker behavior;
- unresolved indirect jumps;
- legal or security constraints;
- tool-version changes that alter analysis;
- decisions that future contributors would otherwise repeat.

## What does not belong in memory

- unsupported guesses presented as facts;
- raw binary blobs;
- secrets, credentials, or private user data;
- transient console noise;
- huge decompiler dumps already stored as artifacts.

## Rendering

`memory/PROJECT_MEMORY.md` is generated. Editing it does not alter the ledger and the
next render overwrites changes.
