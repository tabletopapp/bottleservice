"""DB Models for friends."""

from sqlalchemy import UniqueConstraint
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer

from app.database import Base


class Friend(Base):
    """Some database model."""

    __tablename__ = "friends"

    requesting_guest_id = Column(
        Integer,
        ForeignKey("guests.id"),
        primary_key=True,
        nullable=False,
    )
    addressee_guest_id = Column(
        Integer,
        ForeignKey("guests.id"),
        primary_key=True,
        nullable=False,
    )
    is_active = Column(Boolean, nullable=False, default=True)

    __table_args__ = (
        UniqueConstraint(
            "requesting_guest_id",
            "addressee_guest_id",
            name="unique_friendship",
        ),
    )
