"""Unit tests for :func:`x86decomp.diffing.compare_bytes`."""
from __future__ import annotations

import unittest

from x86decomp.diffing import compare_bytes


class DiffingTests(unittest.TestCase):
    """Tests for byte-level comparison reporting produced by ``compare_bytes``."""
    def test_equal(self) -> None:
        """Identical byte strings compare equal with a full matching prefix and no semantic claim."""
        report = compare_bytes(b"abc", b"abc")
        self.assertTrue(report["equal"])
        self.assertEqual(report["matching_prefix_bytes"], 3)
        self.assertFalse(report["semantic_equivalence_claimed"])

    def test_mismatch(self) -> None:
        """Differing byte strings report unequal with the first mismatch offset recorded."""
        report = compare_bytes(b"abc", b"axc")
        self.assertFalse(report["equal"])
        self.assertEqual(report["reported_mismatches"][0]["offset"], 1)


if __name__ == "__main__":
    unittest.main()
