from gpiozero import LED
from time import sleep
import curses
import threading

#Setup the IO points
disable = LED("GPIO5")
ss1 = LED("GPIO6")
ss2 = LED("GPIO12")
ss3 = LED("GPIO13")
notReset = LED("GPIO16")
notSleep = LED("GPIO19")
step = LED("GPIO20")
direction = LED("GPIO21")

#Set the Step size to the largest
ss1.off()
ss2.off()
ss3.off()

#Get the device ready to move
notSleep.on()
notReset.off()
sleep(1)
notReset.on()
disable.off()

#Set the direction
direction.off()

#set global speed variables
motorSpeed = 100.0

#The motor can handle 1000Hz for startup (probably not under load)
def toggleStartStop():
    global motorSpeed
    if motorSpeed > 2000.0:
        motorSpeed = 2000.0
    disable.toggle()

def changeDir():
    global motorSpeed
    if motorSpeed > 2000.0:
        motorSpeed = 2000.0
    direction.toggle()

#8000 is actually 4000Hz (on then off)
#8000 cannot be used from a cold start, the motor has to ramp to it
def increaseSpeed():
    global motorSpeed
    motorSpeed = motorSpeed + 100.0
    if motorSpeed > 8000.0:
        motorSpeed = 8000.0

def decreaseSpeed():
    global motorSpeed
    motorSpeed = motorSpeed - 100.0
    if motorSpeed < 100.0:
        motorSpeed = 100.0

def motorThread():
    global motorSpeed
    #move the motor
    while True:
        step.on()
        sleep(1.0/motorSpeed)
        step.off()
        sleep(1.0/motorSpeed)

#Start up the motor Thread
threading.Thread(target = motorThread).start()

#Set the key press actions
actions = {
    curses.KEY_UP:          increaseSpeed,
    curses.KEY_DOWN:        decreaseSpeed,
    curses.KEY_BACKSPACE:   toggleStartStop,
    curses.KEY_LEFT:        changeDir,
}

#key screen
def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        key = window.getch()
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()

#Start the key screen (press ctrl+c twice to end it)
curses.wrapper(main)

