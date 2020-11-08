from flask import Flask
from flask import request
from datetime import datetime
import json
import time
from elasticsearch import Elasticsearch

local = True

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
    data["client_time"] = datetime.fromtimestamp(data["client_time"])
    print (data)
    body = {"server_time":datetime.utcnow(),"device":"http_server","message":data}
    es.index(index="server-data", doc_type="_doc", body=body)

    return "Well received!!!"


if __name__ == '__main__':
    app.run()
