"""Schemas for friends."""

from pydantic import BaseModel


class GetFriendsPayload(BaseModel):
    requesting_guest_id: int


class FriendSchemaReturnPayload(BaseModel):
    guest_id: int
    first_name: str
    last_name: str
