#!/usr/bin/env python
"""Test query to Convergence Notary

https://github.com/moxie0/Convergence/wiki/Notary-Protocol

As of 2020-03, no longer working:
ping: cannot resolve notary.thoughtcrime.org: Unknown host
"""

import sys
import httplib
import urllib
import urllib2

# Kudos:
# http://stackoverflow.com/questions/603856/how-do-you-get-default-headers-in-a-urllib2-request
# Modified to handle https instead of http
class MyHTTPSConnection(httplib.HTTPSConnection):
    def send(self, s):
        print "Sending:\n", s
        httplib.HTTPConnection.send(self, s)

class MyHTTPSHandler(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(MyHTTPSConnection, req)

def main(argv=None):
    NOTARY_HOSTNAME = "notary.thoughtcrime.org"
    NOTARY_PORT = 443
    SERVICE_HOSTNAME = "encrypted.google.com"
    SERVICE_PORT = 443

    url = "https://%s:%d/target/%s+%d" % (
        NOTARY_HOSTNAME,
        NOTARY_PORT,
        SERVICE_HOSTNAME,
        SERVICE_PORT)

    print "Using urllib.urlopen()"
    stream = urllib.urlopen(url)
    print "".join(stream.readlines())
    stream.close()

    print "Using urllib2"
    opener = urllib2.build_opener(MyHTTPSHandler)
    stream = opener.open(url)
    print "".join(stream.readlines())
    stream.close()

    return(0)

if __name__ == "__main__":
    sys.exit(main())
