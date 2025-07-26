from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import FindMeeteinDialogSG, NotFoundDialogSG
from dialogs.handlers import NavigateHanlers
from l10n_gen import L10n
from utils.text_formatters import as_full_width
l10n = L10n()


find_miting_dialog = Dialog(
    Window(
        Const(as_full_width(text=l10n.find_meeting_header())),
        Format(text="Какие-то данные или инструкии или акции, да че угодно"),
        Row(
            Button(
                text=Format("Кнопка 1"), id="1", on_click=NavigateHanlers.go_not_fond
            ),
            Button(
                text=Format("Кнопка 2"), id="1", on_click=NavigateHanlers.go_not_fond
            ),
        ),
        Row(
            Button(
                text=Format("Мож фильтр какой"),
                id="1",
                on_click=NavigateHanlers.go_not_fond,
            ),
            Button(
                text=Format("Еще ченить"), id="1", on_click=NavigateHanlers.go_not_fond
            ),
        ),
        Button(text=Const(l10n.main_menu_btn()), id="exit", on_click=NavigateHanlers.close),
        state=FindMeeteinDialogSG.main,
    ),
)
