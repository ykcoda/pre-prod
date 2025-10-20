from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, any_
from fastapi import HTTPException, status
from app.database.models.shipment import Shipment
from .user import UserService
from app.database.models.delivery_partner import DeliveryPartners
from app.database.schema.delivery_partner import DeliveryPartnerCreate


class DeliveryPartnerService(UserService):

    def __init__(self, session: AsyncSession):
        super().__init__(DeliveryPartners, session)  # type: ignore

    async def add_partner(self, partner_data: DeliveryPartnerCreate):
        return await self._add_user(partner_data.model_dump())

    async def partner_token(self, email, password):
        return await self._get_user_token(email, password)

    async def get_delivery_partner_by_zipcode(self, zipcode: int):
        result = await self.session.exec(
            select(DeliveryPartners).where(
                zipcode == any_(DeliveryPartners.servicable_zip_codes)
            )
        )
        return result.all()

    async def assign_shipment(self, shipment: Shipment):
        eligible_partners = await self.get_delivery_partner_by_zipcode(
            shipment.destination
        )

        for partner in eligible_partners:
            if partner.current_handling_capacity > 0:
                partner.shipments.append(shipment)
                return partner

        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="No delivery partner is available",
        )
