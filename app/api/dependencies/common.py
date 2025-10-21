from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends, HTTPException, status
from typing import Annotated

from app.api.service.delivery_partner import DeliveryPartnerService
from app.api.service.seller import SellerService
from app.database.models.delivery_partner import DeliveryPartner
from app.database.models.seller import Seller
from app.database.session import get_db_session
from app.api.core.security import SELLER_OAUTH2_SCHEME
from app.api.core.security import PARTNER_OAUTH2_SCHEME
from app.utils import decode_access_code

DB_SESSION_DEP = Annotated[AsyncSession, Depends(get_db_session)]


async def get_seller_service(session: DB_SESSION_DEP):
    return SellerService(session)


SELLER_SERVICE_DEP = Annotated[SellerService, Depends(get_seller_service)]


async def get_logged_in_seller(
    session: DB_SESSION_DEP, token: str = Depends(SELLER_OAUTH2_SCHEME)
):
    access_token = decode_access_code(token)

    if not token or access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Seller not authorized"
        )

    seller_id = str(access_token["user"]["id"])
    return await session.get(Seller, seller_id)


LOGGED_IN_SELLER_DEP = Annotated[Seller, Depends(get_logged_in_seller)]


async def get_partner_service(session: DB_SESSION_DEP):
    return DeliveryPartnerService(session)


PARTNER_SERVICE_DEP = Annotated[DeliveryPartnerService, Depends(get_partner_service)]


async def get_logged_in_partner(
    session: DB_SESSION_DEP, token: Annotated[str, Depends(PARTNER_OAUTH2_SCHEME)]
):
    access_token = decode_access_code(token)
    
    if not token or access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Delivery Partner not authorized",
        )
    partner_id = str(access_token["user"]["id"])
    return await session.get(DeliveryPartner, partner_id)


LOGGED_IN_PARTNER = Annotated[DeliveryPartner, Depends(get_logged_in_partner)]
