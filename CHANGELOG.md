# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project tries to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Historic and pre-release versions aren't necessarily included.


## [UNRELEASED] - TBC

### Added

- `Event.Recipients` and nested classes

### Fixed

- Example code in README


## [0.9.1] - 2024-05-10

### Changed

- Docstring and README improvements

### Fixed

- `Member`, `Role`, `Subgroup` removed in error from top-level namespace

- Docstring and README errors


## [0.9.0] - 2024-05-09

### Changed

- BREAKING CHANGES: Significantly revised API - see README for details.

- Rewritten from scratch using Pydantic; much closer to API data structure

### Removed

- Support for Python 3.8, 3.9


## [0.8.1] - 2024-05-03

### Added

- Support for Python 3.12 in GitHub CI

### Changed

- Refactors; test improvements

- Use `ruff format` instead of `isort` + `black` in CI/pre-commit

- Update dev/test dependencies: mypy, pre-commit-hooks, pytest, ruff, types-python-dateutil

- Update CI dependencies: actions/setup_python

### Fixed

- `Member.__repr__` follows same pattern as other classes

### Removed

- dev/test dependencies: black, isort


## [0.8.0] - 2023-11-25

### Added

- `Member.email`, `.phone_number`, `.profile_uid` attributes

### Changed

- Simplify/rearrange tests

- Update dev/test dependencies: black, mypy, pytest, ruff, types-python-dateutil


## [0.7.3] - 2023-09-27

### Added

- Documentation: Update README for install from PyPI instead of GitHub

### Fixed

- Missing/outdated/broken package metadata


## [0.7.2] - 2023-09-26

### Added

- Documentation: This changelog

- Enforce linting with isort, black and ruff in CI using GitHub Actions

### Changed

- Update dev/test dependencies: ruff


[0.9.1]: https://github.com/elliot-100/Spond-classes/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/elliot-100/Spond-classes/compare/v0.8.1...v0.9.0
[0.8.1]: https://github.com/elliot-100/Spond-classes/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/elliot-100/Spond-classes/compare/v0.7.3...v0.8.0
[0.7.3]: https://github.com/elliot-100/Spond-classes/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/elliot-100/Spond-classes/compare/v0.7.1...v0.7.2
