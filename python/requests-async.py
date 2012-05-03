#!/usr/bin/env python
"""Demonstrate requests.async"""

# pip install requests gevent
# Installing gevent on my mac requires libevent...
from requests import async

urls = [
    'http://python-requests.org',
    'http://httpbin.org',
    'http://python-guide.org',
    'http://kennethreitz.com'
]

rs = [async.get(u) for u in urls]
responses = async.map(rs)
for response in responses:
    print response.status
