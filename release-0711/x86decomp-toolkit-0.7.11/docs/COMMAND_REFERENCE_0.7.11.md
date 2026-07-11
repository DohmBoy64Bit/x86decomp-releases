# Command reference — 0.7.11

This document is generated from the live `argparse` tree. It covers every root command and canonical route without executing operational handlers.

- Root commands: **166**
- Canonical groups: **59**
- Canonical routes: **239**
- Total parser nodes: **405**

Every example below uses `--help`; it is concrete, valid, non-destructive, and exits with status 0.

## `x86decomp abi`

Canonical abi commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical abi commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp abi --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi [-h] [--project PROJECT] [--actor ACTOR]
                     {compare,export,recover,shim,show,verify} ...

Canonical abi commands implemented by the current capability subsystem.

positional arguments:
  {compare,export,recover,shim,show,verify}
    compare             compare command
    export              export command
    recover             recover command
    shim                shim command
    show                show command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp abi compare`

Execute the `compare` action in the canonical `abi` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compare` action in the canonical `abi` capability group.

Example:

```console
$ x86decomp abi compare --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi compare [-h] left_id right_id

positional arguments:
  left_id
  right_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp abi export`

Execute the `export` action in the canonical `abi` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export` action in the canonical `abi` capability group.

Example:

```console
$ x86decomp abi export --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi export [-h] contract_id output

positional arguments:
  contract_id
  output

options:
  -h, --help   show this help message and exit
```

### `x86decomp abi recover`

Execute the `recover` action in the canonical `abi` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `recover` action in the canonical `abi` capability group.

Example:

```console
$ x86decomp abi recover --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON
                             subject_kind subject_id architecture
                             contract_json

positional arguments:
  subject_kind
  subject_id
  architecture
  contract_json

options:
  -h, --help            show this help message and exit
  --evidence-json EVIDENCE_JSON
```

### `x86decomp abi shim`

Execute the `shim` action in the canonical `abi` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `shim` action in the canonical `abi` capability group.

Example:

```console
$ x86decomp abi shim --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path

positional arguments:
  contract_id
  source_path

options:
  -h, --help   show this help message and exit
  --kind KIND
```

### `x86decomp abi show`

Execute the `show` action in the canonical `abi` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `abi` capability group.

Example:

```console
$ x86decomp abi show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi show [-h] contract_id

positional arguments:
  contract_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp abi verify`

Execute the `verify` action in the canonical `abi` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `abi` capability group.

Example:

```console
$ x86decomp abi verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi verify [-h] contract_id

positional arguments:
  contract_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp abi-check`

validate observed behavior against an ABI contract

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: validate observed behavior against an ABI contract

Example:

```console
$ x86decomp abi-check --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp abi-check [-h] [--base BASE] [--report REPORT] code contract

positional arguments:
  code
  contract

options:
  -h, --help       show this help message and exit
  --base BASE
  --report REPORT
```

## `x86decomp angr-validate`

compare binary functions with the optional angr backend

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compare binary functions with the optional angr backend

Example:

```console
$ x86decomp angr-validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp angr-validate [-h] [--architecture {x86,x86_64}]
                               [--input-register INPUT_REGISTER]
                               [--stack-argument-words STACK_ARGUMENT_WORDS]
                               [--output-register OUTPUT_REGISTER]
                               [--max-steps MAX_STEPS] [--max-paths MAX_PATHS]
                               [--report REPORT]
                               target candidate

positional arguments:
  target
  candidate

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --input-register INPUT_REGISTER
  --stack-argument-words STACK_ARGUMENT_WORDS
  --output-register OUTPUT_REGISTER
  --max-steps MAX_STEPS
  --max-paths MAX_PATHS
  --report REPORT
```

## `x86decomp artifact-import`

import a validated exported function artifact

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: import a validated exported function artifact

Example:

```console
$ x86decomp artifact-import --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp artifact-import [-h] project exported_dir

positional arguments:
  project
  exported_dir

options:
  -h, --help    show this help message and exit
```

## `x86decomp artifact-verify`

verify an exported function artifact and its hashes

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify an exported function artifact and its hashes

Example:

```console
$ x86decomp artifact-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp artifact-verify [-h] artifact_dir

positional arguments:
  artifact_dir

options:
  -h, --help    show this help message and exit
```

## `x86decomp asm`

Canonical asm commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical asm commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp asm --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm [-h] [--project PROJECT] [--actor ACTOR]
                     {annotate,batch,list,materialize,report,verify-roundtrip} ...

Canonical asm commands implemented by the current capability subsystem.

positional arguments:
  {annotate,batch,list,materialize,report,verify-roundtrip}
    annotate            annotate command
    batch               batch command
    list                list command
    materialize         materialize command
    report              report command
    verify-roundtrip    verify-roundtrip command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp asm annotate`

Execute the `annotate` action in the canonical `asm` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `annotate` action in the canonical `asm` capability group.

Example:

```console
$ x86decomp asm annotate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm annotate [-h] --symbol SYMBOL --rva RVA
                              [--image-base IMAGE_BASE]
                              [--architecture {x86,x86_64}]
                              source output

positional arguments:
  source
  output

options:
  -h, --help            show this help message and exit
  --symbol SYMBOL
  --rva RVA
  --image-base IMAGE_BASE
  --architecture {x86,x86_64}
```

### `x86decomp asm batch`

Execute the `batch` action in the canonical `asm` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `batch` action in the canonical `asm` capability group.

Example:

```console
$ x86decomp asm batch --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm batch [-h] [--format {bytes,annotated,mnemonic}]
                           [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                           [--image-base IMAGE_BASE]
                           manifest output

positional arguments:
  manifest
  output

options:
  -h, --help            show this help message and exit
  --format {bytes,annotated,mnemonic}
  --assembler-command-json ASSEMBLER_COMMAND_JSON
  --image-base IMAGE_BASE
```

### `x86decomp asm list`

Execute the `list` action in the canonical `asm` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `asm` capability group.

Example:

```console
$ x86decomp asm list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp asm materialize`

Execute the `materialize` action in the canonical `asm` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `materialize` action in the canonical `asm` capability group.

Example:

```console
$ x86decomp asm materialize --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm materialize [-h] [--input-kind {bytes,assembly}]
                                 --symbol SYMBOL --rva RVA
                                 [--image-base IMAGE_BASE]
                                 [--architecture {x86,x86_64}]
                                 --symbol-map SYMBOL_MAP
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--timeout TIMEOUT] [--report REPORT]
                                 input output_source output_object
                                 output_resolved

positional arguments:
  input
  output_source
  output_object
  output_resolved

options:
  -h, --help            show this help message and exit
  --input-kind {bytes,assembly}
  --symbol SYMBOL
  --rva RVA
  --image-base IMAGE_BASE
  --architecture {x86,x86_64}
  --symbol-map SYMBOL_MAP
  --assembler-command-json ASSEMBLER_COMMAND_JSON
  --timeout TIMEOUT
  --report REPORT
```

### `x86decomp asm report`

Execute the `report` action in the canonical `asm` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `report` action in the canonical `asm` capability group.

Example:

```console
$ x86decomp asm report --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm report [-h] run_id

positional arguments:
  run_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp asm verify-roundtrip`

Execute the `verify-roundtrip` action in the canonical `asm` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify-roundtrip` action in the canonical `asm` capability group.

Example:

```console
$ x86decomp asm verify-roundtrip --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asm verify-roundtrip [-h] --symbol SYMBOL --rva RVA
                                      [--image-base IMAGE_BASE]
                                      [--architecture {x86,x86_64}]
                                      --symbol-map SYMBOL_MAP
                                      [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                      [--timeout TIMEOUT] [--report REPORT]
                                      source original output_object
                                      output_resolved

positional arguments:
  source
  original
  output_object
  output_resolved

options:
  -h, --help            show this help message and exit
  --symbol SYMBOL
  --rva RVA
  --image-base IMAGE_BASE
  --architecture {x86,x86_64}
  --symbol-map SYMBOL_MAP
  --assembler-command-json ASSEMBLER_COMMAND_JSON
  --timeout TIMEOUT
  --report REPORT
```

## `x86decomp asset`

Canonical asset commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical asset commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp asset --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asset [-h] [--project PROJECT] [--actor ACTOR]
                       {inventory} ...

Canonical asset commands implemented by the current capability subsystem.

positional arguments:
  {inventory}
    inventory        inventory command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp asset inventory`

Execute the `inventory` action in the canonical `asset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inventory` action in the canonical `asset` capability group.

Example:

```console
$ x86decomp asset inventory --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp asset inventory [-h] [--output OUTPUT] root

positional arguments:
  root

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp benchmark-run`

run a declared benchmark corpus and emit measured results

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run a declared benchmark corpus and emit measured results

Example:

```console
$ x86decomp benchmark-run --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp benchmark-run [-h] [--report REPORT] manifest

positional arguments:
  manifest

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp boundary`

Canonical boundary commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical boundary commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp boundary --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp boundary [-h] [--project PROJECT] [--actor ACTOR]
                          {audit,audit-project,export-ghidra-fixes,list,show} ...

Canonical boundary commands implemented by the current capability subsystem.

positional arguments:
  {audit,audit-project,export-ghidra-fixes,list,show}
    audit               audit command
    audit-project       audit-project command
    export-ghidra-fixes
                        export-ghidra-fixes command
    list                list command
    show                show command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp boundary audit`

Execute the `audit` action in the canonical `boundary` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `audit` action in the canonical `boundary` capability group.

Example:

```console
$ x86decomp boundary audit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA]
                                inventory_json

positional arguments:
  inventory_json

options:
  -h, --help            show this help message and exit
  --text-end-rva TEXT_END_RVA
```

### `x86decomp boundary audit-project`

Execute the `audit-project` action in the canonical `boundary` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `audit-project` action in the canonical `boundary` capability group.

Example:

```console
$ x86decomp boundary audit-project --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp boundary audit-project [-h] artifact_project binary

positional arguments:
  artifact_project
  binary

options:
  -h, --help        show this help message and exit
```

### `x86decomp boundary export-ghidra-fixes`

Execute the `export-ghidra-fixes` action in the canonical `boundary` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export-ghidra-fixes` action in the canonical `boundary` capability group.

Example:

```console
$ x86decomp boundary export-ghidra-fixes --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp boundary export-ghidra-fixes [-h] output

positional arguments:
  output

options:
  -h, --help  show this help message and exit
```

### `x86decomp boundary list`

Execute the `list` action in the canonical `boundary` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `boundary` capability group.

Example:

```console
$ x86decomp boundary list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]

options:
  -h, --help            show this help message and exit
  --classification CLASSIFICATION
```

### `x86decomp boundary show`

Execute the `show` action in the canonical `boundary` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `boundary` capability group.

Example:

```console
$ x86decomp boundary show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp boundary show [-h] function_id

positional arguments:
  function_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp build`

Canonical build commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical build commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp build --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build [-h] [--project PROJECT] [--actor ACTOR]
                       {add-target,add-variant,compare-modes,create,generate,matrix,show,validate} ...

Canonical build commands implemented by the current capability subsystem.

positional arguments:
  {add-target,add-variant,compare-modes,create,generate,matrix,show,validate}
    add-target          add-target command
    add-variant         add-variant command
    compare-modes       compare-modes command
    create              create command
    generate            generate command
    matrix              matrix command
    show                show command
    validate            validate command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp build add-target`

Execute the `add-target` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add-target` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build add-target --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build add-target [-h] [--kind KIND]
                                  [--output-name OUTPUT_NAME]
                                  [--sources-json SOURCES_JSON]
                                  [--dependencies-json DEPENDENCIES_JSON]
                                  build_id name

positional arguments:
  build_id
  name

options:
  -h, --help            show this help message and exit
  --kind KIND
  --output-name OUTPUT_NAME
  --sources-json SOURCES_JSON
  --dependencies-json DEPENDENCIES_JSON
```

### `x86decomp build add-variant`

Execute the `add-variant` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add-variant` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build add-variant --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build add-variant [-h] --compiler COMPILER --linker LINKER
                                   [--compile-flags-json COMPILE_FLAGS_JSON]
                                   [--link-flags-json LINK_FLAGS_JSON]
                                   [--environment-json ENVIRONMENT_JSON]
                                   target_id name

positional arguments:
  target_id
  name

options:
  -h, --help            show this help message and exit
  --compiler COMPILER
  --linker LINKER
  --compile-flags-json COMPILE_FLAGS_JSON
  --link-flags-json LINK_FLAGS_JSON
  --environment-json ENVIRONMENT_JSON
```

### `x86decomp build compare-modes`

Execute the `compare-modes` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compare-modes` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build compare-modes --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build compare-modes [-h]
                                     historical_build_id portable_build_id

positional arguments:
  historical_build_id
  portable_build_id

options:
  -h, --help           show this help message and exit
```

### `x86decomp build create`

Execute the `create` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build create [-h] --mode MODE [--generator GENERATOR]
                              [--output-root OUTPUT_ROOT]
                              [--metadata-json METADATA_JSON]
                              name

positional arguments:
  name

options:
  -h, --help            show this help message and exit
  --mode MODE
  --generator GENERATOR
  --output-root OUTPUT_ROOT
  --metadata-json METADATA_JSON
```

### `x86decomp build generate`

Execute the `generate` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `generate` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build generate [-h] [--output-root OUTPUT_ROOT] build_id

positional arguments:
  build_id

options:
  -h, --help            show this help message and exit
  --output-root OUTPUT_ROOT
```

### `x86decomp build matrix`

Execute the `matrix` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `matrix` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build matrix --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build matrix [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp build show`

Execute the `show` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build show [-h] build_id

positional arguments:
  build_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp build validate`

Execute the `validate` action in the canonical `build` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `validate` action in the canonical `build` capability group.

Example:

```console
$ x86decomp build validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp build validate [-h] [--variant-id VARIANT_ID] target_id

positional arguments:
  target_id

options:
  -h, --help            show this help message and exit
  --variant-id VARIANT_ID
```

## `x86decomp campaign`

Canonical campaign commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical campaign commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp campaign --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign [-h] [--project PROJECT] [--actor ACTOR]
                          {branch,create,list,pause,plan,resume,snapshot,start,status,stop} ...

Canonical campaign commands implemented by the current capability subsystem.

positional arguments:
  {branch,create,list,pause,plan,resume,snapshot,start,status,stop}
    branch              branch command
    create              create command
    list                list command
    pause               pause command
    plan                plan command
    resume              resume command
    snapshot            snapshot command
    start               start command
    status              status command
    stop                stop command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp campaign branch`

Execute the `branch` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `branch` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign branch --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign branch [-h] [--parent PARENT] campaign_id name

positional arguments:
  campaign_id
  name

options:
  -h, --help       show this help message and exit
  --parent PARENT
```

### `x86decomp campaign create`

Execute the `create` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign create [-h] [--budget-json BUDGET_JSON]
                                 [--policy-json POLICY_JSON]
                                 goal

positional arguments:
  goal

options:
  -h, --help            show this help message and exit
  --budget-json BUDGET_JSON
  --policy-json POLICY_JSON
```

### `x86decomp campaign list`

Execute the `list` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp campaign pause`

Execute the `pause` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `pause` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign pause --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign pause [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp campaign plan`

