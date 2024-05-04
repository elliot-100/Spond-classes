"""Member class."""

from datetime import datetime

from pydantic import BaseModel, Field

from .profile import Profile


class Member(BaseModel):
    """Represents a member in the Spond system.

    A Member is an individual's record within a Group.
    A Member may have a nested Profile.

    Attributes
    ----------
    uid : str
        id of the Member.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    created_time : datetime
        'createdTime' in API, but returns a datetime instead of a string.
    email : str
        'email' in API.
    first_name : str
        'firstName' in API.
    last_name : str
        'lastName' in API.
    phone_number : str
        'phoneNumber' in API.
    profile : Profile
        `profile` in API.
    role_uids : list[str]
        `roles` in API, but aliased here to avoid confusion with `Group.Roles'
    subgroup_uids : list[str]
        `subGroups` in API, but aliased here to avoid confusion with `Group.Subgroups'

    Properties
    ----------
    full_name : str
        The Member's full name.
        Provided for convenience.
    """

    uid: str = Field(alias="id")
    created_time: datetime = Field(alias="createdTime")
    email: str | None = Field(default=None)
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone_number: str | None = Field(alias="phoneNumber", default=None)
    profile: Profile | None = None  # Availability might depend on permissions?
    role_uids: list = Field(alias="roles")
    subgroup_uids: list = Field(alias="subGroups")

    def __str__(self) -> str:
        """Return simple human-readable description.

        Last few chars of uid are included because full name is unlikely to be unique.
        """
        return (
            f"Member '{self.first_name} {self.last_name}' "
            f"(uid ends '...{self.uid[-3:]}')"
        )

    @property
    def full_name(self) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"
