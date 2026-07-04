# Test-suite maintenance contract — 0.7.8

Every product change must update the current catalog, tests, docs, schemas, skill, package metadata, and all four architecture artifacts together.

Do not add release-numbered catalogs, delta catalogs, compatibility baselines, version-specific executables, source-tree installers, overlays, or upgrade reports. The verifier must recurse through all current capability packages and nested schemas.

New functions and methods must be cataloged and executed. New commands and routes must be process-tested. New external integrations must define honest adapter detection and BLOCKED behavior. Skips remain forbidden.
