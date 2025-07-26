from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )



class SafeDisplayMixin:
    _safe_defaults = {
        "gender": {
            "M": "Мужской",
            "F": "Женский",
            "O": "Другое",
            "N": "Не указан",
            None: "—",
        },
        "role": {
            "ADMIN": "Админ",
            "MODERATOR": "Модератор",
            "USER": "Пользователь",
            None: "—",
        },
    }

    _default_fallback = "—"

    def __getattribute__(self, name: str):
        try:
            value = super().__getattribute__(name)

            # Для системных атрибутов возвращаем как есть
            if name.startswith("_") or callable(value):
                return value

            if name in SafeDisplayMixin._safe_defaults:
                return SafeDisplayMixin._safe_defaults[name].get(value, SafeDisplayMixin._default_fallback)

            return value if value is not None else SafeDisplayMixin._default_fallback

        except AttributeError:
            raise
