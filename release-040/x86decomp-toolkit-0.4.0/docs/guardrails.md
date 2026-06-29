# Guardrails

## Factual guardrails

- Never call decompiler output original source.
- Never promote a plausible name/type without provenance.
- Never interpret missing static references as proof of no runtime access.
- Never collapse matching and functional status.
- Never call normalized equality raw equality.
- Never call finite dynamic tests or bounded SMT universal proof.
- Never suppress parser bounds errors, compiler failures, timeouts or contradictions.

## Execution guardrails

- Project initialization and parsing never execute the target.
- External compilers/linkers/MCP/DynamoRIO run only through explicit user commands.
- All subprocess commands are argument arrays with timeouts.
- Unknown binaries belong in an isolated VM/container with network and filesystem
  controls appropriate to the threat model.
- `drcov-run` is an execution boundary; authorization and environment isolation are
  the operator's explicit responsibility.

## Mutation guardrails

- Immutable evidence is never rewritten.
- PE patching writes a new output and supports original/function hash gates.
- Ghidra MCP reads reject probable mutations.
- MCP writes require allowlist, evidence, signed proposal and exact commit hash.
- Database/type changes retain provenance and conflict records.

## Path and artifact guardrails

- Imported artifacts reject symlinks and path traversal.
- Exact body ranges are retained; gaps are not treated as code.
- Atomic writes are used for canonical JSON where practical.
- Hash checks precede trust in copied evidence, toolchains and project input.

## AI guardrails

AI may propose source, names, types, tests and experiments. AI output:

- is not evidence;
- cannot mutate canonical state directly;
- must attach observed evidence;
- must pass all required validators;
- must preserve uncertainty and contradictions;
- must not fabricate a missing implementation or success report.
