# spond-classes

![PyPI Python Version](https://img.shields.io/pypi/pyversions/spond-classes)
![PyPI Types](https://img.shields.io/pypi/types/spond-classes)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Felliot-100%2FSpond-classes%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)

## About

[Spond](https://spond.com/welcome) is a team/group-oriented events system.

The unofficial Python `spond` library package ([GitHub](https://github.com/Olen/Spond/),
[PyPI](https://pypi.org/project/spond/))  returns data from the Spond API.

This unofficial Python `spond-classes` library package
([GitHub](https://github.com/elliot-100/Spond-classes),
[PyPI](https://pypi.org/project/spond-classes/)) parses that data using
[Pydantic](https://docs.pydantic.dev/) to create class instances.

Partial, read-only implementation.


## Install

Install from PyPI, e.g:
```shell
pip install spond-classes
```

Note that [`spond`](https://github.com/Olen/Spond/) is required for practical use, but
is not a technical dependency, so needs to be installed separately.


## Example code

Adapting the example code in [`Spond`](https://github.com/Olen/Spond/) README:

```python
import asyncio
from spond.spond import Spond
from spond_classes import Group

# fake credentials and ids
USERNAME = "my@mail.invalid"
PASSWORD = "Pa55worD"
SUBGROUP_ID = "SG1"


async def main():
    s = Spond(username=USERNAME, password=PASSWORD)
    groups_data = await s.get_groups()
    await s.clientsession.close()

    # Now we can create class instances from the data...
    groups = Group.list_from_data(groups_data)

    # ... use class attributes instead of dict keys ...
    my_group = groups[0]
    print(my_group.uid)

    # ... access subordinate instances and their attributes ...
    for member in my_group.members:
        print(f"{member.full_name} is in the {my_group.name} group")

    # ... and use some helper methods
    subgroup = my_group.subgroup_by_uid(SUBGROUP_ID)
    for member in my_group.members_by_subgroup(subgroup):
        print(f"{member.full_name} is in the {subgroup.name} subgroup")

asyncio.run(main())
```


## Documentation

Full API documentation is published at https://elliot-100.github.io/Spond-classes/ and
is also included as HTML in the package source `docs` folder.


## Development

Build documentation:
```shell
uv run pdoc src/spond_classes -d numpy -t docs_templates -o docs
```
