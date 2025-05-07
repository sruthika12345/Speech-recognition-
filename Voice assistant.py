import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak the given text using the TTS engine."""
    print(f"Speaking: {text}")  # Debugging log
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the microphone and return the recognized command."""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")  # Debugging log
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")  # Debugging log
            return ""
        except sr.RequestError as e:
            print(f"Speech service is unavailable: {e}")  # Debugging log
            return ""

def process_command(command):
    """Process the recognized command and perform the appropriate action."""
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
try:
    speak("Voice assistant activated.")
    while True:
        command = listen()
        if command:
            process_command(command)
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
    speak("Goodbye!")
