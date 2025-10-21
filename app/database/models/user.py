from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel):
    name: str
    email: EmailStr
    password: str = Field(exclude=True)
