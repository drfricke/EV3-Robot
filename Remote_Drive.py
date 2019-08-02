# David Fricke
# Keyboard inputs adapted https://github.com/DanielMcGinn18/EV3Hub/blob/master/EV3Python/Drive.py
# EV3 Project: http://inspiredtoeducate.net/inspiredtoeducate/programming-lego-mindstorms-ev3-with-python/
# Run with python3

import time,termios,tty,sys
import ev3dev.ev3 as ev3
from time import sleep
import ev3dev2.motor

motor_right_A = ev3dev2.motor.Motor('outA')
motor_right_B = ev3dev2.motor.Motor('outB')
motor_C = ev3dev2.motor.Motor('outC')

speed = [50, 0, 0] # Set Speed
gear = [0]         # for indexing
i = 50             # starting value

def getch():        # for keyboard commands
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    except:
        ch = ' '
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def forward():
    motor_right_A.run_direct(duty_cycle_sp=speed[gear[0]])
    motor_right_B.run_direct(duty_cycle_sp=speed[gear[0]])

def backward():
    motor_right_A.run_direct(duty_cycle_sp=abs(speed[gear[0]]-100))
    motor_right_B.run_direct(duty_cycle_sp=abs(speed[gear[0]]-100))

def left():
    motor_right_A.run_direct(duty_cycle_sp=abs(speed[gear[0]]-100))
    motor_right_B.run_direct(duty_cycle_sp=speed[gear[0]])

def right():
    motor_right_A.run_direct(duty_cycle_sp=speed[gear[0]])
    motor_right_B.run_direct(duty_cycle_sp=abs(speed[gear[0]]-100))

def stop():
    motor_right_A.run_direct(duty_cycle_sp=52)
    motor_right_B.run_direct(duty_cycle_sp=52)

def count():
    print('Right Motor', -round(motor_right_A.speed/720,2)) # Get speed values from encoders
    print('Left Motor', round(motor_right_B.speed/720,2)) # 720 one rotation with TAWADE 360 count


stop() # Start with 2.5V ouput
motor_C.run_direct(duty_cycle_sp=100) #turns relay on

print("-----------Connection Initiated-----------")
while True:
   char = getch()
   if char == 'w':
      forward()
      print("Forward")
   if char == 'x':
      backward()
      print("Backward")
   if char == 'a':
      left()
      print("Left")
   if char == 'd':
      right()
   if char == 'm':
      count()
   if char == 'p':  #increases PWM
      i = i + 5
      if i > 100:
          i = 100
          print('Outside driver range, PWM overridden to 100')
      speed[1] = i
      gear = [1]
      print(speed[1], 'Motors')
   if char == 'o':  #decreases PWM
      i = i - 5
      if i < 0:
          i = 0
          print('Outside driver range, PWM overridden to 0')
      speed[1] = i
      gear = [1]
      print(speed[1],' Motors')
   if char == ' ':
      stop()
   if char == 'q':
      print("-------------------EXIT-------------------")
      sleep(0.01)
      stop() # stops motors on exit
      motor_C.run_direct(duty_cycle_spq=0) # turns off relay
      ev3.Leds.all_off()
      exit()

