from uuid import UUID, uuid4
from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship

from .user import User

if TYPE_CHECKING:
    from .shipment import Shipment


# Seller Model
class Seller(User, table=True):
    __tablename__ = "sellers"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    password_hash: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())

    shipments: list["Shipment"] = Relationship(
        back_populates="seller", sa_relationship_kwargs={"lazy": "selectin"}
    )
