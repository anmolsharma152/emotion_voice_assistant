# 🎙️ Real-Time Emotion-Aware Voice Assistant

A modular, real-time voice assistant that understands what users say — and how they feel — and adapts its responses accordingly using speech emotion recognition and natural language understanding.

---

## 🚀 Features

- 🎤 Real-time voice input (microphone)
- 🧠 Emotion detection from voice (MFCC + classifier, synthetic for now)
- 💬 Rule-based intent understanding (keyword matching)
- 🎭 Emotion-aware adaptive responses
- 🔊 High-quality Text-to-Speech (Coqui TTS)
- 🌀 Modular and extensible architecture
- 🛡️ Robust fallback: always responds, even for unknown input

---

## 📚 Project Goals

1. Detect user's **emotional tone** from their voice (audio-based, text fallback).
2. Understand **intent** using NLP models (currently rule-based, ready for ML upgrade).
3. Generate a **response** adapted to both emotion and context.
4. Speak the response back using **TTS** (Coqui TTS).
5. Operate in **real time** (terminal/CLI, GUI planned).

---

## 🧠 System Architecture

```text
Voice Input ──► Speech-to-Text (Google Cloud STT) ──► Emotion Detection (audio/text) ──► Intent Detection (rule-based) ──► Adaptive Response ──► Text-to-Speech (Google TTS)
```

---

## 🧩 Core Modules

| Module           | Function                                             |
|------------------|------------------------------------------------------|
| `capture.py`     | Real-time microphone input                           |
| `stt.py`         | Converts voice to text (Google Cloud STT)            |
| `emotion.py`     | Detects emotion from voice (MFCC + classifier, or text fallback) |
| `intent.py`      | Extracts user intent using rule-based NLP            |
| `respond.py`     | Generates responses based on emotion and intent      |
| `tts.py`         | Converts final response to voice (Google TTS)        |
| `app.py`         | Main loop coordinating all modules                   |

---

## 🛠️ Tech Stack

- **Language**: Python 3.10 (via pyenv)
- **Audio**: `sounddevice`, `librosa`
- **STT**: Google Cloud Speech-to-Text
- **Emotion Detection**: MFCC + synthetic classifier (ready for real model)
- **NLP**: Rule-based (upgradeable to ML/transformers)
- **TTS**: Google Text-to-Speech (gTTS)
- **Async Execution**: `threading`

---

## ⚡ Current Progress

- [x] Modular project structure
- [x] Real-time audio capture
- [x] Google Cloud STT integration
- [x] Synthetic audio/text emotion detection
- [x] Rule-based intent detection
- [x] Google TTS integration
- [x] Robust fallback for unknown/empty input
- [x] Text and audio pipeline test scripts
- [ ] Real emotion classifier (planned)
- [ ] ML/transformer-based intent detection (planned)
- [ ] GUI/web interface (planned)

---

## 🛠️ Setup Instructions

### 1. Install Python 3.10 with pyenv (recommended)

```bash
# Install pyenv (if not already)
yay -S pyenv  # or see pyenv docs for manual install
pyenv install 3.10.14
pyenv local 3.10.14
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set up Google Cloud credentials

Set up Google Cloud Speech-to-Text API credentials:
```bash
# Set the environment variable to your service account key file
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

### 5. Train or generate a synthetic emotion classifier

```bash
python models/train_synthetic_emotion_classifier.py
```

---

## 🧪 Testing

- Run the assistant:
  ```bash
  python app.py
  ```
- Test with text pipeline:
  ```bash
  python test_pipeline_text.py
  ```

---

## 📈 Future Enhancements

- Real emotion classifier (audio/text)
- ML/transformer-based intent detection
- GUI/web interface
- Contextual dialogue
- Multilingual support

---

## 🤝 Contributing

Contributions are welcome! Fork, PR, or open an issue.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 💡 Credits

Inspired by advances in speech AI and human conversation.
