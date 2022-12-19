import time
import threading
import socketserver 
from PCA9685 import PCA9685
from time import ctime  
import socket

def action(message):
    #Based on waveshare servo hat example code
    print("erratic flowers are running!")
    pwm = PCA9685(0x40)
    pwm.setPWMFreq(50)
    for i in range(0, 6):
        pwm.setServoPulse(0,2100)
        time.sleep(0.2)
        pwm.setServoPulse(0,500)
        time.sleep(0.2)

