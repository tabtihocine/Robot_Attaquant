
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class serverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir ="/home/oussama/TER/server/server/file.html"
        try:
                f = open(rootdir)

                self.send_response(200)

                self.send_header("Content-type", "text-html")
                self.end_headers()

                self.wfile.write(f.read())
                f.close()
                return
        except IOError:
            self.send_error(404, "file not found")
    
def run():  
  print('http server is starting...')   
  server_address = ('127.0.0.1', 12341)  
  httpd = HTTPServer(server_address, serverHandler)  
  print('http server is running...')  
  httpd.serve_forever()  

if __name__ == '__main__':  
  run()  
