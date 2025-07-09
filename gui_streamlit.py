import streamlit as st
import os
from core.stt import SpeechToText
from core.emotion import EmotionDetector
from core.intent import IntentDetector
from core.respond import ResponseGenerator
from core.tts import TextToSpeech
import tempfile
from streamlit_audiorecorder import audiorecorder

st.set_page_config(page_title="Emotion Voice Assistant", layout="centered")
st.title("🎙️ Emotion-Aware Voice Assistant")
st.write("Upload or record audio, or type a message. The assistant will detect your emotion and intent, and respond with speech.")

# --- Model Caching ---
if 'stt' not in st.session_state:
    st.session_state['stt'] = SpeechToText()
if 'emotion_detector' not in st.session_state:
    st.session_state['emotion_detector'] = EmotionDetector()
if 'intent_detector' not in st.session_state:
    st.session_state['intent_detector'] = IntentDetector()
if 'responder' not in st.session_state:
    st.session_state['responder'] = ResponseGenerator()
if 'tts' not in st.session_state:
    st.session_state['tts'] = TextToSpeech()

stt = st.session_state['stt']
emotion_detector = st.session_state['emotion_detector']
intent_detector = st.session_state['intent_detector']
responder = st.session_state['responder']
tts = st.session_state['tts']

# --- Conversation History ---
if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- Emotion Emoji Map ---
emotion_emoji = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😠",
    "surprised": "😲",
    "neutral": "😐"
}

def add_to_history(user, text, emotion, intent, response):
    st.session_state['history'].append({
        'user': user,
        'text': text,
        'emotion': emotion,
        'intent': intent,
        'response': response
    })

def clear_history():
    st.session_state['history'] = []

# --- Clear Conversation Button ---
if st.button("Clear Conversation"):
    clear_history()
    st.rerun()

# --- Input Section ---
input_mode = st.radio("Choose input mode:", ("Audio Upload", "Text Input", "Microphone"))

if input_mode == "Audio Upload":
    audio_file = st.file_uploader("Record or upload a WAV file", type=["wav"])
    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
            tmp_wav.write(audio_file.read())
            wav_path = tmp_wav.name
        st.audio(wav_path, format="audio/wav")
        run_btn = st.button("Run Assistant on Audio")
        if run_btn:
            text = stt.transcribe(wav_path)
            emotion = emotion_detector.detect(wav_path, text)
            intent = intent_detector.detect(text)
            response = responder.generate(intent, emotion)
            add_to_history('User (audio)', text, emotion, intent, response)
            tts.speak(response, emotion=emotion)
            if os.path.exists("tts_output.wav"):
                st.audio("tts_output.wav", format="audio/wav")
elif input_mode == "Microphone":
    audio = audiorecorder("Click to record", "Recording...")
    if audio is not None and len(audio) > 0:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
            tmp_wav.write(audio)
            wav_path = tmp_wav.name
        st.audio(wav_path, format="audio/wav")
        run_btn = st.button("Run Assistant on Recorded Audio")
        if run_btn:
            text = stt.transcribe(wav_path)
            emotion = emotion_detector.detect(wav_path, text)
            intent = intent_detector.detect(text)
            response = responder.generate(intent, emotion)
            add_to_history('User (mic)', text, emotion, intent, response)
            tts.speak(response, emotion=emotion)
            if os.path.exists("tts_output.wav"):
                st.audio("tts_output.wav", format="audio/wav")
else:
    user_text = st.text_input("Type your message:")
    run_btn = st.button("Run Assistant on Text")
    if run_btn and user_text:
        emotion = emotion_detector.detect(audio=None, text=user_text)
        intent = intent_detector.detect(user_text)
        response = responder.generate(intent, emotion)
        add_to_history('User', user_text, emotion, intent, response)
        tts.speak(response, emotion=emotion)
        if os.path.exists("tts_output.wav"):
            st.audio("tts_output.wav", format="audio/wav")

# --- Display Conversation History ---
st.markdown("---")
st.subheader("Conversation History")
for entry in st.session_state['history']:
    st.markdown(f"**{entry['user']}:** {entry['text']}")
    st.markdown(f"- Emotion: {emotion_emoji.get(entry['emotion'], '❓')} {entry['emotion']}")
    st.markdown(f"- Intent: {entry['intent']}")
    st.markdown(f"**Assistant:** {entry['response']}")
    st.markdown("---") 