"""Profile class."""

from pydantic import BaseModel, Field


class Profile(BaseModel):
    """Represents a profile in the Spond system.

    A Profile is nested within a Member.
    """

    uid: str = Field(alias="id")
