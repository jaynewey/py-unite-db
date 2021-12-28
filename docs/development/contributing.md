# Contributing

This project uses [`pdm`](https://pdm.fming.dev).

```sh
$ pdm install
```

## Running the tests

The project uses [`pytest`](https://docs.pytest.org/).

```sh
$ pdm run pytest
```

## Type Checking

The project must pass [`mypy`](http://www.mypy-lang.org/) type checking.

```sh
$ pdm run typecheck
```

If you are using `mypy` with an IDE like VS Code make sure you have run

```sh
$ pdm run stubs
```

To work around `mypy` not supporting PEP582 yet. See [https://github.com/python/mypy/issues/10633]() for more info on this.

## Formatting

Imports are sorted with [`isort`](https://pycqa.github.io/isort/) and source files are formatted with [`black`](https://github.com/psf/black).

```sh
$ pdm run format
$ pdm run formatcheck
```

If you are using VS Code this will be automatically done on save.

## Linting

Linting is provided by [`flake8`](github.com/pycqa/flake8).

```sh
$ pdm run lint
```

## Conventional Commits

The project follows the conventional commit style.

## Docs

This project uses [`mkdocs`](https://mkdocs.org), [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings/), [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) for its documentation.

```sh
$ pdm run fetch_charm
$ pdm run mkdocs serve
```
