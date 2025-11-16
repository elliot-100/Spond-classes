# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project tries to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Historic and pre-release versions aren't necessarily included.


## [0.17.0] - 2025-11-16

### Added

- `Member.fields`; basic support for `Group.field_defs`
- Raise TypeError if a non-dict is passed to `Event|Group.from_dict()`

### Changed

- Update dev/test dependencies


## [0.16.1] - 2025-10-08

### Changed

- Tests: minor improvements
- CI/CD:
  - Add Python 3.14 to matrix
  - Only publish documentation site on release
  - Update dependencies
- Update dev dependencies


## [0.16.0] - 2025-07-05

### Added

- `typing` (previously `types_`) module to public API

### Changed

- BREAKING CHANGES: `uid` is used consistently instead of `id`:
  `Event.member|role|subgroup_by_id()` are now `Event.member|role|subgroup_by_uid()`  
- `Event.type` is Literal instead of Enum
- CI: run with read permissions
- Update dev dependencies

### Removed

- `spond_classes.EventType`


## [0.15.0] - 2025-03-05

### Added

- Add support for 'availability request' events
- Add `Event.hidden` attribute; `Event.is_cancelled`, `Event.is_hidden` properties

### Changed

- Rename `types` to `types_` as it shadowed a built-in
- Update dev dependencies mypy, pre-commit, pytest, ruff


## [0.14.0] - 2024-12-27

### Added

- Explicit constructors `Event.from_dict()`, `Group.from_dict()`
- Tests: missing tests for `Profile` optional attributes; simplify `Event` tests

### Changed

- Email attributes are Pydantic `EmailStr` type
- Docs: be explicit when referring to Spond API; attributes aren't 'optional', they 'may not be present'.
- Update dev dependencies: mypy, pdoc, pytest, ruff


## [0.13.1] - 2024-11-19

### Changed

- Remove upper bound on Python version
- Docs: add intro, highlight `Event` and `Group` classes
- Tests: instantiate with `MyClass(**dict)` instead of Pydantic internals; refactor fixtures


## [0.13.0] - 2024-11-04

### Added

- Event `Responses` to public API
- API documentation at https://elliot-100.github.io/Spond-classes/

### Changed

- Update dev dependencies: mypy, ruff
- Docs: don't document Pydantic internals


## [0.12.0] - 2024-10-11

### Added

- Add `Profile` to public API, with additional attributes: `email`, `first_name`,
  `last_name`, `phone_nunber`, property `full_name`
- Support for Python 3.13
- Docs: pdoc-generated HTML documentation in `/docs`

### Changed

- Update dev dependencies: pdoc, pre-commit, ruff
- Dependencies: remove pydantic version upper bound


## [0.11.2] - 2024-09-16

### Fixed

- Hotfix: pdoc wouldn't render; solved by setting Pydantic dependency < 2.9


## [0.11.1] - 2024-09-16

#### Added

- Tests for `Group.member|role|subgroup_by_id()` when `Group.members|roles|subgroups`
  is empty

### Changed

- Dev dependencies: add pdoc; update mypy, ruff, pytest

### Removed

- Explicit dependency on spond


## [0.11.0] - 2024-07-17

### Added

- `Event` attributes: `cancelled`, `created_time`, `end_time`, `invite_time`, `type`,
  property `url`

### Changed

- Public API is defined using `__all__` instead of import aliasing, which improves e.g.
  documentation handling in IDEs
- Consistent pattern for all classes' string representation, including full `uid`
- Simplified and improved docstrings
- Dependencies: remove upper bounds for simplicity; drop redundant python-dateutil
- Dev dependencies: drop redundant types-python-dateutil

### Fixed

- Tests didn't import from the top-level namespace, i.e. didn't use public API


## [0.10.1] - 2024-07-02

### Changed

- Update dev dependencies: ruff, pre-commit-hooks

### Fixed

- Docs: licence classifier, docstring omissions, backticks and paragraph breaks


## [0.10.0] - 2024-06-19

### Changed

- Dependencies: allow `spond` >= 1


## [0.9.2] - 2024-06-09

### Changed

- `Group.members_by_role|subgroup()` raises ValueError if passed instances
  aren't compatible
- Tests for `Group.member|role|subgroup_by_id()`, `Group.members_by_role|subgroup()`
- Update dev dependency: pre-commit-hooks

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

- BREAKING CHANGES: Significantly revised API - see README for details
- Rewritten from scratch using Pydantic; much closer to API data structure

### Removed

- Support for Python 3.8, 3.9


## [0.8.1] - 2024-05-03

### Added

- Support for Python 3.12 in GitHub CI

### Changed

- Refactors; test improvements
- Use `ruff format` instead of `isort` + `black` in CI/pre-commit
- Update dev/test dependencies: mypy, pre-commit-hooks, pytest, ruff,
  types-python-dateutil
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


[0.17.0]: https://github.com/elliot-100/Spond-classes/compare/v0.16.1...v0.17.0
[0.16.1]: https://github.com/elliot-100/Spond-classes/compare/v0.16.0...v0.16.1
[0.16.0]: https://github.com/elliot-100/Spond-classes/compare/v0.15.0...v0.16.0
[0.15.0]: https://github.com/elliot-100/Spond-classes/compare/v0.14.0...v0.15.0
[0.14.0]: https://github.com/elliot-100/Spond-classes/compare/v0.13.1...v0.14.0
[0.13.1]: https://github.com/elliot-100/Spond-classes/compare/v0.13.0...v0.13.1
[0.13.0]: https://github.com/elliot-100/Spond-classes/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/elliot-100/Spond-classes/compare/v0.11.2...v0.12.0
[0.11.2]: https://github.com/elliot-100/Spond-classes/compare/v0.11.1...v0.11.2
[0.11.1]: https://github.com/elliot-100/Spond-classes/compare/v0.11.0...v0.11.1
[0.11.0]: https://github.com/elliot-100/Spond-classes/compare/v0.10.1...v0.11.0
[0.10.1]: https://github.com/elliot-100/Spond-classes/compare/v0.10.0...v0.10.1
[0.10.0]: https://github.com/elliot-100/Spond-classes/compare/v0.9.2...v0.10.0
[0.9.2]: https://github.com/elliot-100/Spond-classes/compare/v0.9.1...v0.9.2
[0.9.1]: https://github.com/elliot-100/Spond-classes/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/elliot-100/Spond-classes/compare/v0.8.1...v0.9.0
[0.8.1]: https://github.com/elliot-100/Spond-classes/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/elliot-100/Spond-classes/compare/v0.7.3...v0.8.0
[0.7.3]: https://github.com/elliot-100/Spond-classes/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/elliot-100/Spond-classes/compare/v0.7.1...v0.7.2
