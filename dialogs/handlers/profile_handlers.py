from typing import Any
from loguru import logger

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from db.repositories.user import UserRepository

from dialogs.states import ProfileDialogSG


class ProfileHandlers:
    async def edit(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.switch_to(state=ProfileDialogSG.edit)



    async def edit_first_name(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_first_name)


    async def input_first_name(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
        dialog_manager.dialog_data['first_name'] = text
        await message.delete()
        await dialog_manager.switch_to(ProfileDialogSG.edit,
                                       show_mode=ShowMode.EDIT
                                       )
        await dialog_manager.show()


    async def edit_last_name(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_last_name)


    async def input_last_name(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
        dialog_manager.dialog_data['last_name'] = text
        await message.delete()
        await dialog_manager.switch_to(ProfileDialogSG.edit, show_mode=ShowMode.EDIT)


    async def edit_city(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_city)


    # TODO: Сделать выбор из кнопок
    async def input_city(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
        dialog_manager.dialog_data["city"] = text
        await message.delete()
        await dialog_manager.switch_to(ProfileDialogSG.edit, show_mode=ShowMode.EDIT)


    async def edit_age(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_age)

    # TODO: Сделать ввод с инлайн клавиатуры
    async def input_age(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str | int):
        dialog_manager.dialog_data["age"] = text
        await message.delete()
        await dialog_manager.switch_to(ProfileDialogSG.edit, show_mode=ShowMode.EDIT)


    async def edit_gender(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_gender)


    # TODO: Сделать выбор из кнопок
    async def input_gender(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
        dialog_manager.dialog_data["gender"] = text
        await message.delete()
        await dialog_manager.switch_to(ProfileDialogSG.edit, show_mode=ShowMode.EDIT)



    async def save_profile(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        tg_id = callback.from_user.id
        session = dialog_manager.middleware_data['session']
        repo = UserRepository(session)
        user = await repo.get_by_telegram_id(tg_id)

        data = dialog_manager.dialog_data
        update_data = {}

        # Универсальные функции преобразования
        def convert_gender(value: Any) -> str | None:
            if isinstance(value, str) and value in {'M', 'F', 'O', 'N'}:
                return value  # уже в правильном формате

            mapping = {
                "Мужской": "M",
                "Женский": "F",
                "Другое": "O",
                "Не указан": "N"
            }
            return mapping.get(str(value), "N")

        def convert_age(value: Any) -> int | None:
            if value is None:
                return None
            if isinstance(value, int):
                return value  # уже число
            if str(value) == "—" or not str(value).isdigit():
                return None
            return int(value)

        def convert_city(value: Any) -> str | None:
            if value in [None, "—"]:
                return None
            return str(value)

        def convert_name(value: Any) -> str | None:
            if value in [None, "—"]:
                return None
            return str(value)

        # Преобразование данных
        if "first_name" in data:
            update_data["first_name"] = convert_name(data["first_name"])

        if "last_name" in data:
            update_data["last_name"] = convert_name(data["last_name"])

        if "city" in data:
            update_data["city"] = convert_city(data["city"])

        if "age" in data:
            update_data["age"] = convert_age(data["age"])

        if "gender" in data:
            update_data["gender"] = convert_gender(data["gender"])

        # Сохранение только если есть изменения
        if update_data:
            await repo.update_user(user_id=user.id, **update_data)

        await dialog_manager.switch_to(ProfileDialogSG.main)