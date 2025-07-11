from core.capture import AudioCapture
from core.stt import SpeechToText
#import subprocess

if __name__ == "__main__":
    # Step 1: Record 10 seconds of audio using AudioCapture
    recorder = AudioCapture()
    wav_file = recorder.record(duration=5, filename="test_output.wav")

    # Step 2: Transcribe the recorded audio
    stt = SpeechToText()
    transcription = stt.transcribe(wav_file)

    # Step 3: Print the transcription
    print("Transcription:", transcription)

    # Step 4: Check audio file properties
    # subprocess.run(["soxi", wav_file])
