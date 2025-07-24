# from aiogram import Router
# from aiogram.types import Message
# from aiogram.filters import Command, CommandStart


# router = Router()

# сделать так, что бы сюда передавался видоизменный текст с возможностями админа и уведомлением, что пользователь админ
# @router.message(CommandStart())
# async def process_bot_stat_command(message: Message):
#     await message.answer('You are admin\n'
#                         'Старт: /start\n' \
#                         'Хелп: /help\n'
#                         'Статистика: /stat')


# @router.message(Command(commands='stat'))
# async def process_bot_stat_command(message: Message):
#     await message.delete()
#     await message.answer('Статистика вот она тут')