import time
import pygame
import random
import serial
import node_classes as nc
import myself
import topic_action_mapping as tam
import json
import sys

connection_info = {
    #"mqtt_username":,
     #"mqtt_password":, 
     "mqtt_url": "192.168.1.150", 
     "mqtt_port": 1883

}
commander = nc.create_commander(myself.myself["name"], connection_info)
mode = "new"
#mode = "old"

if len(sys.argv) <= 1:
    mode = "new"
else:
    mode = sys.argv[1]

com_port = '/dev/ttyUSB0'
arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)
pygame.mixer.init()
pygame.mixer.music.load('sounds/thunder.mp3')
sleep_time = 1.5

group_1_actions = ["clock", "erratic_flowers", "shaking_box", "knock_over"]
group_2_actions = ["thunder", "glass"]
new_finish_action = "lantern"




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
    #First, get all the actions we will take here. 
    num_group_1_actions = random.randrange(2, len(group_1_actions)+1)
    num_group_2_actions = random.randrange(1, len(group_2_actions)+1)
    group_1_actions  = random.sample(group_1_actions, num_group_1_actions)
    group_2_actions  = random.sample(group_2_actions, num_group_2_actions)
    whole_list = group_1_actions + group_2_actions
    random.shuffle(whole_list)
    print(whole_list)
    finish_action = new_finish_action
    #play_sound("wand_finish")

#Returning with their own wand 
elif mode == "old":
    whole_list = ["lantern_on", "knock_over", "music_box"]
    finish_action = "lantern_off"

keep_going = True

while(keep_going):
      #Read in a message
      data = arduino.readline()
      #print(data)
      message = data.decode()
      if len(message) > 1:
        print(message)
        print(type(message))
        if "FAST BACK" in message:
            if whole_list != []:
                item = whole_list.pop()
                message = {"message": item}
                print("Item", item)
                print("Whole List", whole_list)
                if item == "clock":
                    commander.publish(item, json.dumps(message))
                    play_sound("good_cuckoo")
                if item == "erratic_flowers":
                    commander.publish(item, json.dumps(message))
                if item == "knock_over":
                    commander.publish(item, json.dumps(message))
                if item == "lantern_on":
                    commander.publish(item, json.dumps(message))
                if item == "music_box":
                    commander.publish(item, json.dumps(message))
                if item == "shaking_box":
                    commander.publish(item, json.dumps(message))
                if item == "thunder":
                    play_sound("thunder")
                if item == "glass":
                    play_sound("glass")
            else:
                keep_going = False
                print(finish_action)
                message = {"message": finish_action}
                if finish_action == "lantern":
                    commander.publish(finish_action, json.dumps(message))
                    play_sound("wand_finish")
                if finish_action == "lantern_off":
                    commander.publish(finish_action, json.dumps(message))

            time.sleep(1.5)

