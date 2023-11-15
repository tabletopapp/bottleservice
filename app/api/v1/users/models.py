"""DB Models for user."""

import enum

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Date, Enum, Integer, String

from app.database import Base


class Gender(str, enum.Enum):
    M = "M"  # Male
    F = "F"  # Female
    O = "O"  # Other
    U = "U"  # Unknown


class User(Base):
    """Some database model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=False)
