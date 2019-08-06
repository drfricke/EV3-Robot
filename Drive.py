# David Fricke
# Run with python3


from time import sleep
import ev3dev2.motor
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor

motor_A = ev3dev2.motor.Motor('outA')
motor_B = ev3dev2.motor.Motor('outB')
motor_C = ev3dev2.motor.Motor('outC')
motor_D = ev3dev2.motor.Motor('outD')

motor_C.position = 0 #resets encoders positions
motor_D.position = 0

left = [1]   #setups steering
right = [1]

ts1 = TouchSensor('in1') # functions as brake 
ts2 = TouchSensor('in2') # ends program
motor_C.run_direct(duty_cycle_sp=100) #turns on relay

def stop():
        motor_A.run_direct(duty_cycle_sp=50)
        motor_B.run_direct(duty_cycle_sp=50)

print('start')

try:
        while True:
                stop()
                while ts1.is_pressed:
                        if 3 > motor_C.position > -3:
                                left[0] = 1
                                right[0] = 1
                                if 10 > motor_D.position > -10:
                                        stop()
                                elif 49 > motor_D.position > 10:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*(motor_D.position+50))
                                        motor_B.run_direct(duty_cycle_sp=right[0]*(motor_D.position+50))
                                elif motor_D.position > 49:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*100)
                                        motor_B.run_direct(duty_cycle_sp=right[0]*100)
                                elif -10 > motor_D.position > -49:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*(motor_D.position+50))
                                        motor_B.run_direct(duty_cycle_sp=right[0]*(motor_D.position+50))
                                elif -49 > motor_D.position:
                                        motor_A.run_direct(duty_cycle_sp=0)
                                        motor_B.run_direct(duty_cycle_sp=0)
                        elif 80 > motor_C.position > 3:
                                left[0] = (1 - (motor_C.position/80))
                                right[0] = 1
                                if 10 > motor_D.position > -10:
                                        stop()
                                elif 49 > motor_D.position > 10:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*(motor_D.position+50))
                                        motor_B.run_direct(duty_cycle_sp=right[0]*(motor_D.position+50))
                                elif motor_D.position > 49:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*100)
                                        motor_B.run_direct(duty_cycle_sp=right[0]*100)
                                elif -10 > motor_D.position > -49:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*(motor_D.position+50))
                                        motor_B.run_direct(duty_cycle_sp=right[0]*(motor_D.position+50))
                                elif -99 > motor_D.position:
                                        motor_A.run_direct(duty_cycle_sp=0)
                                        motor_B.run_direct(duty_cycle_sp=0)
                        elif -3 > motor_C.position > -80:
                                left[0] = 1
                                right[0] = (1 + motor_C.position/80)
                                if 10 > motor_D.position > -10:
                                        stop()
                                elif 49 > motor_D.position > 10:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*(motor_D.position+50))
                                        motor_B.run_direct(duty_cycle_sp=right[0]*(motor_D.position+50))
                                elif motor_D.position > 49:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*100)
                                        motor_B.run_direct(duty_cycle_sp=right[0]*100)
                                elif -10 > motor_D.position > -49:
                                        motor_A.run_direct(duty_cycle_sp=left[0]*(motor_D.position+50))
                                        motor_B.run_direct(duty_cycle_sp=right[0]*(motor_D.position+50))
                                elif -49 > motor_D.position:
                                        motor_A.run_direct(duty_cycle_sp=0)
                                        motor_B.run_direct(duty_cycle_sp=0)
                if ts2.is_pressed:
                        print('closed')
                        stop()
                        motor_C.run_direct(duty_cycle_sp=0) #relay off
                        exit()
except:     # in case of any strange errors
        print('END.')
        stop()
        motor_C.run_direct(duty_cycle_sp=0) #relay off
        exit()
