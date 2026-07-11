# Test and gate report

## Runtime tests

- 268/268 source inventory tests passed in six cache-disabled batches.
- Zero failures, errors, or skips.
- 21/21 packaged duplicate self-tests passed independently.
- 405/405 generated command examples parsed successfully against the live CLI.

## Static and generated gates

- Contract, schema, Java syntax, static lint, examples, skill, and release-shape validation: passed.
- Deterministic docstring report check: passed; 215 files, 0 missing, 0 generic, 0 repeated-leading-verb defects.
- Generated command reference check: passed; 166 root commands, 239 canonical routes, 405 parser nodes.
- Self-test synchronization: 6/6 pairs passed.
- Ruff: passed.
- Pyright: 0 errors, 0 warnings, 0 information diagnostics.
- Corpus synchronization: 24/24 files passed.
- MkDocs strict build: passed; only the upstream Material advisory about possible MkDocs 2.0 incompatibilities was emitted.

## Compatibility limit

The execution image did not provide CPython 3.11.0, and uv had no downloadable 3.11.0 build for this platform. The pre-3.11.4 `TarFile.extractall(path)` signature and modern filtered signature were both exercised directly; CI now pins 3.11.0.
