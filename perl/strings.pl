#!/usr/bin/env perl

my $s1 = 'Hello "World"';
my $s2 = '$s1 and So Long...';  # $s1 will be taken literally
my $s3 = "$s1 and 'so long'..."; # $s1 will be expanded

print $s1 . "\n";
print $s2 . "\n";
print $s3 . "\n";
