"""Event class and nested classes:
Responses, Recipients, EventRecipientsGroup, EventRecipientsGroupMember.
"""

from datetime import datetime

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

    def _erg_members_by_response(
        self, response_category: str
    ) -> list[EventRecipientsGroupMember]:
        response_categories = [
            "accepted",
            "declined",
            "unanswered",
            "waiting_list",
            "unconfirmed",
        ]
        if response_category not in response_categories:
            err_msg = (
                f"Invalid `response_category` value '{response_category}'. "
                f"Expected one of: {response_categories}"
            )
            raise ValueError(err_msg)
        return [
            self._erg_member_by_id(uid)
            for uid in getattr(self.responses, f"{response_category}_uids")
        ]

    def _erg_member_by_id(self, erg_member_uid: str) -> EventRecipientsGroupMember:
        """Return the nested EventRecipientsGroupMember with matching uid.

        Parameters
        ----------
        erg_member_uid
            ID to look up.

        Raises
        ------
        LookupError if uid is not found.
        """
        for erg_member in self.recipients.group.members:
            if erg_member.uid == erg_member_uid:
                return erg_member
        err_msg = f"No EventRecipientsGroupMember found with id='{erg_member_uid}'."
        raise LookupError(err_msg)
