"""
Main runner script for the Emotion-Aware Voice Assistant.
Coordinates all core modules in real time.
"""
from core.capture import AudioCapture
from core.stt import SpeechToText
from core.emotion import EmotionDetector
from core.intent import IntentDetector
from core.respond import ResponseGenerator
from core.tts import TextToSpeech
import os

def main():
    # Step 1: Record audio
    capture = AudioCapture()
    wav_path = capture.record(duration=3, filename="audio/output.wav")

    # Step 2: Transcribe audio
    model_path = "models/vosk"
    if not os.path.exists(model_path):
        print(f"Vosk model not found at {model_path}.")
        print("Download a model from https://alphacephei.com/vosk/models and unpack it to models/vosk")
        return
    stt = SpeechToText(model_path=model_path)
    text = stt.transcribe(wav_path)
    print(f"Recognized text: {text}")

    # Step 3: Detect emotion
    emotion_detector = EmotionDetector()
    emotion = emotion_detector.detect(wav_path, text)

    # Step 4: Detect intent
    intent_detector = IntentDetector()
    intent = intent_detector.detect(text)

    # Step 5: Generate response
    responder = ResponseGenerator()
    response = responder.generate(intent, emotion)

    # Step 6: Speak response
    tts = TextToSpeech()
    tts.speak(response, emotion=emotion)

if __name__ == "__main__":
    main() 