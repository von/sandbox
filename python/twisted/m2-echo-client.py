#!/usr/bin/env python
"""http://twistedmatrix.com/documents/current/core/howto/ssl.html#auto3"""
from twisted.internet import ssl, reactor
from twisted.internet.protocol import ClientFactory, Protocol
from twisted.python import log
from M2Crypto.SSL import Context, Checker
# See http://www.heikkitoivonen.net/m2crypto/api/M2Crypto.SSL.TwistedProtocolWrapper-module.html#connectSSL
from M2Crypto.SSL.TwistedProtocolWrapper import connectSSL

class EchoClient(Protocol):
    def connectionMade(self):
        print "hello, world"
        self.transport.write("hello, world!")

    def dataReceived(self, data):
        if len(data) == 0:
            return
        print "Server said:", data
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print "Connection lost:", reason.getErrorMessage()

class EchoClientFactory(ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()

class CtxFactory:
    def getContext(self):
        ctx = Context()
        return ctx

def postConnectionCheck(cert, target):
    """The first argument to this function is an X509 object, the second is the expected host name string.

    Returns True if check succeed, False otherwise."""
    print "Server DN:", str(cert.get_subject())
    return True

def observer(dict):
    """Custom Twisted observer that ignores some exceptions

    Kudos: http://stackoverflow.com/questions/6962738/twisted-unhandled-error"""
    if dict["isError"]:
        failure = dict["failure"]
        if failure.check(Checker.SSLVerificationError):
            # Ignore validation failures resulting from post connection check
            pass
        else:
            print "Error:", failure.getErrorMessage()
    else:
        # Only print things originally sent to stdout or stderr
        if dict.has_key("printed"):
            print dict["message"]
    return True

if __name__ == '__main__':
    # setStdout=False so we can print to stdout without creating a loop
    log.startLoggingWithObserver(observer, setStdout=False)
    factory = EchoClientFactory()
    connectSSL('localhost', 8000, factory, CtxFactory(),
               postConnectionCheck=postConnectionCheck)
    reactor.run()
