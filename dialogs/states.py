from aiogram.fsm.state import StatesGroup, State


class NotFoundDialogSG(StatesGroup):
    main = State()

class StartDialogSG(StatesGroup):
    main = State()


class MainMenuDialogSG(StatesGroup):
    main = State()
    my_profile = State()
    change_city = State()
    settings = State()

class CreateMeeteinDialogSG(StatesGroup):
    main = State()

class FindMeeteinDialogSG(StatesGroup):
    main = State()

class ProfileDialogSG(StatesGroup):
    main = State()
    edit = State()
    edit_first_name = State()
    edit_last_name = State()
    edit_city = State()
    edit_age = State()
    edit_gender = State()
    edit_inline = State()
    confirm = State()

class SettingsDialogSG(StatesGroup):
    main = State()
