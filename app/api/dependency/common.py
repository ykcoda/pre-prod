from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

# from app.api.services.delivery_partner import DelieryPartnerService
from app.api.core.security import SELLER_OAUTH2_SCHEME, PARTNER_OAUTH2_SCHEME
from app.api.services.seller import SellerService
from app.api.services.delivery_partner import DeliveryPartnerService
from app.api.services.shipment import ShipmentService
from app.database.models.seller import Seller
from app.database.models.delivery_partner import DeliveryPartners
from app.database.session import get_database_session
from app.utils import decode_access_token


DB_MAIN_SESSION_DEP = Annotated[AsyncSession, Depends(get_database_session)]


async def get_shipment_service(session: DB_MAIN_SESSION_DEP):
    return ShipmentService(session)


SHIPMENT_SERVICE_DEP = Annotated[ShipmentService, Depends(get_shipment_service)]


async def get_seller_service(session: DB_MAIN_SESSION_DEP):
    return SellerService(session)


SELLER_SERVICE_DEP = Annotated[SellerService, Depends(get_seller_service)]


async def get_partner_service(session: DB_MAIN_SESSION_DEP):
    return DeliveryPartnerService(session)


PARTNER_SERVICE_DEP = Annotated[DeliveryPartnerService, Depends(get_partner_service)]


async def _get_access_token(token):
    return decode_access_token(token)


async def get_logged_in_seller(
    token: Annotated[str, Depends(SELLER_OAUTH2_SCHEME)], session: DB_MAIN_SESSION_DEP
):
    access_token = await _get_access_token(token)

    if not token or access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not Authorized"
        )

    user_id = str(access_token["user"]["id"])
    return await session.get(Seller, user_id)


LOGGED_IN_SELLER = Annotated[Seller, Depends(get_logged_in_seller)]


async def get_logged_in_partner(
    token: Annotated[str, Depends(PARTNER_OAUTH2_SCHEME)], session: DB_MAIN_SESSION_DEP
):
    access_token = await _get_access_token(token)

    if not token or access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not Authorized"
        )

    user_id = str(access_token["user"]["id"])
    return await session.get(DeliveryPartners, user_id)


LOGGED_IN_PARTNER = Annotated[DeliveryPartners, Depends(get_logged_in_partner)]
