#!/usr/bin/env perl

use Date::Parse;

# Format returned by Crypt::OpenSSL::X509->notAfter()
$dateString = "Tue Nov 17 06:47:13 2009";
        
$time = str2time($dateString);

print "$dateString => $time\n";

