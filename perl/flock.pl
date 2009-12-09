#!/usr/bin/env perl

use Fcntl qw(:flock);

my $fh;
if (!open($fh, ">", "/tmp/flock"))
{
    die $!;
}
if (!flock($fh, LOCK_EX))
{
    die $!;
}
print "Locked. Sleeping...\n";
sleep(10);
if (!flock($fh, LOCK_UN))
{
    die $!;
}
print "Unlocked.\n";
close($fh);
print "Success.\n";
exit(0);

