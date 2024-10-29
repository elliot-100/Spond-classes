"""Module containing `Event` class and related `EventType`,`Responses` classes."""

from datetime import datetime
from enum import Enum

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


class EventType(Enum):
    """Represents the kind of `Event`."""

    EVENT = "EVENT"
    RECURRING = "RECURRING"


class Event(BaseModel):
    """Represents an event in the Spond system.

    Events data is retrieved from the `events` API endpoint.
    """

    uid: str = Field(alias="id")
    """`id` in API; aliased as that's a Python built-in, and the Spond package
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


class MatchType(Enum):
    """Represents the kind of `Match`."""

    HOME = "HOME"
    AWAY = "AWAY"


class MatchInfo(BaseModel):
    """Represents match data."""
    opponent_name: str = Field(alias="opponentName")
    opponent_score: int = Field(alias="opponentScore")
    scores_final: bool = Field(alias="scoresFinal")
    scores_public: bool = Field(alias="scoresPublic")
    scores_set: bool = Field(alias="scoresSet")
    scores_set_ever: bool = Field(alias="scoresSetEver")
    team_name: str = Field(alias="teamName")
    team_score: int = Field(alias="teamScore")
    type: MatchType


class Match(Event):
    """Represents match event."""
    match_event: bool = Field(alias="matchEvent", default=True)
    match_info: MatchInfo = Field(alias="matchInfo")

