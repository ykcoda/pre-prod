from sqlmodel.ext.asyncio.session import AsyncSession

from .user import UserService
from app.database.models.seller import Seller
from app.database.schema.seller import SellerCreate


class SellerService(UserService):

    def __init__(self, session: AsyncSession):
        super().__init__(Seller, session)  # type: ignore

    async def add_seller(self, seller_data: SellerCreate):
        return await self._add_user(seller_data.model_dump())

    async def seller_token(self, email, password):
        return await self._get_user_token(email, password)

        