# -*- coding: utf-8 -*-
import BaseHTTPServer
import SocketServer


class TCPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        # TODO здесь маршрутизация
        print self.path
        print self.command
        self.end_headers()
        self.wfile.write("hello !")

    # def handle(self):
    #     response = 'NOT VALID REQUEST'
    #     data = self.request.recv(1024).strip()
    #     get_match = re.match('([A-Za-z]+) /([a-zA-Z0-9_\?=&-]+) HTTP', data)
    #     request_type = get_match.group(1)
    #     path, params = self.parse(get_match)
    #     if params:
    #         param = self.validate(params)
    #         if param:
    #             process = router.get(request_type, dict()).get(path, 'BAD REQUEST')
    #             response = process if isinstance(process, basestring) else process(param).run()
    #     self.request.sendall(response)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999
    server = BaseHTTPServer.HTTPServer((HOST, PORT), TCPHandler)
    try:
        print '***SERVICE RUN  127.0.0.1:9999'
        print '***PRESS CTRL+C TO EXIT'
        server.serve_forever()
    except:
        server.socket.close()
        print '***SERVICE STOP'
