# Some docker tips:
- Startup the lab: `docker-compose up --build`
- Stop the lab: `control +c` and `docker-compose down`
- Stop the lab and remove the storage: `control +c` and `docker-compose down -v`
- List the docker networks: `docker inspect network ls`
- Inspect the docker network: `docker inspect network some_network`
- Cleanup Docker: `docker system prune -a`

# The docker file
```
FROM python:3
RUN pip install requests
COPY server.py /
CMD [ "python", "/server.py" ]
```
- First line contains the source image. This case python version 3
- Second line installs the required packages via PIP. Add what is required here.
- Third line copies the server python file to /
- Fourth runs the python file.
***NOTE*** You need an infinite loop in the python file otherwise it will exit.
