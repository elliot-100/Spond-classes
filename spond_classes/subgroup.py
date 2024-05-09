"""Subgroup class."""

from pydantic import BaseModel, Field


class Subgroup(BaseModel):
    """Subgroup.

    Belongs to one Group.
    May contain zero, one or more SpondMembers.

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
