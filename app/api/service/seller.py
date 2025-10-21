from app.database.models.seller import Seller
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.schema.seller import SellerCreate

from .user import UserService


class SellerService(UserService):

    def __init__(self, session: AsyncSession):
        super().__init__(Seller, session)  # type:ignore

    async def add_seller(self, seller_data: SellerCreate):
        return await self.add_user(seller_data.model_dump())
