"""
Layer 1: Limbo
"""

import hashlib
import time


def sha256(s):
    return hashlib.sha256(s).hexdigest()


class Handler:
    def __init__(self):
        self.html = open('lust.html', 'r').read()
        self.key = sha256(str(time.clock()))  # Should change once every hour
        self.custom_headers = False
        with open('lust.key', 'w') as f:
            f.write(self.key)

    def handle(self, handler, get_vars, post_vars):
        if 'key' in post_vars and 'answer' in post_vars:
            with open('limbo.key', 'r') as f:
                key = f.read().strip()
            if post_vars['key'][0] == key:
                if sha256(post_vars['answer'][0]) == '35602208e86ac7d6b3a63780a9538a9d1763a646d5b9f3930a0548e0983e0ca6':
                    handler.wfile.write(self.html.replace('{{ answer }}', self.key))
                else:
                    handler.wfile.write(self.html.replace('{{ answer }}', 'Wrong!'))
            else:
                handler.wfile.write(self.html.replace('{{ answer }}', 'Wrong!'))
        else:
            handler.wfile.write(self.html.replace('{{ answer }}', ''))
