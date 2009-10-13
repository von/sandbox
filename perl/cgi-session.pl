#!/usr/bin/env perl

use CGI::Session;

my $id = shift;

if (defined($id))
{
    $session = CGI::Session->load($id);
}
else
{
    $session = new CGI::Session(undef);
}

if (!defined($id))
{
    print "Id: " . $session->id() . "\n";
}

my $count = $session->param("count");

if (!defined($count))
{
    $count = 0;
}
else
{
    $count += 1;
}

print "Count: $count\n";

$session->param("count", $count);

my $params = $session->dataref();

foreach $key (keys(%$params))
{
    print $key . "=" . $params->{$key} . "\n";
}


