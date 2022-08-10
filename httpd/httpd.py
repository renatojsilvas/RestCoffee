from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):        
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        body = "<h1>O Servidor tá ON!</h1>"
        self.wfile.write(body.encode('utf-8', 'replace'))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='0.0.0.0')
    parser.add_argument('--port', '-p', default=8000, type=int)
    args = parser.parse_args()

    with HTTPServer((args.bind, args.port), MyHTTPHandler) as httpd:
        host, port = httpd.socket.getsockname()[:2]
        url_host = f'[{host}]' if ':' in host else host

        print(
            f'Serving HTTP on {host} port {port} '
            f'(http://{url_host}:{port}/) ..'
        )

        try:        
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nTchau!')
            sys.exit(0)

    
