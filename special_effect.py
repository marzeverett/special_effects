
#Make sure you start mosquitto by typing "mosquitto!" - in your terminal. 

import node_classes as nc
import myself
import topic_action_mapping as tam
import json

connection_info = {
    #"mqtt_username":,
     #"mqtt_password":, 
     #"mqtt_url": "192.168.1.150", 
     "mqtt_url": "10.42.0.1", 
     "mqtt_port": 1883

}

#External libraries - from SkyWeather2 System primarily 
#Background Scheduler stuff 
from apscheduler.schedulers.background import BackgroundScheduler
import apscheduler.events
import os
import sys 
import time 

def ap_my_listener(event):
        if event.exception:
            print(event.exception)
            print(event.traceback)
            print(event.job_id)
            print(event)
            sys.stdout.flush()
            #The following code line will restart the program - note that this could lead to a continuous sequence of crashes forevermore
            #But if it's an odd, one-off crash, it should restart the program. 
            #Need to decide if this is how to handle failure or not
            #Probably better to alert another watchdog. 
            #os.execv(sys.executable, ['python3'] + [sys.argv[0]])

#Get your own instance
me = myself.myself["name"]

if me == "commander": 
    message = {"Hola": "Como estas?"}
    #commander = nc.command_node("commander", connection_info)
    commander = nc.create_commander(me, connection_info)

    #Listen for triggers and choose based on them. Probably going to be pyserial. 

    #Might also pass commander in as an argument, depending. 
    if "mode" in list(myself.myself.keys()):
        mode  = myself.myself["mode"]
        if mode == "harry_potter":
            import harry_potter
            harry_potter.harry_potter(commander)

    #commander.publish("Hola", json.dumps(message))
    #commander.publish("Hello", json.dumps(message))
    #commander.disconnect()

    # Main Loop
        #while True:
            #time.sleep(1.0)

else:
    try: 
        topic_dict = tam.mapping[me]
        thread_config = {'apscheduler.executors.default': {'class': 'apscheduler.executors.pool:ThreadPoolExecutor', 'max_workers': '30'}}
        scheduler = BackgroundScheduler(thread_config)
        scheduler.add_listener(ap_my_listener, apscheduler.events.EVENT_JOB_ERROR)

        for topic in list(topic_dict.keys()):
            job_id = str(me)+str(topic)
            scheduler.add_job(nc.create_servant, id=job_id, args=[job_id, connection_info, topic])
   
        scheduler.start()
        print ("-----------------")
        print ("Scheduled Jobs")
        print ("-----------------")
        scheduler.print_jobs()
        print ("-----------------")

        # Main Loop
        while True:
            time.sleep(1.0)

    except Exception as e:
        print(e)
        print("Could not instantiate node for: ", me)
    

    




    
