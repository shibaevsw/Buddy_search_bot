from aiogram_dialog import Dialog, Window

from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import NotFoundDialogSG
from dialogs.handlers.main_menu_handlers import MainMenuHandlers
from dialogs.handlers.navigate_handlers import NavigateHanlers

from l10n_gen import L10n
l10n = L10n()


not_found_dialog = Dialog(
    Window(
        Const(text='<b>Тут пока ничего нет</b>'),
        Format(text='Но скоро будет...'),
        Button(text=Format(l10n.back_btn()), id='go_back', on_click=NavigateHanlers.close),
        Button(text=Const(l10n.main_menu_btn()), id='menu', on_click=MainMenuHandlers.main_menu),
        state=NotFoundDialogSG.main
    ),
)