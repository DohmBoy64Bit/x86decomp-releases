from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pe_fixture import build_minimal_pe32
from x86decomp.errors import FormatError
from x86decomp.pe32 import parse_pe32


class PE32Tests(unittest.TestCase):
    def test_parse_minimal_i386_image(self) -> None:
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
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "not.exe"
            path.write_bytes(b"not a pe")
            with self.assertRaises(FormatError):
                parse_pe32(path)


if __name__ == "__main__":
    unittest.main()
