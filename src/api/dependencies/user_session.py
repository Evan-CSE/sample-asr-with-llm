import google.generativeai as genai
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserSession:
   chat: genai.GenerativeModel.start_chat
   last_active: datetime
   prev_message: str = ""
   awaiting_confirmation: bool = False