from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.database.models.user import User

from .base import BaseService


class UserService(BaseService):

    def __init__(self, model: User, session: AsyncSession):
        super().__init__(model, session)

    async def _get_by_email(self, email):
        statement = select(self.model).where(self.model.email == email)
        result = await self.session.exec(statement)
        return result.first()
