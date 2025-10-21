from datetime import datetime
from sqlmodel import ARRAY, INTEGER, Column, Field
from uuid import UUID, uuid4
from .user import User


class DeliveryPartner(User, table=True):

    __tablename__ = "delivery_partners"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    hashed_password: str
    max_capacity: int
    servicable_zipcodes: list[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    created_at: datetime = Field(default_factory=lambda: datetime.now())
