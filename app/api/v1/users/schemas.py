"""Schemas for user."""

from pydantic import BaseModel


class Stub(BaseModel):
    """Stub schema."""

    some_string: str
