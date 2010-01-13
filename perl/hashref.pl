#!/usr/bin/env perl

my $hashref = {
    hello => "world",
    foo => "bar"
};

foreach my $key (keys(%$hashref))
{
    print sprintf("%s => %s\n", $key, $hashref->{$key});
}

