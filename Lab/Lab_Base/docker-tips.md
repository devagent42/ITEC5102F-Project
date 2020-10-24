# Some docker tips:
- Startup the lab: `docker-compose up --build`
- Stop the lab: `control +c` and `docker-compose down`
- Stop the lab and remove the storage: `control +c` and `docker-compose down -v`
- List the docker networks: `docker inspect network ls`
- Inspect the docker network: `docker inspect network some_network`
- Cleanup Docker: `docker system prune -a`
