import time,termios,tty,sys
import ev3dev.ev3 as ev3
from time import sleep
import serial

motor_right_A = ev3.LargeMotor('outA')

speed = [0, 50, 100, 0] # Set Speeds
gear = [2] #indexes Speeds
i = 50

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
    motor_right_A.run_direct(duty_cycle_sp=50)

print("-----------Connection Initiated-----------")
while True:
   char = getch()
   if char == 'w':
      forward()
      print("Drive")
   if char == 'h':
      gear = [2]
      print('Full Forward')
   if char == 'p':
      i = i + 10
      if i > 100:
          i = 100
          print('Outside driver range, PWM overridden to 100')
      speed[3] = i
      gear = [3]
      print(speed[3])
   if char == 'o':
      i = i - 10
      if i < 0:
          i = 0
          print('Outside driver range, PWM overridden to 0')
      speed[3] = i
      gear = [3]
      print(speed[3])
   if char == 'm':
      gear = [1]
      print('Stop')
   if char == 'l':
      gear = [0]
      print('Full Backward')
   if char == ' ':
      stop()
   if char == 'q':
      print("-------------------EXIT-------------------")
      sleep(0.01)
      stop()
      ev3.Leds.all_off()
      exit()

