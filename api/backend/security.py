import base64
import hashlib


def hashup(data):
    sha256 = hashlib.sha256(data.encode('utf-8')).digest()
    return str(base64.b64encode(sha256), encoding='utf-8')
