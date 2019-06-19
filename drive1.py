# David Fricke adapted from Dan McGinn
# Keyboard inputs adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
# EV3 Project: http://inspiredtoeducate.net/inspiredtoeducate/programming-lego-mindstorms-ev3-with-python/
# Run with python3

import time,termios,tty,sys
import ev3dev.ev3 as ev3
from time import sleep

# Define motor outputs
motor_left_B = ev3.LargeMotor('outB')
motor_left_C = ev3.LargeMotor('outC')
motor_right_A = ev3.LargeMotor('outA')
motor_right_D = ev3.LargeMotor('outD')
speed = 90 # Set Speed

# Initiate keybaord inputs
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def back():
   motor_left_B.run_direct(duty_cycle_sp=speed)
   motor_left_C.run_direct(duty_cycle_sp=speed)
   motor_right_A.run_direct(duty_cycle_sp=speed)
   motor_right_D.run_direct(duty_cycle_sp=speed)
   
def forward():
    motor_left_B.run_direct(duty_cycle_sp=-speed)
    motor_left_C.run_direct(duty_cycle_sp=-speed)
    motor_right_A.run_direct(duty_cycle_sp=-speed)
    motor_right_D.run_direct(duty_cycle_sp=-speed)
	
def right():
   motor_left_B.run_direct(duty_cycle_sp=-speed)
   motor_left_C.run_direct(duty_cycle_sp=-speed)
   motor_right_A.run_direct(duty_cycle_sp=speed)
   motor_right_D.run_direct(duty_cycle_sp=speed)
   
def left():
   motor_left_B.run_direct(duty_cycle_sp=speed)
   motor_left_C.run_direct(duty_cycle_sp=speed)
   motor_right_A.run_direct(duty_cycle_sp=-speed)
   motor_right_D.run_direct(duty_cycle_sp=-speed)
   
def stop():
    motor_left_B.run_direct(duty_cycle_sp=0)
    motor_left_C.run_direct(duty_cycle_sp=0)
    motor_right_A.run_direct(duty_cycle_sp=0)
    motor_right_D.run_direct(duty_cycle_sp=0)
   
def red():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    sleep(0.01)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    sleep(0.01)
def orange():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.ORANGE)
    sleep(0.01)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.ORANGE)
    sleep(0.01)
def yellow():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
    sleep(0.01)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)
    sleep(0.01)
def green():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    sleep(0.01)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    sleep(0.01)

print("-----------Connection Initiated-----------")
while True:
   char = getch()
   if char == 'w':
      forward()
      print("Forward")
   if char == 's':
      back()
      print("Backward")
   if char == 'a':
      left()
      print("Left")
   if char == 'd':
      right()
      print("Right")
   if char == ' ':
      stop()
      ev3.Leds.all_off()
   if char == 'r':
      red()
      print("Red")
   if char == 'o':
      orange()
      print("Orange")
   if char == 'y':
      yellow()
      print("Yellow")
   if char == 'g':
      green()
      print("Green")
   if char == 'q':
      print("-------------------EXIT-------------------")
      sleep(0.01)
      stop()
      ev3.Leds.all_off()
      exit()
