
# 🎙️ Real-Time Emotion-Aware Voice Assistant

A modular, real-time voice assistant that not only understands what users say — but how they feel — and adapts its responses accordingly using speech emotion recognition and natural language understanding.

> “It’s not just what you say, but how you say it — your assistant should know the difference.”

---

## 🚀 Features

- 🎤 Real-time voice input
- 🧠 Emotion detection from voice tone
- 💬 NLP-based intent understanding
- 🎭 Emotion-aware adaptive responses
- 🔊 Human-like Text-to-Speech output
- 🌀 Modular and extensible architecture

---

## 📚 Project Goals

1. Detect user's **emotional tone** from their voice.
2. Understand **intent** using NLP models.
3. Generate a **response** adapted to both emotion and context.
4. Speak the response back using **TTS**.
5. Operate in **real time**, optionally with a terminal or GUI.

---

## 🧠 System Architecture

```text
Voice Input ──► Speech-to-Text ──► Emotion Detection ──► Intent Detection ──► Adaptive Response ──► Text-to-Speech
     🎤                 📄                    😶‍🌫️                     🧠                       💬                     🔊
```

---

## 🧩 Core Modules

| Module           | Function                                             |
|------------------|------------------------------------------------------|
| `capture.py`     | Real-time microphone input                           |
| `stt.py`         | Converts voice to text (STT)                         |
| `emotion.py`     | Detects emotion from voice (and optionally text)     |
| `intent.py`      | Extracts user intent using NLP                       |
| `respond.py`     | Generates responses based on emotion and intent      |
| `tts.py`         | Converts final response to voice                     |
| `app.py`         | Main loop coordinating all modules                   |

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Audio**: `sounddevice`, `pyaudio`, `librosa`
- **STT**: Whisper, Vosk, Google STT
- **Emotion Detection**: MFCC + SVM/CNN, or pretrained models
- **NLP**: `transformers`, `spaCy`, `RASA`
- **TTS**: `pyttsx3`, `gTTS`, Tortoise TTS, Bark
- **Async Execution**: `asyncio`, `threading`

---

## 📁 Project Structure

```
emotion_voice_assistant/
├── data/                 # Audio datasets
├── audio/                # Real-time recorded audio
├── models/               # Saved ML models
├── utils/                # Helper scripts
├── core/                 # Main modules
│   ├── capture.py
│   ├── stt.py
│   ├── emotion.py
│   ├── intent.py
│   ├── respond.py
│   └── tts.py
├── app.py                # Main runner script
├── index.md              # Project index and roadmap
└── README.md             # Project overview
```

---

## 🧪 Datasets You Can Use

- RAVDESS
- CREMA-D
- EMO-DB
- TESS

---

## 📈 Future Enhancements

- 🗣️ Expressive voice synthesis (emotional TTS)
- 👀 Facial emotion detection (webcam)
- 🌍 Multilingual support
- 🧠 Context memory for continuous interaction
- 🧪 RLHF (Reinforcement Learning from Human Feedback)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a PR or create an issue for discussion.

---

## 📄 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 💡 Credits

Inspired by human conversation, mental health support systems, and advances in speech AI.
