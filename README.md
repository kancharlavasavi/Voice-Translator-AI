# Voice-Translator-AI
A smart voice translator built using SpeechRecognition, GoogleTranslator, gTTS, and Pygame to convert spoken words into translated speech.



Smart Voice Translator is an AI-powered speech translation tool built using:
SpeechRecognition – Converts speech to text
GoogleTranslator (deep-translator) – Translates text
gTTS (Google Text-to-Speech) – Converts translated text to audio
Pygame – Plays the generated audio
pyttsx3 – Optional offline text-to-speech

This application allows users to **speak in one language**, automatically **translate it**, and **hear it spoken back** in another language.

---

## 🎯 Features

* 🎤 Real-time speech recognition
* 🔄 Automatic language detection
* 🌍 Translate to any supported language
* 🔊 Text-to-speech output
* 🔈 Plays speech using Pygame
* ⚙️ Simple, clean Python implementation

---

Requirements

Install dependencies:

```
SpeechRecognition
deep-translator
gTTS
pygame
pyttsx3
pyaudio
```

### ⚠ Important (Windows Users)

If **pyaudio** fails to install, run:

```bash
pip install pipwin
pipwin install pyaudio
```


## 🚀 How to Run

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

### 2️⃣ Navigate into the project folder:

```bash
cd your-repo-name
```

### 3️⃣ Install required libraries:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the script:

```bash
python translator.py
```


## 🧠 How It Works

1. Listen through the microphone
2. Convert speech → text using SpeechRecognition
3. Translate text → target language
4. Convert translated text → audio using gTTS
5. Play the audio using Pygame

📂 Project Structure
📁 Voice-Translator
│── translator.py
│── README.md
│── requirements.txt

