"""Example __init__.py

This shows how to make modules in a package more easily accessible by
importing them here, which makes them available to code importing the
package. E.g. instead of:

from PackageDemo.SomeClass import SomeClass

you can use:

from PackageDemo import SomeClass

because of the 'import SomeClass' in this file.

The trick is to understand that 'import PackageDemo' causes this file to
be invoked and results in the PackageDemo namespace, so anything you define
or import into this file will be available under 'PackageDemo'.
"""

class FooClass:
    "This is FooClass. It does nothing."""
    pass

from SomeClass import SomeClass

# Both FooClass and SomeClass can now be imported via PackageDemo

# __path__ is set to a list containing a single element, that being
# the path holding the package's __init__.py file.
my_package_path = __path__[0]


    
