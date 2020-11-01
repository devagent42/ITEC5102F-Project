from flask import Flask
from flask import Request
from datetime import datetime
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

@app.route("/process_data", methods=["POST"])
def process_data():
    data = Request.get_json(force=True)
    
    type = data['type'].format(str())
    secret = data['data]'].format(str())
    client_time = data['client_time'].format(datetime(), time)
    device = data['device'].format(str())
    client_ID = data['client_ID'].format(str())
    
    
    return '''
           The type is: {}
           The secret is: {}
           The client time is: {}
           The device is: {}
           The client ID is: {} '''

if __name__ == "__main__":
    app.run()
        
