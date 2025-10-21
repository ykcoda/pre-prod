from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.database.schema.delivery_partner import (
    DeliveryPartnerCreate,
    DeliveryPartnerUpdate,
)
from app.api.dependencies.common import PARTNER_SERVICE_DEP, LOGGED_IN_PARTNER


partner = APIRouter(prefix="/partners", tags=["Delivery Partners"])


@partner.post("/signup")
async def register_partner(
    partner_data: DeliveryPartnerCreate, service: PARTNER_SERVICE_DEP
):
    return await service.add_partner(partner_data)


@partner.post("token")
async def partner_login(
    login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: PARTNER_SERVICE_DEP,
):
    token = await service.get_token(login_data.username, login_data.password)

    return {"access_token": token, "token_type": "jwt"}


@partner.get("/dashboard")
async def get_dashboard(
    partner: LOGGED_IN_PARTNER,
):
    return {"Partner id": partner.id, "Partner name": partner.name}


@partner.patch("/")
async def update_partner(
    partner_id: str,
    partner_data: DeliveryPartnerUpdate,
    service: PARTNER_SERVICE_DEP,
):
    return await service.update_partner(
        partner_id, partner_data.model_dump(exclude_none=True)
    )
