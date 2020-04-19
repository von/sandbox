#!/usr/bin/env python
"""Demonstrate assignment in a lambda.

Kudos: http://stackoverflow.com/a/14617232/197789

Note this does not work in Python3, one would have to use
some form of assignment express with :=, see:
https://www.python.org/dev/peps/pep-0572/
"""

# This lambda creates an array and returns the last element
# In the process, the first element sets message in the scope.
say_hello = lambda: [
    # Assign to message
    [None for message in ["Hello world"]],
    "Some random string",
    message
][-1] # Return last element, which is message

print(say_hello())
