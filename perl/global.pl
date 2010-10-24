#!/usr/bin/env perl -w
# Demonstrate how to create a globally-accessible variable in a module

use GlobalModule qw($globalVar);

print "globalVar: " . $globalVar . "\n";
