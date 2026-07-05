"""Provide tests.test_diffing functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import unittest

from x86decomp.diffing import compare_bytes


class DiffingTests(unittest.TestCase):
    """Implement the DiffingTests class using its declared base class contract.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def test_equal(self) -> None:
        """Verify equal.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        report = compare_bytes(b"abc", b"abc")
        self.assertTrue(report["equal"])
        self.assertEqual(report["matching_prefix_bytes"], 3)
        self.assertFalse(report["semantic_equivalence_claimed"])

    def test_mismatch(self) -> None:
        """Verify mismatch.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        report = compare_bytes(b"abc", b"axc")
        self.assertFalse(report["equal"])
        self.assertEqual(report["reported_mismatches"][0]["offset"], 1)


if __name__ == "__main__":
    unittest.main()
