from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from .models import User
from .schemas import UserCreateSchema
from .utils import generate_passwd_hash

class UserService:
  async def get_user_by_email(self, email: str, session: AsyncSession):
    statement = select(User).where(User.email == email)
    result = await session.exec(statement)
    user = result.first()
    return user
  
  async def user_exists(self, email: str, session: AsyncSession) -> bool:
    user = await self.get_user_by_email(email, session)
    return False if User else True
  
  async def create_a_user(self, user: UserCreateSchema, session: AsyncSession):
    user_data_dict = user.model_dump()
    new_user = User(**user_data_dict)
    new_user.password_hash = generate_passwd_hash(user_data_dict["password"].get_secret_value())
    session.add(new_user)
    await session.commit()
    return new_user
