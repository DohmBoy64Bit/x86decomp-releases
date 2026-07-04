# Command Reference Strict Audit

This audit was generated from the v0.7.8 toolkit parser and the v0.7.8 verification-harness parser. It checks command-page coverage, exact usage strings, source hashes, unfinished markers, stale version references, and command Markdown hashes.

## Result

PASS

## Counts

| Metric | Value |
| --- | --- |
| Toolkit root commands | 166 |
| Canonical groups | 59 |
| Canonical routes | 239 |
| Verification harness commands | 6 |
| Command Markdown pages | 168 |
| Exact usage records checked | 411 |
| Command Markdown hashes | 168 |
| Errors | 0 |

## Source basis

| Parser source | SHA-256 |
| --- | --- |
| `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
| `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |
| `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |
| `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |
| `src/x86decomp/assembly/cli.py` | `6c8a227f8c1a9c48a83e1f048f6160f8740e97552fa6967dea122f42fab45f88` |
| `test-suite/src/x86decomp_testkit/cli.py` | `c4be8f226c0b7067846b385618b2392017fbbb113082016b4d72855098b07c44` |

## Coverage statement

Every live `x86decomp` root command has a command page; every canonical routed action on those pages has an exact parser-derived usage string and canonical owner; the `x86decomp-test` page includes every verification-harness subcommand, including `capabilities`; and every command Markdown file is represented in the command hash manifest.
