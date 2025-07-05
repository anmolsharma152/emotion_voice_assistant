"""
Module for generating responses based on emotion and intent.
"""

class ResponseGenerator:
    def __init__(self):
        pass

    def generate(self, intent, emotion):
        """Generate a response based on intent and emotion."""
        if intent == "greeting":
            if emotion == "happy":
                return "Hi there! You sound cheerful today!"
            elif emotion == "sad":
                return "Hello. I'm here if you need to talk."
            else:
                return "Hello! How can I help you?"
        elif intent == "question":
            return "That's a great question. Let me think about it."
        elif intent == "command":
            return "I'm on it!"
        elif intent == "goodbye":
            return "Goodbye! Take care."
        elif intent == "music":
            return "Playing your favorite music!"
        elif intent == "weather":
            return "Here's the latest weather update."
        elif intent == "alarm":
            return "Setting your alarm now."
        elif intent == "reminder":
            return "I've added that to your reminders."
        elif intent == "emotion":
            return f"I can tell you're feeling {emotion}. I'm here for you."
        elif intent == "joke":
            return "Why did the computer go to the doctor? Because it had a virus!"
        else:
            return "I'm not sure how to respond to that, but I'm here to help!" 