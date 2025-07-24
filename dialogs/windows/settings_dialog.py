from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import SettingsDialogSG, NotFoundDialogSG
from dialogs.handlers import NavigateHanlers
from l10n_gen import L10n
l10n = L10n()

settings_dialog = Dialog(
    Window(
        Const(text=l10n.settings_header()),
        Format(text="НУ тут заданные параметры"),
        Row(
            Button(
                text=Format("Редактировать то"),
                id="1",
                on_click=NavigateHanlers.go_not_fond,
            ),
            Button(
                text=Format("Редактировмть сё"),
                id="1",
                on_click=NavigateHanlers.go_not_fond,
            ),
        ),
        Button(text=Format(l10n.main_menu_btn()), id="exit", on_click=NavigateHanlers.close),
        state=SettingsDialogSG.main,
    ),
)
