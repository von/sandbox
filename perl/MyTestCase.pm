package MyTestCase;
use base qw(Test::Unit::TestCase);

sub new {
    my $self = shift()->SUPER::new(@_);
    # your state for fixture here
    return $self;
}

sub set_up {
    # provide fixture
}
sub tear_down {
    # clean up after test
}
sub test_foo {
    my $self = shift;
    $self->assert_equals(1,1);
}
sub test_bar {
    my $self = shift;
    $self->annotate("This should fail...");
    $self->assert_equals(1,0);
}

1;
