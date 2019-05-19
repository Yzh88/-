from http_server.bll import *
from config.http_config import *

http = HTTPServer(ADDR)
http.serve_forever()
