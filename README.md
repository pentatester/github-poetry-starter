# Github Poetry Starter

GitHub Actions starter for python with [python-poetry](https://github.com/python-poetry/poetry).

The [complete documentation](https://python-poetry.org/docs/) of python-poetry is available on the [official website](https://python-poetry.org).

- [Github Poetry Starter](#github-poetry-starter)
  - [Publish to pypi](#publish-to-pypi)
  - [Dependency](#dependency)
    - [Update dependencies](#update-dependencies)
    - [Install dependency](#install-dependency)
    - [Remove dependency](#remove-dependency)
    - [Export requirements.txt](#export-requirementstxt)

## Publish to pypi

You need to have [PyPI](https://pypi.org/ "PyPI - Python Package Index") account.

```bash
poetry publish --build
```

## Dependency

### Update dependencies

```bash
poetry update
```

### Install dependency

```bash
poetry add requests
```

For dev requirement

```bash
poetry add requests --dev
```

### Remove dependency

```bash
poetry remove requests
```

For dev requirement

```bash
poetry remove requests --dev
```

### Export requirements.txt

`-o` for output.

```bash
poetry export -f requirements.txt -o requirements.txt --without-hashes
```

For dev requirements

```bash
poetry export -f requirements.txt -o requirements-dev.txt --dev --without-hashes
```
