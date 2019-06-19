import serial
from time import sleep
import ev3dev.ev3 as ev3

serial.tools.list_ports()

ser = serial.Serial ("outA", 9600)    #Open port with baud rate
while True:                   
    serial.write(received_data)
    sleep(0.03)
    

    
