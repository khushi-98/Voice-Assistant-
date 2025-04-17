# 🔊 Voice Assistant: An Interactive AI Companion for Daily Tasks



Welcome to the **AI Voice Assistant**, a smart Python-based voice-controlled assistant that can interact with you using natural language. This project integrates speech recognition, text-to-speech, and web automation to assist you with tasks such as searching for information, playing YouTube videos, telling jokes, and more!

---

## 🧠 Key Features

- 🎙️ **Voice Interaction** – Listen and respond to your voice commands
- 📖 **Wikipedia Search** – Provides summarized topic information
- 📺 **YouTube Playback** – Plays requested videos via voice command
- 🧠 **Random Facts** – Shares fun and interesting facts
- 😂 **Jokes** – Delivers a two-part joke for a quick laugh
- 📅 **Date Reader** – Reads out the current date
- 👋 **Exit Commands** – Ends session on "thank you" or "bye"

---

## 🛠️ Technologies Used

- **Python 3**
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – Text-to-Speech
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) – Speech to Text
- [`pyaudio`](https://pypi.org/project/PyAudio/) – Microphone integration
- [`randfacts`](https://pypi.org/project/randfacts/) – Fetches random facts
- [`selenium`](https://pypi.org/project/selenium/) – Used for Wikipedia automation
- **Multithreading** – Ensures smooth and parallel execution of tasks
- **Custom Python Modules**:
  - `selenium_new.py` – Handles info search and extraction
  - `yt_autor.py` – Automates YouTube playback
  - `jokes.py` – Provides joke content

---

## 📁 Project Structure

```bash
📦 Voice-Assistant-Project
├── assistant.py          # Main voice assistant script
├── selenium_new.py       # Wikipedia search automation
├── yt_autor.py           # YouTube video automation
├── jokes.py              # Joke module
└── README.md             # Project documentation
