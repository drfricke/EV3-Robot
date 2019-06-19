import time,termios,tty,sys
import ev3dev.ev3 as ev3
from time import sleep

motor_right_A = ev3.LargeMotor('outA')

speed = [50, 75, 100] # Set Speed
gear = [2]

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def forward():
    motor_right_A.run_direct(duty_cycle_sp=speed[gear[0]])

def stop():
    motor_right_A.run_direct(duty_cycle_sp=0)

print("-----------Connection Initiated-----------")
while True:
   char = getch()
   if char == 'w':
      forward()
      print("Forward")
   if char == 'h':
      gear = [2]
      print('High Speeed')
   if char == 'm':
      gear = [1]
      print('Mid Speeed')
   if char == 'l':
      gear = [0]
      print('Low Speeed')
   if char == ' ':
      stop()
   if char == 'q':
      print("-------------------EXIT-------------------")
      sleep(0.01)
      stop()
      ev3.Leds.all_off()
      exit()
