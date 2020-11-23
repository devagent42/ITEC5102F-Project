FROM ubuntu:focal
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y update
RUN apt-get -y install wireguard iputils-ping curl wget iproute2 mosquitto-clients
COPY ./nginx.list /etc/apt/sources.list.d/nginx.list
RUN wget https://nginx.org/keys/nginx_signing.key -O /tmp/nginx.key
RUN apt-key add /tmp/nginx.key
RUN apt-get -y update
RUN apt-get -y install nginx
