from http.server import HTTPServer
from clients.Webserver import MyServer

hostName = "localhost"
serverPort = 8080

if __name__ == '__main__':
  webServer = HTTPServer((hostName, serverPort), MyServer)
  print("Server started http://%s:%s" % (hostName, serverPort))

  try:
      webServer.serve_forever()
  except KeyboardInterrupt:
      pass

  webServer.server_close()
  print("Server stopped.")
