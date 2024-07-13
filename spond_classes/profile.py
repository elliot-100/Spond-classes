"""Module containing `Profile` class."""

from pydantic import BaseModel, Field


class Profile(BaseModel):
    """Represents a profile in the Spond system.

    A `Profile` is nested within a `Member`.
    """

    uid: str = Field(alias="id")
    """`id` in API, but that's a reserved term in Python and the Spond package
    uses `uid`."""

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Profile(uid='{self.uid}')"
