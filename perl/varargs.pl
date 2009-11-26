#!/usr/bin/env perl

print "testFunc:\n";
testFunc("hello world", -world=>"Earth", -lifetime=>100, -bar=>"foo");

print "testHashArg:\n";
my %hash = (
    "foo" => "bar",
    "one" => 1,
    "file" => "name"
    );

testHashArg(%hash);

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

sub testHashArg
{
    my @args = @_;
    foreach my $arg (@args)
    {
	print "Arg: $arg\n";
    }
}
