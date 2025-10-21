from sqlmodel import Field, SQLModel
from uuid import UUID
from app.database.models.shipment import ShipmentStatus


class ShipmentBase(SQLModel):

    content: str
    weight: float = Field(gt=0, le=25)
    destination: int


class ShipmentCreate(ShipmentBase):
    seller_id: UUID | None = Field(default=None)
    partner_id: UUID | None = Field(default=None)


class ShipmentUpdate(SQLModel):
    status: ShipmentStatus
