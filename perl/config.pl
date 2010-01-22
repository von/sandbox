#!/usr/bin/env perl

use Config::General;

my $configString = "
<Block block1>
  Var = Value1
  <SubBlock foo>
    Var = SubValue
  </SubBlocl>
</Block>
<Block block2>
  Var = Value2
</Block>

RootVar=Hello World
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
    my $block = $blocks->obj($key);
    my $value = $block->value("Var");
    print "Block: $key Var = $value\n";
    print "Keys: " . join (' ', $block->keys()) . "\n";
    if ($block->exists("SubBlock"))
    {
	print "Subblock:\n";
	my @subBlockKeys = $block->keys("SubBlock");
	for my $subBlockKey (@subBlockKeys)
	{
	    print "\t$subBlockKey\n";
	}
    }
}

my %rootHash = $config->getall();

print "Root Keys: " . join(' ', keys(%rootHash)) . "\n";
print "RootVar=" . $rootHash{"RootVar"} . "\n";
$rootHash{"RootVar"} = "Goodbye World";
print $config->save_file("/tmp/rootHash", \%rootHash);

