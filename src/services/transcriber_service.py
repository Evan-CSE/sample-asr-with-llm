import whisper

class Transcriber:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.model_name = "tiny"
    
    def transcribe_audio_in_English(self):
        model = whisper.load_model(self.model_name)
        result = model.transcribe(self.file_path)
        return result["text"]