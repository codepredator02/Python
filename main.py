import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
#recognizer = sr.Recognizer()


def talk(text):
    engine.say(text)
    engine.runAndWait()




try:
    with sr.Microphone() as source:
        print('listening..')
        voice = listener.listen(source, timeout=4)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'hello jasmine' in command:
           print(command)
           talk('hello boss did you said :'+command)

    #with sr.Microphone() as source:
        #print("Adjusting noise ")
        #recognizer.adjust_for_ambient_noise(source, duration=1)
        #print("Recording for 4 seconds")
        #recorded_audio = recognizer.listen(source, timeout=4)
        #print("Done recording")
        #talk("here there cool!")
   
   
except Exception as e:
    print('exception : ',e)
    talk("Sorry, I did get that retry again")
    
        
    
