import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

class Setting(BaseSettings):
    DATABASE_URL: str

    DB_PATH: str = os.path.join(BASE_DIR, "wallets.db")

    @property
    def DATABASE_URL_aiosqlite(self):
        return f"sqlite+aiosqlite:///{self.DB_PATH}"

    model_config = SettingsConfigDict(env_file=ENV_FILE)

setting = Setting()