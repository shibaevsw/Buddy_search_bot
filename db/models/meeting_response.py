from sqlalchemy import (
    Column, Integer, String, ForeignKey, Date, Time, Enum, Text, Boolean, DateTime
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
import enum

from db import Base
from db.models.mixins import TimestampMixin



class ResponseStatus(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    declined = "declined"
    canceled = "canceled"  # если отклик отозван пользователем


class MeetingResponse(Base, TimestampMixin):
    __tablename__ = "meeting_responses"

    id: Mapped[int] = mapped_column(primary_key=True)
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    status: Mapped[ResponseStatus] = mapped_column(
        Enum(ResponseStatus), default=ResponseStatus.pending
    )

    meeting = relationship("Meeting", back_populates="responses")
    user = relationship("User")  # если нужно получить информацию о пользователе
