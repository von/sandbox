#!/usr/bin/env perl
#use Error qw(:try);
use myException qw(:try);

my $text = "Hi world";

# This block will return either the value of the try block, if it
# succeeds, or the value of the catch/otherwise block if an error
# occurs. The thing to note is that a 'return' statement in a
# try/catch block does not return from the outer scope, but returns
# *to* the outer scope.
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

}; # Note that this semi-colon is important, if it's not present you
   # get weird behavior.

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
    };
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
	return; # Returns to testNested() not from testNested()
    };
    print "After otherwise block\n";
}
