import requests
import uuid
from datetime import datetime
import time
from elasticsearch import Elasticsearch

now = datetime.utcnow()
ID = uuid.uuid4()
ID = str(ID).replace('-', '')

# es = Elasticsearch(host='http://127.0.0.1:5000')
while True:
    response = requests.get('http://127.0.0.1:5000',
                            json={"type": "secret", "secret": str(ID), "client_time": now.timestamp(),
                                  "device": "http_client",
                                  "client_ID": str(ID)})

    print("Status code: ", response.status_code)
    secret = {"type": "secret", "secret": str(ID), "client_time": now.timestamp(), "device": "http_client", "client_ID": str(ID)}
    # es.index(index="client-data", doc_type="_doc", body=secret)
    time.sleep(2)


