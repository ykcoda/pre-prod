from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.models.shipment import Shipment
from app.database.schema.shipment import ShipmentCreate
from .base import BaseService


class ShipmentService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(Shipment, session)  # type:ignore

    async def add_shipment(self, shipment_data: ShipmentCreate, seller):
        new_shipment = Shipment(**shipment_data.model_dump(), seller_id=seller.id)
        return await self._add(new_shipment)
    
    
