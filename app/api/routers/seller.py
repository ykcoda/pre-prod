from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.database.schema.seller import SellerCreate
from app.api.dependency.common import LOGGED_IN_SELLER, SELLER_SERVICE_DEP


seller = APIRouter(prefix="/sellers", tags=["Sellers"])


@seller.post("/")
async def register_seller(
    seller_data: SellerCreate,
    service: SELLER_SERVICE_DEP,
):
    return await service.add_seller(seller_data)


@seller.post("/token")
async def seller_login(
    login_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: SELLER_SERVICE_DEP,
):
    token = await service.seller_token(login_form.username, login_form.password)
    return {"access_token": token, "token_type": "jwt"}


@seller.get("/dashboard")
async def get_dashboard(logged_in_seller:LOGGED_IN_SELLER):
    
    return logged_in_seller