Execute the `plan` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `plan` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign plan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign plan [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp campaign resume`

Execute the `resume` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `resume` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign resume --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign resume [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp campaign snapshot`

Execute the `snapshot` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `snapshot` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign snapshot --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign snapshot [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp campaign start`

Execute the `start` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `start` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign start --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign start [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp campaign status`

Execute the `status` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `status` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign status --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign status [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

### `x86decomp campaign stop`

Execute the `stop` action in the canonical `campaign` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `stop` action in the canonical `campaign` capability group.

Example:

```console
$ x86decomp campaign stop --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp campaign stop [-h] campaign_id

positional arguments:
  campaign_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp candidate`

Canonical candidate commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical candidate commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp candidate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate [-h] [--project PROJECT] [--actor ACTOR]
                           {add-file,compare,create,evaluate,list,promote,search,show,transition} ...

Canonical candidate commands implemented by the current capability subsystem.

positional arguments:
  {add-file,compare,create,evaluate,list,promote,search,show,transition}
    add-file            add-file command
    compare             compare command
    create              create command
    evaluate            evaluate command
    list                list command
    promote             promote command
    search              emit an ordered candidate-search plan only; no source
                        edits or promotions are performed
    show                show command
    transition          transition command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp candidate add-file`

Execute the `add-file` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add-file` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate add-file --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate add-file [-h] candidate_id source relative_path

positional arguments:
  candidate_id
  source
  relative_path

options:
  -h, --help     show this help message and exit
```

### `x86decomp candidate compare`

Execute the `compare` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compare` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate compare --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate compare [-h] left_id right_id

positional arguments:
  left_id
  right_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp candidate create`

Execute the `create` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID]
                                  [--parent PARENT]
                                  [--objective-json OBJECTIVE_JSON]
                                  branch_name

positional arguments:
  branch_name

options:
  -h, --help            show this help message and exit
  --campaign-id CAMPAIGN_ID
  --parent PARENT
  --objective-json OBJECTIVE_JSON
```

### `x86decomp candidate evaluate`

Execute the `evaluate` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `evaluate` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate evaluate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate evaluate [-h] [--value VALUE]
                                    [--details-json DETAILS_JSON]
                                    candidate_id metric status

positional arguments:
  candidate_id
  metric
  status

options:
  -h, --help            show this help message and exit
  --value VALUE
  --details-json DETAILS_JSON
```

### `x86decomp candidate list`

Execute the `list` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]

options:
  -h, --help            show this help message and exit
  --campaign-id CAMPAIGN_ID
```

### `x86decomp candidate promote`

Execute the `promote` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `promote` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate promote --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate promote [-h] --candidate CANDIDATE --report REPORT
                                   [--stage STAGE] [--update-workflow]
                                   [--update-build] [--overwrite]
                                   function_id

positional arguments:
  function_id

options:
  -h, --help            show this help message and exit
  --candidate CANDIDATE
  --report REPORT
  --stage STAGE
  --update-workflow
  --update-build
  --overwrite
```

### `x86decomp candidate search`

Execute the `search` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `search` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate search --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate search [-h] [--phase PHASE] [--output OUTPUT]

emit an ordered candidate-search plan only; no source edits or promotions are
performed

options:
  -h, --help       show this help message and exit
  --phase PHASE
  --output OUTPUT
```

### `x86decomp candidate show`

Execute the `show` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate show [-h] candidate_id

positional arguments:
  candidate_id

options:
  -h, --help    show this help message and exit
```

### `x86decomp candidate transition`

Execute the `transition` action in the canonical `candidate` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `transition` action in the canonical `candidate` capability group.

Example:

```console
$ x86decomp candidate transition --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp candidate transition [-h] --reason REASON candidate_id state

positional arguments:
  candidate_id
  state

options:
  -h, --help       show this help message and exit
  --reason REASON
```

## `x86decomp capsule`

Canonical capsule commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical capsule commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp capsule --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp capsule [-h] [--project PROJECT] [--actor ACTOR]
                         {create,inspect,reproduce,verify} ...

Canonical capsule commands implemented by the current capability subsystem.

positional arguments:
  {create,inspect,reproduce,verify}
    create              create command
    inspect             inspect command
    reproduce           reproduce command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp capsule create`

Execute the `create` action in the canonical `capsule` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `capsule` capability group.

Example:

```console
$ x86decomp capsule create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp capsule create [-h] [--include INCLUDE]
                                [--external-json EXTERNAL_JSON]
                                name output

positional arguments:
  name
  output

options:
  -h, --help            show this help message and exit
  --include INCLUDE
  --external-json EXTERNAL_JSON
```

### `x86decomp capsule inspect`

Execute the `inspect` action in the canonical `capsule` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inspect` action in the canonical `capsule` capability group.

Example:

```console
$ x86decomp capsule inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp capsule inspect [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

### `x86decomp capsule reproduce`

Execute the `reproduce` action in the canonical `capsule` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `reproduce` action in the canonical `capsule` capability group.

Example:

```console
$ x86decomp capsule reproduce --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp capsule reproduce [-h] path destination

positional arguments:
  path
  destination

options:
  -h, --help   show this help message and exit
```

### `x86decomp capsule verify`

Execute the `verify` action in the canonical `capsule` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `capsule` capability group.

Example:

```console
$ x86decomp capsule verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp capsule verify [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

## `x86decomp changeset`

Canonical changeset commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical changeset commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp changeset --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset [-h] [--project PROJECT] [--actor ACTOR]
                           {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify} ...

Canonical changeset commands implemented by the current capability subsystem.

positional arguments:
  {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify}
    add-operation       add-operation command
    apply               apply command
    conflicts           conflicts command
    create              create command
    export              export command
    inspect             inspect command
    merge               merge command
    rebase              rebase command
    show                show command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp changeset add-operation`

Execute the `add-operation` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add-operation` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset add-operation --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset add-operation [-h] changeset_id operation_json

positional arguments:
  changeset_id
  operation_json

options:
  -h, --help      show this help message and exit
```

### `x86decomp changeset apply`

Execute the `apply` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `apply` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset apply --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset apply [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

### `x86decomp changeset conflicts`

Execute the `conflicts` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `conflicts` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset conflicts --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset conflicts [-h] changeset_id

positional arguments:
  changeset_id

options:
  -h, --help    show this help message and exit
```

### `x86decomp changeset create`

Execute the `create` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH]
                                  name

positional arguments:
  name

options:
  -h, --help            show this help message and exit
  --base-audit-hash BASE_AUDIT_HASH
```

### `x86decomp changeset export`

Execute the `export` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset export --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output

positional arguments:
  output

options:
  -h, --help            show this help message and exit
  --after-hash AFTER_HASH
```

### `x86decomp changeset inspect`

Execute the `inspect` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inspect` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset inspect [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

### `x86decomp changeset merge`

Execute the `merge` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `merge` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset merge --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset merge [-h] left_id right_id name

positional arguments:
  left_id
  right_id
  name

options:
  -h, --help  show this help message and exit
```

### `x86decomp changeset rebase`

Execute the `rebase` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `rebase` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset rebase --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset rebase [-h] changeset_id new_base_hash

positional arguments:
  changeset_id
  new_base_hash

options:
  -h, --help     show this help message and exit
```

### `x86decomp changeset show`

Execute the `show` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset show [-h] changeset_id

positional arguments:
  changeset_id

options:
  -h, --help    show this help message and exit
```

### `x86decomp changeset verify`

Execute the `verify` action in the canonical `changeset` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `changeset` capability group.

Example:

```console
$ x86decomp changeset verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp changeset verify [-h] changeset_id

positional arguments:
  changeset_id

options:
  -h, --help    show this help message and exit
```

## `x86decomp claim-attach`

attach an evidence record to an existing claim

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: attach an evidence record to an existing claim

Example:

```console
$ x86decomp claim-attach --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp claim-attach [-h] project claim_id evidence_id

positional arguments:
  project
  claim_id
  evidence_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp claim-contradict`

attach contradictory evidence to a claim

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: attach contradictory evidence to a claim

Example:

```console
$ x86decomp claim-contradict --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp claim-contradict [-h] project claim_id evidence_id

positional arguments:
  project
  claim_id
  evidence_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp claim-create`

create an evidence-linked project claim

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create an evidence-linked project claim

Example:

```console
$ x86decomp claim-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE
                              --object OBJECT_VALUE [--evidence EVIDENCE]
                              [--id ID]
                              project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --subject SUBJECT
  --predicate PREDICATE
  --object OBJECT_VALUE
  --evidence EVIDENCE
  --id ID
```

## `x86decomp claim-verify`

evaluate whether a claim has sufficient independent evidence

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: evaluate whether a claim has sufficient independent evidence

Example:

```console
$ x86decomp claim-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp claim-verify [-h] project claim_id

positional arguments:
  project
  claim_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp class`

Canonical class commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical class commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp class --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp class [-h] [--project PROJECT] [--actor ACTOR] {scaffold} ...

Canonical class commands implemented by the current capability subsystem.

positional arguments:
  {scaffold}
    scaffold         scaffold command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp class scaffold`

Execute the `scaffold` action in the canonical `class` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `scaffold` action in the canonical `class` capability group.

Example:

```console
$ x86decomp class scaffold --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp class scaffold [-h] [--headers HEADERS] vtable_report output

positional arguments:
  vtable_report
  output

options:
  -h, --help         show this help message and exit
  --headers HEADERS
```

## `x86decomp coff-comdat-resolve`

resolve COMDAT groups across COFF objects

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: resolve COMDAT groups across COFF objects

Example:

```console
$ x86decomp coff-comdat-resolve --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp coff-comdat-resolve [-h] [--report REPORT]
                                     objects [objects ...]

positional arguments:
  objects

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp coff-extract`

extract one symbol payload from a COFF object

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: extract one symbol payload from a COFF object

Example:

```console
$ x86decomp coff-extract --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp coff-extract [-h] [--size SIZE] object symbol output

positional arguments:
  object
  symbol
  output

options:
  -h, --help   show this help message and exit
  --size SIZE
```

## `x86decomp coff-inspect`

inspect COFF object metadata, symbols, and relocations

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: inspect COFF object metadata, symbols, and relocations

Example:

```console
$ x86decomp coff-inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp coff-inspect [-h] object

positional arguments:
  object

options:
  -h, --help  show this help message and exit
```

## `x86decomp coff-synthesize`

create a synthetic COFF object from code and relocations

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a synthetic COFF object from code and relocations

Example:

```console
$ x86decomp coff-synthesize --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]
                                 [--relocations RELOCATIONS]
                                 code symbol output

positional arguments:
  code
  symbol
  output

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --relocations RELOCATIONS
```

## `x86decomp commands`

list canonical capability routes and implementation owners

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: list canonical capability routes and implementation owners

Example:

```console
$ x86decomp commands --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp commands [-h]
                          [--group {abi,asm,asset,boundary,build,campaign,candidate,capsule,changeset,class,compiler-rules,consensus,counterexample,decompiler,diff,family,function,game-pattern,ghidra-mcp,graph,headers,hybrid,hypothesis,image-text,library,llm,loop,match,mod,module,pattern,pe,playability,plugin,progress,project,proof,provenance,regression,release-policy,reloc,review,runtime,runtime-analysis,script-port,security,source,source-map,source-stage,staging,subsystem,tests,text-swap,toolchain,triage,type,vtable,windows,worker}]
                          [--owner {governance,reconstruction,native,assembly}]

options:
  -h, --help            show this help message and exit
  --group {abi,asm,asset,boundary,build,campaign,candidate,capsule,changeset,class,compiler-rules,consensus,counterexample,decompiler,diff,family,function,game-pattern,ghidra-mcp,graph,headers,hybrid,hypothesis,image-text,library,llm,loop,match,mod,module,pattern,pe,playability,plugin,progress,project,proof,provenance,regression,release-policy,reloc,review,runtime,runtime-analysis,script-port,security,source,source-map,source-stage,staging,subsystem,tests,text-swap,toolchain,triage,type,vtable,windows,worker}
  --owner {governance,reconstruction,native,assembly}
```

## `x86decomp compile`

compile one source file under a declared compiler profile

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compile one source file under a declared compiler profile

Example:

```console
$ x86decomp compile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compile [-h] [--report REPORT] [--extra-arg EXTRA_ARG]
                         [--cache CACHE]
                         profile source output

positional arguments:
  profile
  source
  output

options:
  -h, --help            show this help message and exit
  --report REPORT
  --extra-arg EXTRA_ARG
  --cache CACHE
```

## `x86decomp compile-worker`

run a bounded local or containerized compilation worker

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run a bounded local or containerized compilation worker

Example:

```console
$ x86decomp compile-worker --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compile-worker [-h] [--isolation {local_bounded,container}]
                                [--container-image CONTAINER_IMAGE]
                                [--cache CACHE] [--report REPORT]
                                profile source output

positional arguments:
  profile
  source
  output

options:
  -h, --help            show this help message and exit
  --isolation {local_bounded,container}
  --container-image CONTAINER_IMAGE
  --cache CACHE
  --report REPORT
```

## `x86decomp compiler-lab`

run a compiler experiment matrix from a lab manifest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run a compiler experiment matrix from a lab manifest

Example:

```console
$ x86decomp compiler-lab --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compiler-lab [-h] [--report REPORT] lab

positional arguments:
  lab

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp compiler-rules`

Canonical compiler-rules commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical compiler-rules commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp compiler-rules --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compiler-rules [-h] [--project PROJECT] [--actor ACTOR]
                                {compare-flags,learn-rule,rule-report} ...

Canonical compiler-rules commands implemented by the current capability
subsystem.

positional arguments:
  {compare-flags,learn-rule,rule-report}
    compare-flags       compare-flags command
    learn-rule          learn-rule command
    rule-report         rule-report command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp compiler-rules compare-flags`

Execute the `compare-flags` action in the canonical `compiler-rules` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compare-flags` action in the canonical `compiler-rules` capability group.

Example:

```console
$ x86decomp compiler-rules compare-flags --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compiler-rules compare-flags [-h] [--output OUTPUT]
                                              reports [reports ...]

positional arguments:
  reports

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp compiler-rules learn-rule`

Execute the `learn-rule` action in the canonical `compiler-rules` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `learn-rule` action in the canonical `compiler-rules` capability group.

Example:

```console
$ x86decomp compiler-rules learn-rule --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compiler-rules learn-rule [-h] rule_id observations output

positional arguments:
  rule_id
  observations
  output

options:
  -h, --help    show this help message and exit
```

### `x86decomp compiler-rules rule-report`

Execute the `rule-report` action in the canonical `compiler-rules` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `rule-report` action in the canonical `compiler-rules` capability group.

Example:

```console
$ x86decomp compiler-rules rule-report --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp compiler-rules rule-report [-h] [--output OUTPUT]
                                            rules [rules ...]

positional arguments:
  rules

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp consensus`

Canonical consensus commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical consensus commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp consensus --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp consensus [-h] [--project PROJECT] [--actor ACTOR]
                           {conflicts,explain,record,resolve,scan} ...

Canonical consensus commands implemented by the current capability subsystem.

positional arguments:
  {conflicts,explain,record,resolve,scan}
    conflicts           conflicts command
    explain             explain command
    record              record command
    resolve             resolve command
    scan                scan command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp consensus conflicts`

Execute the `conflicts` action in the canonical `consensus` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `conflicts` action in the canonical `consensus` capability group.

Example:

```console
$ x86decomp consensus conflicts --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp consensus conflicts [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp consensus explain`

Execute the `explain` action in the canonical `consensus` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `explain` action in the canonical `consensus` capability group.

Example:

```console
$ x86decomp consensus explain --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp consensus explain [-h] subject_kind subject_id property_name

positional arguments:
  subject_kind
  subject_id
  property_name

options:
  -h, --help     show this help message and exit
```

### `x86decomp consensus record`

Execute the `record` action in the canonical `consensus` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `record` action in the canonical `consensus` capability group.

Example:

```console
$ x86decomp consensus record --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp consensus record [-h] --adapter ADAPTER
                                  --adapter-version ADAPTER_VERSION
                                  --evidence-id EVIDENCE_ID --group GROUP
                                  [--confidence CONFIDENCE]
                                  subject_kind subject_id property_name
                                  value_json

positional arguments:
  subject_kind
  subject_id
  property_name
  value_json

options:
  -h, --help            show this help message and exit
  --adapter ADAPTER
  --adapter-version ADAPTER_VERSION
  --evidence-id EVIDENCE_ID
  --group GROUP
  --confidence CONFIDENCE
```

### `x86decomp consensus resolve`

Execute the `resolve` action in the canonical `consensus` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `resolve` action in the canonical `consensus` capability group.

Example:

```console
$ x86decomp consensus resolve --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE
                                   [--lock]
                                   subject_kind subject_id property_name
                                   selected_value_json

positional arguments:
  subject_kind
  subject_id
  property_name
  selected_value_json

options:
  -h, --help            show this help message and exit
  --method METHOD
  --rationale RATIONALE
  --lock
```

### `x86decomp consensus scan`

Execute the `scan` action in the canonical `consensus` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `scan` action in the canonical `consensus` capability group.

Example:

```console
$ x86decomp consensus scan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND]
                                [--subject-id SUBJECT_ID]

options:
  -h, --help            show this help message and exit
  --subject-kind SUBJECT_KIND
  --subject-id SUBJECT_ID
```

## `x86decomp content-put`

store content by cryptographic digest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: store content by cryptographic digest

Example:

```console
$ x86decomp content-put --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp content-put [-h] [--media-type MEDIA_TYPE]
                             [--reference REFERENCE] [--kind KIND]
                             [--owner OWNER]
                             store file

positional arguments:
  store
  file

options:
  -h, --help            show this help message and exit
  --media-type MEDIA_TYPE
  --reference REFERENCE
  --kind KIND
  --owner OWNER
```

## `x86decomp content-verify`

verify content-addressed storage integrity

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify content-addressed storage integrity

Example:

```console
$ x86decomp content-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp content-verify [-h] store

positional arguments:
  store

options:
  -h, --help  show this help message and exit
```

## `x86decomp convergence-analyze`

measure image convergence and append history

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: measure image convergence and append history

Example:

```console
$ x86decomp convergence-analyze --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp convergence-analyze [-h] [--profile PROFILE]
                                     [--previous PREVIOUS] [--report REPORT]
                                     [--history HISTORY]
                                     reference candidate

positional arguments:
  reference
  candidate

options:
  -h, --help           show this help message and exit
  --profile PROFILE
  --previous PREVIOUS
  --report REPORT
  --history HISTORY
```

## `x86decomp corpus-build`

build a reproducible compiler/version ground-truth corpus

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: build a reproducible compiler/version ground-truth corpus

Example:

```console
$ x86decomp corpus-build --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp corpus-build [-h] [--report REPORT] manifest output_directory

positional arguments:
  manifest
  output_directory

options:
  -h, --help        show this help message and exit
  --report REPORT
```

## `x86decomp corpus-compare`

compare compiler/version ground-truth corpus reports

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compare compiler/version ground-truth corpus reports

Example:

```console
$ x86decomp corpus-compare --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp corpus-compare [-h] [--report REPORT] reports [reports ...]

positional arguments:
  reports

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp corpus-create-manifest`

create the bundled compiler ground-truth manifest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create the bundled compiler ground-truth manifest

Example:

```console
$ x86decomp corpus-create-manifest --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp corpus-create-manifest [-h] repository output

positional arguments:
  repository
  output

options:
  -h, --help  show this help message and exit
```

## `x86decomp corpus-generate`

generate a deterministic parameterized C/C++ source corpus

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: generate a deterministic parameterized C/C++ source corpus

Example:

```console
$ x86decomp corpus-generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY]
                                 [--seed SEED] [--c-only] [--cpp-only]
                                 [--report REPORT]
                                 output_directory

positional arguments:
  output_directory

options:
  -h, --help            show this help message and exit
  --cases-per-family CASES_PER_FAMILY
  --seed SEED
  --c-only
  --cpp-only
  --report REPORT
```

## `x86decomp corpus-generated-verify`

verify generated corpus source identities

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify generated corpus source identities

Example:

```console
$ x86decomp corpus-generated-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp corpus-generated-verify [-h] report

positional arguments:
  report

options:
  -h, --help  show this help message and exit
```

## `x86decomp corpus-verify`

verify source and output hashes in a ground-truth corpus

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify source and output hashes in a ground-truth corpus

Example:

```console
$ x86decomp corpus-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp corpus-verify [-h] report

positional arguments:
  report

options:
  -h, --help  show this help message and exit
```

## `x86decomp counterexample`

Canonical counterexample commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical counterexample commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp counterexample --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp counterexample [-h] [--project PROJECT] [--actor ACTOR]
                                {add,list,promote,show} ...

Canonical counterexample commands implemented by the current capability
subsystem.

positional arguments:
  {add,list,promote,show}
    add                 add command
    list                list command
    promote             promote command
    show                show command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp counterexample add`

Execute the `add` action in the canonical `counterexample` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add` action in the canonical `counterexample` capability group.

Example:

```console
$ x86decomp counterexample add --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON
                                    [--provenance-json PROVENANCE_JSON]
                                    scope_kind scope_id payload

positional arguments:
  scope_kind
  scope_id
  payload

options:
  -h, --help            show this help message and exit
  --predicate-json PREDICATE_JSON
  --provenance-json PROVENANCE_JSON
```

### `x86decomp counterexample list`

Execute the `list` action in the canonical `counterexample` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `counterexample` capability group.

Example:

```console
$ x86decomp counterexample list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp counterexample list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp counterexample promote`

Execute the `promote` action in the canonical `counterexample` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `promote` action in the canonical `counterexample` capability group.

Example:

```console
$ x86decomp counterexample promote --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp counterexample promote [-h] counterexample_id destination

positional arguments:
  counterexample_id
  destination

options:
  -h, --help         show this help message and exit
```

### `x86decomp counterexample show`

Execute the `show` action in the canonical `counterexample` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `counterexample` capability group.

Example:

```console
$ x86decomp counterexample show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp counterexample show [-h] counterexample_id

positional arguments:
  counterexample_id

options:
  -h, --help         show this help message and exit
```

## `x86decomp cpp-recover`

recover bounded C++ metadata and class relationships

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: recover bounded C++ metadata and class relationships

Example:

```console
$ x86decomp cpp-recover --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp cpp-recover [-h] [--metadata-report METADATA_REPORT]
                             [--object OBJECT] [--map MAP] [--report REPORT]
                             pe

positional arguments:
  pe

options:
  -h, --help            show this help message and exit
  --metadata-report METADATA_REPORT
  --object OBJECT
  --map MAP
  --report REPORT
```

## `x86decomp crosscheck-ghidra`

compare toolkit disassembly with a Ghidra export

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compare toolkit disassembly with a Ghidra export

Example:

```console
$ x86decomp crosscheck-ghidra --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp crosscheck-ghidra [-h] --base BASE
                                   [--architecture {x86,x86_64}]
                                   [--report REPORT]
                                   instructions_jsonl code

positional arguments:
  instructions_jsonl
  code

options:
  -h, --help            show this help message and exit
  --base BASE
  --architecture {x86,x86_64}
  --report REPORT
```

## `x86decomp db-constraint-accept`

accept a selected analysis constraint

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: accept a selected analysis constraint

Example:

```console
$ x86decomp db-constraint-accept --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp db-constraint-accept [-h] database constraint_id

positional arguments:
  database
  constraint_id

options:
  -h, --help     show this help message and exit
```

## `x86decomp db-constraint-add`

add a provenance-bearing analysis constraint

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: add a provenance-bearing analysis constraint

Example:

```console
$ x86decomp db-constraint-add --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID]
                                   [--confidence CONFIDENCE]
                                   database subject relation object_value
                                   provenance

positional arguments:
  database
  subject
  relation
  object_value
  provenance

options:
  -h, --help            show this help message and exit
  --evidence-id EVIDENCE_ID
  --confidence CONFIDENCE
```

## `x86decomp db-constraint-conflicts`

list conflicting constraints for a subject and relation

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: list conflicting constraints for a subject and relation

Example:

```console
$ x86decomp db-constraint-conflicts --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp db-constraint-conflicts [-h] database subject relation

positional arguments:
  database
  subject
  relation

options:
  -h, --help  show this help message and exit
```

## `x86decomp db-ingest`

ingest an analysis artifact into the project database

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: ingest an analysis artifact into the project database

Example:

```console
$ x86decomp db-ingest --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact

positional arguments:
  database
  artifact

options:
  -h, --help            show this help message and exit
  --image-base IMAGE_BASE
```

## `x86decomp db-query`

run a bounded read-only SQL query against the analysis database

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run a bounded read-only SQL query against the analysis database

Example:

```console
$ x86decomp db-query --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON]
                          database sql

positional arguments:
  database
  sql

options:
  -h, --help            show this help message and exit
  --parameters-json PARAMETERS_JSON
```

## `x86decomp decompiler`

Canonical decompiler commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical decompiler commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp decompiler --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp decompiler [-h] [--project PROJECT] [--actor ACTOR]
                            {cleanup} ...

Canonical decompiler commands implemented by the current capability subsystem.

positional arguments:
  {cleanup}
    cleanup          cleanup command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp decompiler cleanup`

Execute the `cleanup` action in the canonical `decompiler` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `cleanup` action in the canonical `decompiler` capability group.

Example:

```console
$ x86decomp decompiler cleanup --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp decompiler cleanup [-h] [--compiler COMPILER]
                                    [--language LANGUAGE] [--locals-at-top]
                                    input_file output

positional arguments:
  input_file
  output

options:
  -h, --help           show this help message and exit
  --compiler COMPILER
  --language LANGUAGE
  --locals-at-top
```

## `x86decomp decompme-pack`

create a decomp.me-compatible packet from an artifact

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a decomp.me-compatible packet from an artifact

Example:

```console
$ x86decomp decompme-pack --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp decompme-pack [-h] [--overwrite] artifact_dir output_dir

positional arguments:
  artifact_dir
  output_dir

options:
  -h, --help    show this help message and exit
  --overwrite
```

## `x86decomp dependency-audit`

run an installed pip-audit adapter and preserve exact findings

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run an installed pip-audit adapter and preserve exact findings

Example:

```console
$ x86decomp dependency-audit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp dependency-audit [-h] [--executable EXECUTABLE]
                                  [--timeout TIMEOUT] [--report REPORT]

options:
  -h, --help            show this help message and exit
  --executable EXECUTABLE
  --timeout TIMEOUT
  --report REPORT
```

## `x86decomp diff`

Canonical diff commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical diff commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp diff --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp diff [-h] [--project PROJECT] [--actor ACTOR] {explain} ...

Canonical diff commands implemented by the current capability subsystem.

positional arguments:
  {explain}
    explain          explain command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp diff explain`

Execute the `explain` action in the canonical `diff` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `explain` action in the canonical `diff` capability group.

Example:

```console
$ x86decomp diff explain --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp diff explain [-h] [--source SOURCE] [--output OUTPUT]
                              diff_report

positional arguments:
  diff_report

options:
  -h, --help       show this help message and exit
  --source SOURCE
  --output OUTPUT
```

## `x86decomp diff-bytes`

compare two files byte-for-byte with bounded mismatch reporting

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compare two files byte-for-byte with bounded mismatch reporting

Example:

```console
$ x86decomp diff-bytes --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp diff-bytes [-h] [--report REPORT]
                            [--max-mismatches MAX_MISMATCHES]
                            target candidate

positional arguments:
  target
  candidate

options:
  -h, --help            show this help message and exit
  --report REPORT
  --max-mismatches MAX_MISMATCHES
```

## `x86decomp diff-function`

compare a linked PE function to a COFF symbol

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compare a linked PE function to a COFF symbol

Example:

```console
$ x86decomp diff-function --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol

positional arguments:
  pe
  rva
  size
  coff
  symbol

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp disassemble`

decode bounded machine-code instructions

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: decode bounded machine-code instructions

Example:

```console
$ x86decomp disassemble --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp disassemble [-h] [--base BASE] [--architecture {x86,x86_64}]
                             [--report REPORT]
                             code

positional arguments:
  code

options:
  -h, --help            show this help message and exit
  --base BASE
  --architecture {x86,x86_64}
  --report REPORT
```

## `x86decomp drcov-parse`

parse a DynamoRIO drcov coverage log

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: parse a DynamoRIO drcov coverage log

Example:

```console
$ x86decomp drcov-parse --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp drcov-parse [-h] log

positional arguments:
  log

options:
  -h, --help  show this help message and exit
```

## `x86decomp drcov-run`

run a target under DynamoRIO drcov tracing

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run a target under DynamoRIO drcov tracing

Example:

```console
$ x86decomp drcov-run --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp drcov-run [-h] [--drrun DRRUN] [--program-arg PROGRAM_ARG]
                           [--timeout TIMEOUT] [--report REPORT]
                           executable output_directory

positional arguments:
  executable
  output_directory

options:
  -h, --help            show this help message and exit
  --drrun DRRUN
  --program-arg PROGRAM_ARG
  --timeout TIMEOUT
  --report REPORT
```

## `x86decomp dynamic-validate`

differentially execute and compare two binaries

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: differentially execute and compare two binaries

Example:

```console
$ x86decomp dynamic-validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp dynamic-validate [-h] [--target-base TARGET_BASE]
                                  [--candidate-base CANDIDATE_BASE]
                                  [--report REPORT]
                                  target candidate harness

positional arguments:
  target
  candidate
  harness

options:
  -h, --help            show this help message and exit
  --target-base TARGET_BASE
  --candidate-base CANDIDATE_BASE
  --report REPORT
```

## `x86decomp evidence-add`

add a provenance-bearing evidence record to a project

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: add a provenance-bearing evidence record to a project

Example:

```console
$ x86decomp evidence-add --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp evidence-add [-h]
                              --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
                              --source SOURCE --locator LOCATOR
                              --assertion ASSERTION
                              --independent-group INDEPENDENT_GROUP
                              [--file FILE] [--id ID]
                              project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
  --source SOURCE
  --locator LOCATOR
  --assertion ASSERTION
  --independent-group INDEPENDENT_GROUP
  --file FILE
  --id ID
```

## `x86decomp family`

Canonical family commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical family commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp family --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp family [-h] [--project PROJECT] [--actor ACTOR]
                        {add,correlate,create,report} ...

Canonical family commands implemented by the current capability subsystem.

positional arguments:
  {add,correlate,create,report}
    add                 add command
    correlate           correlate command
    create              create command
    report              report command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp family add`

Execute the `add` action in the canonical `family` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add` action in the canonical `family` capability group.

Example:

```console
$ x86decomp family add --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp family add [-h] [--metadata-json METADATA_JSON]
                            family_id label path

positional arguments:
  family_id
  label
  path

options:
  -h, --help            show this help message and exit
  --metadata-json METADATA_JSON
```

### `x86decomp family correlate`

Execute the `correlate` action in the canonical `family` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `correlate` action in the canonical `family` capability group.

Example:

```console
$ x86decomp family correlate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE]
                                  left_member_id right_member_id

positional arguments:
  left_member_id
  right_member_id

options:
  -h, --help            show this help message and exit
  --block-size BLOCK_SIZE
```

### `x86decomp family create`

Execute the `create` action in the canonical `family` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `family` capability group.

Example:

```console
$ x86decomp family create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp family create [-h] name

positional arguments:
  name

options:
  -h, --help  show this help message and exit
```

### `x86decomp family report`

Execute the `report` action in the canonical `family` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `report` action in the canonical `family` capability group.

Example:

```console
$ x86decomp family report --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp family report [-h] family_id

positional arguments:
  family_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp function`

Canonical function commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical function commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp function --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp function [-h] [--project PROJECT] [--actor ACTOR]
                          {classify,discover,reconcile,sort} ...

Canonical function commands implemented by the current capability subsystem.

positional arguments:
  {classify,discover,reconcile,sort}
    classify            classify command
    discover            discover command
    reconcile           reconcile command
    sort                sort command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp function classify`

Execute the `classify` action in the canonical `function` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `classify` action in the canonical `function` capability group.

Example:

```console
$ x86decomp function classify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp function classify [-h] [--output OUTPUT] functions_json

positional arguments:
  functions_json

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp function discover`

Execute the `discover` action in the canonical `function` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `discover` action in the canonical `function` capability group.

Example:

```console
$ x86decomp function discover --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp function discover [-h] [--profile {prologue,ret-boundary}]
                                   [--architecture {x86,x86_64}]
                                   [--min-size MIN_SIZE] [--max-size MAX_SIZE]
                                   [--align ALIGN] [--output OUTPUT]
                                   image

positional arguments:
  image

options:
  -h, --help            show this help message and exit
  --profile {prologue,ret-boundary}
  --architecture {x86,x86_64}
  --min-size MIN_SIZE
  --max-size MAX_SIZE
  --align ALIGN
  --output OUTPUT
```

### `x86decomp function reconcile`

Execute the `reconcile` action in the canonical `function` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `reconcile` action in the canonical `function` capability group.

Example:

```console
$ x86decomp function reconcile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp function reconcile [-h] [--output OUTPUT]
                                    reports [reports ...]

positional arguments:
  reports

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp function sort`

Execute the `sort` action in the canonical `function` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `sort` action in the canonical `function` capability group.

Example:

```console
$ x86decomp function sort --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp function sort [-h] [--key KEY] [--output OUTPUT]
                               functions_json

positional arguments:
  functions_json

options:
  -h, --help       show this help message and exit
  --key KEY
  --output OUTPUT
```

## `x86decomp game-pattern`

Canonical game-pattern commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical game-pattern commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp game-pattern --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp game-pattern [-h] [--project PROJECT] [--actor ACTOR]
                              {state-machine} ...

Canonical game-pattern commands implemented by the current capability
subsystem.

positional arguments:
  {state-machine}
    state-machine    state-machine command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp game-pattern state-machine`

Execute the `state-machine` action in the canonical `game-pattern` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `state-machine` action in the canonical `game-pattern` capability group.

Example:

```console
$ x86decomp game-pattern state-machine --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp game-pattern state-machine [-h] [--output OUTPUT] root

positional arguments:
  root

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp ghidra-export`

run the bundled Ghidra export workflow

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run the bundled Ghidra export workflow

Example:

```console
$ x86decomp ghidra-export --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR]
                               [--ghidra-home GHIDRA_HOME] [--overwrite]
                               [--selector SELECTOR] [--timeout TIMEOUT]
                               [--report REPORT] [--print-command]
                               binary ghidra_project_dir ghidra_project_name
                               output_dir

positional arguments:
  binary
  ghidra_project_dir
  ghidra_project_name
  output_dir

options:
  -h, --help            show this help message and exit
  --scripts-dir SCRIPTS_DIR
  --ghidra-home GHIDRA_HOME
  --overwrite
  --selector SELECTOR
  --timeout TIMEOUT
  --report REPORT
  --print-command
```

## `x86decomp ghidra-mcp`

Canonical ghidra-mcp commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical ghidra-mcp commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp ghidra-mcp --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-mcp [-h] [--project PROJECT] [--actor ACTOR]
                            {batch-decompile,decompile,functions,probe,sync-names} ...

Canonical ghidra-mcp commands implemented by the current capability subsystem.

positional arguments:
  {batch-decompile,decompile,functions,probe,sync-names}
    batch-decompile     batch-decompile command
    decompile           decompile command
    functions           functions command
    probe               probe command
    sync-names          sync-names command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp ghidra-mcp batch-decompile`

Execute the `batch-decompile` action in the canonical `ghidra-mcp` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `batch-decompile` action in the canonical `ghidra-mcp` capability group.

Example:

```console
$ x86decomp ghidra-mcp batch-decompile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-mcp batch-decompile [-h] [--timeout TIMEOUT]
                                            url addresses output

positional arguments:
  url
  addresses
  output

options:
  -h, --help         show this help message and exit
  --timeout TIMEOUT
```

### `x86decomp ghidra-mcp decompile`

Execute the `decompile` action in the canonical `ghidra-mcp` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `decompile` action in the canonical `ghidra-mcp` capability group.

Example:

```console
$ x86decomp ghidra-mcp decompile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-mcp decompile [-h] [--timeout TIMEOUT]
                                      [--output OUTPUT]
                                      url address

positional arguments:
  url
  address

options:
  -h, --help         show this help message and exit
  --timeout TIMEOUT
  --output OUTPUT
```

### `x86decomp ghidra-mcp functions`

Execute the `functions` action in the canonical `ghidra-mcp` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `functions` action in the canonical `ghidra-mcp` capability group.

Example:

```console
$ x86decomp ghidra-mcp functions --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-mcp functions [-h] [--timeout TIMEOUT]
                                      [--output OUTPUT]
                                      url

positional arguments:
  url

options:
  -h, --help         show this help message and exit
  --timeout TIMEOUT
  --output OUTPUT
```

### `x86decomp ghidra-mcp probe`

Execute the `probe` action in the canonical `ghidra-mcp` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `probe` action in the canonical `ghidra-mcp` capability group.

Example:

```console
$ x86decomp ghidra-mcp probe --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-mcp probe [-h] [--timeout TIMEOUT] [--output OUTPUT]
                                  url

positional arguments:
  url

options:
  -h, --help         show this help message and exit
  --timeout TIMEOUT
  --output OUTPUT
```

### `x86decomp ghidra-mcp sync-names`

Execute the `sync-names` action in the canonical `ghidra-mcp` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `sync-names` action in the canonical `ghidra-mcp` capability group.

Example:

```console
$ x86decomp ghidra-mcp sync-names --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp ghidra-mcp sync-names [-h] [--output OUTPUT] names_json

positional arguments:
  names_json

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp graph`

Canonical graph commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical graph commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp graph --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp graph [-h] [--project PROJECT] [--actor ACTOR]
                       {edge,impact,node} ...

Canonical graph commands implemented by the current capability subsystem.

positional arguments:
  {edge,impact,node}
    edge              edge command
    impact            impact command
    node              node command

options:
  -h, --help          show this help message and exit
  --project PROJECT   project root used by the capability implementation
                      (default: current directory)
  --actor ACTOR
```

### `x86decomp graph edge`

Execute the `edge` action in the canonical `graph` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `edge` action in the canonical `graph` capability group.

Example:

```console
$ x86decomp graph edge --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON]
                            source_id target_id relation

