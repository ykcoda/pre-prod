from fastapi import APIRouter
from .seller import seller

master = APIRouter()
master.include_router(seller)
