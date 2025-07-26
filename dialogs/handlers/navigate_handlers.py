from loguru import logger

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from dialogs.states import NotFoundDialogSG


class NavigateHanlers:

    # Временная заглушка для обратки нажатий кнопок, для которые пока нет хэндлеров
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