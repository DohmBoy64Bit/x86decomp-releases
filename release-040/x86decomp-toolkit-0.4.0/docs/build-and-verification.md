# Build and verification — 0.4.0

## Development environment

Use an isolated Python environment. The repository test commands disable unrelated
third-party pytest plugin autoload so a host workstation plugin cannot change or hang
the release result.

```bash
python -m pip install -e '.[disassembly,dynamic,symbolic,service,dev]'
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 make verify
```

`make verify` performs:

1. Python bytecode compilation for runtime, scripts, tests, and the integrated test suite.
2. Draft 2020-12 validation for every JSON Schema.
3. Validation of shipped compiler, harness, ABI, laboratory, benchmark, target-decision,
   integration, relink, and test-bundle examples.
4. Java syntax parsing for every Ghidra script.
5. Skill-frontmatter and release-contract validation.
6. The complete regression suite, including 0.2 and 0.3.1 compatibility contracts.

## Full integrated release harness

```bash
cd test-suite
python -m pip install -e '.[dev]'
x86decomp-test init-config \
  --toolkit-root .. \
  --output-root ./test-results \
  --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

Detection runs before prompting. Resolved adapters are never queried. Missing adapters
are offered a custom path, then optional consent-gated installation. Unavailable live
integrations are recorded as `BLOCKED`; strict mode exits `2` rather than reporting an
incomplete environment as passing.

## Package build

```bash
python -m build
python -m pip install dist/x86decomp_toolkit-0.4.0-py3-none-any.whl
x86decomp --help

python -m build test-suite
python -m pip install test-suite/dist/x86decomp_test_suite-0.4.0-py3-none-any.whl
x86decomp-test --help
```

The toolkit wheel contains the Python runtime and bundled ground-truth source cases.
The source distribution and source ZIP additionally contain Ghidra scripts, schemas,
examples, documentation, the skill, and the integrated test-suite source.

## Ghidra runtime verification

Java syntax parsing does not prove Ghidra runtime API compatibility. Test the exact
installed Ghidra release against an authorized PE:

```bash
GHIDRA_HOME=/path/to/ghidra \
  scripts/verify-ghidra.sh path/to/authorized-sample.exe /tmp/x86decomp-ghidra
```

The script imports and analyzes the PE, runs the maintained exporters, parses every
JSON/JSONL record, and checks required function artifacts.

## External backend verification

- `drcov-run` requires a compatible DynamoRIO installation and an executable runnable
  inside the selected isolation boundary.
- `angr-validate` requires the optional angr extra.
- historical MSVC profiles require operator-owned compiler installations.
- objdiff, relink, and whole-image results depend on the exact pinned external binary,
  configuration, and target evidence.
- container-backed workers require Docker or Podman and a declared immutable image.

Every external run records its argument array, executable identity/hash where
available, input and output hashes, environment policy, stdout, stderr, return code,
timeout, and isolation declaration.

## Release acceptance

A production release is not accepted solely because unit tests pass. The release gate
must also validate source manifests, architecture maps, compatibility contracts,
package clean installs, the integrated feature catalog, generated project templates,
project migration/recovery, reproducibility reports, and all declared live adapters.
