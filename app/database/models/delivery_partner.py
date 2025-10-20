from uuid import UUID, uuid4
from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import ARRAY, INTEGER
from sqlmodel import Field, Column, Relationship

from .user import User

if TYPE_CHECKING:
    from .shipment import Shipment, ShipmentStatus


class DeliveryPartners(User, table=True):
    __tablename__ = "delivery_partners"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    password_hash: str
    servicable_zip_codes: list[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    max_handling_capacity: int
    created_at: datetime = Field(default_factory=lambda: datetime.now())

    shipments: list["Shipment"] = Relationship(
        back_populates="partner", sa_relationship_kwargs={"lazy": "selectin"}
    )

    @property
    def active_shipments(self):
        return [
            shipment
            for shipment in self.shipments
            if shipment.status == ShipmentStatus.delivered
        ]

    @property
    def current_handling_capacity(self):
        return self.max_handling_capacity - len(self.active_shipments)
