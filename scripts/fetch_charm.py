"""Usage: `fetch_charm.py <path to assets folder>`"""

import os
import shutil
import sys
import tarfile
from pathlib import Path

import requests

_REPO_BASE_URL = "https://github.com/jaynewey/charm-icons"
_LATEST_RELEASE_URL = f"{_REPO_BASE_URL}/releases/latest"
_RELEASES_URL = f"{_REPO_BASE_URL}/archive/refs/tags/"


def fetch_charm(dir: Path):
    """Fetches all Charm icons and puts in specified folder.

    Fetches from latest GitHub release.

    See [Charm Icons](https://github.com/jaynewey/charm-icons).

    Args:
        dir: The directory to store the icons in. Will store at '{dir}/charm/'.
    """

    # first do some checks - if we don't have to fetch, don't
    # if the directory {dir}/charm exists and is not empty, do not fetch
    charm_dir = dir / "charm"
    if charm_dir.is_dir() and any(charm_dir.iterdir()):
        return

    # else, begin our procedure
    os.chdir(str(dir))
    version = (requests.get(_LATEST_RELEASE_URL).url).split("/")[-1]

    tar = requests.get(f"{_RELEASES_URL}/{version}.tar.gz", stream=True)
    file = tarfile.open(fileobj=tar.raw, mode="r|gz")
    file.extractall()
    shutil.rmtree("charm/", ignore_errors=True)
    shutil.copytree(f"charm-icons-{version[1:]}/icons/", "charm/")
    shutil.rmtree(f"charm-icons-{version[1:]}/")


def _main(argv: list[str]):
    if not argv:
        sys.exit("Usage: fetch_charm.py <path to assets folder>")
    fetch_charm(Path(argv[0]))


if __name__ == "__main__":
    _main(sys.argv[1:])
