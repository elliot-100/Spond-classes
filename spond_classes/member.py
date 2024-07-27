"""Module containing `Member` class."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from .profile import Profile


class Member(BaseModel):
    """Represents a member in the Spond system.

    A `Member` is an individual's group-specific record, and is nested within a `Group`.
    A `Member` may have a nested `Profile`.
    """

    uid: str = Field(alias="id")
    """`id` in API, but that's a reserved term in Python and the Spond package
    uses `uid`."""
    created_time: datetime = Field(alias="createdTime")
    """Derived from `createdTime` in API."""
    first_name: str = Field(alias="firstName")
    """`firstName` in API."""
    last_name: str = Field(alias="lastName")
    """`lastName` in API."""

    # Lists which always exist in API data, but may be empty
    subgroup_uids: list[str] = Field(alias="subGroups")
    """`subGroups` in API, but aliased here to avoid confusion with
    `Subgroup` instances."""

    # Optional in API data
    email: str | None = Field(default=None)
    phone_number: str | None = Field(alias="phoneNumber", default=None)
    """`phoneNumber` in API."""
    profile: Profile | None = None  # Availability may depend on permissions
    """Derived from `profile` in API."""
    role_uids: list[str] | None = Field(alias="roles", default=None)
    """`roles` in API, but aliased here to avoid confusion with `Role` instances."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order.
        """
        return f"Member(uid='{self.uid}', full_name='{self.full_name}', …)"

    @property
    def full_name(self) -> str:
        """Return the `Member`'s full name."""
        return f"{self.first_name} {self.last_name}"
