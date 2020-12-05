# Presentation Notes

# Slides
1. Title
1. Introduction *Jeff*
1. Stages *Jeff*
1. Stage 1 *Jeff*
1. HTTP Client and Server
    - see slides
    - Client automatically sends a POST request every 2 seconds
    - Sends a POST request to host 'http' on port 5000 at location /process_data
    - Server listens on port 5000
    - Both sends a copy of the sent/recieved message to the Elasticsearch instance.
1. MQTT Client and Server
    - Client publishes "secret" to a predefined topic.
    - Server subscribes to a generic wildcard topic that all clients would publish to
    - Client sends message on a topic to a broker
    - Server subsribes to a topic on the broker
    - Broker not in scope of this project
    - Copy of sent/recieved messages sent to the Elasticsearch instance
1. Backend Services
    - see slices
    - Standard Elasticsearch configuration
    - Kibana used to visualize the data
    - Kibana saved objects are available to replicate this project
    - Multiple dashboards have been created to help with the data processing
1. Backend Services
    - MQTT broker   - not in scope of this project
    - Used as "SaaS" type setup where the broker is just there to relay messages
    - Standard Mosquitto setup
1. Stage 2 *Fahmida*
1. Base Lab
    - Docker containers
    - Server/Client implementation
    - Uses http
    - No SSL/security/authentication
    - Written in python
    - Client uses the requests library
      - Sends a POST request to "http" on port 5000 to /process_data
      - Sends copy of message to Elasticsearch with timestamp
    - Server uses Flask
      - Listens on port 5000
      - Accepts POST requests on port 5000 at /process_data
      - Sends a copy of messages to Elasticsearch with timestamp
1. Stunnel Implementation
    - Docker containers
    - Transparent proxy implementation
      - Redirect DNS to the "bottom" container so no changes are required in the clients
    - Uses a PSK to authenticate/initiate proxy tunnels
    - Negotiates a TLSv1.3 connection, actual algorithm out of scope of this project. It's "secure"
    - HTTP:
      - Client proxy container listens on port 5000, forwards all requests to port port 9000 on to the "top" HTTP proxy container
      - Server proxy container forwards all requests from the bottom contianer to the HTTP server on port 5000
      - No changes were made to the client/server
    - MQTT:
      - Bottom proxy container listens on port 1883, forwards all requests to port 9001 on to the "top" MQTT proxy container.
      - Different ports were used to simplify the container setup (same config for both HTTP and MQTT)
      - Top "client" proxy container forwards all request from the bottom container to the broker on port 1883
      - No changes were made to the client/server
      - Broker out of scope of this project
      - Uses a PSK to authenticate/initiate proxy tunnels
      - Negotiates a TLSv1.3 connection, actual algorithm is out of scope of this project. It's "secure"
1. Wireguard Implementation
1. Shadowsocks Implementation
1. Stage 3 *Georges*
1. Results Base
1. Results Base   - Wireshark
1. Results Shadowsocks
1. Results Shadowsocks   - Wireshark
1. Results Wireguard
1. Results Wireguard   - Wireshark
1. Results stunnel
1. Results stunnel   - Wireshark
1. Analysis
