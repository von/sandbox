#!/usr/bin/env python3
# Kudos:
# http://www.saltycrane.com/blog/2010/02/python-setdefault-example/

DATA_SOURCE = (('key1', 'value1'),
               ('key1', 'value2'),
               ('key2', 'value3'),
               ('key2', 'value4'),
               ('key2', 'value5'),)

newdata = {}
for k, v in DATA_SOURCE:
    if k in newdata:
        newdata[k].append(v)
    else:
        newdata[k] = [v]
print(newdata)

# This will return same as above.

newdata = {}
for k, v in DATA_SOURCE:
    newdata.setdefault(k, []).append(v)
print(newdata)
