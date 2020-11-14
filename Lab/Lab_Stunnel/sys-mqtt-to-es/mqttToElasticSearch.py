#this code is developed by Matthew Field http://www.smart-factory.net
#distributed under GNU public license https://www.gnu.org/licenses/gpl.txt

#Modified by Georges Ankenmann (100935237) to fullfill the Requirements of the ITEC5102 project.
#OEM version here: https://github.com/devagent42/mqtt-elasticSearch

#This gets system stats and feeds it into ElastiSearch

mqttServer="mqtt"
mqttPort=1883

channelSubs="$SYS/#"

import paho.mqtt.client as mqtt
from datetime import datetime
from elasticsearch import Elasticsearch
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(channelSubs)

def on_message(client, userdata, msg):
    try:
        es.index(index="sys-data", doc_type="_doc", body={"topic" : msg.topic, "dataFloat" : float(msg.payload), "timestamp": datetime.utcnow()})
    except:
        es.index(index="sys-data", doc_type="_doc", body={"topic" : msg.topic, "dataString" : str(msg.payload, 'utf-8'), "timestamp": datetime.utcnow()})
es = Elasticsearch(host='es01')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer,mqttPort, 60)
client.loop_forever()
