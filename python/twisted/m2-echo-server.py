#!/usr/bin/env python
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol
from M2Crypto.SSL import Context
from M2Crypto.SSL.TwistedProtocolWrapper import listenSSL

class Echo(Protocol):
    def connectionMade(self):
        print "Connection accepted"

    def dataReceived(self, data):
        """As soon as any data is received, write it back."""
        if len(data) == 0:
            return
        print "Data received:", data
        self.transport.write(data)

    def connectionLost(self, reason):
        print "Connection lost:", reason.getErrorMessage()

class CtxFactory:
    def getContext(self):
        ctx = Context()
        ctx.load_cert(certfile="cert.pem", keyfile="key.pem")
        return ctx

def postConnectionCheck(cert, client):
    """The first argument to this function is an X509 object, the second is the expected host name string.

    Returns True if check succeed, False otherwise."""
    print "postConnectionCheck(). Client addr", client
    return True

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = Echo
    listenSSL(8000, factory, CtxFactory(),
              postConnectionCheck=postConnectionCheck)
    reactor.run()
