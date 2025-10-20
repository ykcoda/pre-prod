from fastapi import APIRouter


shipment = APIRouter(prefix="/shipments", tags=["Shipments"])


@shipment.get("/")
async def get_shipment():
    return "Shipment"

