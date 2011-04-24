#!/usr/bin/env python
"""Demonstration of using M2Crypto to make a SSL connection and get certificate

No verification of certificate is done."""

from M2Crypto import SSL

context = SSL.Context("sslv3")

conn = SSL.Connection(context)

conn.connect(("encrypted.google.com", 443))

cert = conn.get_peer_cert()

print cert.as_text()

