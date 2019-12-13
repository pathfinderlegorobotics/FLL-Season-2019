#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# # Write your program here
# brick.sound.beep()



# def initVariables():
# Initialize a motor at port B.
motor_right = Motor(Port.B)
motor_left = Motor(Port.C)
# Initialize two motors and a drive base
robot = DriveBase(motor_left, motor_right, 56, 125)

def beepPlz():
    # Play another beep sound.
    # This time with a higher pitch (1000 Hz) and longer duration (500 ms).
    brick.sound.beep(5000, 500)


def go():
    # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
    test_motor.run_target(500, 90)

def turn():
    pass

def turnInPlace():
    pass

def followLine():
    pass

def display():
    # Clear the display
    brick.display.clear()
    # Print ``Hello`` near the middle of the screen
    brick.display.text("Hello", (60, 50))
    # Print ``World`` directly underneath it
    brick.display.text("World")

def routineRed():
    # Make the light red
    brick.light(Color.RED)
    wait(1000)
    # Turn the light off
    brick.light(None)

def routineGreen():
    # Make the light red
    brick.light(Color.GREEN)
    wait(1000)
    # Turn the light off
    brick.light(None)

def routineBlue():
    # Make the light red
    brick.light(Color.BLACK)
    wait(1000)
    # Turn the light off
    brick.light(None)

def routineYellow():
    # Make the light red
    brick.light(Color.YELLOW)
    wait(1000)
    # Turn the light off
    brick.light(None)
    

def checkForTouch():
    touchSensor = TouchSensor(Port.S3)
    beepPlz()
    t = 0
    numberOfTouches = 0
    while (t < 1000):
        if ( touchSensor.pressed() ):
            numberOfTouches += 1
            beepPlz()
        t += 1
        pass
    if (numberOfTouches == 0):
        routineBlue()
    elif (numberOfTouches < 5):
        routineYellow()
    elif (numberOfTouches < 10):
        routineGreen()
    else:
        routineRed()
    beepPlz()


# initVariables()
# beepPlz()
# display()
# wait(1000)
# routineRed()
# wait(1000)
# routineGreen()
# wait(1000)

# checkForTouch()

robot.drive_time(100, 90, 3000)
wait(100)
robot.stop()


