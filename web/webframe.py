from socket import *
from config.web_config import *
from select import select
import json
from web.urls import *


class Application(object):
    def __init__(self):
        self.sock_fd = socket()
        self.sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sock_fd.bind(frame_address)

    def start(self):
        self.sock_fd.listen(5)
        print("listen the port %d" % frame_port)
        r_list = [self.sock_fd]
        w_list = []
        x_list = []
        # select IO多路复用监听请求
        while True:
            rs, ws, xs = select(r_list, w_list, x_list)
            for r in rs:
                if r is self.sock_fd:
                    conn_fd, addr = r.accept()
                    r_list.append(conn_fd)
                else:
                    self.handle(r)
                    r_list.remove(r)

    def handle(self, conn_fd):
        request = conn_fd.recv(1024).decode()
        request = json.loads(request)  # 请求字典
        # 　request==>{'method':'GET','info':'/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or \
                    request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass

        # 将数据发送给ｈｔｔｐｓｅｒｖｅｒ
        response = json.dumps(response)
        conn_fd.send(response.encode())
        conn_fd.close()

    # 　处理网页
    def get_html(self, info):
        if info == '/':
            filename = STATIC_DIR + "/login.html"
        else:
            filename = STATIC_DIR + info

        try:
            fd = open(filename)
        except:
            f = open(STATIC_DIR + "/main.html")
            return {'status': '404', 'data': f.read()}
        else:
            return {'status': '200', 'data': fd.read()}

    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': "Sorry...."}


if __name__ == "__main__":
    app = Application()
    app.start()
