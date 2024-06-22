"""Module for `Member` class."""

from datetime import datetime

from pydantic import BaseModel, Field

from .profile import Profile


class Member(BaseModel):
    """Represents a member in the Spond system.

    A `Member` is an individual's group-specific record, and is nested within a `Group`.
    A `Member` may have a nested `Profile`.

    Attributes
    ----------
    uid : str
        id of the `Member`.

        `id` in API, but that's a reserved term and the `spond` package uses `uid`.

    created_time : datetime
        Derived from `createdTime` in API.

    email : str
        `email` in API.

    first_name : str
        `firstName` in API.

    last_name : str
        `lastName` in API.

    phone_number : str | None
        `phoneNumber` in API.

    profile : Profile | None
        Derived from `profile` in API.

    role_uids : list[str] | None
        `roles` in API, but aliased here to avoid confusion with `Role`s.

    subgroup_uids : list[str]
        `subGroups` in API, but aliased here to avoid confusion with `Subgroup`s.
    """

    uid: str = Field(alias="id")
    created_time: datetime = Field(alias="createdTime")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")

    # Lists which always exist in API data, but may be empty
    subgroup_uids: list[str] = Field(alias="subGroups")

    # Optional in API data
    email: str | None = Field(default=None)
    phone_number: str | None = Field(alias="phoneNumber", default=None)
    profile: Profile | None = None  # Availability may depend on permissions
    role_uids: list[str] | None = Field(alias="roles", default=None)

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
        """Return the `Member`'s full name."""
        return f"{self.first_name} {self.last_name}"
