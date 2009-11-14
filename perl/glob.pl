#!/usr/bin/env perl
#
# Convert a glob to perl-stype regex

sub convert
{
    my $glob = shift;
    my $regex = $glob;
    
    # Protect '.'s
    $regex =~ s/\./\\./g;

    # Convert *s to .+'s
    $regex =~ s/\*/.+/g;

    # Anchor start and stop
    $regex = "^" . $regex . "\$";

    return $regex;
}

my @globs = (
    "Hello World",
    "Hello *",
    "Mr. Hello World",
    "Mr. * World",
    );

for my $glob (@globs)
{
    my $regex = convert($glob);
    print "Glob: \"$glob\" Regex: \"$regex\"\n";
}

exit(0);

