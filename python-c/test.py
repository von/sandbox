print "Hello world"
print "Goodbye world"

def myFunction(i1, i2):
    print "Hello from myFunction: i1=%d i2=%d" % (i1,i2)
    print i1 + i2
    # Return values as a list, with an extra value thrown in for
    # funsies...
    return [i1, i2, 999]

def myListFunction(l):
    sum = 0
    for i in l:
        sum += i
    print "List sum is ", sum
    # Create a new list twice as good as old one!
    l2 = map(lambda i: i*2, l)
    return l2