positional arguments:
  source_id
  target_id
  relation

options:
  -h, --help            show this help message and exit
  --attributes-json ATTRIBUTES_JSON
```

### `x86decomp graph impact`

Execute the `impact` action in the canonical `graph` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `impact` action in the canonical `graph` capability group.

Example:

```console
$ x86decomp graph impact --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp graph impact [-h] [--direction DIRECTION]
                              [--max-depth MAX_DEPTH] [--relations RELATIONS]
                              node_id

positional arguments:
  node_id

options:
  -h, --help            show this help message and exit
  --direction DIRECTION
  --max-depth MAX_DEPTH
  --relations RELATIONS
```

### `x86decomp graph node`

Execute the `node` action in the canonical `graph` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `node` action in the canonical `graph` capability group.

Example:

```console
$ x86decomp graph node --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON]
                            node_id kind label

positional arguments:
  node_id
  kind
  label

options:
  -h, --help            show this help message and exit
  --attributes-json ATTRIBUTES_JSON
```

## `x86decomp harness-generate`

generate an execution harness from binary functions

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: generate an execution harness from binary functions

Example:

```console
$ x86decomp harness-generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp harness-generate [-h]
                                  [--pointer-parameters POINTER_PARAMETERS]
                                  [--no-observe-pointers]
                                  [--max-instructions MAX_INSTRUCTIONS]
                                  [--timeout-ms TIMEOUT_MS]
                                  abi_contract output

