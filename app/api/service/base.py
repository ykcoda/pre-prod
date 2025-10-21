from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseService:

    def __init__(self, model: SQLModel, session: AsyncSession):
        self.model = model
        self.session = session

    async def _add(self, entity: SQLModel):
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity
