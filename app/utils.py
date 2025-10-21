import jwt
from datetime import timedelta, datetime, timezone


from app.config import security_settings


def encode_access_code(data: dict, expiry: timedelta = timedelta(hours=2)):

    return jwt.encode(
        payload={**data, "exp": datetime.now(timezone.utc) + expiry},
        algorithm=security_settings.JWT_ALGORITHM,
        key=security_settings.JWT_SECRET,
    )


def decode_access_code(token: str):
    try:
        return jwt.decode(
            jwt=token,
            algorithms=[security_settings.JWT_ALGORITHM],
            key=security_settings.JWT_SECRET,
        )
    except jwt.PyJWTError:
        return None
