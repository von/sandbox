#!/usr/bin/env perl

use Config::General;

my $configString = "
<Block block1>
  Var = Value1
</Block>
<Block block2>
  Var = Value2
</Block>
";

my %options = (
    -String => $configString,
    # Allow for OO type access to values
    -ExtendedAccess => 1,
    );

my $config = new Config::General(%options);

my $blocks = $config->obj("Block");

for my $key ($config->keys("Block"))
{
    my $value = $blocks->obj($key)->value("Var");
    print "Block: $key Var = $value\n";
}


