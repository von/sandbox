#!/usr/bin/env python
"""Demo of cement framework

builtoncement.org/

pip install cement
"""

from __future__ import print_function  # So we can get at print()

import argparse
import sys

from cement.core import backend, foundation

def main(argv=None):
    myname = 'cement-demo'
    defaults = backend.defaults(myname)
    defaults[myname]['foo'] = "BAR!"

    app = foundation.CementApp(myname, config_defaults=defaults)
    try:
        app.setup()
        app.args.add_argument('-f', '--foo', action='store',
                              metavar='STR', help='set foo')
        app.run()
        print("Hello world from cement-demo")
        if app.pargs.foo:
            app.log.info("Argument Foo == {}".format(app.pargs.foo))
        if app.config.has_key(myname, 'foo'):
            app.log.info(
                "Config Foo == {}".format(app.config.get(myname, 'foo')))
    finally:
        app.close()
    return(0)

if __name__ == "__main__":
    sys.exit(main())
