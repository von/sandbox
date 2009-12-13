#!/usr/bin/env perl

package Foo;

$Var = 1;

sub test
{
    our $Var;
    print "Var = $Var\n";
}

package main;

Foo::test();
