# python_code_quality_and_formatting

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

# Dependency manager

## Poetry

Poetry allows for an easier packaging and dependency manager. It will help us install dependencies in our project and resolve dependency issues. See https://python-poetry.org/.

It creates _pyproject.toml_, where dependencies and groups are configured, and creates a lock file _poetry.lock_ where all dependency versions are set.

One can run _poetry init_ and let be guided or copy these two files.
