from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format

from dialogs.states import CreateMeeteinDialogSG
from dialogs.handlers import NavigateHanlers

from l10n_gen import L10n
l10n = L10n()


create_miting_dialog = Dialog(
    Window(
        Const(text=l10n.create_meeting_header()),
        Format(text="Какие-то данные или инструкии или акции, да че угодно"),
        Row(
            Button(text=Format("Раз"), id="1", on_click=NavigateHanlers.go_not_fond),
            Button(text=Format("Два"), id="1", on_click=NavigateHanlers.go_not_fond),
        ),
        Row(
            Button(
                text=Format("Еще какая-то кнопка"),
                id="1",
                on_click=NavigateHanlers.go_not_fond,
            ),
            Button(
                text=Format("И еще одна чтоб было"),
                id="1",
                on_click=NavigateHanlers.go_not_fond,
            ),
        ),
        Button(text=Const(l10n.main_menu_btn()), id="exit", on_click=NavigateHanlers.close),
        state=CreateMeeteinDialogSG.main,
    ),
)
