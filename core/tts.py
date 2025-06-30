"""
Module for converting text to speech (TTS).
"""
import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text, emotion=None):
        """Speak the given text, optionally modulating for emotion (not implemented)."""
        print(f"Assistant says: {text}")
        self.engine.say(text)
        self.engine.runAndWait() 