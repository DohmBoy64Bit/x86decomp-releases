"""Provide tests.test_test_bundle functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path

import pytest

from pe_fixture import build_minimal_pe32
from x86decomp.errors import ContractError, VerificationError
from x86decomp.test_bundle import MANIFEST_NAME, inspect_test_bundle
from x86decomp.util import sha256_file


def _bundle(tmp_path: Path, *, corrupt_hash: bool = False) -> Path:
    """Implement bundle.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    target = build_minimal_pe32(tmp_path / "target.exe")
    manifest = {
        "schema_version": 1,
        "name": "minimal-authorized-pe32",
        "description": "Synthetic parser regression input",
        "authorization": {
            "owner_or_authorized": True,
            "statement": "Synthetic file created by this test and authorized for analysis."
        },
        "expected_architecture": "x86",
        "artifacts": [{
            "path": "files/target.exe",
            "role": "primary_image",
            "sha256": "0" * 64 if corrupt_hash else sha256_file(target),
        }],
    }
    bundle = tmp_path / "bundle.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(MANIFEST_NAME, json.dumps(manifest))
        archive.write(target, "files/target.exe")
    return bundle


def test_static_test_bundle_inspection(tmp_path: Path) -> None:
    """Verify static test bundle inspection.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    report_path = tmp_path / "report.json"
    report = inspect_test_bundle(_bundle(tmp_path), report_path=report_path)
    assert report["passed"]
    assert report["static_analysis_only"]
    assert report["supplied_code_executed"] is False
    assert report["analyses"]["pe_images"][0]["pe"]["architecture"] == "x86"
    assert report_path.is_file()


def test_test_bundle_hash_is_enforced(tmp_path: Path) -> None:
    """Verify test bundle hash is enforced.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    with pytest.raises(VerificationError, match="hash mismatch"):
        inspect_test_bundle(_bundle(tmp_path, corrupt_hash=True))


def test_test_bundle_rejects_path_traversal(tmp_path: Path) -> None:
    """Verify test bundle rejects path traversal.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    bundle = tmp_path / "bad.zip"
    manifest = {
        "schema_version": 1,
        "authorization": {"owner_or_authorized": True, "statement": "Synthetic test."},
        "artifacts": [{"path": "files/a.exe", "role": "primary_image"}],
    }
    with zipfile.ZipFile(bundle, "w") as archive:
        archive.writestr(MANIFEST_NAME, json.dumps(manifest))
        archive.writestr("../escape.exe", b"MZ")
        archive.writestr("files/a.exe", b"MZ")
    with pytest.raises(ContractError, match="unsafe ZIP member"):
        inspect_test_bundle(bundle)


def test_test_bundle_requires_authorization(tmp_path: Path) -> None:
    """Verify test bundle requires authorization.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    target = build_minimal_pe32(tmp_path / "target.exe")
    manifest = {
        "schema_version": 1,
        "authorization": {"owner_or_authorized": False, "statement": "No authorization."},
        "artifacts": [{"path": "target.exe", "role": "primary_image"}],
    }
    bundle = tmp_path / "unauthorized.zip"
    with zipfile.ZipFile(bundle, "w") as archive:
        archive.writestr(MANIFEST_NAME, json.dumps(manifest))
        archive.write(target, "target.exe")
    with pytest.raises(ContractError, match="owner_or_authorized"):
        inspect_test_bundle(bundle)


def test_create_test_bundle_round_trip(tmp_path: Path) -> None:
    """Verify create test bundle round trip.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    from x86decomp.test_bundle import create_test_bundle

    target = build_minimal_pe32(tmp_path / "target.exe")
    output = tmp_path / "created.zip"
    created = create_test_bundle(
        output,
        artifacts=[("primary_image", target)],
        authorization_statement="Synthetic test artifact owned by the test suite.",
        name="created-test",
        expected_architecture="x86",
    )
    assert created["static_verification_passed"]
    inspected = inspect_test_bundle(output)
    assert inspected["passed"]
    assert inspected["bundle"]["name"] == "created-test"
