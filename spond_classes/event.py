"""Module containing `Event` class and nested `Responses` class."""

from datetime import datetime

from pydantic import BaseModel, Field


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


class Event(BaseModel):
    """Represents an event in the Spond system.

    Events data is retrieved from the `events` API endpoint.
    """

    uid: str = Field(alias="id")
    """`id` in API, but that's a reserved term in Python and the Spond package
    uses `uid`."""
    heading: str
    responses: Responses
    start_time: datetime = Field(alias="startTimestamp")
    """Datetime at which the `Event` starts.
    Derived from `startTimestamp` in API."""

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
