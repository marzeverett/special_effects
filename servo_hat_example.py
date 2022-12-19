import time
import threading
import socketserver 
from PCA9685 import PCA9685
from time import ctime  
import socket

print("start")

pwm = PCA9685(0x40)
pwm.setPWMFreq(50)

Pos0 = 1500  
Pos1 = 50 
Pos2 = 1500 
Pos3 = 1500 
Step0 = 0  
Step1 = 0  
Step2 = 0  
Step3 = 0  
pwm.setServoPulse(0,Pos0)
time.sleep(5)
pwm.setServoPulse(0,Pos1)
#pwm.setServoPulse(1,Pos1)
#pwm.setServoPulse(2,Pos2)
#pwm.setServoPulse(3,Pos3)

time.sleep(5)

	
