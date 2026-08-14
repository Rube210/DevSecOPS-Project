from http.server import HTTPServer, SimpleHTTPRequestHandler

ip = "0.0.0.0"
port = 8000
server_address = (ip, port)

api = HTTPServer(
    server_address=server_address,
    RequestHandlerClass=SimpleHTTPRequestHandler,
)

print("Listening for HTTP requests...")
api.serve_forever()
