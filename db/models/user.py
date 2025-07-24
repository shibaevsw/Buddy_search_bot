from types import SimpleNamespace
from sqlalchemy import BigInteger, CheckConstraint, String, Integer, CHAR, text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
from db.models.mixins import SafeDisplayMixin, TimestampMixin

class User(Base, TimestampMixin, SafeDisplayMixin):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint("gender IN ('M', 'F', 'O', 'N')", name="ck_gender_valid"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str | None] = mapped_column(String, nullable=True)
    city: Mapped[str | None] = mapped_column(String, nullable=True)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    gender: Mapped[str | None] = mapped_column(CHAR(1), server_default=text("'N'"))
    role: Mapped[str | None] = mapped_column(String, server_default=text("'USER'"))
