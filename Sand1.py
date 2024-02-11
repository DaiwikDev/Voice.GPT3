import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
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

    # Create synonym mapping dictionary
    synonym_map = {"hey robo": "hey google"}

    while True:
        command = take_command(listener)
        print(command)

        # Check for mapped synonym before original phrase
        if command in synonym_map:
            command = synonym_map[command]

        if command == 'hey google play':
            song = command.replace('hey google play', '')
            talk(engine, 'playing ' + song)
            pywhatkit.playonyt(song)
        elif command == 'hey google':
            talk(engine, 'HI')
        elif 'hey robo' in command:
             talk(engine, 'HI')
        elif 'nice to meet you' in command:
            talk(engine, 'nice to meet you too.')
        elif 'what is your name' in command:
            talk(engine, 'i am the PJHS robot')
        elif 'could you tell me more about yourself' in command:
            talk(engine, 'i work on i7 processor 2.3 Ghz 11th generation, 8 GB Ram, 3050TI Graphic Card from Nvedia, the source is Wikipedia')
        elif 'could you tell me about aga khan education Service' in command:
            talk(engine, 'Aga Khan Education Services is part of the Aga Khan Development Network The Aga Khan Education Services is one of the largest private, not-for-profit, non-denominational educational networks in the developing world. AKES extensive reach, progressive programmes and emphasis on inclusivity create a positive, permanent impact on the students, teachers, parents, alumni, and communities we serve. AKES was established in 1905 by Aga Khan III as the first school in Mundra, Gujarat, India')
        elif 'tell me more about akes' in command:
            talk(engine, 'AKES evolved into a vast network of over 240 schools across 13 countries, with 199 schools and 100+ education centers, educating over 89,500 students')
        elif 'when was platinum jubilee high school established' in command:
            talk(engine, 'The Platinum Jubilee High School, Warangal (PJHSW), under the flagship of Aga Khan Education Service, India (AKESI), was established in 1953. The school aims to provide quality education and offers classes from Nursery to Grade 10')
        elif 'what makes platinum jubilee high school unique' in command:
            talk(engine, 'We prioritize all-round student development with innovative teaching methods, focusing on conceptual understanding through activity-based learning, enhancing communication skills, and building confidence—steering clear of rote learning. Our goal is to equip students for success in our progressive world.')
        elif 'what facilities does pjhsw offer' in command:
            talk(engine, 'We have well-equipped labs for Mathematics, Physics, and Biology, an Atal Tinkering Laboratory (ATL), a spacious library with an extensive collection of books, a large playground with sports equipment, dance classes, counseling services, basketball and badminton courts, a sandpit area, a swimming pool, hygienic washrooms, and more.')
        elif 'what is the purpose of the atal tinkering laboratory' in command:
            talk(engine, 'The ATL is established to impart 21st-century skills essential for science, innovation, and creativity to our students. Our overarching goal is to nurture students into productive community members, actively contributing to the creation of a better tomorrow')
        elif 'any major achievement for this academic year' in command:
            talk(engine, 'The school has been ranked as the number 1 institution for Co-Curricular Education by the India School Merit Awards and acknowledged as one of Indias Top State Board Schools by Education Today.')
        elif 'who created you' in command:
            talk(engine, 'I was created by Om Tanmay, Daiwik, Ruthwik, Sai harshith ,I.Rithvik , RishiVardhan, 8th-grade students from Platinum Jubilee High School, under the guidance of Miss Anita.')
        elif 'hey robo time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(engine, 'Current time is ' + current_time)
        elif 'hey robo who are you' in command:
            talk(engine, 'I AM PLATINUM JUBILEE ROBOT')
        elif 'hey robo who is' in command:
            person = command.replace('hey robo who is', '')
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(engine, info)
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Ambiguous search term: {e}")
                talk(engine, "I'm not sure. Please provide more details.")
        elif 'hey robo date' in command:
            talk(engine, 'Sorry, I have a headache')
        elif 'hey robo are you single' in command:
            talk(engine, 'I am in a relationship with WiFi')
        elif 'hey robo joke' in command:
            talk(engine, pyjokes.get_joke())
        elif 'hey robo bye' in command:
            talk(engine, 'Nice talking to you, bye!')
            break
        else:
            talk(engine, 'I Dont Have The info right now, Ask Kalyan Ram')

if __name__ == "__main__":
    run_bot()
