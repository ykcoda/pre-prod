from fastapi import APIRouter

from app.database.schema.seller import SellerCreate


seller = APIRouter(prefix="/sellers", tags=["Sellers"])


@seller.post("/")
async def register_seller(seller_data: SellerCreate):
    pass
