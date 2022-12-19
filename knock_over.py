import time
import threading
import socketserver 
from PCA9685 import PCA9685
from time import ctime  
import socket

def action(message):
    index = 8
    #Based on waveshare servo hat example code
    print("knock over is running!")
    pwm = PCA9685(0x40)
    pwm.setPWMFreq(50)

    pwm.setServoPulse(8,500)
    time.sleep(0.2)
    pwm.setServoPulse(8,2200)
    time.sleep(0.2)
    pwm.setServoPulse(8,500)
    time.sleep(0.2)




