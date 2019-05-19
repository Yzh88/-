from http_server.bll import *

http = HTTPServer(ADDR)
http.serve_forever()
