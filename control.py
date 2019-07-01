import time,termios,tty,sys
import ev3dev.ev3 as ev3
from time import sleep
import serial

motor_right_A = ev3.LargeMotor('outA')
motor_right_B = ev3.LargeMotor('outB')

speed = [50, 0, 0] # Set Speed
gearA = [0]
gearB = [0]
i = 50
n = 50

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
    motor_right_A.run_direct(duty_cycle_sp=speed[gearA[0]])
    motor_right_B.run_direct(duty_cycle_sp=speed[gearB[0]])

def stop():
    motor_right_A.run_direct(duty_cycle_sp=50)
    motor_right_B.run_direct(duty_cycle_sp=50)

print("-----------Connection Initiated-----------")
while True:
   char = getch()
   if char == 'w':
      forward()
      print("Drive")
   if char == 'p':
      i = i + 5
      if i > 100:
          i = 100
          print('Outside driver range, PWM overridden to 100')
      speed[1] = i
      gearA = [1]
      print(speed[1], 'Motor A')
   if char == 'o':
      i = i - 5
      if i < 0:
          i = 0
          print('Outside driver range, PWM overridden to 0')
      speed[1] = i
      gearA = [1]
      print(speed[1],' Motor A')
   if char == 'l':
      n = n + 5
      if n > 100:
          n = 100
          print('Outside driver range, PWM overridden to 100')
      speed[2] = n
      gearB = [2]
      print(speed[2], 'Motor B')
   if char == 'k':
      n = n - 5
      if n < 0:
          n = 0
          print('Outside driver range, PWM overridden to 0')
      speed[2] = n
      gearB = [2]
      print(speed[2], 'Motor B')
   if char == ' ':
      stop()
   if char == 'q':
      print("-------------------EXIT-------------------")
      sleep(0.01)
      stop()
      ev3.Leds.all_off()
      exit()

