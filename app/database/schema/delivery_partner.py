from pydantic import EmailStr
from sqlmodel import ARRAY, INTEGER, Column, Field, SQLModel


class DeliveryPartnerBase(SQLModel):
    name: str
    email: EmailStr


class DeliveryPartnerRead(DeliveryPartnerBase):
    pass


class DeliveryPartnerCreate(DeliveryPartnerBase):
    password: str
    max_capacity: int
    servicable_zipcodes: list[int] = Field(sa_column=Column(ARRAY(INTEGER)))


class DeliveryPartnerUpdate(SQLModel):
    max_capacity: int | None = Field(default=None)
    servicable_zipcodes: list[int] | None = Field(
        sa_column=Column(ARRAY(INTEGER)), default=None
    )
