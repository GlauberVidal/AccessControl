import subprocess
import os
import time
import os.path
from gpiozero import LED, Button
from signal import pause

checkTorF = []
led = []
button = []
lamp = []

lamp = LED(18)
lock = LED(25)
button = Button(2)
opendoor = False

lamp.on()
lock.on()

while True:

    subprocess.call(['fswebcam','./AccessControl/capturePicture.jpeg'])

    checkTorF = os.path.exists("./AccessControl/LetDoorOpen.txt")

    bool([checkTorF])

    if button.is_pressed:
        f= open("./AccessControl/LetProgRun.txt","w+")
        f.write("Let Program Run")
        f.close()

    if checkTorF is True:
        print('ItWorked')
        lamp.off()
        opendoor = True
    else:
        lock.on()

    if opendoor and button.is_pressed:
        lock.off()
        lamp.on()
        os.remove("./AccessControl/LetDoorOpen.txt")
        os.remove("./AccessControl/LetProgRun.txt")
        opendoor = False
