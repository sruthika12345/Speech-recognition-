import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak your note...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return None

def save_note(note, filename="newfile.txt"):
    try:
        with open(filename, "newfile") as file:
            file.write(note + "\n")
        print(f"Note saved to {newfile}")
    except IOError as e:
        print(f"Error saving note: {e}")

def read_notes(filename="newfile.txt"):
    try:
        with open(filename, "r") as file:
            notes = file.readlines()
            print("\nSaved Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found. Start by taking a note.")

def main():
    print("1. Take a note")
    print("2. Read notes")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        note = listen_and_transcribe()
        if note:
            save_note(note)
    elif choice == "2":
        read_notes()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
