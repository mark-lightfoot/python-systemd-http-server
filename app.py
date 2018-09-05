#!/usr/bin/python
import http.server
import SocketServer

PORT = 9000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
