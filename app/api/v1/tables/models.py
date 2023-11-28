"""DB Models for tables."""

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from app.database import Base


class Table(Base):
    """Some database model."""

    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    num_seats = Column(Integer, nullable=False)
    price_in_usd_cents = Column(Integer, nullable=False)
    tier = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    max_num_tables = Column(Integer, nullable=False, server_default="1")
