# Spond-classes

## About

The unofficial Python [`Spond` library package](https://github.com/Olen/Spond/) gets
data from the Spond  API and returns `dict` objects.

This unofficial Python `Spond-classes` package parses those `dict` objects to create
class instances, i.e. provides an object abstraction layer.

Experimental, very partial, read-only implementation.

## Install

Not yet available at PyPI. Install from GitHub, e.g:

`
pip install git+https://github.com/elliot-100/spond-classes.git#egg=spond-classes
`

or for a specific version:

`
pip install git+https://github.com/elliot-100/spond-classes.git@v0.1.0#egg=spond-classes
`

If you're using Poetry:

`
poetry add git+https://github.com/elliot-100/spond-classes.git
`

or for a specific version:

`
poetry add git+https://github.com/elliot-100/spond-classes.git#0.1.0
`

## Key features

* Create `SpondGroup` class instance from the dict returned by the corresponding `Spond`
method:

```
spond_classes.SpondGroup.from_dict()
```

* Then access attributes:

```
SpondGroup.uid: str
SpondGroup.name: str
SpondGroup.members: List[SpondMember]
SpondGroup.subgroups: List[SpondSubgroup]

SpondMember.uid: str
SpondMember.created_time: datetime
SpondMember.first_name: str
SpondMember.last_name: str
SpondMember.name: str
SpondMember.roles: List[str]

SpondSubgroup.uid: str
SpondSubgroup.name: str
```
* Create `SpondEvent` class instance from the dict returned by the corresponding `Spond`
method:

```
spond_classes.SpondEvent.from_dict()
```

* Then access attributes:

```
SpondEvent.uid: str
SpondEvent.heading: str
SpondEvent.name: str
SpondEvent.start_time: datetime
SpondEvent.accepted_uids: list
SpondEvent.declined_uids: list
SpondEvent.unanswered_uids: list
SpondEvent.waiting_list_uids: list
SpondEvent.unconfirmed_uids: list
```
## Example code

Adapting the example code in [`Spond`](https://github.com/Olen/Spond/) README:

```
import asyncio
from spond import spond

username = 'my@mail.invalid'
password = 'Pa55worD'
group_id = 'C9DC791FFE63D7914D6952BE10D97B46'  # fake 

async def main():
    s = spond.Spond(username=username, password=password)
    group = await s.get_group(group_id)
    
    # create class instance
    sg = SpondGroup.from_dict(group)
    
    # use class properties instead of dict keys
    print(sg.name)
    
    await s.clientsession.close()

asyncio.run(main())
```
