
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):

    command = c.lower().strip()

    print("Processing command:", command)

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif command.startswith("play"):
        song = command.replace("play ", "", 1).strip()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Song not found in your music library")

    else:
        speak("Sorry, I did not understand that command")
        print("Unknown command:", command)



if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=1
                )

            word = recognizer.recognize_google(audio)

            print("Recognized:", word)

            if "jarvis" in word.lower():

                speak("Yaaa")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)

                print("Command:", command)

            processCommand(command)
        except sr.WaitTimeoutError:
            print("Listening timeout...")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
