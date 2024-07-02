"""Module for `Event` class and nested `Responses` class."""

from datetime import datetime

from pydantic import BaseModel, Field


class Responses(BaseModel):
    """Represents the responses to an `Event`.

    Attributes
    ----------
    accepted_uids: list[str]
        `acceptedIds` in API.

    declined_uids: list[str]
        `declinedIds` in API.

    unanswered_uids: list[str]
        `unansweredIds` in API.

    unconfirmed_uids: list[str]
        `unconfirmedIds` in API.

    waiting_list_uids: list[str]
        `waitinglistIds` in API.
    """

    # Lists which always exist in API data, but may be empty
    accepted_uids: list[str] = Field(alias="acceptedIds")
    declined_uids: list[str] = Field(alias="declinedIds")
    unanswered_uids: list[str] = Field(alias="unansweredIds")
    waiting_list_uids: list[str] = Field(alias="waitinglistIds")
    unconfirmed_uids: list[str] = Field(alias="unconfirmedIds")


class Event(BaseModel):
    """Represents an event in the Spond system.

    `Event`s are retrieved from the `events` API endpoint.

    Attributes
    ----------
    uid : str
        id of the `Event`.

        `id` in API, but that's a reserved term and the `spond` package uses `uid`.

    cancelled : bool, optional
        `cancelled` in API.

    heading : str
        Heading/name of the `Event`.

        `heading` in API.

    responses : `Responses`

    created_time : datetime
        Derived from `createdTime` in API.

    end_time : datetime
        Datetime at which the `Event` ends.

        Derived from `endTimestamp` in API.

    invite_time : datetime
        Derived from `inviteTime` in API.

    start_time : datetime
        Datetime at which the `Event` starts.

        Derived from `startTimestamp` in API.
    """

    uid: str = Field(alias="id")
    heading: str
    responses: Responses
    created_time: datetime = Field(alias="createdTime")
    end_time: datetime = Field(alias="endTimestamp")
    invite_time: datetime = Field(alias="inviteTime")
    start_time: datetime = Field(alias="startTimestamp")

    # Optional in API data
    cancelled: bool | None = Field(default=None)

    def __str__(self) -> str:
        """Return simple human-readable description.

        Date is included because heading is unlikely to be unique.
        """
        return f"Event '{self.heading}' on {self.start_time.date()}"

    @property
    def url(self) -> str:
        """Return the URL of the `Event`."""
        return f"https://spond.com/client/sponds/{self.uid}/"
