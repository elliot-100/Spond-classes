"""Module for `Role` class."""

from pydantic import BaseModel, Field


class Role(BaseModel):
    """Represents a role in the Spond system.

    A `Role` is nested within a `Group`.

    Use `Group.members_by_role()` to get `Member`s.

    Attributes
    ----------
    uid : str
        id of the `Role`.

        `id` in API, but that's a reserved term and the `spond` package uses `uid`.

    name : str
        Name of the `Role`.

        `name` in API.
    """

    uid: str = Field(alias="id")
    name: str

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Role '{self.name}'"
