# speech to text by Copilot (probably popular code since easily generated)

import speech_recognition as sr
 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    # audio = r.listen(source)
    # make time limit 5 seconds
    audio = r.listen(source, timeout=11)
    print("Time over, thanks")
    print ("Text: " + r.recognize_google(audio))

# Status: Working
