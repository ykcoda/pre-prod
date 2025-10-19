from fastapi import APIRouter

from app.database.schema.delivery_partner import DeliveryPartnerCreate


partner = APIRouter(prefix="/partners", tags=["Delivery Partner"])


@partner.post("/")
async def register_delivery_partner(partner_data: DeliveryPartnerCreate):
    pass
