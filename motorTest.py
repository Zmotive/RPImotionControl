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
status = "stopped"

def stop():
    global disable
    global motorSpeed
    global status
    disable.on()
    motorSpeed = 100.0
    status = "stopped"

def start():
    global disable
    global motorSpeed
    global status
    disable.off()
    motorSpeed = 100.0
    status = "started"

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

threading.Thread(target = motorThread).start()

actions = {
    curses.KEY_UP:    increaseSpeed,
    curses.KEY_DOWN:  decreaseSpeed,
    curses.KEY_ENTER: disable.on,
    curses.KEY_BACKSPACE: disable.off,
}

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

curses.wrapper(main)

