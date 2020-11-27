import requests
import uuid
from datetime import datetime
import time
from elasticsearch import Elasticsearch

ID = uuid.uuid4()
ID = str(ID).replace('-', '')

local = False

if local:
    esHost = 'localhost'
    httpHost = 'localhost'
else:
    esHost = "es01"
    httpHost = '172.16.238.10'

proxies = {'http': "socks5://proxy:7777"}


es = Elasticsearch(host=esHost)

while True:
    now = datetime.utcnow()
    secret_passwrd = uuid.uuid4()
    response = requests.post('http://'+httpHost+':5000/process_data',
                            json={"type": "secret", "secret": str(secret_passwrd), "client_time": str(now.isoformat()),
                                  "device": "http_client",
                                  "client_ID": str(ID)},proxies=proxies)

    #print("Status code: ", response.status_code)
    secret = {"timestamp":datetime.utcnow(),"type": "secret", "secret": str(secret_passwrd), "client_time": now, "device": "http_client", "client_ID": str(ID)}
    es.index(index="data", doc_type="_doc", body=secret)
    time.sleep(2)
