from loguru import logger

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from dialogs.states import (
    MainMenuDialogSG,
    CreateMeeteinDialogSG,
    FindMeeteinDialogSG,
    ProfileDialogSG,
    SettingsDialogSG,
)


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