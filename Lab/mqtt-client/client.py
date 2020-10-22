
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import os, json, uuid, random
from datetime import datetime
import time
ID = uuid.uuid4()
ID = str(ID).replace('-','')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish("client","I'm active! "+str(ID))
    #subscribe to something
    client.subscribe("ping")
#publish
def publish(channel,msg):
    client.publish(str(channel), str(msg))

def on_message(client, userdata, msg):
    do_something(msg.payload)

def on_publish(client,userdata,result):
    pass

def do_something(msg):
        print ("Doing something!")
        client.publish("pong","Pong from "+str(ID))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect("mqtt", 1883, 60)
client.loop_forever()
