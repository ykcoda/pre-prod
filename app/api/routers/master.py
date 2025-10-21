from fastapi import APIRouter
from .seller import seller
from .delivery_partner import partner
from .shipment import shipment


master = APIRouter()
master.include_router(seller)
master.include_router(partner)
master.include_router(shipment)
