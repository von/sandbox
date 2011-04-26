#!/usr/bin/env python
"""Show how to use ssl.SSLSocket and M2Crypto.SSL.Connection with non-blocking IO

The issues are:

1) If you only read a partial record (e.g., recv() with a buffer
smaller than the record size), select() will not indicate socket is
ready to read from. True for both ssl.SSLSocket and
M2Crypto.SSL.Connection.

2) M2Crypto.SSL.Connection returns None instead of raising an
exception with a non-blocking recv() and no data available.
"""
import argparse
import logging
import Queue
import SocketServer
import select
import ssl
import sys
import threading
import time

import M2Crypto

chars = str(["a" * 1024])

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    queue = Queue.Queue()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    """An SSL Server using ssl.SSLSocket"""

    def handle(self):
        buflen = 256
        queue = self.server.queue
        s = ssl.wrap_socket(self.request,
                            keyfile = "key.pem",
                            certfile = "cert.pem",
                            server_side=True)
        s.setblocking(False)
        # ssl.SSLSocket throws an SSLError when doing a non-blocking read
        # and data isn't ready.
        try:
            data = s.recv(buflen)
        except ssl.SSLError as e:
            data = None
        print "Read on empty client socket: {}".format(data)
        # Msg #1
        queue.put(True)
        # Give client a chance to write something
        time.sleep(1)
        while True:
            try:
                data = s.recv(buflen)
            except ssl.SSLError:
                data = None
            if data is None:
                print "Done"
                break
            else:
                print "Client said {}".format(data)
        # Make sure client has to wait for response
        time.sleep(1)
        s.write("Goodbye")
        time.sleep(1)
        s.write(chars)
        time.sleep(5)
        # Msg #2
        queue.put(True)

def client(ip, port, queue, buflen=256):
    """An SSL client using M2Crypto.SSL.Connection"""
    context = M2Crypto.SSL.Context("sslv3")
    s = M2Crypto.SSL.Connection(context)
    # Turn off checking if CN == expected service name (hostname)
    # Kudos: http://stackoverflow.com/questions/2328265/turn-sslchecking-off-in-m2crypto-in-python
    s.postConnectionCheck = None
    s.connect((ip, port))
    s.setblocking(False)
    data = s.recv(buflen)
    print "Read on empty server socket returned: {}".format(data)  # None
    # Wait for Msg #1
    queue.get()
    s.write("Hello world")
    s.write(chars)
    while True:
        read_ready, write_ready, errors = select.select([s], [], [])
        if s in read_ready:
            try:
                # To read a record bigger than buflen, we need to keep
                # reading until we read None. The select() call will not
                # return immediately if we call it again even with data
                # pending.
                while True:
                    data = s.recv(buflen)
                    # SSL.Connection returns None when doing non-blocking IO
                    # and doing a read with no data available
                    if data is None:
                        print "Done reading."
                        break
                    else:
                        print "Server says {}".format(data)
            except M2Crypto.SSL.SSLError:
                print "Got EOF"
                break

    s.close()
    # Msg #2
    queue.get()

def main(argv=None):
    # Do argv default this way, as doing it in the functional
    # declaration sets it at compile time.
    if argv is None:
        argv = sys.argv

    # Set up out output via logging module
    output = logging.getLogger(argv[0])
    output.setLevel(logging.DEBUG)
    output_handler = logging.StreamHandler(sys.stdout)  # Default is sys.stderr
    # Set up formatter to just print message without preamble
    output_handler.setFormatter(logging.Formatter("%(message)s"))
    output.addHandler(output_handler)

    # Argument parsing
    parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        # Don't mess with format of description
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # To have --help print defaults with trade-off it changes
        # formatting, use: ArgumentDefaultsHelpFormatter
        )
    # Only allow one of debug/quiet mode
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-d", "--debug",
                                 action='store_const', const=logging.DEBUG,
                                 dest="output_level", default=logging.INFO,
                                 help="print debugging")
    verbosity_group.add_argument("-q", "--quiet",
                                 action="store_const", const=logging.WARNING,
                                 dest="output_level",
                                 help="run quietly")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    output_handler.setLevel(args.output_level)

    host = "localhost"
    port = 0  # Select arbitrary unused port

    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.handle_request)
    server_thread.setDaemon(True)
    server_thread.start()
    
    client(ip, port, server.queue)
    return(0)

if __name__ == "__main__":
    sys.exit(main())
