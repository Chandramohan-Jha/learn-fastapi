from pydantic import BaseModel, Field, EmailStr, SecretStr
from datetime import datetime


class UserSchema(BaseModel):
    uid: str
    username: str
    email: str
    password_hash: str = Field(exclude=True)
    first_name: str
    last_name: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    username: str = Field(min_length=4, max_length=20)
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    first_name: str
    last_name: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=8)
