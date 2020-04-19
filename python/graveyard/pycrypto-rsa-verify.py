#!/usr/bin/env python
"""Use pyCrypto to generate a RSA key, sign something and then verify signature"""
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool

rpool = RandomPool()

print "Generating RSA key pair"
RSAkey = RSA.generate(1024, rpool.get_bytes)

print "Creating signature"
hash = MD5.new("Hello world").digest()
signature = RSAkey.sign(hash, "")

print "Verifying signature"
if not RSAkey.verify(hash, signature):
    print "Failed."


