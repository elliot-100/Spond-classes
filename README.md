# Spond-classes

## About

Python class abstraction layer for [`spond`](https://github.com/Olen/Spond/) library package.

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

## Key methods

Each of these creates a class instance from the dict returned by the corresponding `spond`
method:

```
spond_classes.SpondEvent.from_dict()
spond_classes.SpondGroup.from_dict()
spond_classes.SpondMember.from_dict()
```

## Example code

Adapting the example code in `spond` README:

```
import asyncio
from spond import spond

username = 'my@mail.invalid'
password = 'Pa55worD'
group_id = 'C9DC791FFE63D7914D6952BE10D97B46'  # fake 

async def main():
    s = spond.Spond(username=username, password=password)
    group = await s.get_group(group_id)
    
    # convert to class instance
    sg = SpondGroup.from_dict(group)
    
    # use class properties instead of dict keys
    print(sg.name)
    
    await s.clientsession.close()

asyncio.run(main())
```
