from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.database.schema.seller import SellerCreate
from app.api.dependencies.common import SELLER_SERVICE_DEP


seller = APIRouter(prefix="/sellers", tags=["Sellers"])


@seller.post("/")
async def register_seller(
    seller_data: SellerCreate,
    service: SELLER_SERVICE_DEP,
):
    return await service.add_seller(seller_data)


@seller.post("/token")
async def seller_login(
    login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: SELLER_SERVICE_DEP,
):
    token = await service.get_token(login_data.username, login_data.password)
    return {"access_token": token, "token_type": "jwt"}
