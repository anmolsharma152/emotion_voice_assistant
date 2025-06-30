"""
Module for real-time microphone input.
"""
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class AudioCapture:
    def __init__(self, samplerate=16000, channels=1):
        self.samplerate = samplerate
        self.channels = channels

    def record(self, duration=3, filename="output.wav"):
        """Record audio from the microphone and save to a WAV file."""
        print(f"Recording for {duration} seconds...")
        audio = sd.rec(int(duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, dtype='int16')
        sd.wait()
        write(filename, self.samplerate, audio)
        print(f"Saved recording to {filename}")
        return filename

    def start_stream(self):
        """Start capturing audio from the microphone."""
        pass

    def stop_stream(self):
        """Stop capturing audio."""
        pass 