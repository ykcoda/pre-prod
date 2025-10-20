from sqlmodel import select
from fastapi import HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from passlib.context import CryptContext  # type: ignore
from app.database.models.user import User


from .base import BaseService
from app.utils import encode_access_token


password_context = CryptContext(schemes="bcrypt")


class UserService(BaseService):

    def __init__(self, model: User, session: AsyncSession):
        self.model = model
        self.session = session

    async def _add_user(self, user_data: dict):
        new_user = self.model(
            **user_data, password_hash=password_context.hash(user_data["password"])
        )  # type:ignore

        return await self._add(new_user)

    async def _get_user_by_email(self, email):
        statement = select(self.model).where(self.model.email == email)
        result = await self.session.exec(statement)
        return result.first()

    async def _get_user_token(self, email, password):
        user = await self._get_user_by_email(email)

        if user is None or not password_context.verify(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized"
            )

        return encode_access_token(
            {"user": {"email": user.email, "id": str(user.id)}},
        )
