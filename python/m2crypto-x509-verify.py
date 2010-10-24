#!/usr/bin/env python
"""Use M2Crypto to verify x509 signature

Usage: m2crypto-x509-verify.py <cert file> <signature file>
"""
from M2Crypto import EVP, RSA, X509

cert = X509.load_cert("PKICert.pem")
pub_key = cert.get_pubkey()

plaintext = "Hello World"

signature = "XXX" # Put signature here
pub_key.verify_init()
pub_key.verify_update(plaintext)
if not pub_key.verify_final(signature):
    print "Signature failed"
