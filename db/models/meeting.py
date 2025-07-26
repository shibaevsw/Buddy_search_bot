import datetime
from typing import Optional

from attr import dataclass
from sqlalchemy import (
    Column, Integer, String, ForeignKey, Date, Time, Enum, Text, Boolean
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db import Base
from db.models.mixins import TimestampMixin
import enum


class MeetingStatus(enum.Enum):
    open = "open"                # Заявка открыта, доступна для откликов
    closed = "closed"            # Заявка закрыта автором вручную
    expired = "expired"          # Просрочена (дата истекла)
    filled = "filled"            # Нужное количество напарников найдено


class Meeting(Base, TimestampMixin):
    __tablename__ = "meetings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    activity: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)

    meeting_date: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)
    meeting_time: Mapped[Optional[datetime.time]] = mapped_column(Time, nullable=True)

    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[MeetingStatus] = mapped_column(Enum(MeetingStatus), default=MeetingStatus.open)

    is_permanent: Mapped[bool] = mapped_column(Boolean, default=False)

    # Отношения
    creator = relationship("User", back_populates="meetings")
    responses = relationship("MeetingResponse", back_populates="meeting", cascade="all, delete-orphan")
