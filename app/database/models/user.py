from pydantic import EmailStr
from sqlmodel import SQLModel


class User(SQLModel):
    name: str
    email: EmailStr
    password: str 