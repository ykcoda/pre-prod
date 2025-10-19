from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy import ARRAY, INTEGER
from sqlmodel import Field, Column

from .user import User


class DeliverPartners(User):
    __tablename__ = "delivery_partners"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    password_hash: str
    servicable_zip_codes: list[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    max_handling_capacity: int
    created_at: datetime = Field(default_factory=lambda: datetime.now())
