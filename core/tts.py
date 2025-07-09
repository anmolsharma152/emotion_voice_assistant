"""
Module for converting text to speech (TTS) using Google Text-to-Speech (gTTS).
"""
from gtts import gTTS
from pydub import AudioSegment

class TextToSpeech:
    def __init__(self):
        pass

    def speak(self, text, emotion=None):
        """Speak the given text using Google Text-to-Speech (gTTS). Emotion modulation not implemented."""
        if not text:
            print("[TTS] No text to speak.")
            return
        print(f"Assistant says: {text}")
        # Generate TTS mp3
        tts = gTTS(text=text, lang='en')
        tts.save("tts_output.mp3")
        # Convert mp3 to wav for Streamlit
        sound = AudioSegment.from_mp3("tts_output.mp3")
        sound.export("tts_output.wav", format="wav") 