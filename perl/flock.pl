#!/usr/bin/env perl

use Fcntl qw(:flock);

open(my $fh, ">", "/tmp/flock") || die $!;
flock($fh, LOCK_EX) || die $!;
print "Locked. Sleeping...\n";
sleep(10);
flock($fh, LOCK_UN) || die $!;
print "Unlocked.\n";
close($fh);
print "Success.\n";
exit(0);

