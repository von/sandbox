package MySuite;

use base qw(Test::Unit::TestSuite);

sub name { 'My very own test suite' } 
sub include_tests { qw(MyTestCase) }

1;
