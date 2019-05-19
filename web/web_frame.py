import json
from select import select
from socket import *

from config.web_config import *


# from web.urls import *

# 应用类，将功能封装在类中
class Application(object):
    def __init__(self):
        self.sock_fd = socket()
        self.sock_fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sock_fd.bind(frame_address)

    def start(self):
        self.sock_fd.listen(5)
        print('Listen the port:%d' % frame_port)
        r_list = [self.sock_fd]
        w_list = []
        x_list = []
        # select IO多路复用
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
        request = json.loads(request)

        # request = {'method': 'GET', 'info': '/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            # else:
            #     response = self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass

        # 将数据发送给Http_Server
        response = json.dumps(response)
        conn_fd.send(response.encode())
        conn_fd.close()

        #   测试
        # print(request.decode(), 222)
        # dict = {'status':'200','data':'OK'}
        # conn_fd.send(json.dumps(dict).encode())

    @staticmethod
    def get_html(info):
        if info == '/':
            filename = STATIC_DIR + '/login.html'
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except Exception as e:
            print(e)
            f = open(STATIC_DIR + "/404.html")
            return {'status': '404', 'data': f.read()}
        else:
            return {'status': '200', 'data': fd.read()}

    # def get_data(self, info):
    #     for url, func in urls:
    #         if url == info:
    #             return {'status': '200', 'data': func()}
    #     return {'status': '404', 'data': 'sorry,...'}


if __name__ == '__main__':
    app = Application()
    app.start()
