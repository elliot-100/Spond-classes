"""Module for `Subgroup` class."""

from pydantic import BaseModel, Field


class Subgroup(BaseModel):
    """Represents a subgroup in the Spond system.

    A `Subgroup` is nested within a `Group`.

    Use `Group.members_by_subgroup()` to get
    `Member`s.

    Attributes
    ----------
    uid : str
        id of the `Subgroup`.

        `id` in API, but that's a reserved term and the `spond` package uses `uid`.

    name : str
        Name of the `Subgroup`.

        `name` in API.
    """

    uid: str = Field(alias="id")
    name: str

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Subgroup '{self.name}'"
