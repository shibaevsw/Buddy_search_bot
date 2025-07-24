from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from bot_commands.bot_commands import BOT_COMMANDS_RU

# TODO: админские команды в отдельный скоуп
async def set_bot_commands(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in BOT_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(commands=main_menu_commands, scope=BotCommandScopeDefault())