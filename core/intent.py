"""
Module for extracting user intent using NLP.
"""
import random

class IntentDetector:
    def __init__(self):
        self.intents = ["greeting", "question", "command", "goodbye"]

    def detect(self, text):
        """Dummy: Randomly select an intent."""
        intent = random.choice(self.intents)
        print(f"Detected intent: {intent}")
        return intent 