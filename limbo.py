"""
Layer 1: Limbo
"""

import hashlib
import time


def sha256(s):
    return hashlib.sha256(s).hexdigest()


class Handler:
    def __init__(self):
        self.html = open('limbo.html', 'r').read()
        self.key = sha256(str(time.clock()))  # Should change once every hour
        self.custom_headers = False
        with open('limbo.key', 'w') as f:
            f.write(self.key)

    def handle(self, handler, get_vars, post_vars):
        if 'answer' in post_vars:
            if sha256(post_vars['answer'][0]) == '4d56158eb590bd5a1b48042740f88bdb0d80c3839c770e77fb91805ba8f3935a':
                handler.wfile.write(self.html.replace('{{ answer }}', self.key))
            else:
                handler.wfile.write(self.html.replace('{{ answer }}', 'Fail!'))
        else:
            handler.wfile.write(self.html.replace('{{ answer }}', ''))
