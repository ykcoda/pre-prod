from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends
from typing import Annotated

from app.api.service.seller import SellerService
from app.database.session import get_db_session

DB_SESSION_DEP = Annotated[AsyncSession, Depends(get_db_session)]


async def get_seller_service(session: DB_SESSION_DEP):
    return SellerService(session)


SELLER_SERVICE_DEP = Annotated[SellerService, Depends(get_seller_service)]
