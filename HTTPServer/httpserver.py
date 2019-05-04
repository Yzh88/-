#建立httpserver

from socket import *
from HTTPServer.config import *


class HTTPServer():
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.bind()

    def bind(self):
       self.sockfd.bind(ADDR)
       self.sockfd.listen(5)

    def start_sever(self):
        pass

