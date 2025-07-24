from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import StartDialogSG
from dialogs.handlers import MainMenuHandlers
from dialogs.getters import get_name

from l10n_gen import L10n


l10n = L10n()


bot_commands_dialog = Dialog(
    Window(
        Format(l10n.welcome_user(name='{name}')),
        Format(text=l10n.start_command_answer()),
        Button(text=Const(l10n.main_menu_btn()), id='main_menu', on_click=MainMenuHandlers.main_menu),
        getter=get_name,
        state=StartDialogSG.main
        ),
)