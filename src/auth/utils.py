from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import uuid
import logging

from src.config import Config

passwd_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 3600


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)
    return hash


def verify_passwd(password: str, hash: str) -> bool:
    return passwd_context.verify(password.get_secret_value(), hash)


def create_access_token(
    user_data: dict, expiry: timedelta = None, refresh: bool = False
) -> str:
    payload = {}
    payload["user"] = user_data
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh
    payload["exp"] = datetime.now() + (
        expiry if expiry else timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    )
    token = jwt.encode(
        payload=payload, key=Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM
    )
    return token


def decode_access_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token, key=Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None
