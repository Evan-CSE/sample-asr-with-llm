from fastapi import Request
from fastapi.responses import JSONResponse
from src.app.core.exceptions import AudioFileError
from typing import Union
import logging

logger = logging.getLogger(__name__)

async def global_exception_handler(
    request: Request,
    exc: Union[AudioFileError, Exception]
) -> JSONResponse:
    if isinstance(exc, AudioFileError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    
    # Log unexpected errors
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )