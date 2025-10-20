from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, any_
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
