from core.emotion import EmotionDetector
from core.intent import IntentDetector

# Sample transcriptions/text inputs for testing
sample_texts = [
    "Hello, how are you?",
    "What time is it?",
    "Please turn on the lights.",
    "Goodbye, see you later.",
    "I'm feeling sad today.",
    "Can you play some music?",
    "Why is the sky blue?",
    "Set an alarm for 7 am.",
    "Hey there!",
    "I am so happy right now!",
    # New and edge cases:
    "Remind me to call mom tomorrow.",
    "Tell me a joke!",
    "It's raining outside.",
    "Wake me up at 6.",
    "I'm bored.",
    "Delete my last reminder.",
    "Could you please play my favorite playlist?",
    "What's the weather forecast for tomorrow?",
    "I'm angry about the delay.",
    "Make me laugh!",
    "",
    None,
    "asdfghjkl",  # gibberish
    "I feel nothing.",
    "Turn off the alarm.",
    "You are awesome!"
]

# Initialize detectors
emotion_detector = EmotionDetector()
intent_detector = IntentDetector()

print("--- Pipeline Test: Text Input ---")
for text in sample_texts:
    print(f"\nInput: {text}")
    # For text-only, pass None for audio
    emotion = emotion_detector.detect(audio=None, text=text)
    intent = intent_detector.detect(text)
    print(f"Detected Emotion: {emotion}")
    print(f"Detected Intent: {intent}") 