from sqlmodel.ext.asyncio.session import AsyncSession
from passlib.context import CryptContext  # type: ignore


from app.database.models.user import User

from .base import BaseService

password_context = CryptContext(schemes=["bcrypt"])


class UserService(BaseService):

    def __init__(self, model: User, session: AsyncSession):
        self.model = model
        self.session = session

    async def add_user(self, user_data: dict):
        new_user = self.model(
            **user_data, hashed_password=password_context.hash(user_data["password"])
        )  # type: ignore

        return await self._add(new_user)
