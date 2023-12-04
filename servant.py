
import node_classes as nc
import json

connection_info = {
    #"mqtt_username":,
     #"mqtt_password":, 
     #"mqtt_url": "192.168.0.28", 
     "mqtt_url": "10.42.0.1",
     "mqtt_port": 1883

}

servant = nc.subscriber_node("servant_1", connection_info, "Hola")
servant.disconnect()


