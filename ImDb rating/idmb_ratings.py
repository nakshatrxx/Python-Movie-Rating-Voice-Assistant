import speech_recognition as sr
import pyttsx3
from Extraction.extract_ratings import GetRating

r = sr.Recognizer()

def text_to_audio(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

try:

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)

        print("Which movie rating would you like to know?")
        text_to_audio("Which movie rating would you like to know?")
        audio = r.listen(source)

        # Google web speech API to recognize audio
        movie_name = r.recognize_google(audio)
        movie_name = movie_name.lower()

        print("Recognized text: " + movie_name)

        get_rating_obj = GetRating(movie_name)
        rating = get_rating_obj.get_rating()
        
        if rating is not None:
            output = "Rating of {} is {}".format(movie_name, rating)
            print(output)
            text_to_audio(output)
        else:
            print("Unable to fetch the rating. Please try again with a valid movie name.")

except sr.RequestError as error:
    print("Unable to request the results {0}".format(error))

except sr.UnknownValueError:
    print("An unknown error occurred")
