#!/usr/bin/env perl
#use Error qw(:try);
use myException qw(:try);

my $text = "Hi world";

try {
    print $text . "\n";
    testNested("exceptional world");
}
catch myExceptionalException with {
    my $ex = shift;
    print "MyExceptionalException: " . $ex->text() . "\n";
    print "Details: " . $ex->details() . "\n";
}
catch myException with {
    my $ex = shift;
    print "MyException: " . $ex->text() . "\n";
    print "Details: " . $ex->details() . "\n";
}
otherwise {
    my $ex = shift;
    print "Exception: " . $ex->text() . "\n";
    #print "Details: " . $ex->details() . "\n";
};
#Error::flush();
print "Done.\n";
exit(0);

sub test
{
    my $name = shift;
    try
    {
	throw myException("Bad code");
	1;
    }
    catch Error with
    {
	throw myException("Worse code");
    }
}

sub test2
{
    die "A slow death";
}

sub test3
{
    a syntax error;
}

sub testNested
{
    try
    {
	test2();
    }
    otherwise
    {
	my $ex = shift;
	print "Nested: " . $ex->text() . "\n";
	return;
    };
    print "After otherwise block\n";
}
