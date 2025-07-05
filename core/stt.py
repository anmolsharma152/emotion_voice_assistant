"""
Module for converting voice to text (STT).
"""
from vosk import Model, KaldiRecognizer
import wave
import os
from core.capture import AudioCapture

class SpeechToText:
    def __init__(self, model_path="models/vosk-model-small-en-us-0.15"): 
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Vosk model not found at {model_path}. Download and unpack a model from https://alphacephei.com/vosk/models")
        self.model = Model(model_path)

    def transcribe(self, wav_path):
        """Transcribe a WAV file to text using Vosk."""
        wf = wave.open(wav_path, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())
        import json
        texts = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                part = rec.Result()
                try:
                    part_text = json.loads(part).get("text", "")
                    if part_text:
                        texts.append(part_text)
                except Exception:
                    pass
        # Get the final result
        final = rec.FinalResult()
        print("RAW VOSK RESULT:", final)
        try:
            final_text = json.loads(final).get("text", "")
            if final_text:
                texts.append(final_text)
        except Exception:
            pass
        # Join all recognized segments
        full_text = " ".join(texts).strip()
        return full_text

def record_audio():
    recorder = AudioCapture()
    wav_file = recorder.record(duration=5, filename="test_output.wav")
    print(f"Recorded audio saved to {wav_file}")
    return wav_file

def transcribe_audio(wav_file, model_path="models/vosk-model-small-en-us-0.15"):
    stt = SpeechToText(model_path=model_path)
    transcription = stt.transcribe(wav_file)
    print(f"Transcription for {wav_file}: {transcription}")

if __name__ == "__main__":
    # 1. Transcribe a known good sample file
    transcribe_audio("test.wav")

    # 2. Transcribe your own recorded file (if it exists)
    transcribe_audio("test_output.wav")

    # 3. Optionally, record new audio and transcribe it
    # Uncomment the next two lines to record and transcribe
    # new_wav = record_audio()
    # transcribe_audio(new_wav) 