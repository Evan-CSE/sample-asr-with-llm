import os
from datetime import datetime
import google.generativeai as genai
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class UserSession:
   chat: genai.GenerativeModel.start_chat
   last_active: datetime
   prev_message: str = ""
   awaiting_confirmation: bool = False


class FunctionCaller:

    sessions: Dict[str, UserSession] = {}
    def __init__(self):
        api_key = os.environ.get('FLASH_API_KEY')
        genai.configure(api_key=api_key)

        FunctionCaller.model = genai.GenerativeModel(model_name='gemini-1.5-flash',
                              tools=[self.assign_ticket_for_device_request,  self.apply_for_leave, self.get_todays_date])



    def assign_ticket_for_device_request(self, project_name: str, amount: float, reason: str) -> bool:
        """Create a ticket requesting a device as per user's need.

        Args:
            project_name: Project name for which user is asking for the device
            amount: amount of money user requires for purchase
            reason: reason of why user needs the device

        Returns:
            boolean: True
        """
        print(f"{project_name} || {amount} || {reason}")
        return True

    @staticmethod
    def get_session(user_id: str) -> Optional[UserSession]:
       session = FunctionCaller.sessions.get(user_id)
       if not session or (datetime.now() - session.last_active).seconds > 100:
           chat = FunctionCaller.model.start_chat(enable_automatic_function_calling=True)
           session = UserSession(chat=chat, last_active=datetime.now(), prev_message="")
           FunctionCaller.sessions[user_id] = session
       return session


    def apply_for_leave(self, employee_id: str, number_of_days: float, reason: str, starting_date: str) -> bool:
        """Create a ticket for leave as per user's need.

        Args:
            employee_id: Employee id
            number_of_days: Leave for how many number of days
            reason: reason of why user needs the leave
            starting_date: starting date for leave in dd/mm/yyyy  format 

        Returns:
            boolean: True
        """
        print(f"{employee_id} || {number_of_days} || {reason} || {starting_date}")
        return True


    def get_todays_date(self) -> datetime:
        return datetime.datetime.now()


    def handle_user_prompt(self, prompt: str, user_id='123'):
       session = FunctionCaller.get_session(user_id=user_id)

       if session.awaiting_confirmation is True and prompt.lower().__contains__("yes"):
           session.awaiting_confirmation = False
           response = session.chat.send_message(session.prev_message)

       else:
           response = session.chat.send_message(f"You are a customer care agent. You can call different function based on user query.Confirm your detected params from user. For missing params let the user know about missing information. User Prompt: {prompt}")
        #    if response.candidates[0].content.function_call:
        #        session.params = response.candidates[0].content.function_call
           session.awaiting_confirmation = True
           session.prev_message = prompt


       session.last_active = datetime.now()
       return f"{response._result.candidates[0].content.parts[0].text}"


