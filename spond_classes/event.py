"""Module containing `Event` class and nested classes."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class EventRecipientsGroupMemberProfile(BaseModel):
    """Represents a profile within EventRecipientsGroupMember.

    Simpler than a Profile.

    Attributes
    ----------
    uid : str
        id of the Member.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    """

    uid: str = Field(alias="id")


class EventRecipientsGroupMember(BaseModel):
    """Represents a member within EventRecipientsGroup.

    Simpler than a Member.

    Attributes
    ----------
    uid : str
        id of the Member.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    first_name : str
        'firstName' in API.
    last_name : str
        'lastName' in API.

    Properties
    ----------
    full_name : str
        The Member's full name.
        Provided for convenience.
    """

    uid: str = Field(alias="id")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")

    # Optional in API data
    profile: EventRecipientsGroupMemberProfile | None = (
        None  # Availability may depend on permissions
    )

    @property
    def full_name(self) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"


class EventRecipientsGroup(BaseModel):
    """Represents a group within Recipients.

    Simpler than a Group.

    Attributes
    ----------
    uid : str
        id of the Group.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    members : list[Member]
        Members belonging to the Group.
        'members' in API.
    name : str
        Name of the Group.
        'name' in API.
    """

    uid: str = Field(alias="id")
    name: str

    # Lists which always exist in API data, but may be empty
    members: list[EventRecipientsGroupMember]


class Recipients(BaseModel):
    """Represents the recipients of an Event.

    Attributes
    ----------
    group : EventRecipientsGroup
    """

    group: EventRecipientsGroup


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
    recipients: Recipients
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
        """Return the URL of the `Event`."""
        return f"https://spond.com/client/sponds/{self.uid}/"
