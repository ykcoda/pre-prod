from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field

from .user import User


class Seller(User, table=True):
    __tablename__ = "sellers"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now()) 