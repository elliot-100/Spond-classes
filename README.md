# Spond-classes

## About

[Spond](https://spond.com/welcome) is a team/group-oriented events system.

The unofficial Python `spond` library package ([GitHub](https://github.com/Olen/Spond/),
[PyPI](https://pypi.org/project/spond/))  gets data from the Spond API and returns
`dict` objects.

This unofficial Python `spond-classes` library package
([GitHub](https://github.com/elliot-100/Spond-classes), 
[PyPI](https://pypi.org/project/spond-classes/)) parses those `dict`s using
[Pydantic](https://docs.pydantic.dev/) to create class instances.

Partial, read-only implementation.


## Install

Install from PyPI, e.g:
```shell
pip install spond-classes
```
Or if you're using Poetry:
```shell
poetry add spond-classes
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
USERNAME = 'my@mail.invalid'
PASSWORD = 'Pa55worD'
GROUP_ID = 'G1'
SUBGROUP_ID = 'SG1'

async def main():
    s = Spond(username=USERNAME, password=PASSWORD)
    group_data = await s.get_group(GROUP_ID)
    await s.clientsession.close()

    # Now we can create a class instance ...
    group = Group.from_dict(group_data)

    # ... use class attributes instead of dict keys ...
    print(group.name)

    # ... access subordinate instances and their attributes ...
    for member in group.members:
        print(f"{member.full_name} is in the {group.name} group")

    # ... and use some helper methods
    subgroup = group.subgroup_by_uid(SUBGROUP_ID)
    for member in group.members_by_subgroup(subgroup):
        print(f"{member.full_name} is in the {subgroup.name} subgroup")

asyncio.run(main())
```


## Documentation

Full API documentation is published at https://elliot-100.github.io/Spond-classes/ and
is also included as HTML in the package source `docs` folder.


# Development

Build documentation:
```shell
pdoc spond_classes -d numpy -t docs_templates -o docs
```
