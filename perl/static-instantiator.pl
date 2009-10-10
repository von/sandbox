#!/usr/bin/env perl

package Test;

sub new
{
    my $class = shift;
    my $s = shift;
    my $self = {};
    $self->{string} = $s;
    bless($self, $class);
    return $self;
}

sub staticNew
{
    my $class = shift;
    my $s = shift;
    my $obj = $class->new($s);
    return $obj;
}

sub getString
{
    my $self = shift;
    return $self->{string};
}

package main;
use Test;

my $obj = Test->staticNew("Hello world");
print $obj->getString() . "\n";
exit(0);
