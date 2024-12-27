from fastapi import APIRouter, Depends, UploadFile, File
from src.api.dependencies.common import get_function_caller_instance, get_file_processing_service, get_transcriber_instance
from src.services import function_caller
from src.services.file_service import FileService

router = APIRouter()

@router.post('/voice-command/')
async def process_voice_command(uploaded_file: UploadFile, function_caller: function_caller = Depends(get_function_caller_instance), file_service: FileService = Depends(get_file_processing_service)):
    temporary_file_location = await file_service.save_file_temporarily(uploaded_file)
    file_service.validate_file_extension(temporary_file_location)
    transcriber = get_transcriber_instance(temporary_file_location)
    transcription = transcriber.transcribe_audio_in_English()
    function_response = function_caller.handle_user_prompt(transcription)
    print(function_response)
    return function_response 

