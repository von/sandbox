#!/usr/bin/env python3
# Currently failing with the following error:
#
# Traceback (most recent call last):
#  File "./comb.py", line 47, in <module>
#    for subset in a:
# RuntimeError: generator raised StopIteration
#
# I think StopIteration handling has changed:
# https://www.python.org/dev/peps/pep-0479/

def rangeIter(value1, value2=None):
    if value2:
        for value in range(value1, value2):
            yield value
    else:
        for value in range(value1):
            yield value

def comb(set, n):
    """Iterate over all combinations of n elements from set."""
    if len(set) < n:
        raise Exception("Not enough elements")
    elif len(set) == n:
        yield set
    else:
        setLen = len(set)
        iters = [rangeIter(setLen - n + 1)]
        values = [0] * n
        values[0] = next(iters[0])
        level = 1
        while True:
            # Fill array of iterators back up
            while level < n:
                iters.append(rangeIter(values[level - 1] + 1,
                                   setLen - n + level + 1))
                values[level]=next(iters[level])
                level += 1
            subset = [set[i] for i in values]
            yield subset
            while True:
                try:
                    values[level - 1] = next(iters[level - 1])
                    break
                except StopIteration:
                    iters.pop()
                    level -= 1
                    if level == 0:
                        # Top-level iterator is done, so we are too
                        raise StopIteration

a = comb([1,2,3,4,5],2)
for subset in a:
    print(f"Subset: {subset}")
