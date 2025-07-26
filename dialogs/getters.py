from aiogram_dialog import DialogManager
from sqlalchemy.ext.asyncio import AsyncSession
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

    return data


async def get_edited_user_data(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data



async def get_edit_data(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data



async def get_cities(**kwargs):
    cities = [
        ('Сафоново', 1),
        ('Рославль', 2),
        ('Любой', 3),
    ]
    return {'cities': cities}


async def get_genders(**kwargs):
    genders = [
        ('Мужской', 'M'),
        ('Женский', 'F'),
        ('Не важно', 'O'),
    ]
    return {'genders': genders}