positional arguments:
  abi_contract
  output

options:
  -h, --help            show this help message and exit
  --pointer-parameters POINTER_PARAMETERS
  --no-observe-pointers
  --max-instructions MAX_INSTRUCTIONS
  --timeout-ms TIMEOUT_MS
```

## `x86decomp headers`

Canonical headers commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical headers commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp headers --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers [-h] [--project PROJECT] [--actor ACTOR]
                         {create,cycles,declare,explain,include,synthesize,synthesize-project,validate} ...

Canonical headers commands implemented by the current capability subsystem.

positional arguments:
  {create,cycles,declare,explain,include,synthesize,synthesize-project,validate}
    create              create command
    cycles              cycles command
    declare             declare command
    explain             explain command
    include             include command
    synthesize          synthesize command
    synthesize-project  synthesize-project command
    validate            validate command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp headers create`

Execute the `create` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers create [-h] [--visibility VISIBILITY] path

positional arguments:
  path

options:
  -h, --help            show this help message and exit
  --visibility VISIBILITY
```

### `x86decomp headers cycles`

Execute the `cycles` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `cycles` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers cycles --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers cycles [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp headers declare`

Execute the `declare` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `declare` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers declare --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers declare [-h] [--kind KIND] [--confidence CONFIDENCE]
                                 [--evidence-json EVIDENCE_JSON]
                                 header_id symbol_id declaration

positional arguments:
  header_id
  symbol_id
  declaration

options:
  -h, --help            show this help message and exit
  --kind KIND
  --confidence CONFIDENCE
  --evidence-json EVIDENCE_JSON
```

### `x86decomp headers explain`

Execute the `explain` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `explain` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers explain --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers explain [-h] header_id

positional arguments:
  header_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp headers include`

Execute the `include` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `include` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers include --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers include [-h] --reason REASON
                                 source_header_id target_header_id

positional arguments:
  source_header_id
  target_header_id

options:
  -h, --help        show this help message and exit
  --reason REASON
```

### `x86decomp headers synthesize`

Execute the `synthesize` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `synthesize` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers synthesize --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers synthesize [-h] [--output-root OUTPUT_ROOT] header_id

positional arguments:
  header_id

options:
  -h, --help            show this help message and exit
  --output-root OUTPUT_ROOT
```

### `x86decomp headers synthesize-project`

Execute the `synthesize-project` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `synthesize-project` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers synthesize-project --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers synthesize-project [-h] [--module MODULE] output

positional arguments:
  output

options:
  -h, --help       show this help message and exit
  --module MODULE
```

### `x86decomp headers validate`

Execute the `validate` action in the canonical `headers` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `validate` action in the canonical `headers` capability group.

Example:

```console
$ x86decomp headers validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp headers validate [-h] header_id

positional arguments:
  header_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp hybrid`

Canonical hybrid commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical hybrid commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp hybrid --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hybrid [-h] [--project PROJECT] [--actor ACTOR]
                        {compose,generate,verify} ...

Canonical hybrid commands implemented by the current capability subsystem.

positional arguments:
  {compose,generate,verify}
    compose             compose command
    generate            generate command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp hybrid compose`

Execute the `compose` action in the canonical `hybrid` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compose` action in the canonical `hybrid` capability group.

Example:

```console
$ x86decomp hybrid compose --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hybrid compose [-h] run_id output

positional arguments:
  run_id
  output

options:
  -h, --help  show this help message and exit
```

### `x86decomp hybrid generate`

Execute the `generate` action in the canonical `hybrid` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `generate` action in the canonical `hybrid` capability group.

Example:

```console
$ x86decomp hybrid generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 source_project output

positional arguments:
  source_project
  output

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --asm-format {bytes,annotated,mnemonic}
  --image-base IMAGE_BASE
  --assembler-command-json ASSEMBLER_COMMAND_JSON
  --symbol-map SYMBOL_MAP
  --overwrite
```

### `x86decomp hybrid verify`

Execute the `verify` action in the canonical `hybrid` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `hybrid` capability group.

Example:

```console
$ x86decomp hybrid verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hybrid verify [-h] composition_id

positional arguments:
  composition_id

options:
  -h, --help      show this help message and exit
```

## `x86decomp hybrid-generate`

compatibility alias for: x86decomp hybrid generate

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compatibility alias for: x86decomp hybrid generate

Example:

```console
$ x86decomp hybrid-generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hybrid-generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 project output

positional arguments:
  project
  output

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --asm-format {bytes,annotated,mnemonic}
  --image-base IMAGE_BASE
  --assembler-command-json ASSEMBLER_COMMAND_JSON
  --symbol-map SYMBOL_MAP
  --overwrite
```

## `x86decomp hypothesis`

Canonical hypothesis commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical hypothesis commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp hypothesis --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis [-h] [--project PROJECT] [--actor ACTOR]
                            {create,dependency,evidence,gate,list,show,transition} ...

Canonical hypothesis commands implemented by the current capability subsystem.

positional arguments:
  {create,dependency,evidence,gate,list,show,transition}
    create              create command
    dependency          dependency command
    evidence            evidence command
    gate                gate command
    list                list command
    show                show command
    transition          transition command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp hypothesis create`

Execute the `create` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis create [-h] --origin ORIGIN
                                   statement scope_kind scope_id

positional arguments:
  statement
  scope_kind
  scope_id

options:
  -h, --help       show this help message and exit
  --origin ORIGIN
```

### `x86decomp hypothesis dependency`

Execute the `dependency` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `dependency` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis dependency --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id

positional arguments:
  hypothesis_id
  depends_on_id

options:
  -h, --help     show this help message and exit
```

### `x86decomp hypothesis evidence`

Execute the `evidence` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `evidence` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis evidence --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT
                                     --kind KIND --group GROUP
                                     [--artifact-sha256 ARTIFACT_SHA256]
                                     [--details-json DETAILS_JSON]
                                     hypothesis_id evidence_id

positional arguments:
  hypothesis_id
  evidence_id

options:
  -h, --help            show this help message and exit
  --stance STANCE
  --weight WEIGHT
  --kind KIND
  --group GROUP
  --artifact-sha256 ARTIFACT_SHA256
  --details-json DETAILS_JSON
```

### `x86decomp hypothesis gate`

Execute the `gate` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `gate` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis gate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis gate [-h] hypothesis_id

positional arguments:
  hypothesis_id

options:
  -h, --help     show this help message and exit
```

### `x86decomp hypothesis list`

Execute the `list` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]

options:
  -h, --help           show this help message and exit
  --state STATE
  --scope-id SCOPE_ID
```

### `x86decomp hypothesis show`

Execute the `show` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis show [-h] hypothesis_id

positional arguments:
  hypothesis_id

options:
  -h, --help     show this help message and exit
```

### `x86decomp hypothesis transition`

Execute the `transition` action in the canonical `hypothesis` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `transition` action in the canonical `hypothesis` capability group.

Example:

```console
$ x86decomp hypothesis transition --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp hypothesis transition [-h] --reason REASON [--lock]
                                       hypothesis_id state

positional arguments:
  hypothesis_id
  state

options:
  -h, --help       show this help message and exit
  --reason REASON
  --lock
```

## `x86decomp image-match`

compare complete PE images under an explicit layout profile

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compare complete PE images under an explicit layout profile

Example:

```console
$ x86decomp image-match --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp image-match [-h] [--profile PROFILE] [--report REPORT]
                             reference candidate

positional arguments:
  reference
  candidate

options:
  -h, --help         show this help message and exit
  --profile PROFILE
  --report REPORT
```

## `x86decomp image-profile`

derive a target-specific whole-image profile

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: derive a target-specific whole-image profile

Example:

```console
$ x86decomp image-profile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp image-profile [-h] reference output

positional arguments:
  reference
  output

options:
  -h, --help  show this help message and exit
```

## `x86decomp image-text`

Canonical image-text commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical image-text commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp image-text --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp image-text [-h] [--project PROJECT] [--actor ACTOR]
                            {compose} ...

Canonical image-text commands implemented by the current capability subsystem.

positional arguments:
  {compose}
    compose          compose command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp image-text compose`

Execute the `compose` action in the canonical `image-text` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compose` action in the canonical `image-text` capability group.

Example:

```console
$ x86decomp image-text compose --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp image-text compose [-h] [--function-list FUNCTION_LIST]
                                    [--fallback-byte FALLBACK_BYTE]
                                    output

positional arguments:
  output

options:
  -h, --help            show this help message and exit
  --function-list FUNCTION_LIST
  --fallback-byte FALLBACK_BYTE
```

## `x86decomp init`

initialize a native PE project

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: initialize a native PE project

Example:

```console
$ x86decomp init --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp init [-h] [--reference-binary] binary project

positional arguments:
  binary
  project

options:
  -h, --help          show this help message and exit
  --reference-binary
```

## `x86decomp inspect-pe`

parse PE32 or PE32+ metadata

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: parse PE32 or PE32+ metadata

Example:

```console
$ x86decomp inspect-pe --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp inspect-pe [-h] binary

positional arguments:
  binary

options:
  -h, --help  show this help message and exit
```

## `x86decomp integration-run`

execute declared integration scenarios

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: execute declared integration scenarios

Example:

```console
$ x86decomp integration-run --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp integration-run [-h] [--allow-host-execution]
                                 [--report REPORT]
                                 manifest

positional arguments:
  manifest

options:
  -h, --help            show this help message and exit
  --allow-host-execution
  --report REPORT
```

## `x86decomp layout-reconstruct`

correlate PE sections, linker map contributions, and COFF objects

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: correlate PE sections, linker map contributions, and COFF objects

Example:

```console
$ x86decomp layout-reconstruct --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp layout-reconstruct [-h] [--report REPORT]
                                    pe map [objects ...]

positional arguments:
  pe
  map
  objects

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp lib-inspect`

inspect a COFF archive/static or import library

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: inspect a COFF archive/static or import library

Example:

```console
$ x86decomp lib-inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp lib-inspect [-h] library

positional arguments:
  library

options:
  -h, --help  show this help message and exit
```

## `x86decomp library`

Canonical library commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical library commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp library --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library [-h] [--project PROJECT] [--actor ACTOR]
                         {accept,candidates,externalize,identify,reconstruct,reject} ...

Canonical library commands implemented by the current capability subsystem.

positional arguments:
  {accept,candidates,externalize,identify,reconstruct,reject}
    accept              accept command
    candidates          candidates command
    externalize         externalize command
    identify            identify command
    reconstruct         reconstruct command
    reject              reject command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp library accept`

Execute the `accept` action in the canonical `library` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `accept` action in the canonical `library` capability group.

Example:

```console
$ x86decomp library accept --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library accept [-h] match_id

positional arguments:
  match_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp library candidates`

Execute the `candidates` action in the canonical `library` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `candidates` action in the canonical `library` capability group.

Example:

```console
$ x86decomp library candidates --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library candidates [-h] subject_id

positional arguments:
  subject_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp library externalize`

Execute the `externalize` action in the canonical `library` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `externalize` action in the canonical `library` capability group.

Example:

```console
$ x86decomp library externalize --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library externalize [-h] match_id

positional arguments:
  match_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp library identify`

Execute the `identify` action in the canonical `library` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `identify` action in the canonical `library` capability group.

Example:

```console
$ x86decomp library identify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library identify [-h] [--version-range VERSION_RANGE]
                                  --confidence CONFIDENCE
                                  --evidence-json EVIDENCE_JSON
                                  subject_id library_name

positional arguments:
  subject_id
  library_name

options:
  -h, --help            show this help message and exit
  --version-range VERSION_RANGE
  --confidence CONFIDENCE
  --evidence-json EVIDENCE_JSON
```

### `x86decomp library reconstruct`

Execute the `reconstruct` action in the canonical `library` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `reconstruct` action in the canonical `library` capability group.

Example:

```console
$ x86decomp library reconstruct --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library reconstruct [-h] match_id

positional arguments:
  match_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp library reject`

Execute the `reject` action in the canonical `library` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `reject` action in the canonical `library` capability group.

Example:

```console
$ x86decomp library reject --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp library reject [-h] match_id

positional arguments:
  match_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp linker-plan`

build a grounded linker reconstruction plan

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: build a grounded linker reconstruction plan

Example:

```console
$ x86decomp linker-plan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER]
                             [--output-image OUTPUT_IMAGE] [--report REPORT]
                             [--write-relink-manifest WRITE_RELINK_MANIFEST]
                             pe map objects [objects ...]

positional arguments:
  pe
  map
  objects

options:
  -h, --help            show this help message and exit
  --library LIBRARY
  --linker LINKER
  --output-image OUTPUT_IMAGE
  --report REPORT
  --write-relink-manifest WRITE_RELINK_MANIFEST
```

## `x86decomp llm`

Canonical llm commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical llm commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp llm --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm [-h] [--project PROJECT] [--actor ACTOR]
                     {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify} ...

Canonical llm commands implemented by the current capability subsystem.

positional arguments:
  {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify}
    batch-create        create local-LLM jobs for eligible project function
                        packets
    batch-match         run bounded match loops for a deterministic job queue
    cpp-generate        generate one bounded C++ proposal using a local-model
                        profile
    generate            generate one uncompiled C proposal
    job-create          create a local-LLM job from a function packet
    job-from-range      create a local-LLM job from an explicit byte range
    match               run bounded generation, compilation, relocation
                        resolution, and exact byte matching
    probe               probe the provider model-list endpoint
    profile-create      create a validated local-model provider profile
    profile-validate    validate a local-model provider profile
    prompt              materialize the deterministic prompt without
                        contacting a model
    providers           list built-in local-model provider presets
    verify              verify a local-model byte-match report and accepted
                        artifact hashes

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp llm batch-create`

Execute the `batch-create` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `batch-create` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm batch-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm batch-create [-h] --architecture {x86,x86_64}
                                  [--image-base IMAGE_BASE]
                                  [--max-bytes MAX_BYTES]
                                  [--max-attempts MAX_ATTEMPTS] [--overwrite]
                                  project_root output_directory

create local-LLM jobs for eligible project function packets

positional arguments:
  project_root
  output_directory

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --image-base IMAGE_BASE
  --max-bytes MAX_BYTES
  --max-attempts MAX_ATTEMPTS
  --overwrite
```

### `x86decomp llm batch-match`

Execute the `batch-match` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `batch-match` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm batch-match --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm batch-match [-h] [--max-workers MAX_WORKERS]
                                 [--max-attempts MAX_ATTEMPTS] [--overwrite]
                                 profile compiler_profile jobs
                                 output_directory

run bounded match loops for a deterministic job queue

positional arguments:
  profile
  compiler_profile
  jobs
  output_directory

options:
  -h, --help            show this help message and exit
  --max-workers MAX_WORKERS
  --max-attempts MAX_ATTEMPTS
  --overwrite
```

### `x86decomp llm cpp-generate`

Execute the `cpp-generate` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `cpp-generate` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm cpp-generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm cpp-generate [-h] [--class-context CLASS_CONTEXT]
                                  [--report REPORT] [--overwrite]
                                  profile job output

generate one bounded C++ proposal using a local-model profile

positional arguments:
  profile
  job
  output

options:
  -h, --help            show this help message and exit
  --class-context CLASS_CONTEXT
  --report REPORT
  --overwrite
```

### `x86decomp llm generate`

Execute the `generate` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `generate` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm generate [-h] [--report REPORT] [--overwrite]
                              profile job output

generate one uncompiled C proposal

positional arguments:
  profile
  job
  output

options:
  -h, --help       show this help message and exit
  --report REPORT
  --overwrite
```

