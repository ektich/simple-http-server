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


def main():
    httpd = http.server.ThreadingHTTPServer(('0.0.0.0', 8080),
                                            Handler)
    print("Hit me!")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Good bye, and thanks for all the fish!")


if __name__ == '__main__':
    main()
