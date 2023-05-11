"""Event class and nested classes:
Responses, Recipients, EventRecipientsGroup, EventRecipientsGroupMember.
"""

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


class EventRecipientsGroupSubgroup(BaseModel):
    """Represents a subgroup within EventRecipientsGroup.

    Attributes
    ----------
    uid : str
        id of the Subgroup.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    name : str
        Name of the Subgroup.
        'name' in API.
    """

    uid: str = Field(alias="id")
    name: str

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Subgroup '{self.name}'"


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
    subgroups : list[EventRecipientsGroupSubgroup]
        'subgroups' in API.
    """

    uid: str = Field(alias="id")
    name: str

    # Lists which always exist in API data, but may be empty
    members: list[EventRecipientsGroupMember]

    # Optional in API data
    subgroups: list[EventRecipientsGroupSubgroup] | None = Field(
        alias="subGroups", default=None
    )


class Recipients(BaseModel):
    """Represents the recipients of an Event.

    Attributes
    ----------
    group : EventRecipientsGroup
    """

    group: EventRecipientsGroup


class Responses(BaseModel):
    """Represents the responses to an Event.

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


class ResponseCategory(Enum):
    """Represents possible response categories.

    Values are used to reference fields.

    """

    ACCEPTED = "accepted"
    DECLINED = "declined"
    UNANSWERED = "unanswered"
    UNCONFIRMED = "unconfirmed"
    WAITING_LIST = "waiting_list"


class Event(BaseModel):
    """Represents an event in the Spond system.

    Events are retrieved from the 'events' API endpoint.

    Attributes
    ----------
    uid : str
        id of the Event.
        `id` in API, but `id` is a reserved term and the `spond` package uses `uid`.
    heading : str
        Heading/name of the Event.
        `heading` in API.
    recipients : Recipients
    responses : Responses
    start_time : datetime.
        Datetime at which the Event starts.
        `startTimestamp` in API, but returns a datetime instead of a string.
    """

    uid: str = Field(alias="id")
    heading: str
    recipients: Recipients
    responses: Responses
    start_time: datetime = Field(alias="startTimestamp")

    def __str__(self) -> str:
        """Return simple human-readable description.

        Date is included because heading is unlikely to be unique.
        """
        return f"Event '{self.heading}' on {self.start_time.date()}"



    def get_responses(
        self, response_category: ResponseCategory, group: Group,
    ) -> list[Member]:
        """Get the Members from response category.

        Parameters
        ----------
        response_category
            ACCEPTED | DECLINED | UNANSWERED | UNCONFIRMED | WAITING_LIST
        group

        Returns
        -------
        List of Members in the response category.
        """
        uids = getattr(self, f"{response_category.value}_uids")
        return [group.member_by_id(uid) for uid in uids]
