from core.capture import AudioCapture
from core.stt import SpeechToText

if __name__ == "__main__":
    # Step 1: Record 10 seconds of audio
    recorder = AudioCapture()
    wav_file = recorder.record(duration=3, filename="test_output.wav")

    # Step 2: Transcribe the recorded audio
    stt = SpeechToText(model_path="models/vosk-model-small-en-us-0.15")
    transcription = stt.transcribe(wav_file)

    # Step 3: Print the transcription
    print("Transcription:", transcription) 