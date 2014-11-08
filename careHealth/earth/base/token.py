import uuid
import hashlib


def short_token():
    raw_token = hashlib.sha1(str(uuid.uuid4()))
    token = raw_token.hexdigest()[::2]
    return token


def long_token():
    raw_token = hashlib.sha1(str(uuid.uuid4()))
    token = raw_token.hexdigest()
    return token
