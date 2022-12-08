#Reused some code from vineheart project 
#Help from the documentation here: https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#multiple
import paho.mqtt.client as paho
from paho import mqtt
import time

#connection info - dictionary with fields:
#"mqtt_username", "mqtt_password", "mqtt_url", "mqtt_port"
#message - payload should also be a dictionary with relevant fields!


def action_handler(client, userdata, message):
    print(message.topic)
    print(message.payload)
    #Use some kind of configuration to figure out what should go where to route messages and stuff. 
    topic_list = message.topic.split('/')
    print(topic_list)


class command_node:
    def __init__(self, client_id, connection_info):
        #self.client = paho.Client(client_id=client_id, protocol=paho.MQTTv5)
        self.client = paho.Client(client_id=client_id)
        if "mqtt_username" in connection_info and "mqtt_password" in connection_info:
            self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
            self.client.username_pw_set(connection_info["mqtt_username"], connection_info["mqtt_password"])
        connection = self.client.connect(connection_info["mqtt_url"], port=connection_info["mqtt_port"])
        self.client.loop_start()

    def publish(self, topic, message):
        return_code = self.client.publish(topic, message, qos=1)
        #time.sleep(1)
        print("MSGPUB RC")
        print(return_code.rc)
        if return_code.rc != paho.MQTT_ERR_SUCCESS:
            print("Could not publish message on: ", topic)
            return False
        return True

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()


class subscriber_node:
    def __init__(self, client_id, connection_info, topic, callback_function=None):
        user_data = {"topic": topic}
        #self.client = paho.Client(client_id=client_id, protocol=paho.MQTTv5, userdata=user_data)
        self.client = paho.Client(client_id=client_id, userdata=user_data)

        if "mqtt_username" in connection_info and "mqtt_password" in connection_info:
            client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
            client.username_pw_set(connection_info["mqtt_username"], connection_info["mqtt_password"])
        self.client.on_connect = self.on_connect
        if callback_function == None:
            self.client.message_callback_add(topic, action_handler)
        else:
            self.client.message_callback_add(topic, callback_function)
        #self.client.connect(connection_info["mqtt_url"], port=connection_info["mqtt_port"], clean_start=False)
        self.client.connect(connection_info["mqtt_url"], port=connection_info["mqtt_port"])

        self.client.loop_forever()


    def on_connect(self, client, userdata, flags, reasonCode, properties=None):
        if reasonCode==0:
            print(userdata["topic"], "connected, return code:", reasonCode)
            self.client.subscribe(userdata["topic"], qos=1)
        else:
            print(userdata["topic"], "bad Connection, return code:", reasonCode)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
