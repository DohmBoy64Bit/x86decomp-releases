"""Provide tests.test_pe32 functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pe_fixture import build_minimal_pe32
from x86decomp.errors import FormatError
from x86decomp.pe32 import parse_pe32


class PE32Tests(unittest.TestCase):
    """Implement the PE32Tests class using its declared base class contract.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def test_parse_minimal_i386_image(self) -> None:
        """Verify parse minimal i386 image.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with tempfile.TemporaryDirectory() as temp:
            binary = build_minimal_pe32(Path(temp) / "sample.exe")
            image = parse_pe32(binary)
            self.assertEqual(image.machine, 0x014C)
            self.assertEqual(image.image_base, 0x00400000)
            self.assertEqual(image.entry_rva, 0x1000)
            self.assertEqual(image.entry_va, 0x00401000)
            self.assertEqual(len(image.sections), 1)
            self.assertEqual(image.sections[0].name, ".text")
            self.assertEqual(image.imports, ())

    def test_reject_non_pe(self) -> None:
        """Verify reject non pe.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "not.exe"
            path.write_bytes(b"not a pe")
            with self.assertRaises(FormatError):
                parse_pe32(path)


if __name__ == "__main__":
    unittest.main()
