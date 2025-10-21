from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel):
    name: str
    email: EmailStr
    
