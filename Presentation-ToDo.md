# Presentation Notes

# Slides
1. Title
1. Introduction *Jeff*
1. Stages *Jeff*
1. Stage 1 *Jeff*
1. HTTP Client and Server
  1. see slides
  1. Client automatically sends a POST request every 2 seconds
  1. Sends a POST request to host 'http' on port 5000 at location /process_data
  1. Server listens on port 5000
  1. Both sends a copy of the sent/recieved message to the Elasticsearch instance.
1. MQTT Client and Server
  1. Client publishes "secret" to a predefined topic.
  1. Server subscribes to a generic wildcard topic that all clients would publish to
  1. Client sends message on a topic to a broker
  1. Server subsribes to a topic on the broker
  1. Broker not in scope of this project
  1. Copy of sent/recieved messages sent to the Elasticsearch instance
1. Backend Services
  1. see slices
  1. Standard Elasticsearch configuration
  1. Kibana used to visualize the data
  1. Kibana saved objects are available to replicate this project
  1. Multiple dashboards have been created to help with the data processing
1. Backend Services
  1. MQTT broker 1. not in scope of this project
  1. Used as "SaaS" type setup where the broker is just there to relay messages
  1. Standard Mosquitto setup
1. Stage 2 *Fahmida*
1. Base Lab
  1. Docker containers
  1. Server/Client implementation
  1. Uses http
  1. No SSL/security/authentication
  1. Written in python
  1. Client uses the requests library
    1. Sends a POST request to "http" on port 5000 to /process_data
    1. Sends copy of message to Elasticsearch with timestamp
  1. Server uses Flask
    1. Listens on port 5000
    1. Accepts POST requests on port 5000 at /process_data
    1. Sends a copy of messages to Elasticsearch with timestamp
1. Stunnel Implementation
  1. Docker containers
  1. Transparent proxy implementation
    1. Redirect DNS to the "bottom" container so no changes are required in the clients
  1. Uses a PSK to authenticate/initiate proxy tunnels
  1. Negotiates a TLSv1.3 connection, actual algorithm out of scope of this project. It's "secure"
  1. HTTP:
    1. Client proxy container listens on port 5000, forwards all requests to port port 9000 on to the "top" HTTP proxy container
    1. Server proxy container forwards all requests from the bottom contianer to the HTTP server on port 5000
    1. No changes were made to the client/server
  1. MQTT:
    1. Bottom proxy container listens on port 1883, forwards all requests to port 9001 on to the "top" MQTT proxy container.
    1. Different ports were used to simplify the container setup (same config for both HTTP and MQTT)
    1. Top "client" proxy container forwards all request from the bottom container to the broker on port 1883
    1. No changes were made to the client/server
    1. Broker out of scope of this project
    1. Uses a PSK to authenticate/initiate proxy tunnels
    1. Negotiates a TLSv1.3 connection, actual algorithm is out of scope of this project. It's "secure"
1. Wireguard Implementation
1. Shadowsocks Implementation
1. Stage 3 *Georges*
1. Results Base
1. Results Base - Wireshark
1. Results Shadowsocks
1. Results Shadowsocks - Wireshark
1. Results Wireguard
1. Results Wireguard - Wireshark
1. Results stunnel
1. Results stunnel - Wireshark
1. Analysis
