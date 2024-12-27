import tempfile
from fastapi import UploadFile, HTTPException
import os
from src.app.core.config import settings

class FileService:

    async def save_file_temporarily(self, uploaded_file: UploadFile) -> str:
        try:    
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.split(uploaded_file.filename)[1]) as temp_file:
                content = await uploaded_file.read()
                temp_file.write(content)
                return  temp_file.name
        except Exception as ex:
            print(ex)
            # Save exception to logger
            raise ex
        
    
    def validate_file_extension(self, filename: str):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in settings.ALLOWED_AUDIO_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"File extension not allowed. Allowed extensions are: {', '.join(settings.ALLOWED_AUDIO_EXTENSIONS)}"
            )

