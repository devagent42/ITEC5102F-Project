from flask import Flask
from flask import request
from datetime import datetime
import json
import time
from elasticsearch import Elasticsearch

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
    print (data)
    #type = data['type'].format(str())
    #secret = data['data]'].format(str())
    #client_time = data['client_time'].format(datetime(), time)
    #device = data['device'].format(str())
    #client_ID = data['client_ID'].format(str())


    return "Well received!!!"

def on_message(client, userdata, data):
    try:
        msg = json.loads(msg.payload)
        msg["client_time"] = datetime.fromtimestamp(msg["client_time"])
        body = {"server_time":datetime.utcnow(),"device":"http_server","message":data}
        es.index(index="server-data", doc_type="_doc", body=body)
    except:
        pass
    
if __name__ == '__main__':
    app.run()
