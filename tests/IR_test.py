import time
import random
import serial

#com_port = 'COM0'
#com_port = '/dev/ttyACM0'
com_port = '/dev/ttyUSB0'

arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)

while(1):
      #Read in a message
      data = arduino.readline()
      #print(data)
      message = data.decode()
      if len(message) > 1:
        print(message)
        print(type(message))
      #Check the message

