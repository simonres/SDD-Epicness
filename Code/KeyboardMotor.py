#!/usr/bin/env python3
# import curses and GPIO
import curses
import RPi.GPIO as GPIO

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
# set pin 18 as pwm with a 100Hz frequency
pwm = GPIO.PWM(12, 100)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        #The movement is defined here. For a better understanting check the Hardware section on the GitHub page
        elif char == curses.KEY_UP:
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)
            GPIO.output(16, True)
        elif char == curses.KEY_DOWN:
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)
            GPIO.output(16, False)
        elif char == curses.KEY_RIGHT:
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(16, True)
        elif char == curses.KEY_LEFT:
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, True)
            GPIO.output(16, False)
        elif char == 10:
            GPIO.output(16, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
        #Defining the diferent speeds
        elif char == 1:
            pwm.ChangeDutyCycle(10)
        elif char == 2:
            pwm.ChangeDutyCycle(25)
        elif char == 3:
            pwm.ChangeDutyCycle(50)
        elif char == 4:
            pwm.ChangeDutyCycle(75)
        elif char == 5:
            pwm.ChangeDutyCycle(100)

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
    GPIO.cleanup()


