from pydantic import EmailStr
from sqlmodel import SQLModel


class SellerBase(SQLModel):
    name: str
    email: EmailStr


class SellerRead(SellerBase):
    pass


class SellerCreate(SellerBase):
    password: str
