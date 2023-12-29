import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "hello" in command:
        speak("Hello Rishi How can I help you?")
    elif "how are you" in command:
        speak("I'm doing well, thank you!")
    elif "goodbye" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    speak("Hello! I'm your text-based voice assistant. How can I assist you?")
    while True:
        command = input("Enter a command: ").lower()
        process_command(command)
