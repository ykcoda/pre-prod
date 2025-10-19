from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class User(SQLModel):
    name: str
    email: EmailStr
    password: str  = Field(exclude=True)