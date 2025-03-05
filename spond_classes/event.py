"""Module containing `Event` class and related `EventType`,`Responses` classes."""

import sys

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self


from enum import Enum

from attrs import define, field
from cattrs import Converter
from cattrs.gen import make_dict_structure_fn

from .types_ import DictFromJSON


@define
class Responses:
    """Represents the responses to an `Event`."""

    # Lists which always exist in API data, but may be empty
    accepted_uids: list[str] = field(alias="acceptedIds")
    """`acceptedIds` in Spond API.
    May be empty."""
    declined_uids: list[str] = field(alias="declinedIds")
    """`declinedIds` in Spond API.
    May be empty."""
    unanswered_uids: list[str] = field(alias="unansweredIds")
    """`unansweredIds` in Spond API.
    May be empty."""
    waiting_list_uids: list[str] = field(alias="waitinglistIds")
    """`waitinglistIds` in Spond API.
    May be empty."""
    unconfirmed_uids: list[str] = field(alias="unconfirmedIds")
    """`unconfirmedIds` in Spond API.
    May be empty."""

    @classmethod
    def from_dict(cls, dict_: DictFromJSON) -> Self:
        c = Converter()
        hook = make_dict_structure_fn(cls, c, _cattrs_use_alias=True)
        c.register_structure_hook(cls, hook)
        return c.structure(dict_, cls)


class EventType(Enum):
    """Represents the kind of `Event`."""

    AVAILABILITY = "AVAILABILITY"
    """Availability request."""
    EVENT = "EVENT"
    RECURRING = "RECURRING"


@define
class Event:
    """Represents an event in the Spond system."""

    uid: str = field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    heading: str
    responses: Responses
    type: EventType
    # created_time: datetime = field(alias="createdTime")
    # """Derived from `createdTime` in Spond API."""
    # end_time: datetime = field(alias="endTimestamp")
    # """Datetime at which the `Event` ends.
    # Derived from `endTimestamp` in Spond API."""
    # start_time: datetime = field(alias="startTimestamp")
    # """Datetime at which the `Event` starts.
    # Derived from `startTimestamp` in Spond API."""

    # Optional in API data
    cancelled: bool | None = field(default=None)
    """Not always present. Use `Event.is_cancelled` instead to always return
    a `bool`."""
    hidden: bool | None = field(default=None)
    """Not always present. Use `Event.is_hidden` instead to always return
    a `bool`."""
    # invite_time: datetime | None = field(alias="inviteTime", default=None)
    # """Derived from `inviteTime` in Spond API.
    # Not always present."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order.
        """
        return (
            f"Event(uid='{self.uid}', "
            f"heading='{self.heading}', "
            f"start_time: {self.start_time}, "
            "…)"
        )

    @property
    def url(self) -> str:
        """Return the URL of the `Event`, for convenience."""
        return f"https://spond.com/client/sponds/{self.uid}/"

    @property
    def is_cancelled(self) -> bool:
        """Return whether the `Event` is cancelled."""
        return getattr(self, "cancelled", False)

    @property
    def is_hidden(self) -> bool:
        """Return whether the `Event` is hidden."""
        return getattr(self, "hidden", False)

    @classmethod
    def from_dict(cls, dict_: DictFromJSON) -> Self:
        """Construct an `Event`.

        Parameters
        ----------
        dict_
            as returned by `spond.spond.Spond.get_event()`
            or from the list returned by `spond.spond.Spond.get_events()`.

        Returns
        -------
        `Event`
        """
        c = Converter()
        hook = make_dict_structure_fn(cls, c, _cattrs_use_alias=True)
        c.register_structure_hook(cls, hook)
        return c.structure(dict_, cls)
