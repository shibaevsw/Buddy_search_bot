import pprint
from loguru import logger

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.user import UserRepository
from dialogs.states import (
    MainMenuDialogSG,
    NotFoundDialogSG,
    CreateMeeteinDialogSG,
    FindMeeteinDialogSG,
    ProfileDialogSG,
    SettingsDialogSG,
)




class NavigateHanlers:

    async def go_not_fond(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.start(state=NotFoundDialogSG.main)

    async def go_next(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.next()

    async def go_back(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.back()

    async def close(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.done()


class MainMenuHandlers:
    async def main_menu(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.start(state=MainMenuDialogSG.main)

    async def create_meening(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.start(state=CreateMeeteinDialogSG.main)

    async def find_meening(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.start(state=FindMeeteinDialogSG.main)

    async def profile(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.start(state=ProfileDialogSG.main)

    async def settings(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.start(state=SettingsDialogSG.main)


class ProfileHandlers:
    async def edit(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
    ):
        await dialog_manager.switch_to(state=ProfileDialogSG.edit)


    async def edit_first_name(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_first_name)


    async def input_first_name(message: Message, dialog_manager: DialogManager):
        dialog_manager.dialog_data["first_name"] = message.text
        await dialog_manager.switch_to(ProfileDialogSG.edit)


    async def edit_last_name(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_last_name)


    async def input_last_name(message: Message, dialog_manager: DialogManager):
        dialog_manager.dialog_data["last_name"] = message.text
        await dialog_manager.switch_to(ProfileDialogSG.edit)


    async def edit_city(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_city)


    # Сделать выбор из кнопок
    async def input_city(message: Message, button: Button, dialog_manager: DialogManager):
        dialog_manager.dialog_data["city"] = message.text
        await dialog_manager.switch_to(ProfileDialogSG.edit)


    async def edit_age(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_age)


    async def input_age(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, age: str | int):
        dialog_manager.dialog_data["age"] = message.text
        await dialog_manager.switch_to(ProfileDialogSG.edit)


    async def edit_gender(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_gender)


    # Сделать выбор из кнопок
    async def input_gender(message: Message, button: Button, dialog_manager: DialogManager):
        dialog_manager.dialog_data["gender"] = message.text
        await dialog_manager.switch_to(ProfileDialogSG.edit)


    async def edit_inline(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await dialog_manager.switch_to(ProfileDialogSG.edit_inline)




    # Повтори аналогично для других полей

    # @staticmethod
    # async def save_profile(callback: CallbackQuery, dialog_manager: DialogManager, **_):
    #     tg_id = callback.from_user.id
    #     user = await get_by_telegram_id(tg_id)

    #     data = dialog_manager.dialog_data
    #     if "first_name" in data:
    #         user.first_name = data["first_name"]
    #     if "last_name" in data:
    #         user.last_name = data["last_name"]
    #     if "city" in data:
    #         user.city = data["city"]
    #     if "age" in data:
    #         user.age = int(data["age"])
    #     if "gender" in data:
    #         user.gender = data["gender"]

    #     await session.commit()
    #     await dialog_manager.switch_to(ProfileDialogSG.main)