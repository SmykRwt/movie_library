from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)

SECRET_KEY = "mysupersecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return user_id

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    user_id = verify_access_token(
        token
    )

    db = SessionLocal()

    user = db.query(
        models.User
    ).filter(
        models.User.id == user_id
    ).first()

    db.close()

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user

def get_current_admin(
    current_user=Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Only admins allowed"
        )

    return current_user