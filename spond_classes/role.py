"""Module containing `Role` class."""

from pydantic import BaseModel, ConfigDict, Field


class Role(BaseModel):
    """Represents a role in the Spond system.

    A `Role` is nested within a `Group`.

    Use `Group.members_by_role()` to get `Member` instances.
    """

    model_config = ConfigDict(frozen=True)

    uid: str = Field(alias="id")
    """`id` in API, but that's a reserved term in Python and the Spond package
    uses `uid`."""
    name: str

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Role(uid='{self.uid}', name='{self.name}')"
