from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException

from src.db.main import get_session
from .schemas import UserSchema, UserCreateSchema
from .service import UserService


auth_router = APIRouter()
userService = UserService()


@auth_router.post("/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateSchema, session: AsyncSession = Depends(get_session)):
  email = user_data.email
  user_exists = await userService.user_exists(email, session)
  if user_exists:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already exists")
  
  new_user = await userService.create_a_user(user_data, session)
  return new_user
