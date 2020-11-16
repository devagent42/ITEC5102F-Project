
http-server0:
  build: ./http-server/
  restart: always
  depends_on:
    - es01
  networks:
    http_server_proxy0:
      aliases:
        - http
http-client0:
  build: ./http-client/
  restart: always
  depends_on:
    - es01
  networks:
    http_client_proxy0:
http-server-proxy0:
  build: ./http-server/
  restart: always
  depends_on:
    - es01
  networks:
    proxy0:
      aliases:
        - server
    http_server_proxy0:
      aliases:
        - http
http-client-proxy0:
  build: ./http-client/
  restart: always
  depends_on:
    - es01
  networks:
    proxy0:
      aliases:
        - client
    http_client_proxy0:
      aliases:
        - http
