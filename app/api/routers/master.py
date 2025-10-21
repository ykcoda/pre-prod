from fastapi import APIRouter
from .seller import seller
from .delivery_partner import partner

master = APIRouter()
master.include_router(seller)
master.include_router(partner)
