# Project Index & Roadmap

## Modules
- capture.py: Real-time microphone input
- stt.py: Speech-to-text (Vosk)
- emotion.py: Emotion detection (MFCC + synthetic classifier, text fallback)
- intent.py: Intent detection (rule-based)
- respond.py: Response generation
- tts.py: Text-to-speech (Coqui TTS)
- app.py: Main runner

## Roadmap
- [x] Project structure and stubs
- [x] Implement audio capture
- [x] Integrate Vosk STT
- [x] Add synthetic emotion detection (audio/text)
- [x] Add rule-based intent detection
- [x] Response generation
- [x] Coqui TTS integration
- [x] Robust fallback for unknown/empty input
- [x] Text and audio pipeline test scripts
- [ ] Real emotion classifier (planned)
- [ ] ML/transformer-based intent detection (planned)
- [ ] GUI/web interface (planned)

## How to Test

### Audio Pipeline
- Run the assistant:
  ```bash
  python app.py
  ```
- Speak a variety of test phrases (greetings, questions, commands, music/weather requests, emotional statements, etc.)
- Listen for the TTS response and check the detected intent/emotion in the terminal output.

### Text Pipeline
- Run:
  ```bash
  python test_pipeline_text.py
  ```
- Review detected emotion and intent for each sample string.

## Notes
- Emotion classifier is currently synthetic (for demo/testing). Ready for real model.
- Intent detection is rule-based (keyword matching). Ready for ML upgrade.
- TTS uses Coqui (Tacotron2-DDC, Hifi-GAN) for high-quality speech.
- Python 3.10 via pyenv is recommended for compatibility.
- See README.md for full overview and setup instructions.
