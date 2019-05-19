import json
import re
from socket import *
from threading import Thread
from config.web_config import *
import base64


# 和web建立连接
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))  # 连接 web_frame
    except Exception as e:
        print(e)
        return
    data = json.dumps(env)  # 将字典转化为json数据　发送
    s.send(data.encode())
    try:
        data = s.recv(4096 * 100).decode()
    except UnicodeDecodeError:
        data = s.recv(4096 * 100)
        return {"type": "image/jpeg", 'status': '200', 'data': data}
    else:
        return json.loads(data)  # 返回数据字典


# 封装http_server基本协议
class HTTPServer(object):
    def __init__(self, address):
        self.address = address
        self.ip = self.address[0]
        self.port = self.address[1]
        self.create_socket(self)
        self.bind()

    # 创建套接字
    @staticmethod
    def create_socket(self):
        self.sock_fd = socket()
        self.sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sock_fd.bind(self.address)

    def serve_forever(self):
        self.sock_fd.listen(5)
        print('Listen the port %d...' % self.port)
        while True:
            conn_fd, addr = self.sock_fd.accept()
            print('Connect from ', addr)
            client = Thread(target=self.handle, args=(conn_fd,))
            client.setDaemon(True)
            client.start()

    def handle(self, conn_fd):
        request = conn_fd.recv(4096).decode()
        print(request)
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'
        try:
            env = re.match(pattern, request).groupdict()
        except Exception as e:
            print(e)
            conn_fd.close()
            return
        else:
            print(env)
            data = connect_frame(env)
            if data:
                self.response(conn_fd, data)

    # 将数据整理为response格式发送给浏览器
    @staticmethod
    def response(conn_fd, data):
        # data {'status':200,'data':content}
        response_headers = ""
        con_type = data["type"]
        if data['status'] == '200':
            response_headers = 'HTTP/1.1 200 OK\r\n'
        elif data['status'] == '404':
            response_headers = 'HTTP/1.1 404 Not Found\r\n'
        elif data['status'] == '500':
            pass
        # 将数据发送给浏览器
        if con_type is None:
            return
        elif con_type == "image/jpeg":
            header_str = "content-type:" + con_type + "\r\n"
            response_headers += header_str
            response_headers += 'accept-range:bytes\r\n'
            response_headers += 'content-length:%d\r\n' % len(data["data"])
            response_headers += '\r\n'
            response_body = base64.encodebytes(data['data'])
            response_data = response_headers.encode() + response_body
        else:
            header_str = "content-type" + con_type + "\r\n"
            response_headers += header_str
            response_headers += '\r\n'
            response_body = data['data']
            response_data = response_headers + response_body
            response_data = response_data.encode()
        conn_fd.send(response_data)
        print(response_data.decode())
