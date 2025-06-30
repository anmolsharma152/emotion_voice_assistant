"""
Module for detecting emotion from voice (and optionally text).
"""
import random

class EmotionDetector:
    def __init__(self):
        self.emotions = ["neutral", "happy", "sad", "angry", "surprised"]

    def detect(self, audio, text=None):
        """Dummy: Randomly select an emotion."""
        emotion = random.choice(self.emotions)
        print(f"Detected emotion: {emotion}")
        return emotion 