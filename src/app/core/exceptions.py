from fastapi import HTTPException


class AudioFileError(HTTPException):
    def __init__(self, status_code, detail = None, headers = None):
        super().__init__(status_code, detail, headers)

class FileTooLarge(HTTPException):
    def  __init__(self, status_code, detail = None, headers = None):
        super().__init__(status_code, detail, headers)

class InvalidFileTypeError(HTTPException):
    def __init__(self, status_code, detail = None, headers = None):
        super().__init__(status_code, detail, headers)
