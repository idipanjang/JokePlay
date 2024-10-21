import pyttsx3
# import text to speech  module
import pyjokes
#import pyjoke module


joke= pyjokes.get_joke()
# getting random joke
print("Loading random Joke....: \n", joke )
# print random joke and add new line by \n

engine = pyttsx3.init()
# initiate text to speech
engine.say(joke)
# print what to say for this call for joke
engine.runAndWait()
