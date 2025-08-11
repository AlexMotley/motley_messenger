from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db


ping_router = APIRouter(tags=["Database Check"])


@ping_router.get("/db-ping")
async def db_ping(db: AsyncSession = Depends(get_db)):
    """Проверка подключения к базе данных"""
    try:
        # Простейший SQL-запрос для проверки соединения
        result = await db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connection OK", "data": result.scalar()}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    