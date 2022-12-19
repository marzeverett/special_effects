
import time
import json
import random
import serial


#Make sure you start mosquitto by typing "mosquitto!"

delay_between_triggers = 5
trigger = "serial"
action_list = []

def trigger(commander, message_list, trigger_num, message):
    commander.publish(message_list[trigger_num], json.dumps(message))
    #Here, we will want an if statement that checks the trigger and sees if we need to play a noise 



def harry_potter(commander):
    #First, create the list of actions for the show\
    #message_list = ["Hello", "Hola", "erratic_flowers"]
    #message_list = ["erratic_flowers", "shaking_box", "lantern"]
    #message_list = ["knock_over"]
    #message_list = ["clock"]
    message_list = ["music_box"]

    #Then, as triggers happen, send the correct message. 
    trigger_num = 0
    #This will be replaced by the pyserial wait 
    while trigger_num < len(message_list):
        #Could also check the trigger here? e
        trigger(commander, message_list, trigger_num, "hi!")
        trigger_num += 1
        time.sleep(delay_between_triggers)
    commander.disconnect()


# while(keep_going):
#       #Read in a message
#       data = arduino.readline()
#       #print(data)
#       message = data.decode()
#       if len(message) > 1:
#         print(message)
#         print(type(message))
#       #Check the message
#       activity_flag, count, start_time = check_message(message, activity_flag, start_time, count)

#       #Check to see if we are good to go to start another motion
#       if activity_flag == 1:
#         end_time = time.time()
#         if end_time - start_time > wait_time:
#           activity_flag = 0
 

#  def check_message(message, activity_flag, start_time, count):
#   #First, check if there are 5 observations in the list. 
#   #If there are not, append to the list and return.  
#       #if message == "FAST BACK\n": #If message equals
#       if "FAST BACK" in message: 
#         #Trigger an action
#         if activity_flag == 0:
#           count += 1
#           activity_flag = 1
#           start_time = time.time()
#           print("Magic!", count)
#           if count >= 1:
#             choose_trigger()
#             start_time = time.time()
#       return activity_flag, count, start_time


    




    
