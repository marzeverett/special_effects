import time
import threading
import socketserver 
from PCA9685 import PCA9685
from time import ctime  
import socket

print("start")

pwm = PCA9685(0x40)
pwm.setPWMFreq(50)

for i in range(0, 6):
	pwm.setServoPulse(0,2100)
	time.sleep(0.2)
	pwm.setServoPulse(0,500)
	time.sleep(0.2)
#pwm.setServoPulse(1,Pos1)
#pwm.setServoPulse(2,Pos2)
#pwm.setServoPulse(3,Pos3)

#time.sleep(5)

	
# def timerfunc():
#     global Step0,Step1,Step2,Step3,Pos0,Pos1,Pos2,Pos3,pwm

#     if(Step0 != 0):
#         Pos0 += Step0
#         if(Pos0 >= 2500): 
#             Pos0 = 2500
#         if(Pos0 <= 500):
#             Pos0 = 500
#         #set channel 0
#         pwm.setServoPulse(0,Pos0)    
        
#     if(Step1 != 0):
#         Pos1 += Step1
#         if(Pos1 >= 2500): 
#             Pos1 = 2500
#         if(Pos1 <= 500):
#             Pos1 = 500
#         #set channel 1
#         pwm.setServoPulse(1,Pos1)   

#     if(Step2 != 0):
#         Pos2 += Step2
#         if(Pos2 >= 2500): 
#             Pos2 = 2500
#         if(Pos2 <= 500):
#             Pos2 = 500
#         #set channel 2
#         pwm.setServoPulse(2,Pos2)   

#     if(Step3 != 0):
#         Pos3 += Step3
#         if(Pos3 >= 2500): 
#             Pos3 = 2500
#         if(Pos3 <= 500):
#             Pos3 = 500
#         #set channel 3
#         pwm.setServoPulse(3,Pos3)   

#     global t        #Notice: use global variable!
#     t = threading.Timer(0.02, timerfunc)
#     t.start()
