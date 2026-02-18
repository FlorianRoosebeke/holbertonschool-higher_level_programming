#!/usr/bin/python3
"""Simple HTTP server exposing a few JSON/text endpoints."""

import http.server
import socketserver
import json


class Handler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler for a small JSON/text API."""

    def do_GET(self):
        """Serve the API responses for known endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data_set = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data_set).encode("utf8"))

        elif self.path == "/info":
            data_info = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data_info).encode("utf8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
