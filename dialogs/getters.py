import pprint
from traceback import print_tb
from aiogram_dialog import DialogManager
from aiogram.types import User
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import user
from db.models.user import User
from db.repositories.user import UserRepository



def user_to_dict(user) -> dict:
    allowed_types = (str, int, float, bool, type(None))
    return {
        col.name: getattr(user, col.name)
        for col in user.__table__.columns
        if isinstance(getattr(user, col.name), allowed_types)
    }


async def get_user_data(dialog_manager: DialogManager, **kwargs):

    session: AsyncSession = dialog_manager.middleware_data["session"]
    repo = UserRepository(session)
    tg_id = dialog_manager.event.from_user.id

    user = await repo.get_by_telegram_id(tg_id)

    user_dict = user_to_dict(user)
    dialog_manager.dialog_data.update(user_dict)


    data = {
        "user": user,
    }

    pprint.pprint(data)
    pprint.pprint(dialog_manager.dialog_data)
    return data


async def get_edited_user_data(dialog_manager: DialogManager, **kwargs):
    pprint.pprint(dialog_manager.dialog_data)
    return dialog_manager.dialog_data



async def get_edit_data(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data


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