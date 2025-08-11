from app.core.config import get_db_url
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


DATABASE_URL = get_db_url()
engine = create_async_engine(url=DATABASE_URL, future=True)
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False)
