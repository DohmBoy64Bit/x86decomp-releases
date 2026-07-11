# Command-system audit

## Complete inventory

- Root commands: **166**
- All argparse parser nodes: **405**
- Canonical groups: **59**
- Canonical routes: **239**
- Parser nodes with help: **405/405**
- Parser nodes with long descriptions: **75/405**

Every command, option/argument metadata record, default, choice set, help string, description flag, documentation mention, example match, and safety-flag indicator is in `COMMAND_INVENTORY.csv`. Every canonical group/action route and owner is in `CANONICAL_ROUTE_INVENTORY.csv`. These CSV files are the required one-row-per-command matrices; no command is omitted from the inventory.

## Structure and dispatch

The root parser combines legacy/direct commands with a canonical 59-group/239-route capability plane. Grouped subparsers improve discoverability for large subsystems (governance, reconstruction, native, assembly, local LLM). Root invalid-command output is mechanically correct but very long because argparse prints 166 choices. Missing required-file behavior produced structured JSON and exit status 2.

## Help, errors, and scriptability

- `x86decomp --help`: exit 0; all root commands displayed.
- `x86decomp commands`: machine-readable command inventory generated successfully.
- Invalid command: exit 2 with argparse usage/error.
- Missing input file: exit 2 with a concise structured error.
- `x86decomp --version`: exit 2; no version action exists (UX-001).
- Canonical plan-only routes are explicitly described as non-mutating in the generated reference.

Stable exit-code contracts beyond the executed error paths were not inferred. Commands capable of writes, subprocesses, network access, native execution, or project mutation were reviewed statically and through existing tests rather than invoked on user data.

## Documentation coverage

- Root commands explicitly documented: **23/166**
- Root commands with examples: **23/166**
- All parser nodes explicitly documented: **31/405**
- All parser nodes with matched examples: **30/405**
- Canonical routes documented: **8/239**
- Canonical routes with examples: **7/239**

Built-in help coverage is complete; long-form argument/output/error/example/use-case/safety coverage is not. This distinction is the basis of DOC-002.

## Overall assessment

Command registration and basic help are coherent and mechanically synchronized. The primary weaknesses are breadth, sparse long-form workflow documentation, no version flag, and verbose root error usage. No implemented-but-unregistered root command was verified, and the live parser counts match release inventory claims.