### `x86decomp llm job-create`

Execute the `job-create` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `job-create` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm job-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm job-create [-h] --architecture {x86,x86_64}
                                [--image-base IMAGE_BASE]
                                [--function-name FUNCTION_NAME]
                                [--symbol SYMBOL]
                                [--max-attempts MAX_ATTEMPTS] [--inline]
                                [--overwrite]
                                function_packet output

create a local-LLM job from a function packet

positional arguments:
  function_packet
  output

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --image-base IMAGE_BASE
  --function-name FUNCTION_NAME
  --symbol SYMBOL
  --max-attempts MAX_ATTEMPTS
  --inline
  --overwrite
```

### `x86decomp llm job-from-range`

Execute the `job-from-range` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `job-from-range` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm job-from-range --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm job-from-range [-h] --rva RVA --size SIZE
                                    --architecture {x86,x86_64}
                                    --function-name FUNCTION_NAME
                                    [--symbol SYMBOL]
                                    [--image-base IMAGE_BASE]
                                    [--mnemonics MNEMONICS]
                                    [--max-attempts MAX_ATTEMPTS]
                                    [--overwrite]
                                    image output

create a local-LLM job from an explicit byte range

positional arguments:
  image
  output

options:
  -h, --help            show this help message and exit
  --rva RVA
  --size SIZE
  --architecture {x86,x86_64}
  --function-name FUNCTION_NAME
  --symbol SYMBOL
  --image-base IMAGE_BASE
  --mnemonics MNEMONICS
  --max-attempts MAX_ATTEMPTS
  --overwrite
```

### `x86decomp llm match`

Execute the `match` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `match` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm match --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm match [-h] [--max-attempts MAX_ATTEMPTS] [--overwrite]
                           profile compiler_profile job output_directory

run bounded generation, compilation, relocation resolution, and exact byte
matching

positional arguments:
  profile
  compiler_profile
  job
  output_directory

options:
  -h, --help            show this help message and exit
  --max-attempts MAX_ATTEMPTS
  --overwrite
```

### `x86decomp llm probe`

Execute the `probe` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `probe` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm probe --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm probe [-h] profile

probe the provider model-list endpoint

positional arguments:
  profile

options:
  -h, --help  show this help message and exit
```

### `x86decomp llm profile-create`

Execute the `profile-create` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `profile-create` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm profile-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm profile-create [-h] --model MODEL [--base-url BASE_URL]
                                    [--id ID] [--api-key-env API_KEY_ENV]
                                    [--allow-remote]
                                    {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm}
                                    output

create a validated local-model provider profile

positional arguments:
  {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm}
  output

options:
  -h, --help            show this help message and exit
  --model MODEL
  --base-url BASE_URL
  --id ID
  --api-key-env API_KEY_ENV
  --allow-remote
```

### `x86decomp llm profile-validate`

Execute the `profile-validate` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `profile-validate` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm profile-validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm profile-validate [-h] profile

validate a local-model provider profile

positional arguments:
  profile

options:
  -h, --help  show this help message and exit
```

### `x86decomp llm prompt`

Execute the `prompt` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `prompt` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm prompt --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm prompt [-h] job output

materialize the deterministic prompt without contacting a model

positional arguments:
  job
  output

options:
  -h, --help  show this help message and exit
```

### `x86decomp llm providers`

Execute the `providers` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `providers` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm providers --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm providers [-h]

list built-in local-model provider presets

options:
  -h, --help  show this help message and exit
```

### `x86decomp llm verify`

Execute the `verify` action in the canonical `llm` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `llm` capability group.

Example:

```console
$ x86decomp llm verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp llm verify [-h] report

verify a local-model byte-match report and accepted artifact hashes

positional arguments:
  report

options:
  -h, --help  show this help message and exit
```

## `x86decomp loop`

Canonical loop commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical loop commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp loop --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp loop [-h] [--project PROJECT] [--actor ACTOR]
                      {list,run,show} ...

Canonical loop commands implemented by the current capability subsystem.

positional arguments:
  {list,run,show}
    list             list command
    run              run command
    show             show command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp loop list`

Execute the `list` action in the canonical `loop` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `loop` capability group.

Example:

```console
$ x86decomp loop list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp loop list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp loop run`

Execute the `run` action in the canonical `loop` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `run` action in the canonical `loop` capability group.

Example:

```console
$ x86decomp loop run --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY]
                          [--timeout TIMEOUT] [--execute]
                          function_id source compile_command_json candidate
                          original rva slot_size

positional arguments:
  function_id
  source
  compile_command_json
  candidate
  original
  rva
  slot_size

options:
  -h, --help            show this help message and exit
  --symbol SYMBOL
  --policy POLICY
  --timeout TIMEOUT
  --execute
```

### `x86decomp loop show`

Execute the `show` action in the canonical `loop` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `loop` capability group.

Example:

```console
$ x86decomp loop show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp loop show [-h] loop_id

positional arguments:
  loop_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp map-inspect`

parse an MSVC-compatible linker map

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: parse an MSVC-compatible linker map

Example:

```console
$ x86decomp map-inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp map-inspect [-h] map

positional arguments:
  map

options:
  -h, --help  show this help message and exit
```

## `x86decomp match`

Canonical match commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical match commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp match --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp match [-h] [--project PROJECT] [--actor ACTOR]
                       {batch,compare,mismatches,report} ...

Canonical match commands implemented by the current capability subsystem.

positional arguments:
  {batch,compare,mismatches,report}
    batch               batch command
    compare             compare command
    mismatches          mismatches command
    report              report command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp match batch`

Execute the `batch` action in the canonical `match` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `batch` action in the canonical `match` capability group.

Example:

```console
$ x86decomp match batch --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}]
                             [--pad-bytes-json PAD_BYTES_JSON]
                             original candidates_json

positional arguments:
  original
  candidates_json

options:
  -h, --help            show this help message and exit
  --policy {exact,trailing-padding}
  --pad-bytes-json PAD_BYTES_JSON
```

### `x86decomp match compare`

Execute the `compare` action in the canonical `match` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compare` action in the canonical `match` capability group.

Example:

```console
$ x86decomp match compare --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}]
                               [--pad-bytes-json PAD_BYTES_JSON]
                               [--protected-offsets-json PROTECTED_OFFSETS_JSON]
                               original candidate

positional arguments:
  original
  candidate

options:
  -h, --help            show this help message and exit
  --policy {exact,trailing-padding}
  --pad-bytes-json PAD_BYTES_JSON
  --protected-offsets-json PROTECTED_OFFSETS_JSON
```

### `x86decomp match mismatches`

Execute the `mismatches` action in the canonical `match` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `mismatches` action in the canonical `match` capability group.

Example:

```console
$ x86decomp match mismatches --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp match mismatches [-h] run_id

positional arguments:
  run_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp match report`

Execute the `report` action in the canonical `match` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `report` action in the canonical `match` capability group.

Example:

```console
$ x86decomp match report --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp match report [-h] run_id

positional arguments:
  run_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp mcp-commit`

commit an approved MCP mutation

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: commit an approved MCP mutation

Example:

```console
$ x86decomp mcp-commit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp mcp-commit [-h] [--url URL] [--command-json COMMAND_JSON]
                            --allow-tool ALLOW_TOOL
                            project approval_hash

positional arguments:
  project
  approval_hash

options:
  -h, --help            show this help message and exit
  --url URL
  --command-json COMMAND_JSON
  --allow-tool ALLOW_TOOL
```

## `x86decomp mcp-propose`

propose an evidence-linked MCP mutation for approval

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: propose an evidence-linked MCP mutation for approval

Example:

```console
$ x86decomp mcp-propose --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp mcp-propose [-h] [--url URL] [--command-json COMMAND_JSON]
                             --allow-tool ALLOW_TOOL --rationale RATIONALE
                             --evidence EVIDENCE
                             project tool arguments

positional arguments:
  project
  tool
  arguments

options:
  -h, --help            show this help message and exit
  --url URL
  --command-json COMMAND_JSON
  --allow-tool ALLOW_TOOL
  --rationale RATIONALE
  --evidence EVIDENCE
```

## `x86decomp mcp-read`

invoke a read-only MCP tool through the project gateway

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: invoke a read-only MCP tool through the project gateway

Example:

```console
$ x86decomp mcp-read --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp mcp-read [-h] [--url URL] [--command-json COMMAND_JSON]
                          project tool arguments

positional arguments:
  project
  tool
  arguments

options:
  -h, --help            show this help message and exit
  --url URL
  --command-json COMMAND_JSON
```

## `x86decomp mcp-tools`

list tools exposed by a configured MCP endpoint

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: list tools exposed by a configured MCP endpoint

Example:

```console
$ x86decomp mcp-tools --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp mcp-tools [-h] [--url URL] [--command-json COMMAND_JSON]

options:
  -h, --help            show this help message and exit
  --url URL
  --command-json COMMAND_JSON
```

## `x86decomp memory-add`

append an evidence-linked project-memory entry

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: append an evidence-linked project-memory entry

Example:

```console
$ x86decomp memory-add --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp memory-add [-h] --actor ACTOR --category CATEGORY
                            --summary SUMMARY [--details-json DETAILS_JSON]
                            [--evidence EVIDENCE]
                            project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --actor ACTOR
  --category CATEGORY
  --summary SUMMARY
  --details-json DETAILS_JSON
  --evidence EVIDENCE
```

## `x86decomp memory-render`

render project memory as Markdown

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: render project memory as Markdown

Example:

```console
$ x86decomp memory-render --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp memory-render [-h] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
```

## `x86decomp memory-verify`

verify the integrity of project-memory records

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify the integrity of project-memory records

Example:

```console
$ x86decomp memory-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp memory-verify [-h] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
```

## `x86decomp metadata-scan`

recover bounded MSVC RTTI, vtables, unwind, TLS, and initializer metadata

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: recover bounded MSVC RTTI, vtables, unwind, TLS, and initializer metadata

Example:

```console
$ x86decomp metadata-scan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp metadata-scan [-h] [--object OBJECT] [--map MAP]
                               [--report REPORT]
                               pe

positional arguments:
  pe

options:
  -h, --help       show this help message and exit
  --object OBJECT
  --map MAP
  --report REPORT
```

## `x86decomp mod`

Canonical mod commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical mod commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp mod --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp mod [-h] [--project PROJECT] [--actor ACTOR]
                     {branch-init} ...

Canonical mod commands implemented by the current capability subsystem.

positional arguments:
  {branch-init}
    branch-init      branch-init command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp mod branch-init`

Execute the `branch-init` action in the canonical `mod` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `branch-init` action in the canonical `mod` capability group.

Example:

```console
$ x86decomp mod branch-init --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp mod branch-init [-h] --baseline BASELINE [--output OUTPUT]
                                 name

positional arguments:
  name

options:
  -h, --help           show this help message and exit
  --baseline BASELINE
  --output OUTPUT
```

## `x86decomp module`

Canonical module commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical module commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp module --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module [-h] [--project PROJECT] [--actor ACTOR]
                        {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest} ...

Canonical module commands implemented by the current capability subsystem.

positional arguments:
  {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest}
    add-member          add-member command
    add-unit-member     add-unit-member command
    assign              assign command
    create              create command
    create-unit         create-unit command
    list                list command
    show                show command
    show-unit           show-unit command
    suggest             suggest command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp module add-member`

Execute the `add-member` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add-member` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module add-member --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module add-member [-h] [--ordinal ORDINAL]
                                   [--evidence-json EVIDENCE_JSON]
                                   module_id member_kind member_id

positional arguments:
  module_id
  member_kind
  member_id

options:
  -h, --help            show this help message and exit
  --ordinal ORDINAL
  --evidence-json EVIDENCE_JSON
```

### `x86decomp module add-unit-member`

Execute the `add-unit-member` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add-unit-member` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module add-unit-member --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE]
                                        [--ordinal ORDINAL]
                                        unit_id member_kind member_id

positional arguments:
  unit_id
  member_kind
  member_id

options:
  -h, --help         show this help message and exit
  --linkage LINKAGE
  --ordinal ORDINAL
```

### `x86decomp module assign`

Execute the `assign` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `assign` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module assign --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module assign [-h] --module MODULE [--class-name CLASS_NAME]
                               [--header HEADER] [--source SOURCE]
                               [--report REPORT]
                               function_id

positional arguments:
  function_id

options:
  -h, --help            show this help message and exit
  --module MODULE
  --class-name CLASS_NAME
  --header HEADER
  --source SOURCE
  --report REPORT
```

### `x86decomp module create`

Execute the `create` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH]
                               [--confidence CONFIDENCE]
                               [--evidence-json EVIDENCE_JSON]
                               name

positional arguments:
  name

options:
  -h, --help            show this help message and exit
  --kind KIND
  --source-path SOURCE_PATH
  --confidence CONFIDENCE
  --evidence-json EVIDENCE_JSON
```

### `x86decomp module create-unit`

Execute the `create-unit` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create-unit` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module create-unit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module create-unit [-h] [--module-id MODULE_ID]
                                    [--language LANGUAGE]
                                    [--confidence CONFIDENCE]
                                    [--evidence-json EVIDENCE_JSON]
                                    source_path

positional arguments:
  source_path

options:
  -h, --help            show this help message and exit
  --module-id MODULE_ID
  --language LANGUAGE
  --confidence CONFIDENCE
  --evidence-json EVIDENCE_JSON
```

### `x86decomp module list`

Execute the `list` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp module show`

Execute the `show` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module show [-h] module_id

positional arguments:
  module_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp module show-unit`

Execute the `show-unit` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show-unit` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module show-unit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module show-unit [-h] unit_id

