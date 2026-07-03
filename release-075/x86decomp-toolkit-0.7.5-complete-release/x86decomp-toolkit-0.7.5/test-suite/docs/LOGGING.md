# Logging contract — 0.7.5

Each run receives a unique directory. Human-readable logs and structured JSONL events record command arguments, working directory, start and finish times, return codes, bounded output paths, adapter resolution, and result status. Secrets must be redacted. Evidence files are never overwritten by a later run.
