from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from sqlmodel import SQLModel, Field


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
