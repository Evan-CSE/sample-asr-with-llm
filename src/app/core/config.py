from pydantic_settings import BaseSettings
from typing import Set

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ERP-ASR"
    ALLOWED_AUDIO_EXTENSIONS: Set[str] = {'.wav', '.mp3', '.ogg', '.flac'}
    MAX_FILE_SIZE: int = 10 * 1024 * 1024

settings = Settings()