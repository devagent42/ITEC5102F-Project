import requests
import uuid
from datetime import datetime
import time
from elasticsearch import Elasticsearch

now = datetime.utcnow()
ID = uuid.uuid4()
ID = str(ID).replace('-', '')

local = True

if local:
    esHost = 'localhost'
    httpHost = 'localhost'
else:
    esHost = "es01"
    httpHost = 'http'

es = Elasticsearch(host=esHost)

while True:
    response = requests.post('http://'+httpHost+':5000/process_data',
                            json={"type": "secret", "secret": str(ID), "client_time": str(now.isoformat()),
                                  "device": "http_client",
                                  "client_ID": str(ID)})

    print("Status code: ", response.status_code)
    secret = {"timestamp":datetime.utcnow(),"type": "secret", "secret": str(ID), "client_time": now, "device": "http_client", "client_ID": str(ID)}
    es.index(index="data", doc_type="_doc", body=secret)
    time.sleep(2)
