from fastapi import APIRouter

from app.database.schema.seller import SellerCreate
from app.api.dependencies.common import SELLER_SERVICE_DEP


seller = APIRouter(prefix="/sellers", tags=["Sellers"])


@seller.post("/")
async def register_seller(
    seller_data: SellerCreate,
    service: SELLER_SERVICE_DEP,
):
    return await service.add_seller(seller_data)
