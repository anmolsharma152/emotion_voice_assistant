"""
Module for converting voice to text (STT) using Google Cloud Speech-to-Text.
"""
import os
import wave
from google.cloud import speech
from core.capture import AudioCapture


class SpeechToText:
    def __init__(self):
        """Initialize Google Cloud Speech-to-Text client."""
        # Check if credentials are set
        if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
            print("Warning: GOOGLE_APPLICATION_CREDENTIALS environment variable not set.")
            print("Please set it to the path of your Google Cloud service account key file.")
        
        self.client = speech.SpeechClient()

    def transcribe(self, wav_path):
        """Transcribe a WAV file to text using Google Cloud Speech-to-Text."""
        try:
            # Read the audio file
            with wave.open(wav_path, "rb") as wf:
                audio_data = wf.readframes(wf.getnframes())
                audio = speech.RecognitionAudio(content=audio_data)

            # Configure recognition
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=wf.getframerate(),
                language_code="en-US",
                enable_automatic_punctuation=True,
            )

            # Perform the transcription
            response = self.client.recognize(config=config, audio=audio)
            
            # Extract the transcribed text
            transcript = ""
            for result in response.results:
                transcript += result.alternatives[0].transcript + " "
            
            return transcript.strip()
            
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""


def record_audio():
    """Record audio using the AudioCapture module."""
    recorder = AudioCapture()
    wav_file = recorder.record(duration=5, filename="test_output.wav")
    print(f"Recorded audio saved to {wav_file}")
    return wav_file


def transcribe_audio(wav_file):
    """Transcribe an audio file using Google Cloud STT."""
    stt = SpeechToText()
    transcription = stt.transcribe(wav_file)
    print(f"Transcription for {wav_file}: {transcription}")
    return transcription


if __name__ == "__main__":
    # Test transcription with a sample file if it exists
    if os.path.exists("test.wav"):
        transcribe_audio("test.wav")
    
    # Test with recorded audio if it exists
    if os.path.exists("test_output.wav"):
        transcribe_audio("test_output.wav")
    
    # Optionally, record new audio and transcribe it
    # Uncomment the next two lines to record and transcribe
    # new_wav = record_audio()
    # transcribe_audio(new_wav) 