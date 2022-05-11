from http.server import HTTPServer , SimpleHTTPRequestHandler
import base64

HOST = "127.0.0.3"
PORT = 8080

class MyServer(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        username = "admin"
        password = "admin"
        self._auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Test"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.headers.get("Authorization") == None:
            self.do_AUTHHEAD()
            self.wfile.write(b"no auth header received")
        elif self.headers.get("Authorization") == "Basic " + self._auth:
            self.send_response(200)
            self.send_header("Content-type" , "text/html")
            self.end_headers()
            # use below line if intention is to list files in current directory
            #SimpleHTTPRequestHandler.do_GET(self)
            # otherwise use below approach to display text
            self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>" , "utf-8"))
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.get("Authorization").encode())
            self.wfile.write(b"not authenticated")


server = HTTPServer( (HOST , PORT) , MyServer)
print("My Server has started ...")
server.serve_forever()
server.serve_close()
print("My is closed now ...")