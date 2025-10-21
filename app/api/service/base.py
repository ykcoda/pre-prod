from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseService:

    def __init__(self, model: SQLModel, session: AsyncSession):
        self.model = model
        self.session = session

    async def _get(self, id: str):
        return await self.session.get(self.model, id)  # type:ignore

    async def _get_all(self):
        result = await self.session.exec(select(self.model))
        return result.all()

    async def _add(self, entity: SQLModel):
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def _update(self, entity: SQLModel):
        return await self._add(entity)
