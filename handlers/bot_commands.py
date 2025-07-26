from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from db.repositories.user import UserRepository
from aiogram_dialog import DialogManager, StartMode
from dialogs.states import StartDialogSG
from sqlalchemy.ext.asyncio import AsyncSession

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, dialog_manager: DialogManager, session: AsyncSession):
    repo = UserRepository(session=session)
    await repo.upsert_user(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await message.delete()
    await dialog_manager.start(state=StartDialogSG.main, mode=StartMode.RESET_STACK)


# @router.message(Command(commands="help"))
# async def process_help_command(message: Message):
#     await message.delete()
#     await message.answer('Хелп: /help')


# @router.message(Command(commands='stat'))
# async def process_bot_stat_command(message: Message):
#     await message.delete()
#     await message.answer('Команда не доступна')


# @router.message()
# async def print_update_info(message: Message, dialog_manager: DialogManager):
#     await message.delete()
#     print(message.model_dump_json(indent=4, exclude_none=True))
#     await message.answer(str(message.model_dump_json(indent=4, exclude_none=True)))
