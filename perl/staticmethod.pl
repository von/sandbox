#!/usr/bin/env perl
#
# Demonstrate perl static vs class method calling

package Test;

sub classmethod
{
    my @args = @_;
    print join(" ", @args) . "\n";
}

package main;
use Test;

# This mimics a call to a static method. Will just pass two arguments.
Test::classmethod("Hello", "World");
# This mimics a call to a class method. Will prepend class name to arguments.
Test->classmethod("Hello", "World");
exit(0);

