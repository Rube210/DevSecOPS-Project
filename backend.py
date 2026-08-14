from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Serve files from the working directory (where Dockerfile sets WORKDIR).
os.chdir(os.path.dirname(__file__) or "./")

class Handler(SimpleHTTPRequestHandler):
    pass

if __name__ == "__main__":
    addr = ("0.0.0.0", 8080)
    httpd = HTTPServer(addr, Handler)
    print(f"Serving on {addr[0]}:{addr[1]}")
    httpd.serve_forever()
