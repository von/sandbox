#!/usr/bin/env perl

use Crypt::OpenSSL::X509;

my $x509 = Crypt::OpenSSL::X509->new_from_file('cert.pem');
print "Issuer: " . $x509->issuer() . "\n";
print "Subject: " . $x509->subject() . "\n";
print "Expires: " . $x509->notAfter() . "\n";
print $x509->as_string();
exit(0);
