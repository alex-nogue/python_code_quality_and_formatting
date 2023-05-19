# python_code_quality_and_formatting

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains the settings to set up a set of python code elements listed below. It allows to set one's repository more easily with Python code quality, dependency manager, tests, and CI.

The repository will set the following elements:

Dependency manager:

- poetry

Continuous integration:

- CI (yml)

Tests:

- pytest

Code quality, formatting and validation:

- pylint
- black
- mypy
- pydantic
- isort
- pre-commit

- makefile
- dockerfile
- sonarqube
- semantic release

# Dependency manager

## Poetry

Poetry allows for an easier packaging and dependency manager. It will help us install dependencies in our project and resolve dependency issues. See https://python-poetry.org/.

It creates _pyproject.toml_, where dependencies and groups are configured, and creates a lock file _poetry.lock_ where all dependency versions are set.

One can run `poetry init` and let be guided or copy these two files.

# Code quality, formatting and validation

## pre-commit

pre-commit will perform checks whenever code is committed to the git repository. The checks are in general similar to what is to be checked in the CI, usually in code quality in formatting. https://pre-commit.com/

In pre-commit, we set hooks for every check we want pre-commit to perform. This confifuration is found in _.pre-commit-config.yaml_.

The pre-commit to work, one should run in their command line `pre-commit install`.

In addition to running the checks from the modules in this section (pylint, mypy etc), these are the checks performed by pre-commit:

- _trailing-whitespace_: lines of code shouldn't finish with spaces or tabs
- _end-of-file-fixer_: a file should end with one newline
- _check-yaml_: yaml files syntax must be parseable
- _check-added-large-files_: prevents large files from being committed
- _debug-statements_: to do not commit with debugger imports or calls


## black

black is a Python code formatter. Example of code formatting is having two line breaks after imports.
This way, we ensure every contributor to the repository commits code in same formatting rules.
