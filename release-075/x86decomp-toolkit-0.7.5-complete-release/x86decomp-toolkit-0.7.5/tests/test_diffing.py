from __future__ import annotations

import unittest

from x86decomp.diffing import compare_bytes


class DiffingTests(unittest.TestCase):
    def test_equal(self) -> None:
        report = compare_bytes(b"abc", b"abc")
        self.assertTrue(report["equal"])
        self.assertEqual(report["matching_prefix_bytes"], 3)
        self.assertFalse(report["semantic_equivalence_claimed"])

    def test_mismatch(self) -> None:
        report = compare_bytes(b"abc", b"axc")
        self.assertFalse(report["equal"])
        self.assertEqual(report["reported_mismatches"][0]["offset"], 1)


if __name__ == "__main__":
    unittest.main()
