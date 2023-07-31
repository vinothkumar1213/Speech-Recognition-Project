#speech recognition project

import speech_recognition as sr                            #package
speech=sr.Recognizer()                                     #recognizer object creation
speech.energy_threshold=1000                               #sound level,below value is considered as silence

with sr.Microphone() as input:                             #accessing mic
    print(" ")
    speech.adjust_for_ambient_noise(input)                 #reduce background noise
    command=speech.listen(input)                           #getting input with mic

    out=speech.recognize_google(command).lower()               #recognizing, converting speech to text with recognize_google module
if(out=='turn on' or out=='wake up'):
    print("Hey Dude!")
    
    while(1):                                              #infinite loop

        with sr.Microphone() as input:                     #accessing mic
                print("Say something...")
                speech.adjust_for_ambient_noise(input)     #reduce background noise
                audio=speech.listen(input)                 #getting input with mic

        try:                                                                              #if no error try this

            output=speech.recognize_google(audio).lower()     #recognizing, converting speech to text with recognize_google module
            if(output=='end' or output=='stop' or output=='tata' or output=='bye bye'):   #terminating conditions
                print("Thank You, GoodBye")
                break

            else:                                                                         #printing the recognized output
                print("You said:\n"+output.capitalize())

        except sr.UnknownValueError:                                                      #exceptions handling
            print("Could not understand, Please try again")