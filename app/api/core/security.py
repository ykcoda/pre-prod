from fastapi.security import OAuth2PasswordBearer

SELLER_OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="/sellers/token")