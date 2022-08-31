#!/usr/bin/env python3
#
# Examples of closures
#

# Function factory
# Kudos: https://stackoverflow.com/a/1261952/197789
def make_counter(start=1):
    count = start

    def counter():
        nonlocal count
        r = count
        count += 1
        return r
    return counter


print("Counter example...")
counter = make_counter()
print(f"{counter()} {counter()} {counter()}")

# Late binding gotchas
# https://docs.python-guide.org/writing/gotchas/#late-binding-closures
# https://stackoverflow.com/q/3431676/197789
#
print("Example of late binding in python...")


def closure_gotcha():
    funcs = []
    for i in range(3):
        def f():
            return i
        funcs.append(f)
    return funcs


fs = closure_gotcha()
print("This print 2,2,2...")
print([f() for f in fs])

print("Solution #1: default arguments...")


def closure_fixed1():
    funcs = []
    for i in range(3):
        def f(i=i):  # Force early binding
            return i
        funcs.append(f)
    return funcs


fs = closure_fixed1()
print("This will print 0,1,2...")
print([f() for f in fs])

print("Solution #2: function factory...")


def create_function(i):
    def f():
        return i
    return f


def closure_fixed2():
    funcs = []
    for i in range(3):
        f = create_function(i)
        funcs.append(f)
    return funcs


fs = closure_fixed2()
print("This will print 0,1,2...")
print([f() for f in fs])
