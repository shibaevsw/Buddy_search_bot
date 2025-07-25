from aiogram_dialog import DialogManager
from aiogram.types import User
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.user import User
from db.requests.user import select
from dialogs.virtual_keyboard import VirtualKeyboard


async def get_name(event_from_user: User, **kwargs):
    return {'name': event_from_user.first_name or 'Друг'}


async def get_user_data(dialog_manager: DialogManager, **kwargs):
    def safe(value, default="—"):
        return value if value is not None else default

    session: AsyncSession = dialog_manager.middleware_data["session"]
    tg_id = dialog_manager.event.from_user.id

    user = await session.scalar(
        select(User).where(User.telegram_id == tg_id)
    )

    # return {
    #     "user": user
    # }

    data = {
        "user": user,
    }
    data.update(dialog_manager.dialog_data)
    return data



async def vk_getter(dialog_manager: DialogManager, **kwargs):
    dialog_data = dialog_manager.dialog_data

    if "typed_text" not in dialog_data:
        dialog_data["typed_text"] = ""

    if "lang" not in dialog_data:
        dialog_data["lang"] = 'ru'

    current_text = dialog_data["typed_text"]

    return {
        "typed_text": dialog_manager.dialog_data["typed_text"],
        "lang": dialog_manager.dialog_data["lang"],
    }