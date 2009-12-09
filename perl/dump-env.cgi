#!/usr/bin/env perl

use CGI qw/:standard *table/;

print header();
print start_html(-title=>"Environment Dump");
print h1("Environment Dump");
print start_table({-border=>1});
my @variables = sort(keys(%ENV));
foreach my $variable (@variables)
{
    print Tr([td([$variable, $ENV{$variable}])]);
}
print end_table();

print h1("Cookies");
print start_table({-border=>1});
my @cookies = sort(cookie());
foreach my $name (@cookies)
{
    print Tr([td([$name, cookie($name)])]);

}
print end_table();
print end_html();

