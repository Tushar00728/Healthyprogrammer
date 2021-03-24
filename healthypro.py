#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musicrepeat(file,stopkey):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play
    while True:
        ipt = input()
        if ipt == stopkey:
            mixer.music.stop()
            break


def logger(say):
    with open("logs.txt", "a") as f:
        f.write(f"{say} {datetime.now()}")




if __name__=="__main__":

    

    time_water = time()
    time_eyes = time()
    time_excer = time()

    water_seconds = 40*60
    eye_seconds = 30*60
    excer_seconds = 45*60

    while True:
        if time() - time_water > water_seconds:
            print("Drink water! Type 'drank' to stop the reminder")
            musicrepeat("watersound.mp3", "drank")
            time_water = time()
            logger("You drank water at")

        if time() - time_eyes >eye_seconds:
            print("Eye relaxation time. Enter 'doneeyes' to stop the reminder.")
            musicrepeat('eyes.mp3', 'doneeyes')
            time_eyes = time()
            logger("Eye relaxation performed at")

        if time() - time_excer > excer_seconds:
            print("Physical Activity Time. Enter 'donephy' to stop the reminder.")
            musicrepeat('physical.mp3', 'donephy')
            time_excer = time()
            logger("Physical Activity done at")






