"""DB Models for clubs."""

from sqlalchemy import Time
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from app.database import Base


class Club(Base):
    """Some database model."""

    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address_line_1 = Column(String, nullable=False)
    address_line_2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    pricing_tier = Column(Integer, nullable=True)  # higher is more expensive
    opening_time = Column(Time, nullable=True)
    closing_time = Column(Time, nullable=True)
    banner_image_url = Column(String, nullable=True)
