from uuid import UUID
from fastapi import APIRouter

from app.database.schema.shipment import ShipmentCreate, ShipmentUpdate
from app.api.dependency.common import (
    SHIPMENT_SERVICE_DEP,
    LOGGED_IN_SELLER,
    LOGGED_IN_PARTNER,
)


shipment = APIRouter(prefix="/shipments", tags=["Shipments"])


@shipment.get("/")
async def get_shipment():
    return "Shipment"


@shipment.post("/")
async def create_shipment(
    shipment_data: ShipmentCreate,
    service: SHIPMENT_SERVICE_DEP,
    seller: LOGGED_IN_SELLER,
):
    return await service.add_shipment(shipment_data, seller)


@shipment.put("/")
async def update_shipment(
    id: UUID,
    shipment_data: ShipmentUpdate,
    partner: LOGGED_IN_PARTNER,
):
    return shipment_data
