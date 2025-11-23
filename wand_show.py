import time
import pygame
import random
import serial
import node_classes as nc
import myself
import topic_action_mapping as tam
import json
import sys

#MQTT connection info 
connection_info = {
    #"mqtt_username":,
     #"mqtt_password":, 
     #"mqtt_url": "192.168.1.150", 
     "mqtt_url": "10.42.0.1", 
     "mqtt_port": 1883

}

#Create node class commander
commander = nc.create_commander(myself.myself["name"], connection_info)

#Assume new wand user 
mode = "new"
#mode = "old"

#If no sys argv, assume new. Otherwise, set mode to sys.argv (most likely old)
if len(sys.argv) <= 1:
    mode = "new"
else:
    mode = sys.argv[1]

#Arduino connection setup 
com_port = '/dev/ttyUSB0'
arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)

#Need this for sounds 
pygame.mixer.init()
pygame.mixer.music.load('sounds/thunder.mp3')
sleep_time = 1.5

#These are the motion actions
group_1_actions = ["clock", "erratic_flowers", "shaking_box", "knock_over"]
#group_1_actions = ["clock", "erratic_flowers", "knock_over"]
#These are the sound actions
group_2_actions = ["thunder", "glass"]
#This is the finish action 
new_finish_action = "lantern"

#Grab sound file/load and play from sounds folder.
#Busy wait 
def play_sound(what_sound):
        sound_string = 'sounds/'+what_sound+".mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_string)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
        #print(dev_id)

#New wand buyer
if mode == "new":
    #First, get the NUMBER of the actions we will take here. #Can change number of actions here too 
    num_group_1_actions = random.randrange(2, len(group_1_actions))
    num_group_2_actions = random.randrange(1, len(group_2_actions)+1)
    #GRAB random sample of actions 
    group_1_actions  = random.sample(group_1_actions, num_group_1_actions)
    group_2_actions  = random.sample(group_2_actions, num_group_2_actions)
    #Get the whole list
    whole_list = group_1_actions + group_2_actions
    #Shuffle it for random 
    random.shuffle(whole_list)
    #Print it
    print(whole_list)
    #Set the finish action 
    finish_action = new_finish_action
    #play_sound("wand_finish")

#Returning with their own wand 
elif mode == "old":
    #Set defined actions
    whole_list = ["lantern_on", "knock_over", "music_box"]
    #Finish action is lantern off
    finish_action = "lantern_off"

#Pace through the actions
keep_going = True

while(keep_going):
      #Read in a message
      data = arduino.readline()
      #print(data)
      message = data.decode()
      #If a button on the IR receiver was pressed (any button)
      if len(message) > 1:
        print(message)
        print(type(message))
        #if any meaningful button pressed on IR receiver 
        if len(message) > 2 and len(message) < 20:
            #If we still have actions left
            if whole_list != []:
                #Grab the action off the list (last one)
                item = whole_list.pop()
                #Set the message equal to "message: action_name" 
                message = {"message": item}
                print("Item", item)
                print("Whole List", whole_list)
                #We could litteraly just send these - not sure why case statement?
                #If clock, publish play the cuckoo sound 
                if item == "clock":
                    commander.publish(item, json.dumps(message))
                    play_sound("good_cuckoo")
                #If flowers, publish
                if item == "erratic_flowers":
                    commander.publish(item, json.dumps(message))
                #If flowers, publish
                if item == "knock_over":
                    commander.publish(item, json.dumps(message))
                #If flowers, publish
                if item == "lantern_on":
                    commander.publish(item, json.dumps(message))
                #If flowers, publish
                if item == "music_box":
                    commander.publish(item, json.dumps(message))
                    play_sound("music_box")
                #If flowers, publish
                if item == "shaking_box":
                    commander.publish(item, json.dumps(message))
                #If flowers, play thunder sound
                if item == "thunder":
                    play_sound("thunder")
                #If glass, play glass sound
                if item == "glass":
                    play_sound("glass")
            #If our last action 
            else:
                keep_going = False
                print(finish_action)
                #Set message, as before 
                message = {"message": finish_action}
                #If lantern, publish and play sound
                if finish_action == "lantern":
                    commander.publish(finish_action, json.dumps(message))
                    play_sound("wand_finish")
                #If lantern off, just publish
                if finish_action == "lantern_off":
                    commander.publish(finish_action, json.dumps(message))
            #Sleep wait 
            time.sleep(1.5)

#sudo cp special_effect.service /lib/systemd/system/special_effect.service
#sudo systemctl daemon-reload
#sudo systemctl enable special_effect.service
#sudo systemctl start special_effect.service
#sudo systemctl status special_effect.service
