from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from db.models.user import User

async def upsert_user(
    session: AsyncSession,
    telegram_id: int,
    first_name: str,
    last_name: str | None = None,
):
    stmt = upsert(User).values(
        {
            "telegram_id": telegram_id,
            "first_name": first_name,
            "last_name": last_name,
        }
    )
    stmt = stmt.on_conflict_do_update(
        index_elements=['telegram_id'],
        set_=dict(
            first_name=first_name,
            last_name=last_name,
        ),
    )
    await session.execute(stmt)
    await session.commit()


async def get_by_telegram_id(session: AsyncSession, tg_id: int) -> User | None:
    stmt = select(User).where(User.telegram_id == tg_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def update_user(session: AsyncSession, user_id: int, **fields) -> None:
    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(**fields)
        .execution_options(synchronize_session="fetch")
    )
    await session.execute(stmt)
    await session.commit()