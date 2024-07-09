"""Module for `Profile` class."""

from pydantic import BaseModel, Field


class Profile(BaseModel):
    """Represents a profile in the Spond system.

    A `Profile` is nested within a `Member`.

    Attributes
    ----------
    uid : str
        id of the `Profile`.

        `id` in API, but that's a reserved term and the `spond` package uses `uid`.
    """

    uid: str = Field(alias="id")

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Profile(uid='{self.uid}')"
