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
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Jame Bright",
                "email": "jbright@yahoo.com",
                "password": "*****"
            }
        }
    }

