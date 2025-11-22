import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os

# ---------- TEXT-TO-SPEECH ----------
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "tts.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove(filename)


# ---------- SPEECH RECOGNITION (only once) ----------
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak now...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    spoken_text = recognizer.recognize_google(audio)
    print("📝 You said:", spoken_text)
except:
    spoken_text = "Sorry, I could not understand you."

# ---------- TRANSLATION (only once) ----------
target_lang = "te"    # change output language

translated_text = GoogleTranslator(source="auto", target=target_lang).translate(spoken_text)
print(f"🔄 Translated: {translated_text}")

# ---------- SPEAK OUTPUT (only once) ----------
speak(translated_text, lang=target_lang)





'''
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎙️ Speak now...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 You said:", text)
except sr.UnknownValueError:
    text="Sorry, I couldn't understand."
    print("Sorry, I couldn't understand.")
except sr.RequestError as e:
    print(f"API error: {e}")


from deep_translator import GoogleTranslator

languages = ["fr", "es", "de", "hi", "te"]
tel=GoogleTranslator(source="auto", target = "en").translate(text)

for lang in languages:
    translated = GoogleTranslator(source="auto", target=lang).translate(text)
    print(f"{lang}: {translated}")

import pyttsx3

engine = pyttsx3.init()

# List voices
voices = engine.getProperty('voices')
for i, v in enumerate(voices):
    print(i, v.id)

# Select voice (try changing the index)
engine.setProperty('voice', voices[0].id)  # try 0, 1, 2...

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

engine.say(tel)
engine.runAndWait()



from gtts import gTTS
import pygame
import os

def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "tts.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove(filename)

# Example Telugu
speak(text, lang="te")

# Example Hindi
speak("नमस्ते आप कैसे हो", lang="hi")



import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os

# ---------- TEXT-TO-SPEECH FUNCTION ----------
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "tts.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove(filename)

# ---------- SPEECH RECOGNITION ----------
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎙️ Speak now...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    # Recognize speech (Google auto detects language)
    spoken_text = recognizer.recognize_google(audio)
    print("📝 You said:", spoken_text)
except sr.UnknownValueError:
    spoken_text = "Sorry, I could not understand you."
    print(spoken_text)
except sr.RequestError as e:
    print("API Error:", e)

# ---------- TRANSLATION ----------
# User speaks in ANY language
# You choose: translate to which language?
target_lang = "hi"   # Telugu (change to "hi", "fr", "es", etc.)

translated_text = GoogleTranslator(source="auto", target=target_lang).translate(spoken_text)
print(f"🔄 Translated to ({target_lang}): {translated_text}")

# ---------- SPEAK TRANSLATION ----------
speak(translated_text, lang=target_lang)
'''
