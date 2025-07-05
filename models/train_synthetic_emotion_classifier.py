import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Settings
n_samples = 200  # Number of synthetic audio samples
n_mfcc = 13      # Number of MFCC features (matches feature extractor)
emotions = ["neutral", "happy", "sad", "angry", "surprised"]

# Generate synthetic features and labels
X = np.random.normal(size=(n_samples, n_mfcc))
y = np.random.choice(len(emotions), size=n_samples)

# Train classifier
clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X, y)

# Save classifier
os.makedirs("models", exist_ok=True)
with open("models/emotion_classifier.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Synthetic emotion classifier trained and saved to models/emotion_classifier.pkl") 