import asyncio

from spond import spond

from config import password, username
from spond_classes import SpondGroup


async def main():
    s = spond.Spond(username=username, password=password)
    groups = await s.get_groups()
    for group in groups:
        SpondGroup.from_dict(group)
    await s.clientsession.close()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.run(main())
