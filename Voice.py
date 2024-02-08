import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    return engine

def talk(engine, text):
    engine.say(text)
    engine.runAndWait()

def take_command(listener, timeout=5):
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=timeout)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please repeat.")
        return take_command(listener, timeout)  # Recursive call to listen again
    except sr.WaitTimeoutError:
        print("Listening timed out. Please say the command again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    return command

def run_bot():
    listener = sr.Recognizer()
    engine = init_engine()

    while True:
        command = take_command(listener)
        print(command)

        if 'play' in command:
            song = command.replace('play', '')
            talk(engine, 'playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(engine, 'Current time is ' + current_time)
        elif 'who are you' in command:
            talk(engine, 'I AM PLATINUM JUBILEE ROBOT')
        elif 'who is' in command:
            person = command.replace('who is', '')
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(engine, info)
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Ambiguous search term: {e}")
                talk(engine, "I'm not sure. Please provide more details.")
        elif 'date' in command:
            talk(engine, 'Sorry, I have a headache')
        elif 'are you single' in command:
            talk(engine, 'I am in a relationship with WiFi')
        elif 'joke' in command:
            talk(engine, pyjokes.get_joke())
        elif 'exit' in command:
            talk(engine, 'Nice talking to you, bye!')
            break
        else:
            talk(engine, 'I Dont Have The info right now, Search it on Google')

if __name__ == "__main__":
    run_bot()
