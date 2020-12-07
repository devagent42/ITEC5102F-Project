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
    - Docker-compose script
    - Server/Client implementation
    - Uses http
    - No SSL/security/authentication
    - Written in python
    - HTTP
      - Client uses the requests library
        - Sends a POST request to "http" on port 5000 to /process_data
        - Sends copy of message to Elasticsearch with timestamp
      - Server uses Flask
        - Listens on port 5000
        - Accepts POST requests on port 5000 at /process_data
        - Sends a copy of messages to Elasticsearch with timestamp
    - MQTT
      - Client sends messages with a "secret" to the broker on a given topic
      - Server subscirbes to a wildcard topic that all clients send messages to
      - Written in python
      - Uses default ports (1883 for server)
      - Uses TCP
1. Stunnel Implementation
    - Docker containers
    - Docker-compose script
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
    - Docker containers
    - Docker-compose script
    - Transparent Proxy implementation
    - Secure implementation, acutal security not in scope of this project (asym curve25519 keysy)
    - Uses NGINX to forward HTTP/MQTT TCP sessions
      - Must convert a L7 to a L3
      - NGINX works at the application (L7)
      - Wireguard is at network (L3)
    - NGINX works because MQTT and HTTP are TCP, probably would not work for UDP, would need to test (out of scope of this projects)
    - HTTP
      - "Bottom" NGINX takes in anything on port 5000
      - Forwards it to the "top" NGINX on port 9000 via Wireguard
      - "Top" NGINX takes in anything on port 9000 and forwards it to the HTTP Server on port 5000
      - No changes were made to the HTTP client and server
      - Redirects DNS entries to remove the need change the client/server configuration
    - MQTT
      - "Bottom" NGINX takes in anything on port 1883
      - Forwards it to the "top" NGINX on port 9000 via Wireguard
      - "Top" NGINX takes in anthing on port 9000 and forwards it to the MQTT broker on port 1883
1. Shadowsocks Implementation
    - Docker containers
    - Docker-compose script
    - Transparent SOCKS5 Proxy implementation
    - Does not actually work, does not fulfill the project requirements of "no modifications" to the client/server
    - Had to modify HTTP client to use SOCKS5
    - HTTP client uses a SOCKS5 proxy setting to send data to the proxy, which is then forwarded to the HTTP server
    - HTTP data is secured
    - MQTT python library does not support SOCKS5, no working MQTT implementation for SOCKS5
    - Dependant on the application supporting SOCKS5
    - poly1305 and chacha20
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
    - Base scenario is hard to beat
    - Shadowsocks might be better in latency for HTTP, but it is not ideal as we had to modify the application
    - Wireguard
      - offers lowest average delta for latency for HTTP
      - Lowest maximum latency for MQTT
      - Lowest average CPU (???) - Possible problems here?
    - Stunnel
      - Lowest average for MQTT
      - Highest average for HTTP
    - Results make sense
      - MQTT a much lighter protocol
      - Wireguard is known to be fast
        - NGINX does little processing
    - For this experiment, MQTT is comprable via Wireguard and Stunnel, HTTP is significantly faster via Wireguard even with NGINX
