from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4
from typing import TYPE_CHECKING, Optional
from enum import Enum
from datetime import datetime

if TYPE_CHECKING:
    from .seller import Seller
    from .delivery_partner import DeliveryPartner


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(SQLModel, table=True):
    __tablename__ = "shipments"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    content: str
    weight: float = Field(gt=0, le=25)
    destination: int
    status: ShipmentStatus
    created_at: datetime = Field(default_factory=lambda: datetime.now())

    seller_id: Optional[UUID] = Field(foreign_key="sellers.id", default=None)
    seller: "Seller" = Relationship(
        back_populates="shipments", sa_relationship_kwargs={"lazy": "selectin"}
    )

    partner_id: Optional[UUID] = Field(foreign_key="delivery_partners.id", default=None)
    partner: "DeliveryPartner" = Relationship(
        back_populates="shipments", sa_relationship_kwargs={"lazy": "selectin"}
    )
