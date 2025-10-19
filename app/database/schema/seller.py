from pydantic import EmailStr
from sqlmodel import Field, SQLModel


# Seller Base Schema
class SellerBase(SQLModel):
    name: str
    email: EmailStr
    password: str = Field(exclude=True)


class SellerRead(SellerBase):
    pass


class SellerCreate(SellerBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Jame Bright",
                "email": "jbright@yahoo.com",
                "password": "*****",
            }
        }
    }
