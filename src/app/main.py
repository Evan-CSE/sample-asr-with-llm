from fastapi import FastAPI
from src.app.core.config import settings
from src.api.middleware.error_handler import global_exception_handler
from src.api.endpoints.voice import router
from src.app.core.exceptions import AudioFileError, InvalidFileTypeError, FileTooLarge
from dotenv import load_dotenv
import os


def load_env_file():
    load_dotenv('../../.env')    

def create_application() -> FastAPI:
    app = FastAPI(
        title= settings.API_V1_STR
    )

    app.add_exception_handler(AudioFileError, global_exception_handler)
    app.add_exception_handler(InvalidFileTypeError, global_exception_handler)
    app.add_exception_handler(FileTooLarge, global_exception_handler)
    app.include_router(router=router, prefix=settings.API_V1_STR)

    return app

app = create_application()