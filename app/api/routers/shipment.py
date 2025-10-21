from fastapi import APIRouter

from app.database.schema.shipment import ShipmentCreate
from app.api.dependencies.common import SHIPMENT_SERVICE_DEP, LOGGED_IN_SELLER_DEP


shipment = APIRouter(prefix="/shipment", tags=["Shipments"])


@shipment.post("/")
async def add_shipment(
    shipment_data: ShipmentCreate,
    service: SHIPMENT_SERVICE_DEP,
    seller: LOGGED_IN_SELLER_DEP,
):
    return await service.add_shipment(shipment_data, str(seller.id))


@shipment.get("/")
async def get_all_shipments(
    service: SHIPMENT_SERVICE_DEP,
    seller: LOGGED_IN_SELLER_DEP,
):
    return await service.get_all_shipment_by_seller(seller.id)
