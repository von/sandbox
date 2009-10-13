#!/usr/bin/env perl

use Text::Template;

$template = Text::Template->new(
    TYPE => 'FILE',
    SOURCE => "template",
    );

my $ref = { var1 => "value1", var2 => "value2" };
foreach $key (keys(%$ref)) {
    my $value = $ref->{$key};
    print $key . "=" . $value . "\n";
}
my $hash = {
    session => { one => "uno", two => "dos" },
    test => "foo" };
print $template->fill_in(HASH => $hash);
