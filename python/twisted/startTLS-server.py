#!/usr/bin/env python
# http://twistedsphinx.funsize.net/projects/core/howto/ssl.html
from OpenSSL import SSL
from twisted.internet import reactor, ssl
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver

class TLSServer(LineReceiver):
    def lineReceived(self, line):
        print "received: " + line

        if line == "STARTTLS":
            print "-- Switching to TLS"
            self.sendLine('READY')
            ctx = ServerTLSContext(
                privateKeyFileName='key.pem',
                certificateFileName='cert.pem',
                )
            # Second argument to startTLS is boolean for server or client
            #  default is server.
            self.transport.startTLS(ctx)

class ServerTLSContext(ssl.DefaultOpenSSLContextFactory):
    def __init__(self, *args, **kw):
        kw['sslmethod'] = SSL.TLSv1_METHOD
        ssl.DefaultOpenSSLContextFactory.__init__(self, *args, **kw)

if __name__ == '__main__':
    factory = ServerFactory()
    factory.protocol = TLSServer
    reactor.listenTCP(8000, factory)
    reactor.run()
