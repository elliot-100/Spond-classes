"""Module containing `Event` class and nested `EventType`,`Responses` classes."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Responses(BaseModel):
    """Represents the responses to an `Event`."""

    # Lists which always exist in API data, but may be empty
    accepted_uids: list[str] = Field(alias="acceptedIds")
    """`acceptedIds` in API."""
    declined_uids: list[str] = Field(alias="declinedIds")
    """`declinedIds` in API."""
    unanswered_uids: list[str] = Field(alias="unansweredIds")
    """`unansweredIds` in API."""
    waiting_list_uids: list[str] = Field(alias="waitinglistIds")
    """`waitinglistIds` in API."""
    unconfirmed_uids: list[str] = Field(alias="unconfirmedIds")
    """`unconfirmedIds` in API."""


class EventType(Enum):
    """Represents the kind of `Event`."""

    EVENT = "EVENT"
    RECURRING = "RECURRING"


class Event(BaseModel):
    """Represents an event in the Spond system.

    Events data is retrieved from the `events` API endpoint.
    """

    model_config = ConfigDict(frozen=True)

    uid: str = Field(alias="id")
    """`id` in API, but that's a reserved term in Python and the Spond package
    uses `uid`."""
    heading: str
    responses: Responses
    type: EventType
    created_time: datetime = Field(alias="createdTime")
    """Derived from `createdTime` in API."""
    end_time: datetime = Field(alias="endTimestamp")
    """Datetime at which the `Event` ends.
        Derived from `endTimestamp` in API."""
    start_time: datetime = Field(alias="startTimestamp")
    """Datetime at which the `Event` starts.
    Derived from `startTimestamp` in API."""

    # Optional in API data
    cancelled: bool | None = Field(default=None)
    """Optional."""
    invite_time: datetime | None = Field(alias="inviteTime", default=None)
    """Optional.
    Derived from `inviteTime` in API."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order, and with some prettification.
        """
        start_time_tag = str(self.start_time)
        return (
            f"Event(uid='{self.uid}', "
            f"heading='{self.heading}', "
            f"start_time: {start_time_tag},"
            f" …)"
        )

    @property
    def url(self) -> str:
        """Return the URL of the `Event`."""
        return f"https://spond.com/client/sponds/{self.uid}/"
