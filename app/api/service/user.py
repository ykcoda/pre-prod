from sqlmodel.ext.asyncio.session import AsyncSession
from passlib.context import CryptContext  # type: ignore
from sqlmodel import select
from fastapi import HTTPException, status

from app.database.models.user import User
from app.utils import request_access_code

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

    async def get_user_by_email(self, email) -> User | None:
        result = await self.session.exec(
            select(self.model).where(self.model.email == email)  # type:ignore
        )
        return result.first()

    async def get_user_access_token(self, email, password):
        user = await self.get_user_by_email(email)

        if user is None or not password_context.verify(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access"
            )

        data = {"user": {"email": user.email, "id": str(user.id)}}
        
        return request_access_code(data)
