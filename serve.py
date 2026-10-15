#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8081
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    # Try port 8081, fallback to 8082 if occupied
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"============================================================")
            print(f"  MS Applied Programming (Python) Live Server Running!")
            print(f"  URL: http://localhost:{PORT}")
            print(f"  Root: {DIRECTORY}")
            print(f"  Press Ctrl+C to terminate.")
            print(f"============================================================")
            httpd.serve_forever()
    except OSError:
        PORT = 8082
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"============================================================")
            print(f"  MS Applied Programming (Python) Live Server Running!")
            print(f"  URL: http://localhost:{PORT}")
            print(f"  Root: {DIRECTORY}")
            print(f"  Press Ctrl+C to terminate.")
            print(f"============================================================")
            httpd.serve_forever()
