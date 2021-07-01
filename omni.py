import speech_recognition as sr
from gtts import gTTS
import time
from time import sleep
import random
import os
import pygame
from adafruit_servokit import ServoKit


kit = ServoKit(channels=16)
r = sr.Recognizer()
pygame.mixer.init()

# Initialize motor ranges
kit.servo[0].set_pulse_width_range(500,2500)
kit.servo[1].set_pulse_width_range(500,2500)
kit.servo[2].set_pulse_width_range(500,2500)
kit.servo[3].set_pulse_width_range(500,2500)
kit.servo[4].set_pulse_width_range(500,2500)


def mic_call():
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I do not understand')
        except sr.RequestError:
            print('Sorry my speech service is down')
        return voice_data


def respond(voice_data):
    if 'help' in voice_data:
        return('Welcome to the OmniArm voice interface. You can toggle the default myoelectric arm movement through voice activated commands. Give it a try!')
    if 'grab' in voice_data:
        return('Grab mode, activated')
    if 'pinch' in voice_data:
        return('Pinch mode, activated')
    if 'pointer' in voice_data:
        return('Pointer mode, activated')
    if 'reset' in voice_data:
        return('Resetting arm position')
    if 'flip' in voice_data:
        return("I don't think this is a good idea, but if you say so")
    if 'shut' in voice_data:
        speak('Shutting down system.')
        exit()
    
    
def speak(audio_text):
    tts = gTTS(text=audio_text, lang='en', tld='com', slow=False)
    r = random.randint(1, 2000000)
    audio_file = 'audio'+ str(r) + '.mp3'
    tts.save(audio_file)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    os.remove(audio_file)


def motion_reset():
    
    kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    kit.servo[2].angle = 0
    kit.servo[3].angle = 0
    kit.servo[4].angle = 0
    
    
def motion_grab():

    motion_reset()

    time.sleep(0.5)

    kit.servo[0].angle = 180
    kit.servo[1].angle = 180
    kit.servo[2].angle = 180
    kit.servo[3].angle = 180
    kit.servo[4].angle = 180
    

def motion_pointer():
    
    motion_reset()
    
    time.sleep(0.5)

    kit.servo[1].angle = 180
    kit.servo[2].angle = 180
    kit.servo[3].angle = 180
    

def motion_pinch():
    
    motion_reset()
    
    time.sleep(0.5)
    kit.servo[0].angle = 130    
    kit.servo[4].angle = 130


def motion_flip():
    
    motion_reset()
    
    time.sleep(0.5)
    
    kit.servo[0].angle = 180
    kit.servo[1].angle = 180
    kit.servo[2].angle = 180
    kit.servo[4].angle = 180



time.sleep(2)
print('How can I help you?')
speak("Welcome.")

while True:
    voice_data=mic_call()
    response = respond(voice_data)
    print(response)
    try:
        speak(response)
        if response == 'Grab mode, activated':
            motion_grab()
        elif response == 'Pinch mode, activated':
            motion_pinch()
        elif response == 'Pointer mode, activated':
            motion_pointer()
        elif response == 'Resetting arm position':
            motion_reset()
        elif response == "I don't think this is a good idea, but if you say so":
            motion_flip()
    except AssertionError:
        print('No text to speak')

        


