"""
This class handles the requests for images
"""

import os.path


class Handler:
    def __init__(self):
        self.custom_headers = True

    def handle(self, handler, get_vars, post_vars):

        path = handler.path.replace('/images/', 'images/')
        path = os.path.abspath(path)
        print(path)
        if os.path.abspath('images/') not in path:  # No funny business
            handler.send_response(400)
            handler.end_headers()
        else:
            try:
                data = open(path, 'rb').read()
                handler.send_response(200)
                handler.send_header('Content-type', 'image/' + os.path.splitext(path)[1])
                handler.send_header('Content-Length', str(len(data)))
                handler.end_headers()
                handler.wfile.write(data)
            except IOError:
                handler.send_response(404)
                handler.end_headers()
