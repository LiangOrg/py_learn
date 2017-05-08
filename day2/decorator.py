#!/usr/bin/env python
def log(f):
    def fn(*args):
        print 'call ' + f.__name__ + '()...'
        return f(*args)
    return fn

@log
def func1(*args):
    return reduce(lambda x,y: x*y, range(1,*args))
print func1(10,2)
