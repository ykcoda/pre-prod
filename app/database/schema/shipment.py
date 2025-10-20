from sqlmodel import Field, SQLModel

from app.database.models.shipment import ShipmentStatus


class ShipmentBase(SQLModel):
    content: str
    weight: float = Field(gt=0, le=25)
    destination: int
    status: ShipmentStatus


class ShipmentRead(ShipmentBase):
    pass


class ShipmentCreate(ShipmentBase):
    pass


class ShipmentUpdate(SQLModel):
    status: ShipmentStatus
