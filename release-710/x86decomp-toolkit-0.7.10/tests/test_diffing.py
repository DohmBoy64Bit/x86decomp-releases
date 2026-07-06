"""Verify the current toolkit behavior covered by `tests/test_diffing.py`."""
from __future__ import annotations

import unittest

from x86decomp.diffing import compare_bytes


class DiffingTests(unittest.TestCase):
    """Coordinate diffing tests behavior for the current toolkit workflow."""
    def test_equal(self) -> None:
        """Verify equal behavior."""
        report = compare_bytes(b"abc", b"abc")
        self.assertTrue(report["equal"])
        self.assertEqual(report["matching_prefix_bytes"], 3)
        self.assertFalse(report["semantic_equivalence_claimed"])

    def test_mismatch(self) -> None:
        """Verify mismatch behavior."""
        report = compare_bytes(b"abc", b"axc")
        self.assertFalse(report["equal"])
        self.assertEqual(report["reported_mismatches"][0]["offset"], 1)


if __name__ == "__main__":
    unittest.main()
