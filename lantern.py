import serial
import time


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def action(message):
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)

    print("Before serial send")
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
    print("After serial send")
    num = 8
    value = write_read(num)
    print(value) # printing the value


    