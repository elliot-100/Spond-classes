# Spond-classes

## About

[Spond](https://spond.com/welcome) is a team/group-oriented events system.

The unofficial Python [`spond` library package](https://github.com/Olen/Spond/) gets
data from the Spond API and returns `dict` objects.

This unofficial Python `spond-classes` package parses those `dict` objects to create
class instances, i.e. provides an object abstraction layer.

Experimental, very partial, read-only implementation.

## Install

Install from PyPI, e.g:
`
pip install spond-classes
`
Or if you're using Poetry:
`
poetry add spond-classes
`

## Key features

* Create `Group` class instance from the dict returned by the corresponding `spond`
  method:

```
spond_classes.Group.from_dict()
```

* Then access class instance attributes and methods:

```
Group.uid: str
Group.name: str
Group.members: List[Member]
Group.member_by_id() -> Member
Group.roles: List[SpondRoles]
Group.role_by_id() -> Role
Group.subgroups: List[Subgroup]
Group.subgroup_by_id() -> Subgroup
```

* Also provides access to child `Member`, `Role`, `Subgroup` instances:

```
Member.uid: str
Member.created_time: datetime
Member.first_name: str
Member.last_name: str
Member.full_name: str
Member.phone_number: str
Member.profile_uid: str
Member.roles: List[Role]
Member.subgroups: List[Subgroup]

Role.uid: str
Role.members: List[Member]
Role.name: str

Subgroup.uid: str
Subgroup.members: List[Member]
Subgroup.name: str
```

* Create `Event` class instance from the dict returned by the corresponding `Spond`
  method:

```
spond_classes.Event.from_dict()
```

* Then access attributes:

```
Event.uid: str
Event.heading: str
Event.start_time: datetime
Event.accepted_uids: list
Event.declined_uids: list
Event.unanswered_uids: list
Event.waiting_list_uids: list
Event.unconfirmed_uids: list
```

It's also possible to create `Member.from_dict()`, `Role.from_dict()`,
`Subgroup.from_dict()`.

## Example code

Adapting the example code in [`Spond`](https://github.com/Olen/Spond/) README:

```
import asyncio
from spond import spond
import spond_classes

username = 'my@mail.invalid'
password = 'Pa55worD'
group_id = 'C9DC791FFE63D7914D6952BE10D97B46'  # fake

async def main():
    s = spond.Spond(username=username, password=password)
    group_data = await s.get_group(group_id)
    await s.clientsession.close()

    # Now we can create a class instance ...
    group = spond_classes.Group.from_dict(group_data)

    # ... use class properties instead of dict keys ...
    print(group.name)

    # ... and access child instances and their properties
    for member in group.members:
        print(member.full_name)

asyncio.run(main())
```
