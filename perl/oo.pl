#!/usr/bin/env perl

use myException;
use Error;

my $ex = myException->new("Test");
my $er = Error->new("Test");

if ($ex->isa("Error"))
{
    print "ex == Error\n";
}
if ($ex->isa("myException"))
{
    print "ex == myException\n";
}


if ($er->isa("Error"))
{
    print "er == Error\n";
}
if ($er->isa("myException"))
{
    print "er == myException\n";
}

if ($ex->can("details"))
{
    print "ex has details()\n";
}


if ($er->can("details"))
{
    print "er has details()\n";
}
