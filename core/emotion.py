"""
Module for detecting emotion from voice (and optionally text).
"""
import random
import numpy as np
import librosa
import os
import pickle
from textblob import TextBlob


class EmotionDetector:
    def __init__(self, model_path="models/emotion_classifier.pkl"):
        self.emotions = ["neutral", "happy", "sad", "angry", "surprised"]
        self.model = None
        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            print(f"[EmotionDetector] Warning: No classifier found at {model_path}. Using random emotion.")

    def extract_features(self, audio_path):
        y, sr = librosa.load(audio_path, sr=16000)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs, axis=1)
        return mfccs_mean

    def detect(self, audio, text=None):
        """Detect emotion from audio file. Falls back to text-based or random if no model or no audio."""
        if audio is None:
            # If text is provided, use sentiment analysis
            if text and isinstance(text, str):
                blob = TextBlob(text)
                polarity = blob.sentiment.polarity
                if polarity > 0.3:
                    emotion = "happy"
                elif polarity < -0.3:
                    emotion = "sad"
                else:
                    emotion = "neutral"
                print(f"[Text] Detected emotion: {emotion} (polarity={polarity:.2f})")
                return emotion
            # No audio or text, fallback to random
            emotion = random.choice(self.emotions)
            print(f"[No audio/text] Detected emotion: {emotion}")
            return emotion
        if self.model is not None:
            features = self.extract_features(audio)
            features = features.reshape(1, -1)
            emotion_idx = self.model.predict(features)[0]
            # Always map integer index to label
            if isinstance(emotion_idx, int) or (isinstance(emotion_idx, np.integer)):
                emotion = self.emotions[int(emotion_idx)]
            else:
                emotion = str(emotion_idx)
            print(f"Detected emotion: {emotion}")
            return emotion
        else:
            emotion = random.choice(self.emotions)
            print(f"[Fallback] Detected emotion: {emotion}")
            return emotion
