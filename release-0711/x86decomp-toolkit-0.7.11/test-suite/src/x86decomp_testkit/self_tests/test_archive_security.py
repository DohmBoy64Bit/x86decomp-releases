"""Provide test archive security support for the standalone verification harness."""
from __future__ import annotations

import io
import tarfile
import zipfile
from pathlib import Path

import pytest

from x86decomp_testkit.adapters.download import safe_extract_archive, select_release_asset


def test_safe_zip_and_tar_extraction(tmp_path: Path) -> None:
    """Verify safe zip and tar extraction behavior."""
    zip_path = tmp_path / "ok.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("root/file.txt", "ok")
    out = tmp_path / "zip-out"
    safe_extract_archive(zip_path, out)
    assert (out / "root" / "file.txt").read_text() == "ok"

    tar_path = tmp_path / "ok.tar.gz"
    with tarfile.open(tar_path, "w:gz") as tf:
        data = b"ok"
        info = tarfile.TarInfo("root/file.txt")
        info.size = len(data)
        tf.addfile(info, io.BytesIO(data))
    out2 = tmp_path / "tar-out"
    safe_extract_archive(tar_path, out2)
    assert (out2 / "root" / "file.txt").read_bytes() == b"ok"


def test_rejects_traversal_and_links(tmp_path: Path) -> None:
    """Verify rejects traversal and links behavior."""
    bad = tmp_path / "bad.zip"
    with zipfile.ZipFile(bad, "w") as zf:
        zf.writestr("../escape", "bad")
    with pytest.raises(RuntimeError, match="unsafe archive path"):
        safe_extract_archive(bad, tmp_path / "out")

    link_tar = tmp_path / "link.tar.gz"
    with tarfile.open(link_tar, "w:gz") as tf:
        info = tarfile.TarInfo("link")
        info.type = tarfile.SYMTYPE
        info.linkname = "/tmp/target"
        tf.addfile(info)
    with pytest.raises(RuntimeError, match="links are not permitted"):
        safe_extract_archive(link_tar, tmp_path / "out2")


def test_release_asset_selection_is_deterministic() -> None:
    """Verify release asset selection is deterministic behavior."""
    release = {"assets": [
        {"name": "tool-linux-x86_64-small.zip", "size": 10},
        {"name": "tool-linux-x86_64.zip", "size": 100},
    ]}
    assert select_release_asset(release, ("linux", "x86_64"))["size"] == 100
    with pytest.raises(RuntimeError):
        select_release_asset(release, ("windows",))

def test_download_file_hash_and_size_limit(tmp_path: Path) -> None:
    """Verify download file hash and size limit behavior."""
    from x86decomp_testkit.adapters.download import download_file
    import hashlib

    source = tmp_path / "source.bin"
    source.write_bytes(b"abc")
    destination = tmp_path / "download.bin"
    digest = download_file(source.as_uri(), destination, max_bytes=3)
    assert destination.read_bytes() == b"abc"
    assert digest == hashlib.sha256(b"abc").hexdigest()
    with pytest.raises(RuntimeError, match="too large|exceeded"):
        download_file(source.as_uri(), tmp_path / "too-small.bin", max_bytes=2)
