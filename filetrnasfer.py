import http
import socketserver
PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as https:
    print("Http server is running on PORT ", PORT)
    #http.serve_forever()
