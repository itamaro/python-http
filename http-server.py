#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','image/png')
		self.end_headers()
		with open(curdir + sep + 'logo.png', 'rb') as f:
			self.wfile.write(f.read())

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port' , PORT_NUMBER)
	server.serve_forever()

except KeyboardInterrupt:
	server.server_close()
	print('Stopping server')
