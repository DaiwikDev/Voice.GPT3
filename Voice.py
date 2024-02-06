import pyttsx3
import speech_recognition as sr
import openai

# Set your OpenAI GPT-3.5 API key
openai.api_key = 'sk-'

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def chat_gpt(query):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate GPT-3.5 engine
        prompt=query,
        max_tokens=150,  # Adjust as needed
        n=1,  # Number of responses to generate
        stop=None,  # Can specify stop conditions
    )
    return response.choices[0].text.strip()

while True:
    user_input = listen()
    if user_input:
        # Send user input to ChatGPT
        chat_response = chat_gpt(user_input)

        # Print and speak the response from ChatGPT
        print("ChatGPT:", chat_response)
        speak(chat_response)
