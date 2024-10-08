from fastapi import APIRouter

from passlib.context import CryptContext

from src.api.hotels import router
from src.database import async_session_maker
from src.respositories.users import UserRepository
from src.schemas.users import UserAdd, UserRequestAdd

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
async def register_user(
        data: UserRequestAdd
):
    hash_password = pwd_context.hash(data.password)
    new_user_data = UserAdd(email=data.email, hash_password=hash_password)
    async with async_session_maker() as session:
        result = await UserRepository(session).get_one_or_one(email=data.email)
        if result is None:
                await UserRepository(session).add(new_user_data)
                await session.commit()
                return {"status": "OK"}
        else:
            return {"already created"}


