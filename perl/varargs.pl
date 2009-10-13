#!/usr/bin/env perl

testFunc("hello world", -world=>"Earth", -lifetime=>100, -bar=>"foo");

sub testFunc
{
    my $message = shift;
    my %args = @_;
    print $message . " " . $args{-world} . "\n";
    foreach my $key (keys(%args))
    {
	print $key . ":" . $args{$key} . "\n";
    }
}
