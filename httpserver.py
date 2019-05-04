#建立httpserver

from socket import *
from HTTPServer.config import *


class HTTPServer():
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.bind(ADDR)
