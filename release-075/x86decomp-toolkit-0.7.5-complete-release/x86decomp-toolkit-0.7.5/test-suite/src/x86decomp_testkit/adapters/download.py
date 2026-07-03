from __future__ import annotations

import hashlib
import json
import os
import platform
import shutil
import stat
import tarfile
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any


USER_AGENT = "x86decomp-test-suite/0.7.5"


def platform_key() -> str:
    system = platform.system().lower()
    machine = platform.machine().lower()
    if machine in {"amd64", "x86_64"}:
        machine = "x86_64"
    elif machine in {"arm64", "aarch64"}:
        machine = "arm64"
    return f"{system}-{machine}"


def github_latest_release(repository: str, timeout: int = 30) -> dict[str, Any]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/releases/latest",
        headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.load(response)
    if not isinstance(data, dict) or not isinstance(data.get("assets"), list):
        raise RuntimeError(f"unexpected GitHub release response for {repository}")
    return data


def select_release_asset(release: dict[str, Any], required_tokens: tuple[str, ...]) -> dict[str, Any]:
    tokens = tuple(token.lower() for token in required_tokens)
    matches = []
    for asset in release.get("assets", []):
        name = str(asset.get("name", ""))
        lower = name.lower()
        if all(token in lower for token in tokens):
            matches.append(asset)
    if not matches:
        names = [str(asset.get("name", "")) for asset in release.get("assets", [])]
        raise RuntimeError(f"no release asset matched tokens {tokens}; available assets: {names}")
    matches.sort(key=lambda item: int(item.get("size", 0)), reverse=True)
    return matches[0]


def download_file(url: str, destination: Path, max_bytes: int = 2_000_000_000) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    digest = hashlib.sha256()
    total = 0
    try:
        with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as output:
            length = response.headers.get("Content-Length")
            if length is not None and int(length) > max_bytes:
                raise RuntimeError(f"download is too large: {length} bytes")
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                total += len(chunk)
                if total > max_bytes:
                    raise RuntimeError(f"download exceeded maximum size of {max_bytes} bytes")
                output.write(chunk)
                digest.update(chunk)
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    return digest.hexdigest()


def _safe_destination(root: Path, member_name: str) -> Path:
    pure = PurePosixPath(member_name.replace("\\", "/"))
    if pure.is_absolute() or ".." in pure.parts:
        raise RuntimeError(f"unsafe archive path: {member_name}")
    destination = (root / Path(*pure.parts)).resolve()
    root_resolved = root.resolve()
    if destination != root_resolved and root_resolved not in destination.parents:
        raise RuntimeError(f"archive path escapes destination: {member_name}")
    return destination


def safe_extract_archive(archive: Path, destination: Path, max_members: int = 200_000) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    lower = archive.name.lower()
    if lower.endswith(".exe"):
        shutil.copy2(archive, destination / archive.name)
        return
    if lower.endswith(".zip"):
        with zipfile.ZipFile(archive) as handle:
            infos = handle.infolist()
            if len(infos) > max_members:
                raise RuntimeError("archive contains too many members")
            for info in infos:
                target = _safe_destination(destination, info.filename)
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode):
                    raise RuntimeError(f"symbolic links are not permitted in downloaded archives: {info.filename}")
                if info.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with handle.open(info) as source, target.open("wb") as output:
                    shutil.copyfileobj(source, output)
                if mode & stat.S_IXUSR:
                    target.chmod(target.stat().st_mode | stat.S_IXUSR)
        return
    if lower.endswith((".tar.gz", ".tgz", ".tar.xz", ".tar.bz2")):
        with tarfile.open(archive, "r:*") as handle:
            members = handle.getmembers()
            if len(members) > max_members:
                raise RuntimeError("archive contains too many members")
            for member in members:
                if member.issym() or member.islnk():
                    raise RuntimeError(f"links are not permitted in downloaded archives: {member.name}")
                target = _safe_destination(destination, member.name)
                if member.isdir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                if not member.isfile():
                    continue
                source = handle.extractfile(member)
                if source is None:
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with source, target.open("wb") as output:
                    shutil.copyfileobj(source, output)
                if member.mode & stat.S_IXUSR:
                    target.chmod(target.stat().st_mode | stat.S_IXUSR)
        return
    raise RuntimeError(f"unsupported release archive format: {archive.name}")
