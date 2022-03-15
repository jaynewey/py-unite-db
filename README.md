# py-unite-db 

![GPL-2 Licensed](https://img.shields.io/badge/license-GPL--2-green)
[![.github/workflows/ci.yml](https://github.com/jaynewey/py-unite-db/actions/workflows/ci.yml/badge.svg)](https://github.com/jaynewey/py-unite-db/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/py-unite-db)](https://pypi.org/project/py-unite-db/)
[![Docs: MkDocs](https://img.shields.io/badge/docs-mkdocs-blue)](https://jaynewey.github.io/py-unite-db)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

> Unofficial Python wrapper for the unite-db.com REST API.

## Introduction

[`unite-db`](https://unite-db.com/) is a website dedicated to maintaining a database on various stats in the game Pokemon Unite including stats for Pokemon, Battle Items and Held Items.

This wrapper provides a simple, Pythonic interface to those stats via a REST API, with automatic result caching.

Please be warned that this is an unofficial wrapper and the REST API is a private one, so please do not abuse it.

If you are publishing any of the data collected with this API, please give credit to [`unite-db`](https://unite-db.com/). They spend many hours collecting this data.

### Installation

The package is installable via `pip`.

```sh
pip install py-unite-db
```

### Usage

Import the `UniteDb` object:

```python
from py_unite_db import UniteDb

unite_db = UniteDb()
```

Let's get the names of all supporter Pokemon:

```python
>>> [pokemon.name for pokemon in unite_db.pokemon if pokemon.role == "Supporter"]
['Blissey', 'Eldegoss', 'Mr.Mime', 'Wigglytuff']
```

## Contributing

This project uses [`pdm`](https://pdm.fming.dev).

```sh
$ pdm install
```

### Running the tests

The project uses [`pytest`](https://docs.pytest.org/).

```sh
$ pdm run pytest
```

### Type Checking

The project must pass [`mypy`](http://www.mypy-lang.org/) type checking.

```sh
$ pdm run typecheck
```

If you are using `mypy` with an IDE like VS Code make sure you have run

```sh
$ pdm run stubs
```

To work around `mypy` not supporting PEP582 yet. See https://github.com/python/mypy/issues/10633 for more info on this.

### Formatting

Imports are sorted with [`isort`](https://pycqa.github.io/isort/) and source files are formatted with [`black`](https://github.com/psf/black).

```sh
$ pdm run format
$ pdm run formatcheck
```

If you are using VS Code this will be automatically done on save.

### Linting

Linting is provided by [`flake8`](github.com/pycqa/flake8).

```sh
$ pdm run lint
```

### Conventional Commits

The project follows the conventional commit style.

### Docs

This project uses [`mkdocs`](https://mkdocs.org), [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings/), [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) for its documentation.

```sh
$ pdm run fetch_charm
$ pdm run mkdocs serve
```
