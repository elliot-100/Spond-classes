"""Module containing `Chat` class."""

from datetime import datetime

from pydantic import BaseModel, Field


class Message(BaseModel):
    """Represents a message in the Spond system.

    Nested within a `Chat`.
    """
    chat_id: str
    timestamp: datetime
    user: str

    # Optional in API data
    text: str | None = Field(default=None)

    # Not supported: msgNum, type, reactions


class Chat(BaseModel):
    """Represents a chat in the Spond system.

    Chats data is retrieved from the `chats` API endpoint.
    """

    uid: str = Field(alias="id")
    """`id` in API, but that's a reserved term in Python and the Spond package
    uses `uid`."""
    message: Message
    participants: list[str]
    newest_timestamp: datetime = Field(alias="newestTimestamp")
    """Derived from `newestTimestamp` in API."""

    # Not supported: type, groupId, formerParticipants, unread, muted

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order, and with some prettification.
        """
        newest_timestamp_tag = str(self.newest_timestamp)
        return f"Chat(uid='{self.uid}', " f"newest_time: {newest_timestamp_tag}," " …)"
