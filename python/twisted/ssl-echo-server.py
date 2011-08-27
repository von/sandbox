#!/usr/bin/env python
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class Echo(Protocol):
    def dataReceived(self, data):
        """As soon as any data is received, write it back."""
        print "Data received:", data
        self.transport.write(data)

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = Echo
    reactor.listenSSL(8000,
                      factory,
                      ssl.DefaultOpenSSLContextFactory('key.pem', 'cert.pem'))
    reactor.run()
