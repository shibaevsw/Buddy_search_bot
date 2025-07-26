from turtle import width
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row, Column, Select
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput

from dialogs.states import ProfileDialogSG
from dialogs.handlers.navigate_handlers import NavigateHanlers
from dialogs.handlers.profile_handlers import ProfileHandlers

from dialogs.getters import get_cities, get_user_data, get_edited_user_data

from l10n_gen import L10n
l10n = L10n()
from utils.text_formatters import as_full_width



pofile_dialog = Dialog(

    Window(
        Const(text=as_full_width(l10n.profile_header())),
        Format(l10n.profile_data()),
        Button(text=Format(l10n.edit_btn()), id="edit", on_click=ProfileHandlers.edit),
        Button(text=Format(l10n.main_menu_btn()), id="exit", on_click=NavigateHanlers.close),
        getter=get_user_data,
        state=ProfileDialogSG.main,
    ),

    Window(
        Const(text=as_full_width(l10n.edit_header())),
        Format(l10n.edit_profile_data()),
        Column(
            Button(Const("✏️ Имя"), id="edit_first_name", on_click=ProfileHandlers.edit_first_name),
            Button(Const("✏️ Фамилия"), id="edit_last_name", on_click=ProfileHandlers.edit_last_name),
            Button(Const("🎂 Возраст"), id="edit_age", on_click=ProfileHandlers.edit_age),
            Button(Const("🏙 Город"), id="edit_city", on_click=ProfileHandlers.edit_city),
            Button(Const("🚻 Пол"), id="edit_gender", on_click=ProfileHandlers.edit_gender),
        ),
        Row(
            Button(Format(text=l10n.cancel_btn()), id="cancel", on_click=NavigateHanlers.go_back),
            Button(Format(text=l10n.confirm_btn()), id="confirm", on_click=ProfileHandlers.save_profile),
        ),
        getter=get_edited_user_data,
        state=ProfileDialogSG.edit,
    ),

    Window(
        Const(as_full_width("Введите новое имя:")),
        Button(Format(text=l10n.cancel_btn()), id="cancel", on_click=ProfileHandlers.edit),
        TextInput(id="input_first_name", on_success=ProfileHandlers.input_first_name),
        state=ProfileDialogSG.edit_first_name,
    ),

    Window(
        Const(as_full_width("Введите фамилию:")),
        Button(Format(text=l10n.cancel_btn()), id="cancel", on_click=ProfileHandlers.edit),
        TextInput(id="input_last_name", on_success=ProfileHandlers.input_last_name),
        state=ProfileDialogSG.edit_last_name,
    ),

    Window(
        Const(as_full_width("Введите возраст:")),
        Button(Format(text=l10n.cancel_btn()), id="cancel", on_click=ProfileHandlers.edit),
        TextInput(id="input_age", on_success=ProfileHandlers.input_age),
        state=ProfileDialogSG.edit_age,
    ),

    Window(
        Const(as_full_width("Выберите город:")),
        Column(
            Select(Format('{item[0]}'),
               id='city',
               item_id_getter=lambda x: x[0],
               items='cities',
               on_click=ProfileHandlers.select_city),
        ),
        Button(Format(text=l10n.cancel_btn()), id="cancel", on_click=ProfileHandlers.edit),
        getter=get_cities,
        state=ProfileDialogSG.edit_city,
    ),

    Window(
        Const(as_full_width("Введите пол:")),
        Button(Format(text=l10n.cancel_btn()), id="cancel", on_click=ProfileHandlers.edit),
        TextInput(id="input_city", on_success=ProfileHandlers.input_gender),
        state=ProfileDialogSG.edit_gender,
    ),
)
