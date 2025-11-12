"""Module containing `Event` class and related `EventType`,`Responses` classes."""

import sys

if sys.version_info < (3, 11):
    from typing_extensions import Self

else:
    from typing import Self

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from .typing import DictFromJSON


class Responses(BaseModel):
    """Represents the responses to an `Event`."""

    # Lists which always exist in API data, but may be empty
    accepted_uids: list[str] = Field(alias="acceptedIds")
    """`acceptedIds` in Spond API.
    May be empty."""
    declined_uids: list[str] = Field(alias="declinedIds")
    """`declinedIds` in Spond API.
    May be empty."""
    unanswered_uids: list[str] = Field(alias="unansweredIds")
    """`unansweredIds` in Spond API.
    May be empty."""
    waiting_list_uids: list[str] = Field(alias="waitinglistIds")
    """`waitinglistIds` in Spond API.
    May be empty."""
    unconfirmed_uids: list[str] = Field(alias="unconfirmedIds")
    """`unconfirmedIds` in Spond API.
    May be empty."""


class Event(BaseModel):
    """Represents an event in the Spond system."""

    uid: str = Field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    heading: str
    """Same name in Spond API."""
    responses: Responses
    """Same name in Spond API."""
    type: Literal["AVAILABILITY", "EVENT", "RECURRING"]
    """Same name in Spond API.

    'AVAILABILITY': availability request.
    'EVENT': regular event.
    'RECURRING': instance of recurring event."""
    created_time: datetime = Field(alias="createdTime")
    """Derived from `createdTime` in Spond API."""
    end_time: datetime = Field(alias="endTimestamp")
    """Datetime at which the `Event` ends.
    Derived from `endTimestamp` in Spond API."""
    start_time: datetime = Field(alias="startTimestamp")
    """Datetime at which the `Event` starts.
    Derived from `startTimestamp` in Spond API."""

    # Optional in API data
    cancelled: bool | None = Field(default=None)
    """Same name in Spond API. Not always present. Use `Event.is_cancelled` instead to
    always return a `bool`."""
    hidden: bool | None = Field(default=None)
    """Same name in Spond API. Not always present. Use `Event.is_hidden` instead to
    always return a `bool`."""
    invite_time: datetime | None = Field(alias="inviteTime", default=None)
    """Derived from `inviteTime` in Spond API.
    Not always present."""

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

        Raises
        ------
        `TypeError`
            if `dict_` is not a dictionary.
        """
        if not isinstance(dict_, dict):
            err_msg = f"Expected `dict`, got `{dict_.__class__.__name__}`: '{dict_}'"
            raise TypeError(err_msg)

        return cls(**dict_)
