# Test-suite security model — 0.4.0

## Default deny

The suite defaults to no network, no installation, no target-native execution, no
undeclared environment inheritance, and no privileged package-manager action.
Installation and network consent are separate flags.

## Process boundaries

Tests execute toolkit commands, compilers, linkers, adapter probes, a suite-generated
minimal PE through Ghidra static analysis, and a harmless suite-owned host fixture under
DynamoRIO. They do not natively launch an analyzed user PE. Every subprocess uses an
argument array, timeout, dedicated log directory, and separate stdout/stderr files.

`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` isolates release pytest runs from unrelated host
plugins. This is deterministic test isolation, not a native-code sandbox.

## Workers and containers

Local resource limits mitigate accidental CPU/memory/output exhaustion but are not a
security boundary. Container-backed tests require Docker/Podman, an explicit image,
network policy, mount policy, and operator trust in the runtime/daemon. Unknown native
artifacts should be handled in an appropriately isolated VM/container environment.

## Downloads and installers

Network downloads record source, release, asset, destination, size, and SHA-256; enforce
bounds; and reject traversal, absolute paths, links, and special files. Package-manager
commands are displayed/logged and may require elevation. The suite never captures an
administrator password.

## Dependency audit and SBOM

The toolkit can generate a CycloneDX-formatted environment inventory and invoke
pip-audit when installed. A clean audit is evidence about the scanned dependency set at
the recorded time, not a guarantee that no vulnerability exists.

## Logs and secrets

Logs contain commands, local paths, versions, selected environment data, and tool
output. Do not place credentials in paths, arguments, adapter configuration, or custom
environment values. Review reports before publication.
