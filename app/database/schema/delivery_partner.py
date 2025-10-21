from pydantic import EmailStr
from sqlmodel import ARRAY, INTEGER, Column, Field, SQLModel


class DeliveryPartnerBase(SQLModel):
    name:str
    email: EmailStr 


class DeliveryPartnerRead(DeliveryPartnerBase):
    pass


class DeliveryPartnerCreate(DeliveryPartnerBase):
    max_capacity: int
    servicable_zipcodes: list[int] = Field(sa_column=Column(ARRAY(INTEGER)))