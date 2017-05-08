#!/usr/bin/env python
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn

@log
def func1(a):
    return reduce(lambda x,y: x*y, range(1,a+1))
print func1(10)
