from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseService:

    def __init__(self, model: SQLModel, session: AsyncSession):
        self.model = model
        self.session = session

    # Get by ID
    async def _get(self, id):
        return self.session.get(self.model, id)

    # Get all entries of an entities
    async def _get_all(self):
        return self.session.exec(select(self.model).all())

    # Create an entity
    async def _add(self, entity: SQLModel):
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    # Update an entity
    async def _update(self, entity: SQLModel):
        return await self._add(entity)

    # Delete an entity
    async def _delete(self, entity: SQLModel):
        await self.session.delete(entity)
