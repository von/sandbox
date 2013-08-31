#!/usr/bin/env python
# encoding: utf-8
"""Demonstrate assignment in a lambda.

Kudos: http://stackoverflow.com/a/14617232/197789"""

# This lambda creates an array and returns the last element
# In the process, the first element sets message in the scope.
say_hello = lambda: [
    # Assign to message
    [None for message in ["Hello world"]],
    "Some random string",
    message
][-1] # Return last element, which is message

print say_hello()
