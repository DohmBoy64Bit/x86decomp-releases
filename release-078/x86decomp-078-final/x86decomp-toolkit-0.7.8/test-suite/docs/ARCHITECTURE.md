# Test-suite architecture — 0.7.8

Configuration feeds adapter resolution and the orchestrator. The orchestrator runs recursive inventory, built-in tests, command probes, schema and Java checks, coverage, packaging, installation, and external adapter suites through the safe process runner. Results are normalized to PASS, FAIL, ERROR, or BLOCKED and written as JSON, Markdown, HTML, JUnit, and log evidence.
