# Spond-classes

## About

[Spond](https://spond.com/welcome) is a team/group-oriented events system.

The unofficial Python [`spond` library package](https://github.com/Olen/Spond/) gets
data from the Spond API and returns `dict` objects.

This unofficial Python `spond-classes` library package parses those `dict` objects to create
[Pydantic](https://docs.pydantic.dev/) class instances, i.e. provides an object abstraction layer.

Experimental, partial, read-only implementation.

## Install

Install from PyPI, e.g:
```shell
pip install spond-classes
```
Or if you're using Poetry:
```shell
poetry add spond-classes
```
Note that [`spond`](https://github.com/Olen/Spond/) is required for practical use, but not a technical dependency,
so needs to be installed separately.


## Example code

Adapting the example code in [`Spond`](https://github.com/Olen/Spond/) README:

```python
import asyncio
from spond import spond
import spond_classes

# fake credentials and ids
username = 'my@mail.invalid'
password = 'Pa55worD'
group_id = 'G1'
subgroup_id = 'SG1'

async def main():
    s = spond.Spond(username=username, password=password)
    group_data = await s.get_group(group_id)
    await s.clientsession.close()

    # Now we can create a class instance ...
    group = spond_classes.Group.model_validate(group_data)
    # or `spond_classes.Group(**group_data)`

    # ... use class properties instead of dict keys ...
    print(group.name)

    # ... access subordinate instances and their properties ...
    for member in group.members:
        print(f"{member.full_name} is in the {group.name} group")

    # ... and use some helper methods
    subgroup = group.subgroup_by_id(subgroup_id)
    for member in group.members_by_subgroup(subgroup)
        print(f"{member.full_name} is in the {subgroup.name} subgroup")

asyncio.run(main())
```
## Key features

* Create `Group` instance from the dict returned from the API by the corresponding
  `Spond` method:

```python
spond_classes.Group.model_validate(dict)
# or `spond_classes.Group(**dict)`
```

* Then access class instance attributes and methods:

```python
Group.uid: str
Group.members: list[Member]
Group.name: str
Group.roles: list[Role]
Group.subgroups: list[Subgroup]

Group.member_by_id() -> Member
Group.role_by_id() -> Role
Group.subgroup_by_id() -> Subgroup

Group.members_by_subgroup(subgroup: Subgroup) -> list[Member]
Group.members_by_role(role: Role) -> list[Member]
```

* Also provides access to subordinate `Member`, `Role`, `Subgroup` instances:

```python
Member.uid: str
Member.created_time: datetime
Member.email: str
Member.first_name: str
Member.full_name: str
Member.last_name: str
Member.phone_number: str
Member.Profile.uid: str
Member.role_uids: list[str]
Member.subgroup_uids: list[str]

Role.uid: str
Role.name: str

Subgroup.uid: str
Subgroup.name: str
```

* Create `Event` instance from the dict returned from the API by the corresponding
  `Spond` method:

```python
spond_classes.Event.model_validate(dict)
# or spond_classes.Event(**dict)
```

* Then access attributes:

```python
Event.uid: str
Event.heading: str
Event.start_time: datetime
Event.Responses.accepted_uids: list[str]
Event.Responses.declined_uids: list[str]
Event.Responses.unanswered_uids: list[str]
Event.Responses.waiting_list_uids: list[str]
Event.Responses.unconfirmed_uids: list[str]
```
