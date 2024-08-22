import speech_recognition as sr

def code_main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as Microphone:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(Microphone)
        print("Listening...")

        audio_data = recognizer.listen(Microphone)
        print("Recognizing...")

        try:
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print("Sorry, there was an error with the request; {0}".format(e))

if __name__ == "__main__":
    code_main()