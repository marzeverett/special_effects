#From here: https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0 

import serial
import time
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(x)
    time.sleep(0.5)
    data = arduino.read()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(bytes(num, 'utf-8'))
    print(value) # printing the value