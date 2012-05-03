#!/usr/bin/env python
#
# https://github.com/kennethreitz/clint
# pip install clint
#

from clint import args
from clint.textui import puts, colored, indent

with indent(4, quote='>>>'):
    puts(colored.red('Aruments passed in: ') + str(args.all))
    puts(colored.red('Flags detected: ') + str(args.flags))
    puts(colored.red('Files detected: ') + str(args.files))
    puts(colored.red('NOT Files detected: ') + str(args.not_files))
    puts(colored.red('Grouped Arguments: ') + str(dict(args.grouped)))
    
print
