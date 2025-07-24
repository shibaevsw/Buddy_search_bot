from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from settings import settings

class Base(DeclarativeBase):
    pass  # сюда будут наследоваться модели

engine = create_async_engine(settings.POSTGRES_DSN, echo=False, pool_pre_ping=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Опционально: функция‑генератор для middleware
async def session_generator():
    async with async_session_maker() as session:
        yield session