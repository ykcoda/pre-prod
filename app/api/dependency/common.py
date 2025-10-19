from typing import Annotated
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.session import get_database_session


DB_MAIN_SESSION_DEP = Annotated[AsyncSession, Depends(get_database_session)]


# async def get_seller_service(session: DB_MAIN_SESSION_DEP):
#     return SellerService(session)

# async def get_delivery_partner_service(session: DB_MAIN_SESSION_DEP):
#     return DelieryPartnerService(session)

# SELLER_SERVICE_DEP = Annotated[SellerService, Depends(get_seller_service)]
# DELIVERY_PARTNER_SERVICE_DEP = Annotated[DelieryPartnerService, Depends(get_delivery_partner_service)]
