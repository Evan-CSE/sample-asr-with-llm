from fastapi import FastAPI, Depends
import librosa
from Transcriber import Transcriber
import json
from FunctionCaller import FunctionCaller
from dotenv import load_dotenv
from dataclasses import dataclass
import google.generativeai as genai
from datetime import datetime
from typing import Optional

app = FastAPI()

load_dotenv()


@dataclass
class UserSession:
   chat: genai.GenerativeModel.start_chat
   last_active: datetime
   prev_message: str = ""
   awaiting_confirmation: bool = False


def get_session(self, user_id: str) -> Optional[UserSession]:
    session = self.sessions.get(user_id)
    if not session or (datetime.now() - session.last_active).seconds > self.session_timeout:
        chat = self.model.start_chat(enable_automatic_function_calling=True)
        session = UserSession(chat=chat, last_active=datetime.now(), prev_message="")
        self.sessions[user_id] = session
    return session



def get_transcriber_instance(file_path: str) -> Transcriber:
    return Transcriber(file_path=file_path)

def get_function_caller_instance() -> FunctionCaller:
    return FunctionCaller()


@app.post('/voice_command/')
def process_voice_command(file_path: str, transcriber: Transcriber = Depends(get_transcriber_instance), function_caller: FunctionCaller = Depends(get_function_caller_instance)):
    transcription = transcriber.transcribe_audio_in_English()
    function_response = function_caller.handle_user_prompt(transcription)
    print(function_response)
    return function_response  
