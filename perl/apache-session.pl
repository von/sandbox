#!/usr/bin/env perl

use Apache::Session::File;

my %session;

my $id = shift;

tie %session, 'Apache::Session::File', $id, {
    Directory => '/tmp/sessions',
    LockDirectory   => '/tmp/sessions-lock',
 };

if (!defined($id)) {
    $id = $session{_session_id};
}

if (defined($session{number})) {
    $session{number} = $session{number} + 1;
} else {
    $session{number} = 1;
}

print $id . "\n";
print $session{number} . "\n";  

tied(%session)->delete;

exit(0);

