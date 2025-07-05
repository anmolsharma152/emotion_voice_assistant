"""
Module for converting text to speech (TTS) using Coqui TTS.
"""
try:
    from TTS.api import TTS as CoquiTTS
except ImportError:
    CoquiTTS = None

class TextToSpeech:
    def __init__(self):
        if CoquiTTS is not None:
            # You can specify a model name here, or use the default
            self.tts = CoquiTTS("tts_models/en/ljspeech/tacotron2-DDC")
        else:
            self.tts = None
            print("[TTS] Coqui TTS is not installed. Please run: pip install TTS")

    def speak(self, text, emotion=None):
        """Speak the given text using Coqui TTS. Emotion modulation not implemented."""
        if not text:
            print("[TTS] No text to speak.")
            return
        print(f"Assistant says: {text}")
        if self.tts is not None:
            # Use default speaker and settings
            self.tts.tts_to_file(text=text, file_path="tts_output.wav")
            try:
                import sounddevice as sd
                import soundfile as sf
                data, samplerate = sf.read("tts_output.wav")
                sd.play(data, samplerate)
                sd.wait()
            except Exception as e:
                print(f"[TTS] Could not play audio: {e}")
        else:
            print("[TTS] Coqui TTS is not available. Please install it with: pip install TTS") 