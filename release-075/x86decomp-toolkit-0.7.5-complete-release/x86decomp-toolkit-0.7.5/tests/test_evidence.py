from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from x86decomp.evidence import EvidenceStore
from x86decomp.models import ClaimState, EvidenceKind


class EvidenceTests(unittest.TestCase):
    def test_three_independent_sources_verify_claim(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            store = EvidenceStore(root)
            evidence = []
            for index, (kind, group) in enumerate(
                [
                    (EvidenceKind.BINARY_BYTES, "raw-image"),
                    (EvidenceKind.STATIC_ANALYSIS, "ghidra"),
                    (EvidenceKind.COMPILER_OUTPUT, "compiler"),
                ]
            ):
                path = root / f"e{index}.bin"
                path.write_bytes(bytes([index]))
                evidence.append(
                    store.add_evidence(
                        kind=kind,
                        source=group,
                        locator=f"loc-{index}",
                        assertion="supports the claim",
                        independent_group=group,
                        file_path=path,
                        evidence_id=f"ev-test-{index}",
                    )
                )
            claim = store.create_claim(
                subject="pe-rva:00001000",
                predicate="has_calling_convention",
                object_value="__cdecl",
                evidence_ids=[item.id for item in evidence],
                claim_id="cl-test-claim",
            )
            result = store.verify_claim(claim.id)
            self.assertEqual(result["state"], ClaimState.VERIFIED.value)
            self.assertEqual(result["failures"], [])

    def test_same_group_does_not_verify(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            store = EvidenceStore(root)
            ids = []
            for index in range(3):
                item = store.add_evidence(
                    kind=EvidenceKind.STATIC_ANALYSIS,
                    source="ghidra",
                    locator=f"loc-{index}",
                    assertion="supports",
                    independent_group="same-analyzer",
                    evidence_id=f"ev-same-{index}",
                )
                ids.append(item.id)
            claim = store.create_claim(
                subject="x",
                predicate="is",
                object_value="y",
                evidence_ids=ids,
                claim_id="cl-same-group",
            )
            result = store.verify_claim(claim.id)
            self.assertNotEqual(result["state"], ClaimState.VERIFIED.value)
            self.assertTrue(result["failures"])


if __name__ == "__main__":
    unittest.main()