positional arguments:
  unit_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp module suggest`

Execute the `suggest` action in the canonical `module` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `suggest` action in the canonical `module` capability group.

Example:

```console
$ x86decomp module suggest --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp module suggest [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp objdiff-run`

run an objdiff-compatible comparison manifest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run an objdiff-compatible comparison manifest

Example:

```console
$ x86decomp objdiff-run --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp objdiff-run [-h] [--report REPORT] manifest

positional arguments:
  manifest

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp patch-image`

patch a function body into a PE image

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: patch a function body into a PE image

Example:

```console
$ x86decomp patch-image --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp patch-image [-h] --rva RVA
                             [--expected-original-sha256 EXPECTED_ORIGINAL_SHA256]
                             [--expected-function-sha256 EXPECTED_FUNCTION_SHA256]
                             [--report REPORT]
                             original candidate output

positional arguments:
  original
  candidate
  output

options:
  -h, --help            show this help message and exit
  --rva RVA
  --expected-original-sha256 EXPECTED_ORIGINAL_SHA256
  --expected-function-sha256 EXPECTED_FUNCTION_SHA256
  --report REPORT
```

## `x86decomp pattern`

Canonical pattern commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical pattern commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp pattern --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pattern [-h] [--project PROJECT] [--actor ACTOR]
                         {catalog,generate,match,promote,scan} ...

Canonical pattern commands implemented by the current capability subsystem.

positional arguments:
  {catalog,generate,match,promote,scan}
    catalog             catalog command
    generate            generate command
    match               match command
    promote             promote command
    scan                scan command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp pattern catalog`

Execute the `catalog` action in the canonical `pattern` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `catalog` action in the canonical `pattern` capability group.

Example:

```console
$ x86decomp pattern catalog --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pattern catalog [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp pattern generate`

Execute the `generate` action in the canonical `pattern` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `generate` action in the canonical `pattern` capability group.

Example:

```console
$ x86decomp pattern generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pattern generate [-h] [--symbol-prefix SYMBOL_PREFIX]
                                  scan_report output

positional arguments:
  scan_report
  output

options:
  -h, --help            show this help message and exit
  --symbol-prefix SYMBOL_PREFIX
```

### `x86decomp pattern match`

Execute the `match` action in the canonical `pattern` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `match` action in the canonical `pattern` capability group.

Example:

```console
$ x86decomp pattern match --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pattern match [-h] [--output OUTPUT] generation_report

positional arguments:
  generation_report

options:
  -h, --help         show this help message and exit
  --output OUTPUT
```

### `x86decomp pattern promote`

Execute the `promote` action in the canonical `pattern` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `promote` action in the canonical `pattern` capability group.

Example:

```console
$ x86decomp pattern promote --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pattern promote [-h] --candidate CANDIDATE --report REPORT
                                 [--stage STAGE] [--output OUTPUT]
                                 [--overwrite]
                                 function_id

positional arguments:
  function_id

options:
  -h, --help            show this help message and exit
  --candidate CANDIDATE
  --report REPORT
  --stage STAGE
  --output OUTPUT
  --overwrite
```

### `x86decomp pattern scan`

Execute the `scan` action in the canonical `pattern` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `scan` action in the canonical `pattern` capability group.

Example:

```console
$ x86decomp pattern scan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pattern scan [-h] [--architecture {x86,x86_64}]
                              [--output OUTPUT]
                              root

positional arguments:
  root

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --output OUTPUT
```

## `x86decomp pdb-inspect`

inspect an MSF 7.0 PDB and optionally match it to a PE

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: inspect an MSF 7.0 PDB and optionally match it to a PE

Example:

```console
$ x86decomp pdb-inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pdb-inspect [-h] [--pe PE] pdb

positional arguments:
  pdb

options:
  -h, --help  show this help message and exit
  --pe PE
```

## `x86decomp pe`

Canonical pe commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical pe commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp pe --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe [-h] [--project PROJECT] [--actor ACTOR]
                    {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap} ...

Canonical pe commands implemented by the current capability subsystem.

positional arguments:
  {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap}
    export-coff         export-coff command
    export-sections     export-sections command
    inventory           inventory command
    patch-apply         patch-apply command
    patch-plan          patch-plan command
    text-swap           text-swap command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp pe export-coff`

Execute the `export-coff` action in the canonical `pe` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export-coff` action in the canonical `pe` capability group.

Example:

```console
$ x86decomp pe export-coff --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe export-coff [-h] [--section SECTION] image output

positional arguments:
  image
  output

options:
  -h, --help         show this help message and exit
  --section SECTION
```

### `x86decomp pe export-sections`

Execute the `export-sections` action in the canonical `pe` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export-sections` action in the canonical `pe` capability group.

Example:

```console
$ x86decomp pe export-sections --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe export-sections [-h] [--section SECTION] image output

positional arguments:
  image
  output

options:
  -h, --help         show this help message and exit
  --section SECTION
```

### `x86decomp pe inventory`

Execute the `inventory` action in the canonical `pe` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inventory` action in the canonical `pe` capability group.

Example:

```console
$ x86decomp pe inventory --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe inventory [-h] image

positional arguments:
  image

options:
  -h, --help  show this help message and exit
```

### `x86decomp pe patch-apply`

Execute the `patch-apply` action in the canonical `pe` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `patch-apply` action in the canonical `pe` capability group.

Example:

```console
$ x86decomp pe patch-apply --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe patch-apply [-h] plan_id

positional arguments:
  plan_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp pe patch-plan`

Execute the `patch-plan` action in the canonical `pe` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `patch-plan` action in the canonical `pe` capability group.

Example:

```console
$ x86decomp pe patch-plan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe patch-plan [-h] original output operations_json

positional arguments:
  original
  output
  operations_json

options:
  -h, --help       show this help message and exit
```

### `x86decomp pe text-swap`

Execute the `text-swap` action in the canonical `pe` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `text-swap` action in the canonical `pe` capability group.

Example:

```console
$ x86decomp pe text-swap --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME]
                              original replacement output

positional arguments:
  original
  replacement
  output

options:
  -h, --help            show this help message and exit
  --section-name SECTION_NAME
```

## `x86decomp pipeline-cancel`

cancel a pipeline or one pipeline stage

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: cancel a pipeline or one pipeline stage

Example:

```console
$ x86decomp pipeline-cancel --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pipeline-cancel [-h] [--stage-id STAGE_ID]
                                 project pipeline_id

positional arguments:
  project
  pipeline_id

options:
  -h, --help           show this help message and exit
  --stage-id STAGE_ID
```

## `x86decomp pipeline-create`

create a default durable analysis pipeline manifest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a default durable analysis pipeline manifest

Example:

```console
$ x86decomp pipeline-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pipeline-create [-h] [--without-ghidra] project output

positional arguments:
  project
  output

options:
  -h, --help        show this help message and exit
  --without-ghidra
```

## `x86decomp pipeline-recover`

reset jobs with stale durable runner heartbeats

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: reset jobs with stale durable runner heartbeats

Example:

```console
$ x86decomp pipeline-recover --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pipeline-recover [-h] [--pipeline-id PIPELINE_ID]
                                  [--stale-seconds STALE_SECONDS]
                                  project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --pipeline-id PIPELINE_ID
  --stale-seconds STALE_SECONDS
```

## `x86decomp pipeline-retry`

retry a failed pipeline stage

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: retry a failed pipeline stage

Example:

```console
$ x86decomp pipeline-retry --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pipeline-retry [-h] [--cascade] project pipeline_id stage_id

positional arguments:
  project
  pipeline_id
  stage_id

options:
  -h, --help   show this help message and exit
  --cascade
```

## `x86decomp pipeline-run`

run or resume a durable project pipeline

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: run or resume a durable project pipeline

Example:

```console
$ x86decomp pipeline-run --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pipeline-run [-h] [--continue-on-failure] project manifest

positional arguments:
  project
  manifest

options:
  -h, --help            show this help message and exit
  --continue-on-failure
```

## `x86decomp pipeline-status`

show durable pipeline and stage status

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: show durable pipeline and stage status

Example:

```console
$ x86decomp pipeline-status --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp pipeline-status [-h] project pipeline_id

positional arguments:
  project
  pipeline_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp playability`

Canonical playability commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical playability commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp playability --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp playability [-h] [--project PROJECT] [--actor ACTOR]
                             {smoke-plan} ...

Canonical playability commands implemented by the current capability
subsystem.

positional arguments:
  {smoke-plan}
    smoke-plan       smoke-plan command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp playability smoke-plan`

Execute the `smoke-plan` action in the canonical `playability` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `smoke-plan` action in the canonical `playability` capability group.

Example:

```console
$ x86decomp playability smoke-plan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp playability smoke-plan [-h] [--profile PROFILE] target output

positional arguments:
  target
  output

options:
  -h, --help         show this help message and exit
  --profile PROFILE
```

## `x86decomp plugin`

Canonical plugin commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical plugin commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp plugin --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp plugin [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,install,invoke,list,validate} ...

Canonical plugin commands implemented by the current capability subsystem.

positional arguments:
  {doctor,install,invoke,list,validate}
    doctor              doctor command
    install             install command
    invoke              invoke command
    list                list command
    validate            validate command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp plugin doctor`

Execute the `doctor` action in the canonical `plugin` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `doctor` action in the canonical `plugin` capability group.

Example:

```console
$ x86decomp plugin doctor --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp plugin doctor [-h] plugin_id

positional arguments:
  plugin_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp plugin install`

Execute the `install` action in the canonical `plugin` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `install` action in the canonical `plugin` capability group.

Example:

```console
$ x86decomp plugin install --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp plugin install [-h] manifest

positional arguments:
  manifest

options:
  -h, --help  show this help message and exit
```

### `x86decomp plugin invoke`

Execute the `invoke` action in the canonical `plugin` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `invoke` action in the canonical `plugin` capability group.

Example:

```console
$ x86decomp plugin invoke --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT]
                               plugin_id capability request_json

positional arguments:
  plugin_id
  capability
  request_json

options:
  -h, --help         show this help message and exit
  --timeout TIMEOUT
```

### `x86decomp plugin list`

Execute the `list` action in the canonical `plugin` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `plugin` capability group.

Example:

```console
$ x86decomp plugin list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp plugin list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp plugin validate`

Execute the `validate` action in the canonical `plugin` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `validate` action in the canonical `plugin` capability group.

Example:

```console
$ x86decomp plugin validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp plugin validate [-h] manifest

positional arguments:
  manifest

options:
  -h, --help  show this help message and exit
```

## `x86decomp progress`

Canonical progress commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical progress commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp progress --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp progress [-h] [--project PROJECT] [--actor ACTOR]
                          {reconcile} ...

Canonical progress commands implemented by the current capability subsystem.

positional arguments:
  {reconcile}
    reconcile        reconcile command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp progress reconcile`

Execute the `reconcile` action in the canonical `progress` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `reconcile` action in the canonical `progress` capability group.

Example:

```console
$ x86decomp progress reconcile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp progress reconcile [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp project`

Canonical project commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical project commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp project --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project [-h] [--project PROJECT] [--actor ACTOR]
                         {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout} ...

Canonical project commands implemented by the current capability subsystem.

positional arguments:
  {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout}
    check               check command
    doctor-paths        doctor-paths command
    explain-boundaries  explain-boundaries command
    export              export command
    health              health command
    init                init command
    synthesize-layout   synthesize-layout command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp project check`

Execute the `check` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `check` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project check --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project check [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp project doctor-paths`

Execute the `doctor-paths` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `doctor-paths` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project doctor-paths --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project doctor-paths [-h] [--output OUTPUT] root

positional arguments:
  root

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp project explain-boundaries`

Execute the `explain-boundaries` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `explain-boundaries` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project explain-boundaries --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project explain-boundaries [-h] module_id

positional arguments:
  module_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp project export`

Execute the `export` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project export --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project export [-h] output

positional arguments:
  output

options:
  -h, --help  show this help message and exit
```

### `x86decomp project health`

Execute the `health` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `health` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project health --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project health [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp project init`

Execute the `init` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `init` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project init --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project init [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp project synthesize-layout`

Execute the `synthesize-layout` action in the canonical `project` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `synthesize-layout` action in the canonical `project` capability group.

Example:

```console
$ x86decomp project synthesize-layout --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project synthesize-layout [-h] inventory_json

positional arguments:
  inventory_json

options:
  -h, --help      show this help message and exit
```

## `x86decomp project-backup`

create a deterministic project-state backup

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a deterministic project-state backup

Example:

```console
$ x86decomp project-backup --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-backup [-h] project output

positional arguments:
  project
  output

options:
  -h, --help  show this help message and exit
```

## `x86decomp project-check`

compatibility alias for project state validation

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: compatibility alias for project state validation

Example:

```console
$ x86decomp project-check --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-check [-h] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
```

## `x86decomp project-from-target`

initialize a project from a verified target pack

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: initialize a project from a verified target pack

Example:

```console
$ x86decomp project-from-target --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-from-target [-h] [--reference-binary]
                                     target_pack project

positional arguments:
  target_pack
  project

options:
  -h, --help          show this help message and exit
  --reference-binary
```

## `x86decomp project-gc`

inspect or remove unreferenced project content

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: inspect or remove unreferenced project content

Example:

```console
$ x86decomp project-gc --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-gc [-h] [--apply] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
  --apply
```

## `x86decomp project-migrate`

migrate project state to the current schema

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: migrate project state to the current schema

Example:

```console
$ x86decomp project-migrate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project

positional arguments:
  project

options:
  -h, --help       show this help message and exit
  --dry-run
  --backup BACKUP
```

## `x86decomp project-repair`

inspect or apply deterministic project-state repairs

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: inspect or apply deterministic project-state repairs

Example:

```console
$ x86decomp project-repair --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-repair [-h] [--apply] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
  --apply
```

## `x86decomp project-restore`

restore project state from a verified backup

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: restore project state from a verified backup

Example:

```console
$ x86decomp project-restore --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp project-restore [-h] archive destination

positional arguments:
  archive
  destination

options:
  -h, --help   show this help message and exit
```

## `x86decomp proof`

Canonical proof commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical proof commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp proof --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof [-h] [--project PROJECT] [--actor ACTOR]
                       {evaluate,export,inspect,obligation,result,verify} ...

Canonical proof commands implemented by the current capability subsystem.

positional arguments:
  {evaluate,export,inspect,obligation,result,verify}
    evaluate            evaluate command
    export              export command
    inspect             inspect command
    obligation          obligation command
    result              result command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp proof evaluate`

Execute the `evaluate` action in the canonical `proof` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `evaluate` action in the canonical `proof` capability group.

Example:

```console
$ x86decomp proof evaluate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof evaluate [-h] obligation_id

positional arguments:
  obligation_id

options:
  -h, --help     show this help message and exit
```

### `x86decomp proof export`

Execute the `export` action in the canonical `proof` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export` action in the canonical `proof` capability group.

Example:

```console
$ x86decomp proof export --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof export [-h] [--include INCLUDE] output

positional arguments:
  output

options:
  -h, --help         show this help message and exit
  --include INCLUDE
```

### `x86decomp proof inspect`

Execute the `inspect` action in the canonical `proof` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inspect` action in the canonical `proof` capability group.

Example:

```console
$ x86decomp proof inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof inspect [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

### `x86decomp proof obligation`

Execute the `obligation` action in the canonical `proof` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `obligation` action in the canonical `proof` capability group.

Example:

```console
$ x86decomp proof obligation --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON]
                                  scope_kind scope_id property_name
                                  required_status

positional arguments:
  scope_kind
  scope_id
  property_name
  required_status

options:
  -h, --help            show this help message and exit
  --assumptions-json ASSUMPTIONS_JSON
```

### `x86decomp proof result`

Execute the `result` action in the canonical `proof` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `result` action in the canonical `proof` capability group.

Example:

```console
$ x86decomp proof result --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256]
                              obligation_id status validator report_json

positional arguments:
  obligation_id
  status
  validator
  report_json

options:
  -h, --help            show this help message and exit
  --artifact-sha256 ARTIFACT_SHA256
```

### `x86decomp proof verify`

Execute the `verify` action in the canonical `proof` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `proof` capability group.

Example:

```console
$ x86decomp proof verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp proof verify [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

## `x86decomp provenance`

Canonical provenance commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical provenance commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp provenance --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp provenance [-h] [--project PROJECT] [--actor ACTOR]
                            {binary,export,record,source} ...

Canonical provenance commands implemented by the current capability subsystem.

positional arguments:
  {binary,export,record,source}
    binary              binary command
    export              export command
    record              record command
    source              source command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp provenance binary`

Execute the `binary` action in the canonical `provenance` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `binary` action in the canonical `provenance` capability group.

Example:

```console
$ x86decomp provenance binary --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp provenance binary [-h] [--address ADDRESS] binary_id

positional arguments:
  binary_id

options:
  -h, --help         show this help message and exit
  --address ADDRESS
```

### `x86decomp provenance export`

Execute the `export` action in the canonical `provenance` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `export` action in the canonical `provenance` capability group.

Example:

```console
$ x86decomp provenance export --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp provenance export [-h] output

positional arguments:
  output

options:
  -h, --help  show this help message and exit
```

### `x86decomp provenance record`

Execute the `record` action in the canonical `provenance` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `record` action in the canonical `provenance` capability group.

Example:

```console
$ x86decomp provenance record --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp provenance record [-h] --evidence-json EVIDENCE_JSON
                                   --confidence CONFIDENCE
                                   source_path line_start line_end binary_id
                                   address_start address_end

positional arguments:
  source_path
  line_start
  line_end
  binary_id
  address_start
  address_end

options:
  -h, --help            show this help message and exit
  --evidence-json EVIDENCE_JSON
  --confidence CONFIDENCE
```

### `x86decomp provenance source`

Execute the `source` action in the canonical `provenance` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `source` action in the canonical `provenance` capability group.

Example:

```console
$ x86decomp provenance source --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp provenance source [-h] [--line LINE] source_path

positional arguments:
  source_path

options:
  -h, --help   show this help message and exit
  --line LINE
```

## `x86decomp regression`

Canonical regression commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical regression commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp regression --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp regression [-h] [--project PROJECT] [--actor ACTOR]
                            {compare} ...

Canonical regression commands implemented by the current capability subsystem.

positional arguments:
  {compare}
    compare          compare command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp regression compare`

Execute the `compare` action in the canonical `regression` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compare` action in the canonical `regression` capability group.

Example:

```console
$ x86decomp regression compare --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp regression compare [-h] [--allow ALLOW] [--output OUTPUT]
                                    baseline modded

positional arguments:
  baseline
  modded

options:
  -h, --help       show this help message and exit
  --allow ALLOW
  --output OUTPUT
```

## `x86decomp release-gate`

evaluate explicit target release acceptance contracts

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: evaluate explicit target release acceptance contracts

Example:

```console
$ x86decomp release-gate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp release-gate [-h]
                              [--reproduction-manifest REPRODUCTION_MANIFEST]
                              [--security-report SECURITY_REPORT]
                              [--convergence-report CONVERGENCE_REPORT]
                              [--require-workflows]
                              [--require-verified-claims]
                              [--require-succeeded-pipelines]
                              [--report REPORT]
                              project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --reproduction-manifest REPRODUCTION_MANIFEST
  --security-report SECURITY_REPORT
  --convergence-report CONVERGENCE_REPORT
  --require-workflows
  --require-verified-claims
  --require-succeeded-pipelines
  --report REPORT
```

## `x86decomp release-manifest-verify`

verify every entry in a release hash manifest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify every entry in a release hash manifest

Example:

```console
$ x86decomp release-manifest-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp release-manifest-verify [-h] [--manifest MANIFEST] root

positional arguments:
  root

options:
  -h, --help           show this help message and exit
  --manifest MANIFEST
```

## `x86decomp release-policy`

Canonical release-policy commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical release-policy commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp release-policy --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp release-policy [-h] [--project PROJECT] [--actor ACTOR]
                                {moddable-source} ...

Canonical release-policy commands implemented by the current capability
subsystem.

positional arguments:
  {moddable-source}
    moddable-source  moddable-source command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp release-policy moddable-source`

Execute the `moddable-source` action in the canonical `release-policy` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `moddable-source` action in the canonical `release-policy` capability group.

Example:

```console
$ x86decomp release-policy moddable-source --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp release-policy moddable-source [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp relink`

relink an image from a declared reconstruction manifest

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: relink an image from a declared reconstruction manifest

Example:

```console
$ x86decomp relink --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp relink [-h] [--report REPORT] manifest

positional arguments:
  manifest

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp reloc`

Canonical reloc commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical reloc commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp reloc --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp reloc [-h] [--project PROJECT] [--actor ACTOR]
                       {inspect,resolve,supported} ...

Canonical reloc commands implemented by the current capability subsystem.

positional arguments:
  {inspect,resolve,supported}
    inspect             inspect command
    resolve             resolve command
    supported           supported command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp reloc inspect`

Execute the `inspect` action in the canonical `reloc` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inspect` action in the canonical `reloc` capability group.

Example:

```console
$ x86decomp reloc inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp reloc inspect [-h] [--symbol SYMBOL] object

positional arguments:
  object

options:
  -h, --help       show this help message and exit
  --symbol SYMBOL
```

### `x86decomp reloc resolve`

Execute the `resolve` action in the canonical `reloc` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `resolve` action in the canonical `reloc` capability group.

Example:

```console
$ x86decomp reloc resolve --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp reloc resolve [-h] [--image-base IMAGE_BASE]
                               object symbol base_rva symbol_map output

positional arguments:
  object
  symbol
  base_rva
  symbol_map
  output

options:
  -h, --help            show this help message and exit
  --image-base IMAGE_BASE
```

### `x86decomp reloc supported`

Execute the `supported` action in the canonical `reloc` capability group.

- Kind: `canonical-route`
- Owner: `assembly`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `supported` action in the canonical `reloc` capability group.

Example:

```console
$ x86decomp reloc supported --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp reloc supported [-h]

options:
  -h, --help  show this help message and exit
```

## `x86decomp reproduce-create`

create a reproducibility manifest for declared inputs

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a reproducibility manifest for declared inputs

Example:

```console
$ x86decomp reproduce-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp reproduce-create [-h] [--required-tool REQUIRED_TOOL]
                                  project output

positional arguments:
  project
  output

options:
  -h, --help            show this help message and exit
  --required-tool REQUIRED_TOOL
```

## `x86decomp reproduce-verify`

verify a reproducibility manifest and all input hashes

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify a reproducibility manifest and all input hashes

Example:

```console
$ x86decomp reproduce-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp reproduce-verify [-h] project manifest

positional arguments:
  project
  manifest

options:
  -h, --help  show this help message and exit
```

## `x86decomp review`

Canonical review commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical review commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp review --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review [-h] [--project PROJECT] [--actor ACTOR]
                        {assign,create,decide,list,lock,show} ...

Canonical review commands implemented by the current capability subsystem.

positional arguments:
  {assign,create,decide,list,lock,show}
    assign              assign command
    create              create command
    decide              decide command
    list                list command
    lock                lock command
    show                show command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp review assign`

Execute the `assign` action in the canonical `review` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `assign` action in the canonical `review` capability group.

Example:

```console
$ x86decomp review assign --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review assign [-h] review_id assignee

positional arguments:
  review_id
  assignee

options:
  -h, --help  show this help message and exit
```

### `x86decomp review create`

Execute the `create` action in the canonical `review` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `create` action in the canonical `review` capability group.

Example:

```console
$ x86decomp review create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review create [-h] [--priority PRIORITY]
                               [--details-json DETAILS_JSON]
                               kind subject_id summary

positional arguments:
  kind
  subject_id
  summary

options:
  -h, --help            show this help message and exit
  --priority PRIORITY
  --details-json DETAILS_JSON
```

### `x86decomp review decide`

Execute the `decide` action in the canonical `review` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `decide` action in the canonical `review` capability group.

Example:

```console
$ x86decomp review decide --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review decide [-h] --rationale RATIONALE [--lock]
                               review_id decision

positional arguments:
  review_id
  decision

options:
  -h, --help            show this help message and exit
  --rationale RATIONALE
  --lock
```

### `x86decomp review list`

Execute the `list` action in the canonical `review` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `review` capability group.

Example:

```console
$ x86decomp review list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]

options:
  -h, --help       show this help message and exit
  --status STATUS
  --limit LIMIT
```

### `x86decomp review lock`

Execute the `lock` action in the canonical `review` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `lock` action in the canonical `review` capability group.

Example:

```console
$ x86decomp review lock --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review lock [-h] review_id

positional arguments:
  review_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp review show`

Execute the `show` action in the canonical `review` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `show` action in the canonical `review` capability group.

Example:

```console
$ x86decomp review show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp review show [-h] review_id

positional arguments:
  review_id

options:
  -h, --help  show this help message and exit
```

## `x86decomp runtime`

Canonical runtime commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical runtime commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp runtime --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime [-h] [--project PROJECT] [--actor ACTOR]
                         {launch,map-crash,validate-image} ...

Canonical runtime commands implemented by the current capability subsystem.

positional arguments:
  {launch,map-crash,validate-image}
    launch              launch command
    map-crash           map-crash command
    validate-image      validate-image command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp runtime launch`

Execute the `launch` action in the canonical `runtime` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `launch` action in the canonical `runtime` capability group.

Example:

```console
$ x86decomp runtime launch --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT]
                                [--execute]
                                image

positional arguments:
  image

options:
  -h, --help           show this help message and exit
  --argument ARGUMENT
  --timeout TIMEOUT
  --execute
```

### `x86decomp runtime map-crash`

Execute the `map-crash` action in the canonical `runtime` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `map-crash` action in the canonical `runtime` capability group.

Example:

```console
$ x86decomp runtime map-crash --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime map-crash [-h] rva

positional arguments:
  rva

options:
  -h, --help  show this help message and exit
```

### `x86decomp runtime validate-image`

Execute the `validate-image` action in the canonical `runtime` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `validate-image` action in the canonical `runtime` capability group.

Example:

```console
$ x86decomp runtime validate-image --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime validate-image [-h] image

positional arguments:
  image

options:
  -h, --help  show this help message and exit
```

## `x86decomp runtime-analysis`

Canonical runtime-analysis commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical runtime-analysis commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp runtime-analysis --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime-analysis [-h] [--project PROJECT] [--actor ACTOR]
                                  {identify,match-library,quarantine} ...

Canonical runtime-analysis commands implemented by the current capability
subsystem.

positional arguments:
  {identify,match-library,quarantine}
    identify            identify command
    match-library       match-library command
    quarantine          quarantine command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp runtime-analysis identify`

Execute the `identify` action in the canonical `runtime-analysis` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `identify` action in the canonical `runtime-analysis` capability group.

Example:

```console
$ x86decomp runtime-analysis identify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime-analysis identify [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp runtime-analysis match-library`

Execute the `match-library` action in the canonical `runtime-analysis` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `match-library` action in the canonical `runtime-analysis` capability group.

Example:

```console
$ x86decomp runtime-analysis match-library --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime-analysis match-library [-h] [--output OUTPUT]
                                                library_inventory

positional arguments:
  library_inventory

options:
  -h, --help         show this help message and exit
  --output OUTPUT
```

### `x86decomp runtime-analysis quarantine`

Execute the `quarantine` action in the canonical `runtime-analysis` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `quarantine` action in the canonical `runtime-analysis` capability group.

Example:

```console
$ x86decomp runtime-analysis quarantine --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp runtime-analysis quarantine [-h] [--output OUTPUT]
                                             identification_report

positional arguments:
  identification_report

options:
  -h, --help            show this help message and exit
  --output OUTPUT
```

## `x86decomp sbom-generate`

generate a software bill of materials

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: generate a software bill of materials

Example:

```console
$ x86decomp sbom-generate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp sbom-generate [-h] output

positional arguments:
  output

options:
  -h, --help  show this help message and exit
```

## `x86decomp script-port`

Canonical script-port commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical script-port commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp script-port --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp script-port [-h] [--project PROJECT] [--actor ACTOR]
                             {audit} ...

Canonical script-port commands implemented by the current capability
subsystem.

positional arguments:
  {audit}
    audit            audit command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp script-port audit`

Execute the `audit` action in the canonical `script-port` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `audit` action in the canonical `script-port` capability group.

Example:

```console
$ x86decomp script-port audit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp script-port audit [-h] [--output OUTPUT] root

positional arguments:
  root

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp security`

Canonical security commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical security commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp security --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp security [-h] [--project PROJECT] [--actor ACTOR]
                          {finding,policy,report,scan} ...

Canonical security commands implemented by the current capability subsystem.

positional arguments:
  {finding,policy,report,scan}
    finding             finding command
    policy              policy command
    report              report command
    scan                scan command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp security finding`

Execute the `finding` action in the canonical `security` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `finding` action in the canonical `security` capability group.

Example:

```console
$ x86decomp security finding --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON
                                  rule_id severity subject_id summary

positional arguments:
  rule_id
  severity
  subject_id
  summary

options:
  -h, --help            show this help message and exit
  --evidence-json EVIDENCE_JSON
```

### `x86decomp security policy`

Execute the `policy` action in the canonical `security` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `policy` action in the canonical `security` capability group.

Example:

```console
$ x86decomp security policy --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp security policy [-h] name policy_json

positional arguments:
  name
  policy_json

options:
  -h, --help   show this help message and exit
```

### `x86decomp security report`

Execute the `report` action in the canonical `security` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `report` action in the canonical `security` capability group.

Example:

```console
$ x86decomp security report --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp security report [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp security scan`

Execute the `scan` action in the canonical `security` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `scan` action in the canonical `security` capability group.

Example:

```console
$ x86decomp security scan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp security scan [-h] observations_json

positional arguments:
  observations_json

options:
  -h, --help         show this help message and exit
```

## `x86decomp security-audit`

audit a source tree for declared security checks

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: audit a source tree for declared security checks

Example:

```console
$ x86decomp security-audit --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp security-audit [-h] [--report REPORT] root

positional arguments:
  root

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp serve`

serve the read-only project API on loopback by default

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: serve the read-only project API on loopback by default

Example:

```console
$ x86decomp serve --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp serve [-h] [--host HOST] [--port PORT] [--allow-remote]
                       project

positional arguments:
  project

options:
  -h, --help      show this help message and exit
  --host HOST
  --port PORT
  --allow-remote  explicitly authorize a non-loopback bind
```

## `x86decomp snapshot-tools`

record detected external tool versions and paths

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: record detected external tool versions and paths

Example:

```console
$ x86decomp snapshot-tools --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp snapshot-tools [-h] [--output OUTPUT]
                                [--ghidra-home GHIDRA_HOME]

options:
  -h, --help            show this help message and exit
  --output OUTPUT
  --ghidra-home GHIDRA_HOME
```

## `x86decomp source`

Canonical source commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical source commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp source --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source [-h] [--project PROJECT] [--actor ACTOR]
                        {impact,lock,reconcile,unlock} ...

Canonical source commands implemented by the current capability subsystem.

positional arguments:
  {impact,lock,reconcile,unlock}
    impact              impact command
    lock                lock command
    reconcile           reconcile command
    unlock              unlock command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp source impact`

Execute the `impact` action in the canonical `source` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `impact` action in the canonical `source` capability group.

Example:

```console
$ x86decomp source impact --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source impact [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

### `x86decomp source lock`

Execute the `lock` action in the canonical `source` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `lock` action in the canonical `source` capability group.

Example:

```console
$ x86decomp source lock --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source lock [-h] --reason REASON path

positional arguments:
  path

options:
  -h, --help       show this help message and exit
  --reason REASON
```

### `x86decomp source reconcile`

Execute the `reconcile` action in the canonical `source` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `reconcile` action in the canonical `source` capability group.

Example:

```console
$ x86decomp source reconcile --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256]
                                  [--semantic {true,false}]
                                  path

positional arguments:
  path

options:
  -h, --help            show this help message and exit
  --before-sha256 BEFORE_SHA256
  --semantic {true,false}
```

### `x86decomp source unlock`

Execute the `unlock` action in the canonical `source` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `unlock` action in the canonical `source` capability group.

Example:

```console
$ x86decomp source unlock --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source unlock [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

## `x86decomp source-map`

Canonical source-map commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical source-map commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp source-map --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source-map [-h] [--project PROJECT] [--actor ACTOR]
                            {annotate,verify} ...

Canonical source-map commands implemented by the current capability subsystem.

positional arguments:
  {annotate,verify}
    annotate         annotate command
    verify           verify command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp source-map annotate`

Execute the `annotate` action in the canonical `source-map` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `annotate` action in the canonical `source-map` capability group.

Example:

```console
$ x86decomp source-map annotate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source-map annotate [-h] [--binary BINARY] [--report REPORT]
                                     source_root

positional arguments:
  source_root

options:
  -h, --help       show this help message and exit
  --binary BINARY
  --report REPORT
```

### `x86decomp source-map verify`

Execute the `verify` action in the canonical `source-map` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `source-map` capability group.

Example:

```console
$ x86decomp source-map verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source-map verify [-h] [--report REPORT] source_root

positional arguments:
  source_root

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp source-stage`

Canonical source-stage commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical source-stage commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp source-stage --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source-stage [-h] [--project PROJECT] [--actor ACTOR]
                              {classify} ...

Canonical source-stage commands implemented by the current capability
subsystem.

positional arguments:
  {classify}
    classify         classify command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp source-stage classify`

Execute the `classify` action in the canonical `source-stage` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `classify` action in the canonical `source-stage` capability group.

Example:

```console
$ x86decomp source-stage classify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp source-stage classify [-h] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp staging`

Canonical staging commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical staging commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp staging --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp staging [-h] [--project PROJECT] [--actor ACTOR]
                         {compile-check,generate-context,resolve,scan,unresolved} ...

Canonical staging commands implemented by the current capability subsystem.

positional arguments:
  {compile-check,generate-context,resolve,scan,unresolved}
    compile-check       compile-check command
    generate-context    generate-context command
    resolve             resolve command
    scan                scan command
    unresolved          unresolved command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp staging compile-check`

Execute the `compile-check` action in the canonical `staging` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `compile-check` action in the canonical `staging` capability group.

Example:

```console
$ x86decomp staging compile-check --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT]
                                       command_json

positional arguments:
  command_json

options:
  -h, --help         show this help message and exit
  --cwd CWD
  --timeout TIMEOUT
```

### `x86decomp staging generate-context`

Execute the `generate-context` action in the canonical `staging` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `generate-context` action in the canonical `staging` capability group.

Example:

```console
$ x86decomp staging generate-context --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp staging generate-context [-h] output sources [sources ...]

positional arguments:
  output
  sources

options:
  -h, --help  show this help message and exit
```

### `x86decomp staging resolve`

Execute the `resolve` action in the canonical `staging` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `resolve` action in the canonical `staging` capability group.

Example:

```console
$ x86decomp staging resolve --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp staging resolve [-h] mapping_json

positional arguments:
  mapping_json

options:
  -h, --help    show this help message and exit
```

### `x86decomp staging scan`

Execute the `scan` action in the canonical `staging` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `scan` action in the canonical `staging` capability group.

Example:

```console
$ x86decomp staging scan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp staging scan [-h] sources [sources ...]

positional arguments:
  sources

options:
  -h, --help  show this help message and exit
```

### `x86decomp staging unresolved`

Execute the `unresolved` action in the canonical `staging` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `unresolved` action in the canonical `staging` capability group.

Example:

```console
$ x86decomp staging unresolved --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp staging unresolved [-h]

options:
  -h, --help  show this help message and exit
```

## `x86decomp subsystem`

Canonical subsystem commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical subsystem commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp subsystem --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp subsystem [-h] [--project PROJECT] [--actor ACTOR]
                           {detect} ...

Canonical subsystem commands implemented by the current capability subsystem.

positional arguments:
  {detect}
    detect           detect command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp subsystem detect`

Execute the `detect` action in the canonical `subsystem` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `detect` action in the canonical `subsystem` capability group.

Example:

```console
$ x86decomp subsystem detect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp subsystem detect [-h] [--output OUTPUT] root

positional arguments:
  root

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp symbolic-memory-validate`

angr comparison with symbolic region bases and alias constraints

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: angr comparison with symbolic region bases and alias constraints

Example:

```console
$ x86decomp symbolic-memory-validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp symbolic-memory-validate [-h] [--report REPORT]
                                          target candidate harness

positional arguments:
  target
  candidate
  harness

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp symbolic-validate`

symbolically compare bounded binary functions

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: symbolically compare bounded binary functions

Example:

```console
$ x86decomp symbolic-validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp symbolic-validate [-h] [--architecture {x86,x86_64}]
                                   [--input-register INPUT_REGISTER]
                                   [--stack-argument-words STACK_ARGUMENT_WORDS]
                                   [--output-register OUTPUT_REGISTER]
                                   [--max-steps MAX_STEPS]
                                   [--max-paths MAX_PATHS] [--report REPORT]
                                   target candidate

positional arguments:
  target
  candidate

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --input-register INPUT_REGISTER
  --stack-argument-words STACK_ARGUMENT_WORDS
  --output-register OUTPUT_REGISTER
  --max-steps MAX_STEPS
  --max-paths MAX_PATHS
  --report REPORT
```

## `x86decomp target-pack-infer`

infer a fact-preserving target pack and template plan

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: infer a fact-preserving target pack and template plan

Example:

```console
$ x86decomp target-pack-infer --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp target-pack-infer [-h] [--name NAME] [--pdb PDB] [--map MAP]
                                   [--object OBJECT] [--library LIBRARY]
                                   [--rebuilt-image REBUILT_IMAGE]
                                   [--decisions DECISIONS]
                                   [--reference-artifacts]
                                   primary_image output_directory

positional arguments:
  primary_image
  output_directory

options:
  -h, --help            show this help message and exit
  --name NAME
  --pdb PDB
  --map MAP
  --object OBJECT
  --library LIBRARY
  --rebuilt-image REBUILT_IMAGE
  --decisions DECISIONS
  --reference-artifacts
```

## `x86decomp target-pack-verify`

verify a target-pack contract and referenced artifacts

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify a target-pack contract and referenced artifacts

Example:

```console
$ x86decomp target-pack-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp target-pack-verify [-h] target_pack

positional arguments:
  target_pack

options:
  -h, --help   show this help message and exit
```

## `x86decomp template-derive`

derive a grounded project-template contract from a target pack

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: derive a grounded project-template contract from a target pack

Example:

```console
$ x86decomp template-derive --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp template-derive [-h] target_pack

positional arguments:
  target_pack

options:
  -h, --help   show this help message and exit
```

## `x86decomp template-materialize`

materialize the grounded working layout for an existing target project

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: materialize the grounded working layout for an existing target project

Example:

```console
$ x86decomp template-materialize --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp template-materialize [-h] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
```

## `x86decomp test-bundle-create`

create a hash-sealed authorized static test bundle

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a hash-sealed authorized static test bundle

Example:

```console
$ x86decomp test-bundle-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp test-bundle-create [-h] --artifact ARTIFACT
                                    --authorization AUTHORIZATION
                                    [--name NAME] [--description DESCRIPTION]
                                    [--expected-architecture {x86,x86_64}]
                                    output

positional arguments:
  output

options:
  -h, --help            show this help message and exit
  --artifact ARTIFACT   role=path
  --authorization AUTHORIZATION
  --name NAME
  --description DESCRIPTION
  --expected-architecture {x86,x86_64}
```

## `x86decomp test-bundle-inspect`

safely extract, verify, and statically inspect an authorized test bundle

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: safely extract, verify, and statically inspect an authorized test bundle

Example:

```console
$ x86decomp test-bundle-inspect --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp test-bundle-inspect [-h] [--report REPORT] bundle

positional arguments:
  bundle

options:
  -h, --help       show this help message and exit
  --report REPORT
```

## `x86decomp tests`

Canonical tests commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical tests commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp tests --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp tests [-h] [--project PROJECT] [--actor ACTOR]
                       {add,explain,list,promote-counterexample,synthesize} ...

Canonical tests commands implemented by the current capability subsystem.

positional arguments:
  {add,explain,list,promote-counterexample,synthesize}
    add                 add command
    explain             explain command
    list                list command
    promote-counterexample
                        promote-counterexample command
    synthesize          synthesize command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp tests add`

Execute the `add` action in the canonical `tests` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `add` action in the canonical `tests` capability group.

Example:

```console
$ x86decomp tests add --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON
                           --evidence-json EVIDENCE_JSON
                           name scope_kind scope_id test_kind relative_path
                           content_file

positional arguments:
  name
  scope_kind
  scope_id
  test_kind
  relative_path
  content_file

options:
  -h, --help            show this help message and exit
  --applicability-json APPLICABILITY_JSON
  --evidence-json EVIDENCE_JSON
```

### `x86decomp tests explain`

Execute the `explain` action in the canonical `tests` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `explain` action in the canonical `tests` capability group.

Example:

```console
$ x86decomp tests explain --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp tests explain [-h] test_id

positional arguments:
  test_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp tests list`

Execute the `list` action in the canonical `tests` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `tests` capability group.

Example:

```console
$ x86decomp tests list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp tests list [-h]

options:
  -h, --help  show this help message and exit
```

### `x86decomp tests promote-counterexample`

Execute the `promote-counterexample` action in the canonical `tests` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `promote-counterexample` action in the canonical `tests` capability group.

Example:

```console
$ x86decomp tests promote-counterexample --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp tests promote-counterexample [-h] [--name NAME]
                                              counterexample_id

positional arguments:
  counterexample_id

options:
  -h, --help         show this help message and exit
  --name NAME
```

### `x86decomp tests synthesize`

Execute the `synthesize` action in the canonical `tests` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `synthesize` action in the canonical `tests` capability group.

Example:

```console
$ x86decomp tests synthesize --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id

positional arguments:
  scope_kind
  scope_id

options:
  -h, --help   show this help message and exit
  --name NAME
```

## `x86decomp text-swap`

Canonical text-swap commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical text-swap commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp text-swap --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp text-swap [-h] [--project PROJECT] [--actor ACTOR]
                           {build,inject,plan,verify} ...

Canonical text-swap commands implemented by the current capability subsystem.

positional arguments:
  {build,inject,plan,verify}
    build               build command
    inject              inject command
    plan                plan command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp text-swap build`

Execute the `build` action in the canonical `text-swap` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `build` action in the canonical `text-swap` capability group.

Example:

```console
$ x86decomp text-swap build --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp text-swap build [-h] --original ORIGINAL
                                 [--section-name SECTION_NAME]
                                 replacement output

positional arguments:
  replacement
  output

options:
  -h, --help            show this help message and exit
  --original ORIGINAL
  --section-name SECTION_NAME
```

### `x86decomp text-swap inject`

Execute the `inject` action in the canonical `text-swap` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `inject` action in the canonical `text-swap` capability group.

Example:

```console
$ x86decomp text-swap inject --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp text-swap inject [-h] [--output OUTPUT] plan

positional arguments:
  plan

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

### `x86decomp text-swap plan`

Execute the `plan` action in the canonical `text-swap` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `plan` action in the canonical `text-swap` capability group.

Example:

```console
$ x86decomp text-swap plan --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp text-swap plan [-h] [--section-name SECTION_NAME]
                                original replacement output

positional arguments:
  original
  replacement
  output

options:
  -h, --help            show this help message and exit
  --section-name SECTION_NAME
```

### `x86decomp text-swap verify`

Execute the `verify` action in the canonical `text-swap` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify` action in the canonical `text-swap` capability group.

Example:

```console
$ x86decomp text-swap verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp text-swap verify [-h] [--output OUTPUT] plan image

positional arguments:
  plan
  image

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp toolchain`

Canonical toolchain commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical toolchain commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp toolchain --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp toolchain [-h] [--project PROJECT] [--actor ACTOR]
                           {hash-tree,redact-package,verify-local} ...

Canonical toolchain commands implemented by the current capability subsystem.

positional arguments:
  {hash-tree,redact-package,verify-local}
    hash-tree           hash-tree command
    redact-package      redact-package command
    verify-local        verify-local command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp toolchain hash-tree`

Execute the `hash-tree` action in the canonical `toolchain` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `hash-tree` action in the canonical `toolchain` capability group.

Example:

```console
$ x86decomp toolchain hash-tree --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp toolchain hash-tree [-h] root output

positional arguments:
  root
  output

options:
  -h, --help  show this help message and exit
```

### `x86decomp toolchain redact-package`

Execute the `redact-package` action in the canonical `toolchain` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `redact-package` action in the canonical `toolchain` capability group.

Example:

```console
$ x86decomp toolchain redact-package --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp toolchain redact-package [-h] [--manifest MANIFEST]
                                          root output

positional arguments:
  root
  output

options:
  -h, --help           show this help message and exit
  --manifest MANIFEST
```

### `x86decomp toolchain verify-local`

Execute the `verify-local` action in the canonical `toolchain` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `verify-local` action in the canonical `toolchain` capability group.

Example:

```console
$ x86decomp toolchain verify-local --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp toolchain verify-local [-h] [--output OUTPUT] manifest

positional arguments:
  manifest

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp toolchain-register`

register a versioned compiler toolchain

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: register a versioned compiler toolchain

Example:

```console
$ x86decomp toolchain-register --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp toolchain-register [-h] --executable EXECUTABLE
                                    registry toolchain_id family version

positional arguments:
  registry
  toolchain_id
  family
  version

options:
  -h, --help            show this help message and exit
  --executable EXECUTABLE
                        role=path
```

## `x86decomp toolchain-verify`

verify a registered toolchain and executable hashes

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify a registered toolchain and executable hashes

Example:

```console
$ x86decomp toolchain-verify --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp toolchain-verify [-h] registry toolchain_id

positional arguments:
  registry
  toolchain_id

options:
  -h, --help    show this help message and exit
```

## `x86decomp triage`

Canonical triage commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical triage commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp triage --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp triage [-h] [--project PROJECT] [--actor ACTOR] {next} ...

Canonical triage commands implemented by the current capability subsystem.

positional arguments:
  {next}
    next             emit a triage plan only; no workflow state is modified

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp triage next`

Execute the `next` action in the canonical `triage` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `next` action in the canonical `triage` capability group.

Example:

```console
$ x86decomp triage next --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp triage next [-h] [--goal {matching,playable}] [--limit LIMIT]
                             [--output OUTPUT]

emit a triage plan only; no workflow state is modified

options:
  -h, --help            show this help message and exit
  --goal {matching,playable}
  --limit LIMIT
  --output OUTPUT
```

## `x86decomp type`

Canonical type commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical type commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp type --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp type [-h] [--project PROJECT] [--actor ACTOR] {propagate} ...

Canonical type commands implemented by the current capability subsystem.

positional arguments:
  {propagate}
    propagate        emit a type-propagation plan only; no source edits are
                     performed

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp type propagate`

Execute the `propagate` action in the canonical `type` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `propagate` action in the canonical `type` capability group.

Example:

```console
$ x86decomp type propagate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp type propagate [-h] [--output OUTPUT]

emit a type-propagation plan only; no source edits are performed

options:
  -h, --help       show this help message and exit
  --output OUTPUT
```

## `x86decomp verify-project`

verify project structure, contracts, and recorded hashes

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: verify project structure, contracts, and recorded hashes

Example:

```console
$ x86decomp verify-project --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp verify-project [-h] project

positional arguments:
  project

options:
  -h, --help  show this help message and exit
```

## `x86decomp vtable`

Canonical vtable commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical vtable commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp vtable --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp vtable [-h] [--project PROJECT] [--actor ACTOR] {recover} ...

Canonical vtable commands implemented by the current capability subsystem.

positional arguments:
  {recover}
    recover          recover command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```

### `x86decomp vtable recover`

Execute the `recover` action in the canonical `vtable` capability group.

- Kind: `canonical-route`
- Owner: `reconstruction`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `recover` action in the canonical `vtable` capability group.

Example:

```console
$ x86decomp vtable recover --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp vtable recover [-h] [--metadata-report METADATA_REPORT]
                                --output OUTPUT
                                image

positional arguments:
  image

options:
  -h, --help            show this help message and exit
  --metadata-report METADATA_REPORT
  --output OUTPUT
```

## `x86decomp windows`

Canonical windows commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical windows commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp windows --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp windows [-h] [--project PROJECT] [--actor ACTOR]
                         {discover-ghidra,doctor,response-file} ...

Canonical windows commands implemented by the current capability subsystem.

positional arguments:
  {discover-ghidra,doctor,response-file}
    discover-ghidra     discover-ghidra command
    doctor              doctor command
    response-file       response-file command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp windows discover-ghidra`

Execute the `discover-ghidra` action in the canonical `windows` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `discover-ghidra` action in the canonical `windows` capability group.

Example:

```console
$ x86decomp windows discover-ghidra --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME]
                                         [--platform-name PLATFORM_NAME]

options:
  -h, --help            show this help message and exit
  --ghidra-home GHIDRA_HOME
  --platform-name PLATFORM_NAME
```

### `x86decomp windows doctor`

Execute the `doctor` action in the canonical `windows` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `doctor` action in the canonical `windows` capability group.

Example:

```console
$ x86decomp windows doctor --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]

options:
  -h, --help            show this help message and exit
  --ghidra-home GHIDRA_HOME
```

### `x86decomp windows response-file`

Execute the `response-file` action in the canonical `windows` capability group.

- Kind: `canonical-route`
- Owner: `native`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `response-file` action in the canonical `windows` capability group.

Example:

```console
$ x86decomp windows response-file --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp windows response-file [-h] output arguments_json

positional arguments:
  output
  arguments_json

options:
  -h, --help      show this help message and exit
```

## `x86decomp work-claim`

claim a work-queue task for an assignee

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: claim a work-queue task for an assignee

Example:

```console
$ x86decomp work-claim --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp work-claim [-h] database task_id assignee

positional arguments:
  database
  task_id
  assignee

options:
  -h, --help  show this help message and exit
```

## `x86decomp work-create`

create a validated work-queue task

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: create a validated work-queue task

Example:

```console
$ x86decomp work-create --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]
                             database function_id {matching,functional} kind
                             instructions

positional arguments:
  database
  function_id
  {matching,functional}
  kind
  instructions

options:
  -h, --help            show this help message and exit
  --validator VALIDATOR
  --priority PRIORITY
```

## `x86decomp work-next`

show the next eligible work-queue task

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: show the next eligible work-queue task

Example:

```console
$ x86decomp work-next --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp work-next [-h] [--mode {matching,functional}] database

positional arguments:
  database

options:
  -h, --help            show this help message and exit
  --mode {matching,functional}
```

## `x86decomp work-propose`

attach a proposal and evidence to a work task

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: attach a proposal and evidence to a work task

Example:

```console
$ x86decomp work-propose --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp work-propose [-h] --evidence EVIDENCE
                              database task_id proposal

positional arguments:
  database
  task_id
  proposal

options:
  -h, --help           show this help message and exit
  --evidence EVIDENCE
```

## `x86decomp work-validate`

record a validator result for a work task

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: record a validator result for a work task

Example:

```console
$ x86decomp work-validate --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp work-validate [-h] [--passed]
                               database task_id validator report_path

positional arguments:
  database
  task_id
  validator
  report_path

options:
  -h, --help   show this help message and exit
  --passed
```

## `x86decomp worker`

Canonical worker commands implemented by the current capability subsystem.

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Canonical worker commands implemented by the current capability subsystem.

Example:

```console
$ x86decomp worker --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,list,register,select,status} ...

Canonical worker commands implemented by the current capability subsystem.

positional arguments:
  {doctor,list,register,select,status}
    doctor              doctor command
    list                list command
    register            register command
    select              select command
    status              status command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```

### `x86decomp worker doctor`

Execute the `doctor` action in the canonical `worker` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `doctor` action in the canonical `worker` capability group.

Example:

```console
$ x86decomp worker doctor --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker doctor [-h] worker_id

positional arguments:
  worker_id

options:
  -h, --help  show this help message and exit
```

### `x86decomp worker list`

Execute the `list` action in the canonical `worker` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `list` action in the canonical `worker` capability group.

Example:

```console
$ x86decomp worker list --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker list [-h] [--status STATUS]

options:
  -h, --help       show this help message and exit
  --status STATUS
```

### `x86decomp worker register`

Execute the `register` action in the canonical `worker` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `register` action in the canonical `worker` capability group.

Example:

```console
$ x86decomp worker register --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker register [-h] [--endpoint ENDPOINT]
                                 [--environment-sha256 ENVIRONMENT_SHA256]
                                 name capabilities_json

positional arguments:
  name
  capabilities_json

options:
  -h, --help            show this help message and exit
  --endpoint ENDPOINT
  --environment-sha256 ENVIRONMENT_SHA256
```

### `x86decomp worker select`

Execute the `select` action in the canonical `worker` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `review-required`
- Safety note: Side effects are not provable from parser metadata alone. Review the implementation and run in a disposable workspace when processing untrusted inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `select` action in the canonical `worker` capability group.

Example:

```console
$ x86decomp worker select --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker select [-h] required_json

positional arguments:
  required_json

options:
  -h, --help     show this help message and exit
```

### `x86decomp worker status`

Execute the `status` action in the canonical `worker` capability group.

- Kind: `canonical-route`
- Owner: `governance`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: Execute the `status` action in the canonical `worker` capability group.

Example:

```console
$ x86decomp worker status --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker status [-h] worker_id status

positional arguments:
  worker_id
  status

options:
  -h, --help  show this help message and exit
```

## `x86decomp worker-capabilities`

report local worker and tool capabilities

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: report local worker and tool capabilities

Example:

```console
$ x86decomp worker-capabilities --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp worker-capabilities [-h]

options:
  -h, --help  show this help message and exit
```

## `x86decomp workflow-init`

initialize per-function decompilation workflow state

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: initialize per-function decompilation workflow state

Example:

```console
$ x86decomp workflow-init --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp workflow-init [-h] [--mode {matching,functional}]
                               project function_id

positional arguments:
  project
  function_id

options:
  -h, --help            show this help message and exit
  --mode {matching,functional}
```

## `x86decomp workflow-show`

show validated per-function workflow state

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `apparently-read-only-by-name`
- Safety note: The command name indicates inspection or verification, but optional report paths or external tools can still create files; review the exact argument list before execution.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: show validated per-function workflow state

Example:

```console
$ x86decomp workflow-show --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp workflow-show [-h] project function_id

positional arguments:
  project
  function_id

options:
  -h, --help   show this help message and exit
```

## `x86decomp workflow-update`

update validated per-function workflow state

- Kind: `root-command`
- Owner: `root CLI`
- Safety classification: `potentially-mutating`
- Safety note: Operational execution can modify files, project state, or external-tool outputs. Review all arguments and use a disposable workspace when evaluating unfamiliar inputs.
- Success output: Operational success is serialized as deterministic indented JSON on standard output by x86decomp.cli_utils.run_cli.
- Error behavior: Argument parsing errors exit with status 2 and argparse usage diagnostics. Expected runtime errors exit with status 2 and a JSON object containing `error` and `message` on standard error.
- Real-world use case: Use this command when the task matches its registered purpose: update validated per-function workflow state

Example:

```console
$ x86decomp workflow-update --help
```

Expected result: Print this parser node's usage and argument reference, then exit with status 0.

Generated help:

```text
usage: x86decomp workflow-update [-h]
                                 [--source-stage {original_bytes,generated_assembly,decompiler_candidate,human_candidate,accepted_source}]
                                 [--matching-status {not_started,decompiled,compiles,abi_compatible,instruction_similar,byte_matched,image_integrated,full_relink_validated,blocked}]
                                 [--functional-status {not_started,decompiled,compiles,abi_compatible,differentially_validated,symbolically_bounded,integration_validated,blocked}]
                                 [--candidate CANDIDATE]
                                 [--compiler-profile COMPILER_PROFILE]
                                 [--report-kind REPORT_KIND]
                                 [--report-path REPORT_PATH]
                                 [--blocker BLOCKER] [--allow-regression]
                                 project function_id

positional arguments:
  project
  function_id

options:
  -h, --help            show this help message and exit
  --source-stage {original_bytes,generated_assembly,decompiler_candidate,human_candidate,accepted_source}
  --matching-status {not_started,decompiled,compiles,abi_compatible,instruction_similar,byte_matched,image_integrated,full_relink_validated,blocked}
  --functional-status {not_started,decompiled,compiles,abi_compatible,differentially_validated,symbolically_bounded,integration_validated,blocked}
  --candidate CANDIDATE
  --compiler-profile COMPILER_PROFILE
  --report-kind REPORT_KIND
  --report-path REPORT_PATH
  --blocker BLOCKER
  --allow-regression
```
