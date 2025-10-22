from fastapi import HTTPException, status
from sqlmodel import any_, select
from app.database.models.delivery_partner import DeliveryPartner
from sqlmodel.ext.asyncio.session import AsyncSession


from app.database.models.shipment import Shipment
from app.database.schema.delivery_partner import DeliveryPartnerCreate
from .user import UserService


class DeliveryPartnerService(UserService):
    def __init__(self, session: AsyncSession):
        super().__init__(DeliveryPartner, session)  # type:ignore

    async def get_token(self, email, password):
        return await self.get_user_access_token(email, password)

    async def add_partner(self, partner: DeliveryPartnerCreate):
        return await self.add_user(partner.model_dump())

    async def update_partner(self, partner_id, partner_data: dict):
        partner = await self.get_user(partner_id)

        if partner is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Partner not found."
            )

        return await self.update_user(partner.sqlmodel_update(partner_data))

    async def get_eligible_partners(self, zipcode: int):
        result = await self.session.exec(
            select(DeliveryPartner).where( 
                zipcode == any_(DeliveryPartner.servicable_zipcodes)
            )
        )
        return result.all()

    async def assign_shipment(self, shipment: Shipment):
        eligible_partners = await self.get_eligible_partners(shipment.destination)

        for partner in eligible_partners:
            if partner.current_handling_capacity > 0:
                partner.shipments.append(shipment)
                return partner
