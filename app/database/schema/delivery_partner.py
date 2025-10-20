from pydantic import EmailStr
from sqlmodel import Field, SQLModel


# Delivery Partner Base Schema
class DeliveryPartnerBase(SQLModel):
    name: str
    email: EmailStr
    password: str = Field(exclude=True)


class DeliveryPartnerRead(DeliveryPartnerBase):
    pass


class DeliveryPartnerCreate(DeliveryPartnerBase):
    password: str
    servicable_zip_codes: list[int]
    max_handling_capacity: int
    
    
