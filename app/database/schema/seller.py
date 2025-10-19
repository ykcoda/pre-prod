from pydantic import EmailStr
from sqlmodel import SQLModel


# Seller Base Schema
class SellerBase(SQLModel):
    name: str
    email: EmailStr


class SellerRead(SellerBase):
    pass


class SellerCreate(SellerBase):
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

