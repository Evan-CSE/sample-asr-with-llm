
from src.services.function_caller import FunctionCaller
from src.services.file_service import FileService
from src.services.transcriber_service import Transcriber


def get_transcriber_instance(file_path: str) -> Transcriber:
    return Transcriber(file_path=file_path)


def get_function_caller_instance() -> FunctionCaller:
    return FunctionCaller()

def get_file_processing_service() -> FileService:
    return FileService()