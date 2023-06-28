#!/usr/bin/python
# -*- encoding: utf-8 -*-

from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

# 具备并发处理能力的TCP server
# from socketserver import ThreadingTCPServer
# ...
# if __name__ == '__main__':
#     serv = ThreadingTCPServer(('', 20000), EchoHandler)
#     serv.serve_forever()

# 考虑上述具备并发能力的服务可能被广泛攻击
# ...
# if __name__ == '__main__':
#     from threading import Thread
#     NWORKERS = 16
#     serv = TCPServer(('', 20000), EchoHandler)
#     for n in range(NWORKERS):
#         t = Thread(target=serv.serve_forever)
#         t.daemon = True
#         t.start()
#     serv.serve_forever()
