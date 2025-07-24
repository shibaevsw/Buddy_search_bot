import os
import dotenv


dotenv.load_dotenv(override=True)


class Settings:
    # Bot settings
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    BOT_NAME: str = os.getenv("BOT_NAME", "TelegramBot")
    BOT_DESCRIPTION: str = os.getenv("BOT_DESCRIPTION", "Telegram Bot")
    ADMIN_IDS: str = os.getenv('ADMIN_IDS')
    ADMINS_CHAT: str = os.getenv("ADMINS_CHAT")

    # Logging settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL")

    # Database Configuration
    DB_NAME: str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")

    @property
    def POSTGRES_DSN(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # PgAdmin
    PGADMIN_DEFAULT_EMAIL: str = os.getenv("PGADMIN_DEFAULT_EMAIL")
    PGADMIN_DEFAULT_PASSWORD: str = os.getenv("PGADMIN_DEFAULT_PASSWORD")
    PGADMIN_PORT: str = os.getenv("PGADMIN_PORT")

    # Redis
    REDIS_DATABASE: str = os.getenv("REDIS_DATABASE")
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: str = os.getenv("REDIS_PORT")
    REDIS_USERNAME: str = os.getenv("REDIS_USERNAME")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD")

    # Validation
    def __post_init__(self) -> None:
        """Validate settings after initialization."""
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN environment variable is required")

    @classmethod
    def get_instance(cls) -> "Settings":
        """Get singleton instance of settings."""
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
            cls._instance.__post_init__()
        return cls._instance


# Global settings instance
settings = Settings.get_instance()