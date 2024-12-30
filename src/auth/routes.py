from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from datetime import timedelta

from src.db.main import get_session
from .schemas import UserSchema, UserCreateSchema, UserLoginSchema
from .service import UserService
from .utils import verify_passwd, create_access_token, decode_access_token


auth_router = APIRouter()
userService = UserService()

REFRESH_TOKEN_EXPIRY = timedelta(days=2)


@auth_router.post(
    "/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_data: UserCreateSchema, session: AsyncSession = Depends(get_session)
):
    email = user_data.email
    user_exists = await userService.user_exists(email, session)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User already exists"
        )

    new_user = await userService.create_a_user(user_data, session)
    return new_user


@auth_router.post("/login")
async def login(
    user_data: UserLoginSchema, session: AsyncSession = Depends(get_session)
):
    email = user_data.email
    password = user_data.password

    user = await userService.get_user_by_email(email, session)
    if user:
        password_valid = verify_passwd(password, user.password_hash)
        if password_valid:
            access_token = create_access_token(
                user_data={"email": email, "user_uid": user.uid}
            )
            refresh_token = create_access_token(
                user_data={
                    "email": email,
                    "user_uid": user.uid,
                },
                refresh=True,
                expiry=REFRESH_TOKEN_EXPIRY,
            )

            return JSONResponse(
                content={
                    "message": "User logged in successfully",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {"uid": user.uid, "email": email},
                }
            )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
    )
