import asyncio
from loguru import logger

from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio import Redis

from sqlalchemy.ext.asyncio  import async_sessionmaker  # уже был create_async_engine
from db.base import engine, async_session_maker
from middlewares.db import DBSessionMiddleware


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs

from settings import settings
from handlers import bot_commands
from dialogs.windows.bot_commans_dialog import bot_commands_dialog
from dialogs.windows.not_found_dialog import not_found_dialog
from dialogs.windows.main_menu_dialog import main_menu_dialog
from dialogs.windows.create_meeting_dialog import create_miting_dialog
from dialogs.windows.find_meeteing_dialog import find_miting_dialog
from dialogs.windows.profile_dialog import pofile_dialog
from dialogs.windows.settings_dialog import settings_dialog



class App:

    def __init__(self):
        self._bot: Bot | None = None
        self._dp: Dispatcher | None = None


    def _setup_logging(self) -> None:
        """Setup logging configuration."""
        # Configure loguru
        logger.add(
            "logs/bot.log",
            rotation="1 day",
            retention="7 days",
            level=settings.LOG_LEVEL,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
        )
        logger.info(f"Logging configured with level: {settings.LOG_LEVEL}")


    async def _init_storage(self):
        redis = Redis(host=settings.REDIS_HOST)
        self._storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True),)


    async def _init_database(self):
         self._session_maker: async_sessionmaker = async_session_maker


    async def _close_database(self):
        """Корректно закрыть пул соединений."""
        await engine.dispose()


    def _setup_bot_and_dispatcher(self) -> None:
        """Setup bot and dispatcher."""
        logger.info("Setting up bot and dispatcher...")

        # Create bot instance
        self._bot = Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        # Create dispatcher
        self._dp = Dispatcher(storage=self._storage)


        # Register middlewares
        self._dp.update.middleware(DBSessionMiddleware(self._session_maker))

        # Register handlers
        # self._dp.include_router(bot_commands_admin.router)
        self._dp.include_router(bot_commands.router)

        # Register dialogs
        self._dp.include_routers(bot_commands_dialog,
                                 not_found_dialog,
                                 main_menu_dialog,
                                 create_miting_dialog,
                                 find_miting_dialog,
                                 pofile_dialog,
                                 settings_dialog
                                 )

        # Setup aiogram-dialog
        setup_dialogs(self._dp)


    async def _on_startup(self) -> None:
        """Bot startup callback."""
        logger.info(f"🚀 {settings.BOT_NAME} started successfully!")
        logger.info(f"Bot description: {settings.BOT_DESCRIPTION}")

        # Set bot commands
        # TODO: админские команды в отдельный скоуп
        from keyboards.set_bot_commands import set_bot_commands
        await set_bot_commands(self._bot)

        logger.info("Bot commands set successfully")


    async def _on_shutdown(self) -> None:
                """Bot shutdown callback."""
                logger.info("🛑 Shutting down bot...")
                if self._bot:
                    await self._bot.session.close()
                logger.info("Bot shutdown completed")


    async def run(self) -> None:
                """Run the bot application."""
                try:
                    # Setup logging
                    self._setup_logging()

                    # Initialize memory storage
                    await self._init_storage()

                    # Initialize database
                    await self._init_database()

                    # Setup bot and dispatcher
                    self._setup_bot_and_dispatcher()

                    # Run startup callback
                    await self._on_startup()

                    # Start polling
                    logger.info("Starting bot polling...")
                    await self._dp.start_polling(self._bot)

                except Exception as e:
                    logger.error(f"Error running bot: {e}")
                    raise
                finally:
                    # Cleanup
                    await self._on_shutdown()
                    await self._close_database()


async def main() -> None:
    """Main entry point."""
    app = App()
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())