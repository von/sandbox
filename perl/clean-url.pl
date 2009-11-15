#!/usr/bin/perl

use File::Spec;
use URI;

my @urls = (
    "/foo/bar",
    "http://host/foo/path/file.html",
    "//path//file//something",
    "https:///path/file.txt",
    "https:///path//file.jpg",
    );

foreach my $url (@urls)
{
    print "$url -> " . cleanURL($url) . "\n";
}

sub cleanURL
{
    my $url = shift;
    if ($url =~ /^\w+:/)
    {
	# Absolute URL, just clean up path portion.
	$uri = URI->new($url);
	$uri->path(File::Spec->canonpath($uri->path()));
    }
    else
    {
	# Relative URL, clean up first to avoid URI confusing "//" at
	# start as start of host.
	$uri = URI->new(File::Spec->canonpath($url));
    }
    return $uri->canonical();
}
