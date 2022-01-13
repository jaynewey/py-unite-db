"""Usage: `stubs.py <path to project directory>`"""

import os
import sys
from contextlib import suppress
from pathlib import Path
from shutil import rmtree


def stubs(dir: Path):
    """Collect library stubs and symlink, then ignore missing import errors.

    This should be run after adding any library stubs e.g `types-requests`.

    To work around [this issue](https://github.com/python/mypy/issues/10633).

    Original code by `pawamoy`:

    [https://github.com/python/mypy/issues/10633#issuecomment-974840203]()

    and extended by `jaynewey`.
    """

    os.chdir(str(dir))

    # compute packages directory path
    py = f"{sys.version_info.major}.{sys.version_info.minor}"
    pkgs_dir = Path("__pypackages__", py, "lib").resolve()

    # build the list of available packages
    packages = {}
    for package in pkgs_dir.glob("*"):
        if (
            package.suffix not in {".dist-info", ".pth"}
            and package.name != "__pycache__"
        ):
            packages[package.name] = package

    # handle .pth files
    for pth in pkgs_dir.glob("*.pth"):
        with suppress(OSError):
            for package in Path(Path(pth).read_text().splitlines()[0]).glob("*"):
                if package.suffix != ".dist-info":
                    packages[package.name] = package

    stub_dir = Path(".stubs/")
    rmtree(stub_dir, ignore_errors=True)
    stub_dir.mkdir(parents=True, exist_ok=True)

    # symlink the stubs
    ignore = set()
    for stubs in (path for name, path in packages.items() if name.endswith("-stubs")):
        Path(stub_dir, stubs.name).symlink_to(stubs, target_is_directory=True)
        # try to symlink the corresponding package
        # see https://www.python.org/dev/peps/pep-0561/#stub-only-packages
        pkg_name = stubs.name.replace("-stubs", "")
        if pkg_name in packages:
            ignore.add(pkg_name)
            Path(stub_dir, pkg_name).symlink_to(
                packages[pkg_name], target_is_directory=True
            )

    # create temporary mypy config to ignore stubbed packages
    mypy_config = Path("mypy.ini")
    config_contents = mypy_config.read_text() if mypy_config.exists() else ""
    config_contents += "\n[mypy]\nmypy_path = $MYPY_CONFIG_FILE_DIR\n"
    config_contents += "\n" + "\n\n".join(
        f"[mypy-{pkg}.*]\nignore_errors=true" for pkg in ignore
    )
    Path(stub_dir, "mypy.ini").write_text(config_contents)


def _main(argv: list[str]):
    if not argv:
        sys.exit("Usage: stubs.py <path to project directory>")
    stubs(Path(argv[0]))


if __name__ == "__main__":
    _main(sys.argv[1:])
