#!/usr/bin/env python3

import http.server


class Handler(http.server.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)

    def do_GET(self):
        self.send_response(200)
        print(self.requestline)
        print(self.headers)
        print("==================")
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        print(self.requestline)
        print(self.headers)
        print(self.rfile.read())
        print("=================")
        self.end_headers()


def main():
    httpd = http.server.ThreadingHTTPServer(('0.0.0.0', 3128),
                                            Handler)
    print("Hit me (3128)!")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Good bye, and thanks for all the fish!")


if __name__ == '__main__':
    main()
