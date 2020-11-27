from flask import Flask
from flask import request
from datetime import datetime
import json
import time
from elasticsearch import Elasticsearch
import ntplib
from time import ctime

local = False

if local:
    esHost = 'localhost'
    httpHost = 'localhost'
else:
    esHost = "es01"
    httpHost = 'http'

es = Elasticsearch(host=esHost)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Demo Flask & Docker application is up and running!"

@app.route("/process_data", methods=["POST"])
def process_data():
    data = request.data#Request.get_json(force=True)
    data = data.decode("utf-8")
    data = json.loads(data)
    data["client_time"] = datetime.fromisoformat(str(data["client_time"]))
    #print (type(data["client_time"]))
    now = datetime.utcnow()

    body = {"timestamp":now,"server_time":now,"device":"http_server","message":data}
    es.index(index="data", doc_type="_doc", body=body)

    return "Well received!!!"


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
