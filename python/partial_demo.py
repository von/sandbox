#!/usr/bin/env python3
"""Demonstration of Python functools module"""

from functools import partial

def test_func(name, *args, **kwargs):
    print("Name:\t", name)
    print("Args:\t", ", ".join(args))
    print("KWargs:")
    for k,v in list(kwargs.items()):
        print("\t" + k + "=" + v)

print("Calling test_func('Hello', 'Abc', '123', this='that', test='ground'):")
test_func("Hello world", "Abc", "123", this="that", test="ground")
print("\n")

test_func_partial = partial(test_func, "foo", "bar", hello="world")

print("Calling test_func_partial():")
test_func_partial()
print("\n")

print("Calling test_func_partial('apple', 'orange', color='blue'):")
test_func_partial('apple', 'orange', color='blue')
print("\n")
