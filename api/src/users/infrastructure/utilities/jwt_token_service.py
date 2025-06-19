import jwt
from datetime import datetime, timedelta, timezone
from src.users.application.utilities.token_service import TokenService
from src.config import get_settings
from fastapi import HTTPException

settings = get_settings()

class JWTTokenService(TokenService):
    def create_token(self, data, expires_minutes):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
        to_encode.update({"exp": expire})
        return jwt.encode(payload=to_encode, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    
    def verify_token(self, token):
        print(token)
        try:
            payload = jwt.decode(token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            return payload.get("sub")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired.")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token.")