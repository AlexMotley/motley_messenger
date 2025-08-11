from fastapi import APIRouter
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserResponse, UserCreate

users_router = APIRouter(prefix="/users")

@users_router.get('/', summary="Вывести список пользователей", response_model=List[UserResponse])
async def list_users():
    pass


@users_router.post('/', summary="Создать пользователя", response_model=UserCreate)
async def create_user():
    pass


@users_router.get('/{user_id}', summary="Вывести данные о пользователе", response_model=UserResponse)
async def get_user():
    pass



@users_router.get("/test-db")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(1))
    return {"status": "success", "data": result.scalar()}
