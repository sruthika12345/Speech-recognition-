import speech_recognition as sr

r = sr.Recognizer()

# Replace 'Language code' with the corresponding language codes
language_codes = {
    "Russian": "ru-RU",
    "English": "en-US",
    "German": "de-DE",
    "French": "fr-FR",
    "Spanish": "es-ES"
}

for lang, lang_code in language_codes.items():
    print(f"Listening for {lang} speech...")
    
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = r.listen(source)

    try:
        recognized_text = r.recognize_google(audio, language=lang_code)
        print(f"Recognized {lang}: {recognized_text}")
    except sr.UnknownValueError:
        print(f"Sorry, {lang} speech could not be recognized.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
