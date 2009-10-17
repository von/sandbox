#!/usr/bin/env perl

use CGI::Session;

my $id = shift;
# Name of cookie/parameter in which to store session ID in client
my $params = { "name" => "MYID" };

if (defined($id))
{
    $session = CGI::Session->load(undef, $id, undef, $params);
}
else
{
    $session = new CGI::Session(undef, undef, undef, $params );
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

$session->param("count", $count);

my $params = $session->dataref();

foreach $key (keys(%$params))
{
    print $key . "=" . $params->{$key} . "\n";
}


