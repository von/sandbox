#!/usr/bin/env python
"""ssl_dispatcher and HTTP_dispatcher

Much taken from:
http://bugs.python.org/file20752/asyncore_ssl_v1.patch

"""

# For some sites (e.g., https://githib.com) it can take a long time
# for the connection to be recognized as closed. I'm not sure if that
# is because the site isn't closing the connection and the
# HTTP_dispatcher needs to key off of the content being done, or the
# close just isn't percolating up.

import asyncore
import errno
import httplib
import socket
import ssl
import StringIO
import urlparse

# Enum for SSL connection state (indepedent of socket state)
SSL_STATE = type('SSLState', (), {
    "DISCONNECTED":0,
    "CONNECTING":1,  # Doing SSL Handshake
    "ESTABLISHED":2,
    "DISCONNECTING":3,
    })


class ssl_dispatcher(asyncore.dispatcher):

    _state = SSL_STATE.DISCONNECTED

    # Flag to indicate we should close after SSL shutdown completes
    _close_on_ssl_shutdown = False

    def start_ssl(self):
        """Start SSL connection."""
        if self._state != SSL_STATE.DISCONNECTED:
            raise ValueError(
                "Tried to start already established SSL connection")
        ssl_socket = ssl.wrap_socket(self.socket,
                                     do_handshake_on_connect=False)
        self.set_socket(ssl_socket)
        self._state = SSL_STATE.CONNECTING
        self._do_ssl_handshake()  # Kick things off

    def handle_read_event(self):
        if self._state == SSL_STATE.CONNECTING:
            self._do_ssl_handshake()
        elif self._state == SSL_STATE.DISCONNECTING:
            self.ssl_shutdown()
        else:
            asyncore.dispatcher.handle_read_event(self)

    def handle_write_event(self):
        if self._state == SSL_STATE.CONNECTING:
            self._do_ssl_handshake()
        elif self._state == SSL_STATE.DISCONNECTING:
            self.ssl_shutdown()
        else:
            asyncore.dispatcher.handle_write_event(self)

    def send(self, data):
        try:
            return asyncore.dispatcher.send(self, data)
        except ssl.SSLError as err:
            if err.args[0] in (ssl.SSL_ERROR_EOF,
                               ssl.SSL_ERROR_ZERO_RETURN):
                return 0
            raise

    def recv(self, buffer_size):
        try:
            return asyncore.dispatcher.recv(self, buffer_size)
        except ssl.SSLError as err:
            if err.args[0] in (ssl.SSL_ERROR_EOF,
                               ssl.SSL_ERROR_ZERO_RETURN):
                self.handle_close()
                return ''
            if err.args[0] in (ssl.SSL_ERROR_WANT_READ,
                               ssl.SSL_ERROR_WANT_WRITE):
                return ''
            raise

    def close(self):
        # ssl_shutdown will presumably take a few roundtrips here.
        if self._state == SSL_STATE.ESTABLISHED:
            self._close_on_ssl_shutdown = True
            self.ssl_shutdown()
        if self._state == SSL_STATE.DISCONNECTED:
            return asyncore.dispatcher.close(self)
    
    def ssl_shutdown(self):
        """Tear down SSL layer switching back to a clear text connection."""
        if self._state == SSL_STATE.DISCONNECTED:
            raise ValueError("not using SSL")
        self._state = SSL_STATE.DISCONNECTING
        try:
            self.socket = self.socket.unwrap()
        except ssl.SSLError as err:
            if err.args[0] in (ssl.SSL_ERROR_WANT_READ,
                               ssl.SSL_ERROR_WANT_WRITE):
                return
            elif err.args[0] == ssl.SSL_ERROR_SSL:
                pass
            else:
                raise
        except socket.error as err:
            # Any "socket error" corresponds to a SSL_ERROR_SYSCALL
            # return from OpenSSL's SSL_shutdown(), corresponding to
            # a closed socket condition. See also:
            # http://www.mail-archive.com/openssl-users@openssl.org/msg60710.html
            pass
        self._state = SSL_STATE.DISCONNECTED
        self.handle_ssl_shutdown()
        if self._close_on_ssl_shutdown:
            # We were shutting down SSL because close() was called, now that
            # we are done doing so, return to it.
            self.close()

    def handle_ssl_established(self):
        """Called when the SSL handshake has completed."""
        self.log_info('unhandled handle_ssl_established event', 'warning')

    def handle_ssl_shutdown(self):
        """Called when SSL shutdown() has completed"""
        self.log_info('unhandled handle_ssl_shutdown event', 'warning')

    # --- internals

    def _do_ssl_handshake(self):
        """Kick off another handshake message"""
        try:
            self.socket.do_handshake()
            # No exception -> we are done with handshake
        except ssl.SSLError as err:
            if err.args[0] in (ssl.SSL_ERROR_WANT_READ,
                               ssl.SSL_ERROR_WANT_WRITE):
                return
            elif err.args[0] == ssl.SSL_ERROR_EOF:
                return self.handle_close()
            raise
        else:
            self._state = SSL_STATE.ESTABLISHED
            self.handle_ssl_established()

######################################################################

class StringBuffer(StringIO.StringIO):
    def makefile(self, *args, **kw):
        return self
    def sendall(self, arg):
        self.write(arg)

class HTTP_dispatcher(ssl_dispatcher):

    def __init__(self, url, method="GET", post_data=None, map=None):
        ssl_dispatcher.__init__(self, map=map)
        self.write_buffer = ""
        self.read_buffer = StringBuffer()
        self.amount_read = 0

        self.url = url
        self.parsed_url = urlparse.urlparse(url)
        if self.parsed_url.netloc.find(":") == -1:
            self.hostname = self.parsed_url.netloc
            self.port = 443 if self.parsed_url.scheme == "https" else 80
        else:
            self.hostname, port_str = self.parsed_url.netloc.split(":")
            self.port = int(port_str)
        address = (self.hostname, self.port)
        
        path = urlparse.urlunparse((None, # Scheme
                                    None, # netloc
                                    self.parsed_url.path,
                                    self.parsed_url.params,
                                    self.parsed_url.query,
                                    self.parsed_url.fragment))
        http_conn = httplib.HTTPConnection(self.hostname)
        http_conn.sock = StringBuffer()
        http_conn.request(method,
                          path,
                          post_data
                          )
        request = http_conn.sock.getvalue()
        self.write_buffer = request

        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(address)

    def handle_connect(self):
        if self.parsed_url.scheme == "https":
            self.start_ssl()
        
    def writable(self):
        return (len(self.write_buffer) > 0)

    def handle_write(self):
        sent = self.send(self.write_buffer)
        self.write_buffer = self.write_buffer[sent:]

    def handle_read(self):
        data = self.recv(8192)
        self.read_buffer.write(data)
        self.amount_read += len(data)

    def handle_close(self):
        self.close()

    def get_response(self):
        """Return the HTTPResponse

        Raises EOFError if no response received."""
        self.read_buffer.seek(0)
        if self.amount_read == 0:
            raise EOFError("Read zero bytes")
        response = httplib.HTTPResponse(self.read_buffer)
        response.begin()  # Process the response
        return response
    
if __name__ == "__main__":
    import socket

    dispatchers = []
    dispatchers.append(HTTP_dispatcher("https://www.ietf.org"))
    dispatchers.append(HTTP_dispatcher("http://www.ietf.org"))
    
    asyncore.loop(timeout=1.0, use_poll=True)
    
    for dispatcher in dispatchers: 
        response = dispatcher.get_response()
        print dispatcher.url
        print "Status:", response.status
        data = response.read()
        print "Data:",data[:64]

    
