package myException;

use base qw(Error);
#use overload ('""' => 'stringify');

sub new
{
    my $self = shift;
    my $text = "" . shift;
    my @args = @_;
    
    local $Error::Depth = $Error::Depth + 1;
    local $Error::Debug = 1;  # Enables storing of stacktrace
    
    $self->SUPER::new(-text => $text, @args);
}

sub details
{
    my $self = shift;
    return $self->{-details};
}

package myExceptionalException;

use myException;
@ISA = ("myException");

1;
