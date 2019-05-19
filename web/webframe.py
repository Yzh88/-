import json
from select import select
from socket import *

from config.web_config import *
# from web.urls import *

frame_address = (frame_ip, frame_port)
# 应用类，将功能封装在类中
class Application(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind(frame_address)

    def start(self):
        self.sockfd.listen(5)
        print('Listen the port:%d' % frame_port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        # select IO多路复用
        while True:
            rs, ws, xs = select(rlist, wlist, xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    rlist.append(connfd)
                else:
                    self.handle(r)
                    rlist.remove(r)

    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)

        # request = {'method': 'GET', 'info': '/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass

        # 将数据发送给Http_Server
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

        #   测试
        # print(request.decode(), 222)
        # dict = {'status':'200','data':'OK'}
        # connfd.send(json.dumps(dict).encode())

    def get_html(self, info):
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

    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': 'sorry,...'}


if __name__ == '__main__':
    app = Application()
    app.start()
