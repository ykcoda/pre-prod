from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.api.service.delivery_partner import DeliveryPartnerService
from app.database.models.shipment import Shipment, ShipmentStatus
from app.database.schema.shipment import ShipmentCreate
from .base import BaseService


class ShipmentService(BaseService):
    def __init__(self, session: AsyncSession, partner_service: DeliveryPartnerService):
        super().__init__(Shipment, session)  # type:ignore
        self.partner_service = partner_service

    async def get_shipment(self, id):
        return await self._get(id)

    async def get_all_shipment_by_seller(self, seller_id) -> Shipment:
        result = await self.session.exec(
            select(Shipment).where(Shipment.seller_id == seller_id)
        )

        return result.all()  # type:ignore

    async def add_shipment(self, shipment_data: ShipmentCreate, seller_id: str):
        new_shipment = Shipment(
            **shipment_data.model_dump(),
            seller_id=seller_id,
            status=ShipmentStatus.placed
        )

        await self.partner_service.assign_shipment(new_shipment)

        return await self._add(new_shipment)
