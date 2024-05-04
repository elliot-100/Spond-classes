"""Profile class."""

from pydantic import BaseModel, Field


class Profile(BaseModel):
    """Represents a Member's Profile in the Spond system."""

    uid: str = Field(alias="id")
