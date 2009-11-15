#!/usr/bin/perl

use URI;

my @urls = (
    "/foo/bar",
    "http://host/foo/path/file.html",
    "//path//file//something",
    "https:///path/file.txt",
    );

foreach my $url (@urls)
{
    my $uri = URI->new($url);
    print "$url -> " . $uri->canonical() . "\n";
    print "  Scheme: ", $uri->scheme( ), "\n";
    print "  Authority: ", $uri->authority( ), "\n";
    print "  Path: ", $uri->path( ), "\n";
    print "  Query: ", $uri->query( ), "\n";
}
