package GlobalModule;

use base qw(Exporter);
@EXPORT_OK = qw($globalVar);

our $globalVar; # Repeat here to avoid "used only once" warning
$globalVar = 42;

1;
