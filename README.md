# special_effects
A server for computer-to-pi special effects.

We use this to create a magic show 

I made this a while ago. The code is very bad. But it works for the very specific purpose it was built for. 

[GO HERE TO SET UP THE SPECIFIC SPECIAL EFFECTS SYSTEM FOR THE WAND SHOW](docs/wand_show_setup.md)

![wands](docs/pics/wands.jpg)


## How does this work? 
You need:
- Any untracked .py file named "myself"
- The node classes file 
- A topic action mapping .py file (tracked)

## Untracked myself file

    myself = {
        "name": "your_name"
    } 

    Put your name as "commander", if you are the commander. Otherwise it doesn't matter so much. 

This helps the topic action mapping know what to do.

You could put any other config info in here, if you wanted to.

This is more for servant nodes in terms of usefulness. 

## Node Classes File 
### command_node
- init
    - Receives client_id (your name)
    - Receives connection info (for MQTT)
    - connects to MQTT
- publish
    - receives topic and message
    - publishes message on topic 
- disconnect
    - disconnect client 

### subscriber_node
- init
    - receives client_id, connection_info, topic, optional callback function
    - sets its own name 
    - creates a library variable based on its topic action mapping 
    - uses import to import the library (library follows certain specification)
    - connects subscriber
    - adds action_handler default callback if no callback specified 
    - This default handler will pass the message variable to the "action" function of imported action library when receiving a topic 
- on_connect
    - subsribes to the topic with qos1
- on_disconnect
    - disconnects from MQTT broker 

### create_commander, create_servant
- creates these functions by passing client_id, connection_info, and topic (if servant)

## A topic action mapping .py file (tracked)
Contains a .py with a dictionary. The object imported is called "mapping", and is a dict with:
    mapping = {
        "servant_name": 
            "topic": "python_file_name"
        }

Where the topic is sent to the servant via MQTT. The servant has imported the "python_file_name" as their action library, and will execute the "action" function in that file. 

For example: 

    mapping = {
    "servant_1": {
        "Hola": "greet_action",
        "Hello": "other_action",
        "erratic_flowers": "erratic_flowers",
        "shaking_box": "shaking_box",
        "lantern": "lantern",
        "lantern_on": "lantern_on",
        "lantern_off": "lantern_off",
        "knock_over": "knock_over"
    },
    "servant_2": {
        "clock": "clock",
        "music_box": "music_box"
    }
}

As I am sure you have noticed, there were probably MANY more efficient ways of doing this. Like just providing the topic and an action. It has something to do with a funky erring import chain. I digress. I wish this was better. 

## special_effect.py
NOTE - I am pretty sure this only works for the servant. The commander is different. 

If you are the commander, tries to import a specific library and execute it. It won't work, so don't use this code file as your commander. 

IF you are servant, though, it will import your specific topic action mapping. 

For every topic/mapping, it will create a new scheduled thread with a new servant node (node_commander.create_servant())

Like the commander, it will need CORRECT MQTT connection info to work. 

It will busy wait while the threads run forever until service is terminated

## special_effect.service
To create the correct service so you can start the pi and just have it run 

Your pi environment will need to look like this: 

```bash
    [Unit]
    Description=Special Effect Service 
    After=multi-user.target

    [Service]
    Type=simple
    WorkingDirectory=/home/pi/special_effects
    ExecStart=/usr/bin/python3 /home/pi/special_effects/special_effect.py
    User=pi

    [Install]
    WantedBy=multi-user.target
```

To copy, run: 

    sudo cp special_effect.service /lib/systemd/system/special_effect.service
    sudo systemctl daemon-reload
    sudo systemctl enable special_effect.service
    sudo systemctl start special_effect.service
    sudo systemctl status special_effect.service

I definitely recommend you test this first. 

## Configuring Your System
You need
- An MQTT broker installed somewhere. I use mosquitto. My mosquitto.conf file looks like:

```bash
    pid_file /var/run/mosquitto.pid

    persistence true
    persistence_location /var/lib/mosquitto/

    log_dest file /var/log/mosquitto/mosquitto.log

    include_dir /etc/mosquitto/conf.d

    listener 1883
    allow_anonymous true
```

Make sure mosquitto is running:

    sudo systemctl status mosquitto
    sudo systemctl start mosquitto 

May first need to run:

    sudo systemctl enable mosquitto

- I would highly recommend a plug-in hotspot so you don't have to reconfigure IP addresses. Otherwise, you could use a cloud MQTT broker. The plug-in one doesn't require access to the broader internet, which is really nice 
I use a plug in network with a static ip. 
- Edge nodes to conduct effects that can run python (I use pis)
- Commander node that sends messages (I use my laptop). You could also probably use a pi for this. 

### Configuring your Commander Node
- need mqtt connection info and name to create commander (nc.create_commander)
- some sort of sequence to send messages to your servant nodes 
commander.publish(topic, message)

### Configuring your Servant Node 
- just need myself.py and a bunch of code files with executables that can be conducted by the edge node. Make sure you have installed things correctly. 







