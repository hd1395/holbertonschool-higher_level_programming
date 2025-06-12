import http.server
import socketserver
import json

PORT = 8000

class MyWebServer(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API.
    """

    def do_GET(self):
        """
        Handles GET requests based on the requested path.
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(response_data), "utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            response_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(bytes(json.dumps(response_data), "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", "utf-8"))

def run(server_class=http.server.HTTPServer, handler_class=MyWebServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
if __name__ == "__main__":
    run()
