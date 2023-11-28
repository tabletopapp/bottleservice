"""DB Models for guest."""

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from app.database import Base


class Guest(Base):
    """Some database model."""

    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
