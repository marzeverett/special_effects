
import node_classes as nc
import json

connection_info = {
    #"mqtt_username":,
     #"mqtt_password":, 
     "mqtt_url": "192.168.0.28", 
     "mqtt_port": 1883

}


message = {"Hola": "Como estas?"}
servant = nc.subscriber_node("servant", connection_info, "Hola")
servant.disconnect()


