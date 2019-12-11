import urllib

from flask import request
from flask_caching import Cache

cache = Cache()


# def cache_key():
#     args = request.args
#     key = request.path + '?' + urllib.urlencode([
#         (k, v) for k in sorted(args) for v in sorted(args.getlist(k))
#     ])
#     return key
