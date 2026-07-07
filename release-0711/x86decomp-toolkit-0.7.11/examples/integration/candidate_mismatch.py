"""Negative integration fixture whose add function intentionally mismatches target behavior."""
def add(a: int, b: int) -> int:
    """Return an intentionally different result for mismatch-demo evidence."""
    return a - b
