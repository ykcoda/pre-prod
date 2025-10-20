from enum import Enum
from uuid import UUID, uuid4
from typing import TYPE_CHECKING
from datetime import datetime, timedelta
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .seller import Seller
    from .delivery_partner import DeliveryPartners


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
    estimated_delivery: datetime = Field(
        default_factory=lambda: datetime.now() + timedelta(days=2)
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now())

    seller_id: UUID = Field(foreign_key="sellers.id")
    seller: "Seller" = Relationship(
        back_populates="shipments", sa_relationship_kwargs={"lazy": "selectin"}
    )

    partner_id: UUID = Field(foreign_key="delivery_partners.id")
    partner: "DeliveryPartners" = Relationship(
        back_populates="shipments", sa_relationship_kwargs={"lazy": "selectin"}
    )
