from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from db.models.user import User

from typing import Optional



class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upsert_user(self, telegram_id: int, first_name: str, last_name: Optional[str] = None) -> None:
        stmt = upsert(User).values(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
        ).on_conflict_do_update(
            index_elements=["telegram_id"],
            set_={
                "first_name": first_name,
                "last_name": last_name,
            },
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_by_telegram_id(self, tg_id: int) -> Optional[User]:
        stmt = select(User).where(User.telegram_id == tg_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_user(self, user_id: int, **fields) -> None:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(**fields)
            .execution_options(synchronize_session="fetch")
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def delete_user(self, user_id: int) -> None:
        stmt = delete(User).where(User.id == user_id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def create_user(self, telegram_id: int, first_name: str, last_name: Optional[str] = None) -> User:
        user = User(telegram_id=telegram_id, first_name=first_name, last_name=last_name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user




