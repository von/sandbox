#!/usr/bin/env python3
"""Show any() and all() use in python

Because I keep forgetting what these methods are called."""

a = [0,1,2,3,4]
b = [1,2,3]
c = [0,0,0]

def demo(name, array):
    print(f"{name}: {','.join(map(str, array))}")
    print(f"any({name}) = {any(array)} all({name}) = {all(array)}")

demo("a", a)
demo("b", b)
demo("c", c)

