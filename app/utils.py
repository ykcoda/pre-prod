import jwt
from datetime import timedelta, datetime

from app.config import security_settings


# Encode with JWT
def encode_access_token(data: dict, expiry: timedelta = timedelta(hours=2)):
    return jwt.encode(
        payload={**data, "exp": datetime.now() + expiry},
        algorithm=security_settings.JWT_ALGORITHM,
        key=security_settings.JWT_SCRET,
    )


# Decode token with JWT
def decode_access_token(token: str):
    try:
        return jwt.decode(
            jwt=token,
            algorithms=[security_settings.JWT_ALGORITHM],
            key=security_settings.JWT_SCRET,
        )
    except jwt.PyJWTError:
        return None
