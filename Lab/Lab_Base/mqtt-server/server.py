
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json, uuid, random
from datetime import datetime
from elasticsearch import Elasticsearch
import time

local = False

if local:
    esHost = 'localhost'
    mqttHost = 'localhost'
else:
    esHost = "es01"
    mqttHost = 'mqtt'

es = Elasticsearch(host=esHost)
channelSubs="secret/#"
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(channelSubs)

def on_message(client, userdata, msg):
    try:
        msg = json.loads(msg.payload)
        msg["client_time"] = datetime.fromtimestamp(msg["client_time"])
        body = {"timestamp":datetime.utcnow(),"server_time":datetime.utcnow(),"device":"mqtt_server","message":msg}
        es.index(index="data", doc_type="_doc", body=body)
    except:
        pass
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttHost, 1883, 60)
client.loop_forever()
