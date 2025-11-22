
import node_classes as nc
import json

connection_info = {
    #"mqtt_username":,
     #"mqtt_password":, 
     #"mqtt_url": "192.168.0.28", 
     "mqtt_url": "10.42.0.1", 
     "mqtt_port": 1883

}


message = {"Hola": "Como estas?"}
commander = nc.command_node("commander", connection_info)
commander.publish("Hola", json.dumps(message))
commander.disconnect()


