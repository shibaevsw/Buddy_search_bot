from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import MainMenuDialogSG
from dialogs.handlers import MainMenuHandlers
from l10n_gen import L10n
from utils.text_formatters import as_full_width
l10n = L10n()


main_menu_dialog = Dialog(
    Window(
        Const(as_full_width(text=l10n.main_menu_header())),
        Row(
            Button(text=Format(l10n.create_meeting_btn()), id='create_meeting', on_click=MainMenuHandlers.create_meening),
            Button(text=Format(l10n.find_meeteing_btn()), id='find_meeteing', on_click=MainMenuHandlers.find_meening),
        ),
        Row(
            Button(text=Format(l10n.profile_btn()), id='profile', on_click=MainMenuHandlers.profile),
            Button(text=Format(l10n.settings_btn()), id='settings', on_click=MainMenuHandlers.settings),
        ),
        state=MainMenuDialogSG.main
    ),
)