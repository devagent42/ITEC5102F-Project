from elasticsearch import Elasticsearch
import docker
import time
from datetime import datetime
import uuid
import json
import requests

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

local = False

if local:
    esHost = 'localhost'
else:
    esHost = "es01"

es = Elasticsearch(host=esHost)


# this is taken directly from docker client:
#   https://github.com/docker/docker/blob/28a7577a029780e4533faf3d057ec9f6c7a10948/api/client/stats.go#L309
def calculate_cpu_percent(d):
    cpu_count = len(d["cpu_stats"]["cpu_usage"]["percpu_usage"])
    cpu_percent = 0.0
    cpu_delta = float(d["cpu_stats"]["cpu_usage"]["total_usage"]) - \
                float(d["precpu_stats"]["cpu_usage"]["total_usage"])
    system_delta = float(d["cpu_stats"]["system_cpu_usage"]) - \
                   float(d["precpu_stats"]["system_cpu_usage"])
    if system_delta > 0.0:
        cpu_percent = cpu_delta / system_delta * 100.0 * cpu_count
    return cpu_percent



while True:
#datetime.fromtimestamp(getTime())#.strftime('%Y-%m-%d %H:%M:%S.%f'))
    for container in client.containers.list():
        now = datetime.utcnow()
        stats = container.stats(stream=False)
        #print (json.dumps(stats))
        memory = (stats["memory_stats"]["usage"]/stats["memory_stats"]["limit"])*100
        name = (stats["name"]).strip("/")
        network_stats = stats["networks"]
        real_stats = {"cores":stats["cpu_stats"]["online_cpus"],"cpu_usage":calculate_cpu_percent(stats),"name":name,"memory_usage":memory,"network_stats":network_stats}
        msg = {"id":uuid.uuid4(),"timestamp":now,"stats":real_stats}
        #print (msg)
        es.index(index="stats", doc_type="_doc", body=msg)
    time.sleep(5)
