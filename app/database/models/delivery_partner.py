from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import Field

from .user import User


class DeliverPartners(User):
    __tablename__ = "delivery_partners"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    password_hash: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
