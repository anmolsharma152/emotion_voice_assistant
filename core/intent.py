"""
Module for extracting user intent using NLP.
"""
import random

class IntentDetector:
    def __init__(self):
        self.intents = [
            "greeting", "question", "command", "goodbye",
            "music", "weather", "alarm", "reminder", "emotion", "joke"
        ]
        self.intent_keywords = {
            "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
            "question": ["what", "how", "why", "when", "where", "?"],
            "command": ["do", "please", "can you", "could you", "turn on", "turn off", "set", "remind", "add", "remove", "delete", "start", "stop"],
            "goodbye": ["bye", "goodbye", "see you", "later", "farewell"],
            "music": ["music", "song", "play", "pause", "stop music", "next song", "previous song", "playlist"],
            "weather": ["weather", "temperature", "forecast", "rain", "sunny", "cloudy", "windy", "snow"],
            "alarm": ["alarm", "wake me", "set alarm", "cancel alarm", "snooze"],
            "reminder": ["remind", "reminder", "remember", "note", "to do", "task"],
            "emotion": ["happy", "sad", "angry", "upset", "excited", "bored", "emotion", "feeling", "mood"],
            "joke": ["joke", "funny", "make me laugh", "laugh"]
        }

    def detect(self, text):
        """Detect intent using expanded keyword rules and simple pattern matching."""
        if not text or not isinstance(text, str):
            print("Detected intent: unknown (empty text)")
            return "unknown"
        text_lower = text.lower()
        for intent, keywords in self.intent_keywords.items():
            for kw in keywords:
                if kw in text_lower:
                    print(f"Detected intent: {intent}")
                    return intent
        # Simple pattern: if text ends with a question mark, treat as question
        if text_lower.strip().endswith('?'):
            print("Detected intent: question (pattern match)")
            return "question"
        print("Detected intent: unknown (no match)")
        return "unknown" 