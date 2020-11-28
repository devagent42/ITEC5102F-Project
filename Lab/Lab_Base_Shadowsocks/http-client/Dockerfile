FROM python:3.8
RUN pip install requests elasticsearch pysocks
COPY client.py /
CMD [ "python", "/client.py" ]
