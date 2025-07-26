from aiogram import Router, F
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from dialogs.states import ProfileDialogSG

router = Router()


@router.message()
async def print_update_info(message: Message, dialog_manager: DialogManager):
    await message.delete()
    print(message.model_dump_json(indent=4, exclude_none=True))
    # await message.answer(str(message.model_dump_json(indent=4, exclude_none=True)))