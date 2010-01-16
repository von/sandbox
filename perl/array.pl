#!/usr/bin/env perl -w

# Quote characters here to avoid "Unquoted string" warnings.
my @a = ('a'..'z', 'A'..'Z');

print join(':', @a) . "\n";
