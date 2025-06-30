"""
Module for converting voice to text (STT).
"""
from vosk import Model, KaldiRecognizer
import wave
import os

class SpeechToText:
    def __init__(self, model_path="model"): 
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Vosk model not found at {model_path}. Download and unpack a model from https://alphacephei.com/vosk/models")
        self.model = Model(model_path)

    def transcribe(self, wav_path):
        """Transcribe a WAV file to text using Vosk."""
        wf = wave.open(wav_path, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())
        result = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                part = rec.Result()
                result += part
        result += rec.FinalResult()
        import json
        try:
            text = json.loads(result)["text"]
        except Exception:
            text = ""
        return text 