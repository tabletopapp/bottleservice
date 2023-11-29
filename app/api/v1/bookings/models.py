"""DB Models for bookings."""

from sqlalchemy import DateTime
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer

from app.database import Base


class Booking(Base):
    """Some database model."""

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey("guests.id"), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    booking_datetime = Column(DateTime, nullable=False)
    num_guests = Column(Integer, nullable=True)
    # promoter_id = Column(Integer, ForeignKey("promoters.id"), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
