import time
import os
from http.server import BaseHTTPRequestHandler

from urllib.parse import parse_qs

from commands.main import commands

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.path = '/index.html'
    try:
      split_path = os.path.splitext(self.path)
      request_extension = split_path[1]
      print(self.path[1:])
      if request_extension != ".py":
        f = open(self.path[1:]).read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(f, 'utf-8'))
      else:
        f = "File not found"
        self.send_error(404,f)
    except:
      f = "File not found"
      self.send_error(404,f)
  def parse_POST(self):
    length = int(self.headers['content-length'])
    postvars = parse_qs(self.rfile.read(length))
    return postvars

  def do_POST(self):
    self.send_response(200)
    self.end_headers()
    postvars = self.parse_POST()
    print(postvars)
    command = postvars.get(b'command', None)
    if commands[command[0].decode("utf8")]:
      commands[command[0].decode("utf8")]()
      pass

    # self.send_response(200)
    # self.send_header("Content-type", "text/html")
    # self.end_headers()
    # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
    # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
    # self.wfile.write(bytes("<body>", "utf-8"))
    # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
    # self.wfile.write(bytes("</body></html>", "utf-8"))
    # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
