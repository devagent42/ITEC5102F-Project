FROM python:3
RUN pip install paho-mqtt elasticsearch
COPY mqttToElasticSearch.py /
CMD [ "python", "/mqttToElasticSearch.py" ]
