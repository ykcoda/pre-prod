from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.database.schema.delivery_partner import DeliveryPartnerCreate
from app.api.dependency.common import PARTNER_SERVICE_DEP


partner = APIRouter(prefix="/partners", tags=["Delivery Partner"])


@partner.post("/")
async def register_partner(
    partner_data: DeliveryPartnerCreate,
    service: PARTNER_SERVICE_DEP,
):
    return await service.add_partner(partner_data)


@partner.post("/token")
async def partner_login(
    login_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: PARTNER_SERVICE_DEP,
):
    token = await service.partner_token(login_form.username, login_form.password)
    return {"access_token": token, "token_type": "jwt"}


@partner.get("/dashboard")
async def get_dashboard():

    return {"DETAILS": "PARTNER DASHBOARD"}
