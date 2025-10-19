from pydantic import EmailStr
from sqlmodel import SQLModel


# Delivery Partner Base Schema
class DeliveryPartnerBase(SQLModel):
    name: str
    email: EmailStr


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

