from sqlmodel.ext.asyncio.session import AsyncSession

from app.api.services.delivery_partner import DeliveryPartnerService
from app.database.models.shipment import Shipment
from app.database.schema.shipment import ShipmentCreate
from .base import BaseService


class ShipmentService(BaseService):

    def __init__(self, session: AsyncSession, partner_service: DeliveryPartnerService):
        super().__init__(Shipment, session)  # type:ignore
        self.partner_service = partner_service

    async def add_shipment(self, shipment_data: ShipmentCreate, seller):
        new_shipment = Shipment(**shipment_data.model_dump(), seller_id=seller.id)

        # Assign a partner
        await self.partner_service.assign_shipment(new_shipment)

        return await self._add(new_shipment)
