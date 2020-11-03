from flask import Flask
from flask import request
from datetime import datetime
import json
import time
import uuid
from elasticsearch import Elasticsearch

ID = uuid.uuid4()
ID = str(ID).replace('-','')

local = False

if local:
    esHost = 'localhost'
    httpHost = 'localhost'
else:
    esHost = "es01"
    httpHost = 'http'

es = Elasticsearch(host=esHost)

app = Flask(__name__)

##############################
########## fix this ##########
# request.post(THE URL HERE)
# JSON = JSON file

while True:
    now = datetime.utcnow()
    secret = {"type": "secret", "secret": str(ID), "client_time": now.timestamp(), "device": "http_client",
              "client_ID": str(ID)}
    # Something here to publish secret
    # print (json.dumps(secret))
    # Might need this, might not...
    # secret = {"type": "secret", "secret": str(ID), "client_time": now, "device": "http_client",
    #           "client_ID": str(ID)}
    es.index(index="client-data", doc_type="_doc", body=secret)
    time.sleep(2)