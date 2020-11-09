
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json, uuid, random
from datetime import datetime
from elasticsearch import Elasticsearch
import time
ID = uuid.uuid4()
ID = str(ID).replace('-','')

local = False

if local:
    esHost = 'localhost'
    mqttHost = 'localhost'
else:
    esHost = "es01"
    mqttHost = 'mqtt'

es = Elasticsearch(host=esHost)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(mqttHost, 1883, 60)
while True:
    now = datetime.utcnow()
    secret = {"type":"secret","secret":str(uuid.uuid4()),"client_time":now.timestamp(),"device":"mqtt_client","client_ID":str(ID)}
    client.publish("secret/"+str(ID),json.dumps(secret))
    #print (json.dumps(secret))
    secret = {"timestamp":datetime.utcnow(),"type":"secret","secret":str(uuid.uuid4()),"client_time":now,"device":"mqtt_client","client_ID":str(ID)}
    es.index(index="data", doc_type="_doc", body=secret)
    time.sleep(2)
